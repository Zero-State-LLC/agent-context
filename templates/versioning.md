# Zero State versioning rule

Every Zero State product repository follows this rule. Danny decided it on
2026-11-24 (see `DECISIONS.md`). Homer was the first to adopt it, with its
versioning spec and ADR 012 (`Zero-State-LLC/Homer`, `specs/versioning/`).
Read those for a worked example. Do not copy Homer's scripts here.

## The rule

1. **One product version per repository.** It is a SemVer 2.0.0 version in
   the repository's own manifest (`package.json`, `pyproject.toml`,
   `Cargo.toml`, the app's marketing version, and so on). Every package or
   module inside the repository has the same version. A contract or schema
   keeps its own version, separate from the product version.
2. **SemVer bumps.** From `1.0.0`, a breaking change is a major bump, an
   addition a minor one, and fixes alone a patch. In `0.x`, a breaking change
   or an addition is a minor bump, and fixes alone a patch.
3. **A `CHANGELOG.md` in [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)
   form.**
   - `## Unreleased` comes first.
   - Each version has a section of its own, `## [X.Y.Z] - YYYY-MM-DD`,
     newest first. Every version above `0.0.0` gets one, a release candidate
     included (`## [1.2.0-rc.1] - YYYY-MM-DD`).
   - A section lists what changed since the version before it.
   - A section holds only these subsections: `### Added`, `### Changed`,
     `### Deprecated`, `### Removed`, `### Fixed` and `### Security`. No entry
     sits outside one.
   - A change a user or another repository would notice gets a line under
     Unreleased in the pull request that makes it.
4. **A release is a pull request.** The release pull request, `release:
   vX.Y.Z`, sets the version and turns Unreleased into that version's
   section, then opens a new, empty Unreleased.
5. **Only a human tags.** After the release pull request merges, Danny, or
   the human owner the repository names, tags the merge commit with an
   annotated `vX.Y.Z` tag and pushes it. Agents never push a tag. A release
   candidate, `vX.Y.Z-rc.N`, is prepared and tagged the same way.
6. **Release notes come from the CHANGELOG.** A GitHub Release's notes are
   that version's CHANGELOG section, not a rewrite of it.
7. **CI checks it.** Each repository's CI fails when its versions disagree,
   when the CHANGELOG breaks rule 3, or when the version above `0.0.0` has no
   section. Use the repository's own tooling for the check.

## Adopting it in an existing repository

- Add `CHANGELOG.md` from [`CHANGELOG.md.template`](CHANGELOG.md.template)
  if the repository has none, and the CI check.
- Do not rewrite tags or history. Versions before adoption keep whatever
  record they have; the first section under the rule is the next version.
- A repository already on another scheme moves to this one at its next
  release. Record the move under that release's `### Changed`.
- A repository-specific need, such as build metadata (`1.2.0+a1b2c3d`) or a
  deployed service reporting its version, goes in that repository's spec. It
  does not change this rule.
- An exception to this rule needs its own dated entry in `DECISIONS.md`,
  like any other team rule.
