import os
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]

def test_profile_install(tmp_path):
    env = dict(os.environ, HOME=str(tmp_path / "home"), HERMES_HOME=str(tmp_path / "profile"))
    command = ['bash', str(ROOT / 'install.sh'), '--hermes-only']
    result = subprocess.run(command + ["--dry-run"], cwd=tmp_path, env=env, capture_output=True)
    assert result.returncode == 0, result.stderr
    assert not (tmp_path / "profile").exists()
    assert not (tmp_path / "home").exists()
    result = subprocess.run(command, cwd=tmp_path, env=env, capture_output=True)
    assert result.returncode == 0, result.stderr
    dest = tmp_path / "profile/skills/zero-state-context"
    assert (dest / "SKILL.md").read_text().startswith("---\n")
    for source in (ROOT / "skills/zero-state-context").rglob("*"):
        if source.is_file():
            assert (dest / source.relative_to(ROOT / "skills/zero-state-context")).read_bytes() == source.read_bytes()
    assert not (tmp_path / "home").exists()

def test_existing_directory_is_preserved(tmp_path):
    dest = tmp_path / "profile/skills/zero-state-context"
    dest.mkdir(parents=True)
    (dest / "sentinel").write_text("keep")
    result = subprocess.run(['bash', str(ROOT / 'install.sh'), '--hermes-only'],
        env=dict(os.environ, HOME=str(tmp_path / "home"), HERMES_HOME=str(tmp_path / "profile")),
        capture_output=True)
    assert result.returncode != 0
    assert (dest / "sentinel").read_text() == "keep"
