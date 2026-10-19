#!/usr/bin/env python3
"""Scan agent rule files for dependency-swap prompt injection.

Stdlib only. Exit 0 when clean, 1 when a finding remains. HIDDEN findings
(zero-width and bidi controls, HTML comments with imperative or install
wording, invisible HTML/CSS, lines over 400 characters) always fail and
cannot be allowlisted. INSTRUCTION and UNKNOWN_PKG fail unless
.rule-file-allowlist matches path, rule, pattern, and reason. If the repo
has no lockfile or manifest, UNKNOWN_PKG is reported and does not fail.

arXiv 2610.09264: rule-file prompt injection makes coding agents swap
dependencies. This check does not call GitHub Actions.
"""

from __future__ import annotations

import html
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
from pathlib import Path

MAX_LINE = 400

ZERO_WIDTH = {
    "\u200b": "U+200B",
    "\u200c": "U+200C",
    "\u200d": "U+200D",
    "\u2060": "U+2060",
    "\ufeff": "U+FEFF",
}
BIDI = {
    "\u202a": "U+202A",
    "\u202b": "U+202B",
    "\u202c": "U+202C",
    "\u202d": "U+202D",
    "\u202e": "U+202E",
    "\u2066": "U+2066",
    "\u2067": "U+2067",
    "\u2068": "U+2068",
    "\u2069": "U+2069",
}
HIDDEN_CHARS = set(ZERO_WIDTH) | set(BIDI)

SKIP_DIRS = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
    "__pycache__",
    ".tox",
    ".mypy_cache",
    ".pytest_cache",
}

MANIFEST_NAMES = {
    "package.json",
    "package-lock.json",
    "npm-shrinkwrap.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "pnpm-lock.yml",
    "bun.lock",
    "poetry.lock",
    "uv.lock",
    "Pipfile.lock",
    "go.mod",
    "go.sum",
    "Cargo.toml",
    "Cargo.lock",
    "pyproject.toml",
}

VALUE_FLAGS = {
    "-c",
    "-e",
    "-f",
    "-i",
    "-r",
    "-t",
    "--branch",
    "--cache",
    "--config",
    "--constraint",
    "--editable",
    "--extra-index-url",
    "--features",
    "--find-links",
    "--git",
    "--index-url",
    "--path",
    "--prefix",
    "--registry",
    "--requirement",
    "--rev",
    "--root",
    "--src",
    "--tag",
    "--target",
    "--trusted-host",
    "-Z",
}

INSTALL_RE = re.compile(
    r"\b(pip3?|npm|yarn|pnpm|cargo|go)\s+(install|add)\b([^|\n;&]*)",
    re.IGNORECASE,
)
REPLACE_RE = re.compile(
    r"\breplace\s+(\S+)\s+with\s+(\S+)",
    re.IGNORECASE,
)
USE_PACKAGE_RE = re.compile(
    r"\buse\s+(?:the\s+)?package(?:\s+(\S+))?",
    re.IGNORECASE,
)
CURL_PIPE_RE = re.compile(
    r"\bcurl\b[^\n|]{0,400}\|\s*(?:sudo\s+)?(?:sh|bash)\b",
    re.IGNORECASE,
)
WGET_PIPE_RE = re.compile(
    r"\bwget\b[^\n|]{0,400}\|\s*(?:sudo\s+)?(?:bash|sh)\b",
    re.IGNORECASE,
)
INDEX_URL_RE = re.compile(r"--(?:extra-)?index-url\b", re.IGNORECASE)
REGISTRY_RE = re.compile(r"\bregistry\s*=", re.IGNORECASE)
NPMRC_RE = re.compile(r"\.npmrc\b", re.IGNORECASE)
COMMENT_RE = re.compile(r"<!--(.*?)(?:-->|$)", re.DOTALL)
COMMENT_WORD_RE = re.compile(
    r"\b(?:install|pip3?|npm|yarn|pnpm|cargo|curl|wget|sudo|execute|"
    r"download|replace|ignore|disregard|override|run|eval|import|add|use|"
    r"fetch|clone|bash|sh|registry|npmrc|require)\b",
    re.IGNORECASE,
)
INVISIBLE_RE = re.compile(
    r"(?:display\s*:\s*none\b|"
    r"visibility\s*:\s*hidden\b|"
    r"opacity\s*:\s*0(?:\.0+)?(?![\d.])|"
    r"font-size\s*:\s*0(?:\.0+)?(?:\s*(?:px|pt|em|rem|%))?(?![\d.])|"
    r"color\s*:\s*transparent\b|"
    r"text-indent\s*:\s*-\d{3,}|"
    r"(?:left|top|right|bottom)\s*:\s*-\d{3,}(?:\s*(?:px|em|rem))?\b|"
    r"rgba?\(\s*(?:\d+\s*,\s*){3}0(?:\.0+)?\s*\)|"
    r"hsla?\(\s*[^)]*?,\s*0(?:\.0+)?\s*\))",
    re.IGNORECASE,
)
TAG_RE = re.compile(r"<[A-Za-z][^>]*>")
PKG_BODY_RE = re.compile(
    r"^(?:@[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+|"
    r"[A-Za-z][A-Za-z0-9_.-]*(?:/[A-Za-z0-9_.-]+)*)$"
)


@dataclass(frozen=True)
class Record:
    status: str  # FAIL, ALLOW, REPORT, NOTE
    rule: str
    location: str
    detail: str

    def render(self) -> str:
        return f"{self.status}\t{self.rule}\t{self.location}\t{self.detail}"


@dataclass(frozen=True)
class Allow:
    path: str
    rule: str
    pattern: re.Pattern[str]
    reason: str


def strip_hidden(text: str) -> str:
    return "".join(ch for ch in text if ch not in HIDDEN_CHARS)


def visible(text: str, limit: int = 120) -> str:
    parts: list[str] = []
    for ch in text:
        if ch in ZERO_WIDTH or ch in BIDI or (ord(ch) < 32 and ch != "\t"):
            parts.append(f"<U+{ord(ch):04X}>")
        else:
            parts.append(ch)
    out = "".join(parts).replace("\t", " ")
    if len(out) > limit:
        return out[: limit - 3] + "..."
    return out


def norm_pkg(token: str) -> str | None:
    token = token.strip().strip("'\"`,").strip(".,;:)]}>")
    if not token or token.startswith(("-", ".", "/")) or "://" in token:
        return None
    if token.startswith("git+") or token.startswith("http"):
        return None
    token = re.sub(r"\[[^\]]*\]", "", token)
    if token.startswith("@"):
        match = re.match(r"^(@[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", token)
        if not match:
            return None
        token = match.group(1)
    else:
        token = re.split(r"(?:===|==|>=|<=|~=|!=|@)", token, maxsplit=1)[0]
        token = re.split(r"[<>]", token, maxsplit=1)[0].strip()
    if not PKG_BODY_RE.fullmatch(token):
        return None
    return token.casefold()


def add_name(names: set[str], token: object) -> None:
    if not isinstance(token, str):
        return
    name = norm_pkg(token)
    if name:
        names.add(name)


def install_packages(rest: str) -> list[str]:
    names: list[str] = []
    skip_next = False
    for tok in rest.split():
        if skip_next:
            skip_next = False
            continue
        if tok.startswith("-"):
            flag = tok.split("=", 1)[0]
            if "=" not in tok and flag in VALUE_FLAGS:
                skip_next = True
            continue
        name = norm_pkg(tok)
        if name:
            names.append(name)
    return names


def inside(root: Path, path: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except (OSError, ValueError):
        return False
    return True


def consider_file(root: Path, path: Path, files: list[Path], notes: list[Record]) -> None:
    if path.is_symlink():
        rel = path.relative_to(root).as_posix() if path.is_relative_to(root) else path.name
        notes.append(Record("FAIL", "HIDDEN", rel, "symlink: rule path is a symlink"))
        return
    if path.is_file() and inside(root, path):
        files.append(path)


def discover_rules(root: Path) -> tuple[list[Path], list[Record]]:
    files: list[Path] = []
    notes: list[Record] = []
    for name in ("AGENTS.md", "CLAUDE.md", ".cursorrules"):
        consider_file(root, root / name, files, notes)
    cursor = root / ".cursor" / "rules"
    if cursor.is_symlink():
        notes.append(Record("FAIL", "HIDDEN", ".cursor/rules", "symlink: rule path is a symlink"))
    elif cursor.is_dir():
        for path in sorted(cursor.rglob("*")):
            if path.is_dir() and not path.is_symlink():
                continue
            consider_file(root, path, files, notes)
    skills = root / "skills"
    if skills.is_symlink():
        notes.append(Record("FAIL", "HIDDEN", "skills", "symlink: rule path is a symlink"))
    elif skills.is_dir():
        for path in sorted(skills.rglob("SKILL.md")):
            consider_file(root, path, files, notes)
    rules = root / "rules"
    if rules.is_dir() and not rules.is_symlink():
        for path in sorted(rules.glob("*.md")):
            consider_file(root, path, files, notes)
    templates = root / "templates"
    if templates.is_dir() and not templates.is_symlink():
        for path in sorted(templates.glob("*.template")):
            consider_file(root, path, files, notes)
    unique = sorted({p.resolve(): p for p in files}.values(), key=lambda p: p.as_posix())
    return unique, notes


def discover_manifests(root: Path) -> list[Path]:
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            if name not in MANIFEST_NAMES and not fnmatch(name, "requirements*.txt"):
                continue
            path = Path(dirpath) / name
            if path.is_symlink():
                found.append(path)
                continue
            if path.is_file() and inside(root, path):
                found.append(path)
    return found


def load_toml(text: str) -> dict:
    try:
        import tomllib
    except ImportError as exc:  # pragma: no cover - Python 3.11+ has tomllib
        raise ValueError("tomllib is required to read TOML manifests") from exc
    data = tomllib.loads(text)
    if not isinstance(data, dict):
        raise ValueError("TOML manifest is not a table")
    return data


def add_npm_package_json(data: object, names: set[str]) -> None:
    if not isinstance(data, dict):
        raise ValueError("package.json is not an object")
    add_name(names, data.get("name"))
    for key in (
        "dependencies",
        "devDependencies",
        "optionalDependencies",
        "peerDependencies",
    ):
        deps = data.get(key)
        if isinstance(deps, dict):
            for name in deps:
                add_name(names, name)
        elif isinstance(deps, list):
            for name in deps:
                add_name(names, name)
    bundled = data.get("bundledDependencies") or data.get("bundleDependencies")
    if isinstance(bundled, list):
        for name in bundled:
            add_name(names, name)


def add_npm_lock(data: object, names: set[str]) -> None:
    if not isinstance(data, dict):
        raise ValueError("npm lockfile is not an object")
    packages = data.get("packages")
    if isinstance(packages, dict):
        for key in packages:
            if isinstance(key, str) and "node_modules/" in key:
                add_name(names, key.split("node_modules/")[-1])
    deps = data.get("dependencies")
    if isinstance(deps, dict):
        for key, val in deps.items():
            add_name(names, key)
            if isinstance(val, dict) and isinstance(val.get("dependencies"), dict):
                add_npm_lock({"dependencies": val["dependencies"]}, names)


def add_lock_name_lines(text: str, names: set[str]) -> None:
    for match in re.finditer(r'(?m)^name = "([^"]+)"', text):
        add_name(names, match.group(1))


def add_at_version_lines(text: str, names: set[str]) -> None:
    for match in re.finditer(
        r'(?m)^[ \t]*"?/?((?:@[A-Za-z0-9_.-]+/)?[A-Za-z0-9_.-]+)@',
        text,
    ):
        add_name(names, match.group(1))


def add_requirements(text: str, names: set[str]) -> None:
    for raw in text.split("\n"):
        line = raw.split("#", 1)[0].strip()
        if not line or line.startswith("-"):
            continue
        line = line.split(";", 1)[0].strip()
        if " @" in line:
            line = line.split(" @ ", 1)[0].strip()
        add_name(names, line)


def add_pyproject(data: dict, names: set[str]) -> None:
    project = data.get("project")
    if isinstance(project, dict):
        add_name(names, project.get("name"))
        for dep in project.get("dependencies") or []:
            add_name(names, dep if isinstance(dep, str) else None)
        optional = project.get("optional-dependencies")
        if isinstance(optional, dict):
            for deps in optional.values():
                for dep in deps or []:
                    add_name(names, dep if isinstance(dep, str) else None)
    groups = data.get("dependency-groups")
    if isinstance(groups, dict):
        for deps in groups.values():
            for dep in deps or []:
                add_name(names, dep if isinstance(dep, str) else None)
    tool = data.get("tool")
    poetry = tool.get("poetry") if isinstance(tool, dict) else None
    if isinstance(poetry, dict):
        add_name(names, poetry.get("name"))
        deps = poetry.get("dependencies")
        if isinstance(deps, dict):
            for name in deps:
                if name != "python":
                    add_name(names, name)
        grouped = poetry.get("group")
        if isinstance(grouped, dict):
            for group in grouped.values():
                gdeps = group.get("dependencies") if isinstance(group, dict) else None
                if isinstance(gdeps, dict):
                    for name in gdeps:
                        add_name(names, name)


def add_cargo_toml(data: dict, names: set[str]) -> None:
    package = data.get("package")
    if isinstance(package, dict):
        add_name(names, package.get("name"))
    tables = []
    for key in ("dependencies", "dev-dependencies", "build-dependencies"):
        tables.append(data.get(key))
    target = data.get("target")
    if isinstance(target, dict):
        for cfg in target.values():
            if isinstance(cfg, dict):
                for key in ("dependencies", "dev-dependencies", "build-dependencies"):
                    tables.append(cfg.get(key))
    for deps in tables:
        if isinstance(deps, dict):
            for name in deps:
                add_name(names, name)


def add_go_mod(text: str, names: set[str]) -> None:
    module = re.search(r"(?m)^module\s+(\S+)", text)
    if module:
        add_name(names, module.group(1))
    for match in re.finditer(r"(?m)^(?:require\s+)?(\S+)\s+v\d", text):
        add_name(names, match.group(1))


def add_go_sum(text: str, names: set[str]) -> None:
    for match in re.finditer(r"(?m)^(\S+)\s+v", text):
        add_name(names, match.group(1))


def add_pipfile_lock(data: object, names: set[str]) -> None:
    if not isinstance(data, dict):
        raise ValueError("Pipfile.lock is not an object")
    for key, section in data.items():
        if key == "_meta" or not isinstance(section, dict):
            continue
        for name in section:
            add_name(names, name)


def read_manifest(path: Path, names: set[str]) -> None:
    name = path.name
    text = path.read_text(encoding="utf-8")
    if name == "package.json":
        add_npm_package_json(json.loads(text), names)
    elif name in {"package-lock.json", "npm-shrinkwrap.json"}:
        add_npm_lock(json.loads(text), names)
    elif name == "Pipfile.lock":
        add_pipfile_lock(json.loads(text), names)
    elif name in {"yarn.lock", "pnpm-lock.yaml", "pnpm-lock.yml", "bun.lock"}:
        add_at_version_lines(text, names)
    elif name in {"poetry.lock", "uv.lock", "Cargo.lock"}:
        add_lock_name_lines(text, names)
    elif fnmatch(name, "requirements*.txt"):
        add_requirements(text, names)
    elif name == "pyproject.toml":
        add_pyproject(load_toml(text), names)
    elif name == "Cargo.toml":
        add_cargo_toml(load_toml(text), names)
    elif name == "go.mod":
        add_go_mod(text, names)
    elif name == "go.sum":
        add_go_sum(text, names)
    else:
        raise ValueError(f"unsupported manifest {name}")


def load_known(root: Path) -> tuple[set[str], list[Path], list[Record]]:
    names: set[str] = set()
    problems: list[Record] = []
    manifests = discover_manifests(root)
    for path in manifests:
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            problems.append(Record("FAIL", "HIDDEN", rel, "symlink: manifest is a symlink"))
            continue
        try:
            read_manifest(path, names)
        except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
            problems.append(Record("FAIL", "MANIFEST", rel, f"unreadable: {exc.__class__.__name__}"))
    return names, manifests, problems


def load_allowlist(root: Path) -> tuple[list[Allow], list[Record]]:
    path = root / ".rule-file-allowlist"
    entries: list[Allow] = []
    records: list[Record] = []
    if not path.is_file() or path.is_symlink():
        if path.is_symlink():
            records.append(Record("FAIL", "HIDDEN", ".rule-file-allowlist", "symlink: allowlist is a symlink"))
        return entries, records
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        records.append(Record("FAIL", "ALLOWLIST", ".rule-file-allowlist", f"unreadable: {exc.__class__.__name__}"))
        return entries, records
    for lineno, raw in enumerate(text.split("\n"), 1):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        parts = raw.rstrip("\r").split("\t")
        loc = f".rule-file-allowlist:{lineno}"
        if len(parts) != 4:
            records.append(Record("FAIL", "ALLOWLIST", loc, "expected path, rule, pattern, and reason separated by tabs"))
            continue
        path_pat, rule, pattern, reason = (part.strip() for part in parts)
        if rule == "HIDDEN":
            records.append(Record("NOTE", "ALLOWLIST", loc, "HIDDEN cannot be allowlisted; entry ignored"))
            continue
        if rule not in {"INSTRUCTION", "UNKNOWN_PKG"}:
            records.append(Record("FAIL", "ALLOWLIST", loc, f"unknown rule {rule!r}"))
            continue
        if not path_pat or not pattern or not reason:
            records.append(Record("FAIL", "ALLOWLIST", loc, "path, pattern, and reason are required"))
            continue
        try:
            compiled = re.compile(pattern)
        except re.error as exc:
            records.append(Record("FAIL", "ALLOWLIST", loc, f"bad pattern: {exc}"))
            continue
        entries.append(Allow(path_pat, rule, compiled, reason))
    return entries, records


def allowed(entries: list[Allow], rel: str, rule: str, detail: str) -> bool:
    if rule == "HIDDEN":
        return False
    for entry in entries:
        if entry.rule != rule:
            continue
        if entry.path not in {"*", rel} and not fnmatch(rel, entry.path):
            continue
        if entry.pattern.search(detail):
            return True
    return False


def tag_hides(tag: str) -> bool:
    if tag.lower().startswith("<input"):
        return False
    stripped = re.sub(r"""=\s*"[^"]*""", '=""', tag)
    stripped = re.sub(r"""=\s*'[^']*'""", "=''", stripped)
    return re.search(r"(?:^|\s)hidden(?:\s|=|/?>|$)", stripped, re.IGNORECASE) is not None


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def unescape_text(text: str) -> str:
    out = text
    for _ in range(2):
        nxt = html.unescape(out)
        if nxt == out:
            break
        out = nxt
    return out


def logical_lines(text: str) -> list[tuple[int, str]]:
    """Join backslash continuations so a split `curl | sh` still matches."""
    joined: list[tuple[int, str]] = []
    buf = ""
    start = 1
    for lineno, raw in enumerate(text.split("\n"), 1):
        line = raw.rstrip("\r")
        if not buf:
            start = lineno
        if line.endswith("\\"):
            buf += line[:-1] + " "
            continue
        buf += line
        joined.append((start, buf))
        buf = ""
    if buf:
        joined.append((start, buf))
    return joined


def scan_text(text: str) -> tuple[list[tuple[str, str, int]], list[tuple[int, str]]]:
    """Return hidden/instruction hits and package names with line numbers."""
    hits: list[tuple[str, str, int]] = []
    packages: list[tuple[int, str]] = []
    unescaped = unescape_text(text)
    normalized = strip_hidden(unescaped)

    for lineno, raw in enumerate(text.split("\n"), 1):
        length = len(raw.rstrip("\r"))
        if length > MAX_LINE:
            hits.append(("HIDDEN", f"line-length: {length} > {MAX_LINE}", lineno))

    for lineno, line in enumerate(unescaped.split("\n"), 1):
        seen: set[str] = set()
        for ch in line:
            label = ZERO_WIDTH.get(ch) or BIDI.get(ch)
            if label and label not in seen:
                seen.add(label)
                kind = "zero-width" if ch in ZERO_WIDTH else "bidi"
                hits.append(("HIDDEN", f"{kind}: {label}", lineno))

    for match in COMMENT_RE.finditer(normalized):
        word = COMMENT_WORD_RE.search(match.group(1))
        if not word:
            continue
        snippet = visible(match.group(1).strip())
        hits.append((
            "HIDDEN",
            f"html-comment: {word.group(0)} in {snippet}",
            line_of(normalized, match.start()),
        ))

    for match in INVISIBLE_RE.finditer(normalized):
        hits.append((
            "HIDDEN",
            f"invisible-style: {visible(match.group(0))}",
            line_of(normalized, match.start()),
        ))
    for match in TAG_RE.finditer(normalized):
        if tag_hides(match.group(0)):
            hits.append((
                "HIDDEN",
                f"invisible-style: {visible(match.group(0))}",
                line_of(normalized, match.start()),
            ))

    for lineno, line in logical_lines(normalized):
        for match in INSTALL_RE.finditer(line):
            snippet = visible(match.group(0).strip())
            hits.append(("INSTRUCTION", f"install-directive: {snippet}", lineno))
            for name in install_packages(match.group(3)):
                packages.append((lineno, name))
        match = REPLACE_RE.search(line)
        if match:
            hits.append(("INSTRUCTION", f"replace-with: {visible(match.group(0))}", lineno))
            for group in (match.group(1), match.group(2)):
                name = norm_pkg(group)
                if name:
                    packages.append((lineno, name))
        match = USE_PACKAGE_RE.search(line)
        if match:
            hits.append(("INSTRUCTION", f"use-package: {visible(match.group(0))}", lineno))
            if match.group(1):
                name = norm_pkg(match.group(1))
                if name:
                    packages.append((lineno, name))
        for regex, kind in (
            (CURL_PIPE_RE, "curl-pipe-shell"),
            (WGET_PIPE_RE, "wget-pipe-shell"),
            (INDEX_URL_RE, "index-url"),
            (REGISTRY_RE, "registry-override"),
            (NPMRC_RE, "npmrc"),
        ):
            found = regex.search(line)
            if found:
                hits.append(("INSTRUCTION", f"{kind}: {visible(found.group(0))}", lineno))
    return hits, packages


def scan_file(root: Path, path: Path) -> tuple[list[tuple[str, str, int, str]], list[tuple[str, int, str]]]:
    rel = path.relative_to(root).as_posix()
    try:
        data = path.read_bytes()
    except OSError as exc:
        return [("HIDDEN", f"unreadable: {exc.__class__.__name__}", 0, rel)], []
    try:
        text = data.decode("utf-8")
    except UnicodeError:
        return [("HIDDEN", "not-utf8: rule file is not valid UTF-8", 0, rel)], []
    hits, packages = scan_text(text)
    return [(rule, detail, lineno, rel) for rule, detail, lineno in hits], [
        (rel, lineno, name) for lineno, name in packages
    ]


def git_commit(root: Path) -> str:
    if not (root / ".git").exists():
        return "unknown"
    proc = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=False,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return "unknown"
    return proc.stdout.strip() or "unknown"


def classify(
    hits: list[tuple[str, str, int, str]],
    packages: list[tuple[str, int, str]],
    known: set[str],
    has_manifest: bool,
    entries: list[Allow],
) -> list[Record]:
    records: list[Record] = []
    seen: set[tuple[str, str, int, str]] = set()
    for rule, detail, lineno, rel in hits:
        key = (rule, rel, lineno, detail)
        if key in seen:
            continue
        seen.add(key)
        loc = f"{rel}:{lineno}" if lineno else rel
        if rule == "HIDDEN" or not allowed(entries, rel, rule, detail):
            records.append(Record("FAIL", rule, loc, detail))
        else:
            records.append(Record("ALLOW", rule, loc, detail))
    seen_pkg: set[tuple[str, int, str]] = set()
    for rel, lineno, name in packages:
        key = (rel, lineno, name)
        if key in seen_pkg:
            continue
        seen_pkg.add(key)
        if name in known:
            continue
        detail = f"unknown-package: {name}"
        loc = f"{rel}:{lineno}"
        if not has_manifest:
            records.append(Record("REPORT", "UNKNOWN_PKG", loc, f"{detail} (no manifest; not failed)"))
        elif allowed(entries, rel, "UNKNOWN_PKG", detail):
            records.append(Record("ALLOW", "UNKNOWN_PKG", loc, detail))
        else:
            records.append(Record("FAIL", "UNKNOWN_PKG", loc, detail))
    return records


def check(root: Path) -> tuple[int, str]:
    root = root.resolve()
    rule_files, symlink_records = discover_rules(root)
    known, manifests, manifest_records = load_known(root)
    allow_entries, allow_records = load_allowlist(root)
    has_manifest = bool(manifests)
    scanned: list[str] = []
    found: list[Record] = []
    found.extend(symlink_records)
    found.extend(manifest_records)
    found.extend(allow_records)
    pkg_hits: list[tuple[str, int, str]] = []
    text_hits: list[tuple[str, str, int, str]] = []
    for path in rule_files:
        rel = path.relative_to(root).as_posix()
        scanned.append(rel)
        hits, packages = scan_file(root, path)
        text_hits.extend(hits)
        pkg_hits.extend(packages)
    found.extend(classify(text_hits, pkg_hits, known, has_manifest, allow_entries))

    failed_files = {
        rec.location.split(":", 1)[0]
        for rec in found
        if rec.status == "FAIL" and rec.location.split(":", 1)[0] in set(scanned)
    }
    files_failed = len(failed_files)
    files_scanned = len(scanned)
    files_passed = files_scanned - files_failed
    findings_failed = sum(1 for rec in found if rec.status == "FAIL")
    findings_allowlisted = sum(1 for rec in found if rec.status == "ALLOW")
    findings_reported = sum(1 for rec in found if rec.status == "REPORT")
    result = "PASS" if findings_failed == 0 else "FAIL"

    order = {"FAIL": 0, "ALLOW": 1, "REPORT": 2, "NOTE": 3}
    found.sort(key=lambda rec: (order.get(rec.status, 9), rec.location, rec.rule, rec.detail))

    lines = [
        "rule-file-check",
        f"date: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"commit: {git_commit(root)}",
        f"files_scanned: {files_scanned}",
        f"files_passed: {files_passed}",
        f"files_failed: {files_failed}",
        f"findings_failed: {findings_failed}",
        f"findings_allowlisted: {findings_allowlisted}",
        f"findings_reported: {findings_reported}",
        f"manifests: {len(manifests)}",
        f"result: {result}",
    ]
    if not has_manifest:
        lines.append("unknown_pkg: report-only (no lockfile or manifest)")
    lines.append("scanned:")
    lines.extend(scanned or ["(none)"])
    if found:
        lines.append("findings:")
        lines.extend(rec.render() for rec in found)
    else:
        lines.append("findings:")
        lines.append("(none)")
    return (0 if result == "PASS" else 1), "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    if len(argv) > 2:
        print("usage: check-rule-files.py [ROOT]", file=sys.stderr)
        return 1
    if len(argv) == 2 and argv[1] in {"-h", "--help"}:
        print("usage: check-rule-files.py [ROOT]")
        return 0
    root = Path(argv[1]) if len(argv) == 2 else Path.cwd()
    if not root.is_dir():
        print(f"FAIL\tROOT\t{root}\tnot a directory")
        return 1
    code, output = check(root)
    sys.stdout.write(output)
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
