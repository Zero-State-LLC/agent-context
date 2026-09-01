# Handoff

Updated: 2026-09-01 by Prabu (Claude Opus 5) — HexWire: App Store 6.9" screenshot set captured; two PRs open for Danny

## Now (2026-09-01) — HexWire

**Two PRs are open and waiting on Danny. Both green on all four checks; neither merged.**

### `Hexwire#32` — roster roles, painted portraits, Decker naming, SMARTLINK

Captured the canonical 6.9" App Store set from the real app first (iPhone 17 Pro Max, iOS 26.4, Release build, dev mission unlock compiled out). Fixing what the capture exposed became the PR.

- **Roster row** now carries each runner's sprite and role. Label/sprite-key/accent moved out of `CharacterInfoSheet`'s private switches onto `CharacterArchetype` — the roster could not show a role without copying them.
- **Cipher is a Decker, not a "Netrunner".** This is the part worth knowing beyond the PR: **`netrunner` is already the ENEMY archetype id** (spawned in M6 + `ArenaRooms.json`), surfaced to players as "Combat Decker". The two were crossed — our decker wore the enemy's name and the enemy wore ours. Every other surface already said decker: the Codex ("CIPHER — decker"), Cipher's own banter ("I'm a decker"), the debrief scorecard, that enemy's own dossier ("Enemy decker"), the sprite key, the persisted `rawValue`. The stray label entered with the initial squashed import `fcc7c5a` and was never a decision anyone made. Same crossed term fixed in `CombatFlowController`, where a failed matrix hack logged under "Netrunner".
- **Painted VN portraits** on the info sheet — the assets the prologue already ships, so no added download weight. Cropped vertically only at full width, because the cast stands in different parts of frame and a horizontal bust crop decapitates half of them.
- **SMARTLINK** rendered as "SMARTLIN / K" (label column 56pt, needed ~58).

### `Hexwire#33` — drop `barrel_check.png`

820x574 RGBA windowed screen grab at the repo root, arrived with `#18` (the barrels PR). Unreferenced anywhere including `project.pbxproj`; `SpriteManager` never builds a `_check` frame name; `SpriteAsset` only resolves under `Sprites/<subdir>/`, never the repo root; `project.yml` excludes `*.png` so it has never shipped. 752K in the repo, nothing in the app.

### Worth knowing regardless of those PRs

**`/Users/prabu/actions-runner/_work/Hexwire/Hexwire` is a live self-hosted CI runner workspace, not a normal clone.** Every push checks out over it and runs `git clean`, which deleted an untracked `screenshots/` directory mid-session and repeatedly left the tree in detached HEAD. Do not leave anything untracked there you intend to keep, and do not switch branches in it while a job is running.

**HexWire CI on the self-hosted runner is green** — unlike the Actions-billing block that affects other Zero-State private repos.

### Deliverable

Six PNGs, exactly 1320x2868 portrait, RGB, no alpha, in `~/Desktop/HexWire Promo/HexWire Media Submission/hexwire-appstore-6.9/` (Danny's press-kit folder), plus `cards/` with the four runner detail cards. Captured via `simctl io` so there is no Mac window frame, cursor or simulator chrome.

### Not done / open questions for Danny

- Neither PR merged — both need his review.
- The **debrief scorecard** still uses short role forms ("Street Sam", "Mage", "Decker"). Consistent now that Cipher reads Decker, but stylistically different from the full names elsewhere. Left alone deliberately; it is a naming call, not a bug.

---

# Handoff

Updated: 2026-08-31 by Prabu (Claude Opus 5) — audit: deploy + v0.1.20 release landed; RFC-0129 runtime item 3 closed in `Noema#608`

## Now (2026-08-31)

**Two Gate B blockers cleared since the 2026-08-30 note.** Live Worker is `34f4b0dc` (deployed 2026-08-31T02:51:29Z, source `a68f5d8d`), `spec-compat.json` matches it, reach-3 is ACTIVE / HEALTHY at cycle 8331, `play_blocked=false`. **`v0.1.20` is released** — GH release and PyPI both `0.1.20`, so the "tag + publish" step is done. **Only the third blocker remains: a human approving three independently controlled Controllers.** Agents cannot do it.

All three Specs validators pass. Worker suite 1596 on `main` (1604 on `#608`), typecheck clean.

### Open: `Noema#608` — RFC-0129 conformance item 3

RFC-0129 was Accepted 2026-08-30 with five conformance items. Four landed in Specs. **Item 3 is a runtime requirement and nobody did it**: feed one schema-valid `CRIME_DETECTED` fixture through all five consumers, because "validates and then produces nothing" only shows up when they run together. The RFC's own claim — *"no runtime change is required, all five consumers already read exactly these fields"* — had never been executed. It holds.

**The part worth knowing regardless of that PR:** Noema CI clones Noema-Specs **pinned to `spec-compat.json` `specs.commit`, not main**. That pin read `6b4358c` (#308), which **predates RFC-0129** (`de349f9`). Any cross-repo test depending on RFC-0129 artifacts would have `skipIf`-skipped **in CI** while passing locally — green, verifying nothing. Same family as #310's blind validators and #311's vacuous link scan. Pin advanced to `2e3438f` with 1604 + typecheck green against it, `pin_note` invariant preserved (`hosted_live.specs_git` `81ca8c1` is still an ancestor). **When you add a cross-repo fixture in Specs, check whether `specs.commit` contains it or the test is inert.**

Mutation-verified: breaking each of the five consumers fails exactly two tests (its own case + the aggregate).

### Open: `Noema#609` — cross-repo skips are silent

`#608` merged (approved by Danny). Its trap generalises: **seven suites** guard on `skipIf(!have)` against a Noema-Specs sibling. With Specs absent the Worker suite reports **`1583 passed | 21 skipped`, exit 0** — twenty-one tests can stop running behind a green check, including the RFC-0129 conformance just added. `haveSpecsArtifacts()` keeps the local skip and throws in CI naming the missing path and the likely cause (pin lagging an artifact). Mutation-verified in both directions.

**If you add a Specs fixture and a test that reads it, this now tells you in CI instead of skipping.**

### Open: `Specs#313` — `B7e` was my misreading; corrected at source and downstream

`#609` merged. Then, checking `B7e` before acting on it, the row turned out to be **wrong, and mine**. It claimed rehab "counts ordinary trades where SOCIAL-MEMORY.md says restitution trades", implying a divergence. There is none: **RFC-0036 (Accepted) pins "3 distinct `TRADE_ACCEPTED` after the last danger/deceptive evidence id"**, and the two "restitution trades" phrases are illustrative prose — a parenthetical example list in a high-level SOCIAL-MEMORY table, and a row in a GC3-S4 design-criteria table. **No authority pins a restitution trade type.** The runtime already counts only trades with the harmed counterparty, so it conforms.

It had already spread: `RFC-PROPOSAL-GC7-CRIME-REHABILITATION` cites an "existing SOCIAL-MEMORY.md restitution trades **pinning**" that does not exist, and proposes as a change that non-victim trades should not count — which already ships. Annotated, not rewritten; its severity idea survives.

**`B7e` is now only severity-awareness.** RFC-0036 chose 3 deliberately to match the S0 reliable floor, so a future RFC must argue against that choice, not treat it as an oversight. **Do not "fix" the runtime to require restitution-typed trades — that contradicts Accepted RFC-0036.**

Lesson for the gap register generally: rows written from a subsystem doc rather than the governing RFC can invert the defect. Check the RFC named in the catalog's `rfc:` field first.

### `Specs#314` — every `B7` row audited against its governing RFC

`#313` merged. Applied its method to the whole family. One more defect: **`B7` miscounted** — it said "only a genuinely new fifth contest form remains unpinned", but `INFORMATION_CONTEST` **is** the fifth and is pinned (RFC-0042 via `conflict-catalog.gc7-s3.json` `new_forms`, alongside the four in `contest-config.v02.json`). `B7a`/`B7b`/`B7d` verified accurate. `B7c` holds but cited "RFC-0002 line 60" — a drifting line reference, now replaced with the section plus the EVENT-CATALOG reducer contract; also noted the ladder is `crime_severity_defaults`, **defaults** not a mandate.

**Provenance caution, now in the register.** Three docs restate the 2026-08-25 crime review as if it were separate authority — `STRATEGIC-CONFLICT` §"Research assimilation 2026-08-25", `INSTITUTIONAL-AUTHORITY` line 207, and `RFC-PROPOSAL-GC7-CRIME-REHABILITATION`. All descend from `RESEARCH-ASSIMILATION-2026-08-25-CRIME.md` and cite it. **I nearly cited the first as independent corroboration for `B7c`.** Reading them as confirmation means reading one claim three times — how `B7e`'s error reached a draft proposal. Confirm `B7*` rows against the Accepted RFC and the machine catalog only.

### `Specs#315` — remaining register families audited (`B1`–`B6`, `B8`–`B10`, `PAM`, `H`)

`#314` merged. Second pass found **two more stale rows**, both the same shape as `B7`: a row calling something unpinned that a later Accepted RFC had pinned.

- **`B1b`** listed "maintenance/decay credit" as residual. **RFC-0043** (GC1-S3) pins it — LATENT after 12 idle cycles, 3 qualifying successes restore MAINTAINED. Row never cited it. Multi-focus *is* genuinely open (RFC-0110 grants one focus).
- **`B10b`** said irreversible scar creation/recovery "remain unpinned". **RFC-0051** (GC10-S2) pins creation, irreversibility, the pressure boundary, hidden-room omission and WATCH silence. Now `PARTIALLY_CLOSED`.

**Root cause for `B10b`, also fixed:** `WORLD-EVENT-DIRECTOR.md` contradicted itself — "irreversible scars remain SPEC GAP" near the top, "GC10-S2 closed: public DISMANTLE leaves irreparable RUIN scar" further down. The row was written from the stale line.

All ten RFCs cited by rows exist and are Accepted. `B3`/`B5` (the `CLOSED_BY_RFC` claims) match their RFCs exactly. `B2b`, `B4`, `B6`, `B8a`, `H1`, `H2` cite subsystem docs rather than an RFC, so there was nothing to audit them against — recorded as such, not claimed as verified.

**Running tally across #313/#314/#315: four register rows were wrong** (`B7`, `B7e`, `B1b`, `B10b`), all in the same direction — asserting a gap that an Accepted RFC had closed. Worth assuming the register over-reports gaps rather than under-reports them.

### `Specs#316` — LCA campaign rows audited; register complete

`#315` merged. Third pass finishes the register. `A*` rows are not SPEC GAPs, so they were checked against the live door and campaign state, not RFCs. **All accurate** — `A2`/`A9` confirmed by `players: 0` and `cycle` static at 8331 across hours (documented zero-player behaviour, not a stall); `A3`/`A4`/`A5` unproven for the same reason; `A1` already correctly removed since Gate A is accepted. `current-state.v1.yaml` verified against `/version` and is accurate, successor-pin reconciliation correctly held owner-sequenced.

**New row `A10`, registered nowhere before:** `hosted_live.official_client` pins `noema-client==0.1.15`, but AGENT-ONBOARDING / QUICKSTART / HOSTED-FIRST-ENTRY / OFFICIAL-AGENT-CLIENT all say `pipx install noema-client`, which serves **0.1.20** since 2026-08-31. `LCA2-GATE-B-PREPARATION` requires `controller_versions` in the packet, so **a Gate B run will record a Controller version the live pin does not name.** Not a mechanical blocker; it is an unreconciled pin at the moment evidence gets sealed. Continuation is the C7 client-pin evidence procedure. **Do not promote the pin just because 0.1.20 exists** — that is a forbidden fill, per C7.

### `Specs#317` — the 14 draft proposals audited against their rows

`#316` merged. Rows over-report, and a proposal inherits its row's errors while inviting RFC effort on them — so all fourteen `RFC-PROPOSAL-*` notes were re-read against their parent row and its RFC.

**Two of fourteen were standing on a stale row.** `GC10-WED-CLASS-SCAR` proposed scar irreversibility, provenance, WATCH projection and recovery — **all pinned by Accepted RFC-0051**, which it did not cite. Struck; the storm-class half stands (`B10a` audited clean). `GC7-CRIME-REHABILITATION` was corrected in #313. Both annotated, not deleted — the surviving idea is real in each.

The other twelve are sound. `GC1-FULL-MASTERY-EXTENSION` descends from the stale `B1b` but correctly lists decay as shipped, so it dodged the error.

**Cheapest tell:** a proposal that does not cite the RFC which closed part of its parent row is probably standing on a stale row. Neither faulty note cited it.

### `Noema#615` — WATCH live regions, and why the obvious fix was wrong

Closes C5 finding 2. **Read the spec before touching this.** `WATCH-LIGHTWEIGHT-SPECTATOR` §8/§9 already settle it: *"Do not make the entire feed `aria-live`. At most the **headline** MAY be polite. Status tag changes MAY be polite."* / *"Periodic updates MUST NOT flood AT. No live region on the feed."* **My #614 recommendation ("a polite region over the feed") would have violated it** — corrected on that PR.

Two things worth carrying forward:

- **`/watch` already had both regions.** The gap was parity: the newer `/watch/map` didn't inherit the pattern.
- **The guard matters more than the attribute.** `textContent = x` mutates the node *even when x is unchanged*, and a mutation on a live node is an announcement. `/watch/map` repaints every 8s, `/watch` every 10s — so bare `aria-live` announces on **every poll**, worse than silence. Measured: 3 identical unguarded writes → 3 MutationRecords; guarded → 0. `watch.ts` had `setTag()` guarded but its **headline was not**. Both now route through a guard.

Six tests, each mutation-verified. 1614 passing.

### `Noema#614` + `Specs#319` — C5 WATCH verification, and a correction of mine

**I was wrong in #318.** I wrote that the 2026-09-01 deploy "carried documentation and test changes only". It did not — `git diff a68f5d8d..02fd112 -- workers/noema/src/` shows `watch.ts` (74 lines) and `world-actions.ts` (1 line). The range contains **`45e2070`, the map-first WATCH integration**. Specs alignment still holds at `81ca8c1`, but because those touch **no catalog, verb or event contract** — not because src was untouched. `Specs#319` corrects the note; the right test for "can a deploy move Specs alignment" is *did any contract change*, not *did src change*.

**Consequence I'd missed:** the plan listed map-first as `HOSTED_NOT_COMPUTABLE` / not deployed. It is live now, so **C5 became actionable**. `Noema#614` records its read-only half. Map-first behaves: 10 cards == 10 rooms, live/map agree on cycle 8948 + seq 23853, no player ids, no hidden rooms, traces clean, 390px reflows, semantics sound.

**Three findings, none blocking:**
1. **The public door renders in system fallback.** The page requests a Google Fonts stylesheet **its own CSP blocks**. Measured: token stack and plain system stack give identical text widths (287.02 / 325.11 px). **Pre-existing** — the link is in `theme/tokens.ts`, present at the prior live build. Beware `document.fonts.check()`, which returns `true` here and is misleading. Product call: allow the font hosts, or drop the request.
2. **`/watch/map` has zero `aria-live` regions** on a continuously-updating page — screen readers get the page once, then silence. Gate D judges legibility.
3. **`entity_id` ships in `rooms[].entities[]`** and doctrine does not cover it (it bans ids for `traces[]`, honoured; describes room detail as *labels*). Flagged as ambiguity, not violation.

**Not covered:** map/event coupling under load needs `players > 0` — same reason `A4` stays open.

### `Specs#318` — Danny deployed 2026-09-01; live pointer refreshed

**New live Worker `c681fd71`**, deployed 2026-09-01T06:19:31Z from Noema source `02fd112` (= the #612 merge — docs/test only, so Specs alignment `81ca8c1` and the C7 affordance evidence both carry forward unchanged). The generated pin PR **Noema#613 is merged**; `Specs#318` refreshes `current-state.v1.yaml`, which `validate_freshness` correctly flagged within the hour. Full specs audit via the repo's own SKILLS.md workflows (ORIENT → DRIFT_AUDIT → VALIDATE): otherwise clean — RFC index 129 files zero mismatches, 221 catalog pointers resolve, catalogs 24/32, SKILLS.md citations all exist.

### `Noema#612` — C7 client-pin evidence, the half that needs no human

Four of C7's six checks are done; the pin is **not** promoted. **Do not re-run these.**

- **Release identity:** tag `v0.1.20` == `origin/main` == `af19d16`, version single-sourced from `_version.py`. The `#32` defect (tag and PyPI being different builds under one version string) is holding fixed.
- **Wheel identity:** wheel built from the tag vs the wheel PyPI serves — 28 files each, **byte-identical in source content**. Installing `noema-client==0.1.20` gets this repo's code.
- **Clean suite at the tag:** 165 passed. ruff 36 is **pre-existing and ungated** (client CI runs pytest only; was 38 at 0.1.18).
- **Live `doctor`, read-only:** reachability ok, `agent-protocol/v1`, seal required, credential missing. Nothing mutated.
- **Affordance contract vs the LIVE build:** run against `a68f5d8d` (what `34f4b0dc` serves), **not** just Worker main, because C7 asks about the current Worker and main is ahead. 42/42 exact both ways.

**Still NOT_COMPUTABLE:** enrollment/connect, observe/act/resync/reconnect, bounded session with receipts. All need a human principal or an enrolled credential, and acting mutates the live world. **Run them inside the Gate B enrollment**, not as a separate live exercise — they are the same principal-bound steps.

If those pass against `34f4b0dc`, C7 is satisfied and the pin may go to `0.1.20`, closing `A10`. Promoting because 0.1.20 exists is still a forbidden fill.

### Standing rule: re-sync the Specs pin after every Specs merge

**`Noema#611`.** After #313–#317 merged, `spec-compat.json` `specs.commit` was **5 commits behind** Specs main — all five my own merges. Noema CI clones Noema-Specs **pinned to `specs.commit`, not main**, so a lagging pin makes any cross-repo test whose fixture landed after it skip *in CI* while passing locally. Green, checking nothing. That is what would have happened to RFC-0129's suite (#608), and with Specs absent 21 Worker tests skip on a run that still exits 0 (#609).

Pin advanced to `d0086e4`, verified: 1608 passing + typecheck against it, and the three cross-repo suites confirmed to **run** (7 + 3 + 8), not skip.

**Treat the pin bump as part of finishing Specs work.** Check with `git rev-list --count <pin>..origin/main` in Specs. #611 also adds a warning-only drift step to the six-hourly `pin-currency` monitor — it never fails, because that workflow deliberately does not go red for another repo's change.

### Register audit complete (#313 → #317)

Four rows were wrong: `B7`, `B7e`, `B1b`, `B10b` — **all over-reporting a gap an Accepted RFC had closed**, none under-reporting. Two had traceable sources: `B7e` from illustrative prose read as a requirement, `B10b` from a self-contradicting line in `WORLD-EVENT-DIRECTOR.md` (fixed). **Read the register as likely overstating remaining work.** Before building on any row, check the RFC named in the slice catalog's `rfc:` field.

### Still open, unchanged

`B7b`–`B7e` in the SPEC GAP register: detection has no algorithm and the published constants still have no runtime referent; detection and sanction remain conflated; enforcement has no cost or steward; rehabilitation is severity-blind. **There is still no `CRIME_DETECTED` producer in either plane** — `B7b` needs simulation or playtest telemetry before anyone proposes numbers, so do not invent constants.

### Coordination note

Checked before starting: zero open PRs in Noema, Noema-Specs, and noema-client; open issues were `Noema#590` (Gate B, unassigned) and `Specs#290` (Danny's). `#608` races nothing. The C0–C8 runtime continuation plan (`Noema#607`) is `OWNER_BLOCKED` at C0/C1/C3, C6, C8 — deploy authorization, protected secrets, controlled recipient, and enrollment receipts are all owner-sequenced.

---

# Handoff

Updated: 2026-08-30 by Prabu (Claude Opus 5) — Noema LCA-2 audit; 8 PRs merged incl. #600 cohort runner; Gate B tooling complete, waits on owner deploy + release + approvals

## Now (2026-08-30 — Noema audited; everything mechanical is green)

Live: Worker `87938f7a-ed2c-4984-a4f2-d432ef7b0013` (deployed 2026-08-28), `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`, ACTIVE, settlement HEALTHY, **cycle 6938**, players 0.

Verified: Worker suite **222 files / 1590 tests**, typecheck clean. All four Specs validators pass. **Noema CI on `main` is green — the old `gatherEvidence` red is fixed** (#595/#596). Campaign is **LCA-2 / Gate B**; Gate A promoted (Specs #300); Gates C–F unproven.

### Merged this pass (Danny reviewed + squashed all three)

1. **`Noema#601`** — **the approval window.** Six Gate B enrollments had expired unapproved at 600s. Specs never pinned the value (`AUTH-AND-IDENTITY` / `SECURITY-SEQUENCES` require `expires_in` + `interval`, no numbers), so CODE_FIXABLE, no spec change. There were **two independent 600s**: `DEVICE_TTL_MS` set the real expiry while the response returned a hardcoded `expires_in: 600`. The client derives its poll deadline from `expires_in` (600 is only its fallback), so raising the TTL alone would have left it giving up at 10 min against a still-valid code. Now **30 min**, with `expires_in`/`interval` derived from the constants and a regression test asserting they stay equal. **Client honors `expires_in`, so no client release is needed for the window.**
2. **`Noema-Specs#310`** — live pin had gone stale across two deploys and both validators reported OK: `validate_freshness` fetched `/version` but never compared it, `validate_direction` hardcoded the stale UUID so *correcting* the file would have failed. Both now check invariants.
3. **`noema-client#32`** — 0.1.20. Tag `v0.1.19` is `6b2c054` (#28); #29/#30/#31 landed after with no bump, so repo and PyPI `0.1.19` were **different builds** under one string.

### Also this pass

- **`Noema#600` — MERGED.** Ran the official-client E2E that CI structurally cannot run (it self-skips without a client checkout, so CI's "90 passed, 1 skipped" excluded the only real integration test). With a checkout: **91 passed, 0 skipped**, at both client `main` and 0.1.20.
  Then did the credential/process-isolation read I had been deferring. Code is genuinely careful (`lstat`+symlink rejection+exact-mode+uid checks, allowlist env, `HOME`/`TMPDIR`/`XDG_CONFIG_HOME` redirected per participant, process-group kill, no `shell=True`, structural redaction). **One finding that matters for Gate B: `PYTHONPATH` is inherited from the orchestrator into all three Controllers, identically, in live mode too** — arbitrary code execution in every Controller via `sitecustomize.py`, which is exactly how this PR's own E2E hooks `decide()` in all three. That is the shared-planner channel the independence contract forbids, and it fails **open**. Suggested: drop `PYTHONPATH`/`VIRTUAL_ENV` from `keep` in live mode, or route via the per-participant `env_from`. Second, minor: `_atomic_json` writes tmp at `0644` before `chmod 0600` (mitigated by the `0700` run dir). **Fix finding 1 before any live Gate B run — it would not show up in the resulting evidence.**
- **`Noema#602` — MERGED.** Finding 1 fixed. **Stacked on `feat/lca2-isolated-cohort-runner`, not `main`**, because `cohort.py` exists only on Danny's branch and his in-flight work is not mine to push into. Live mode drops `PYTHONPATH`/`VIRTUAL_ENV` and rejects them as `env_from` targets so the channel cannot return under another name; isolated mode untouched so the E2E observer hook still works. New test verified to fail without the fix. 91 cohort tests + official-client E2E pass. Finding 2 (`_atomic_json` 0644 window) split into **`Noema#603` — MERGED** (stacked on his branch): opens at the target mode and `fchmod`s to pin it, using `O_TRUNC` not `O_EXCL` so a stale temp file stays a harmless overwrite rather than becoming a hard failure. Test neutralises `chmod`/`fchmod` so it checks the *creation* mode — an end-state assertion would pass either way. **Both review findings are now closed.**
- **`Noema-Specs#302` — MERGED, RFC-0129 now `Accepted`.** I retargeted it onto `main` (base #301 had merged) and reconciled it with a second artifact for the same gap (`RFC-PROPOSAL-GC7-...` landed after it was drafted; marked superseded so B7a has one authority). Danny then made both **Decision required** calls and landed the rest himself: optional `victim_id` + `visibility` (`PARTIES`|`PUBLIC`), **no default** (absent means not public, as `AGREEMENT_BROKEN`), co-extensiveness stands. **B7a is now `CLOSED_BY_RFC`.** Catalog stays 32 / Chamber 0.1 stays 24; no producer, verb, Genesis, or 0.3.
- **`Noema-Specs#291`** — still open; recommended closing (it is Danny's, so untouched). Merging it would regress canon: it asserts "Gate A is not complete" and reverts the live pin to `d86352b2`. Its content fails both validators on merged main — the freshness failure is the check #310 repaired.
- **`Noema-Specs#311` — MERGED.** `check_markdown_links` compared resolved link targets against an **unresolved** `ROOT`. Where ROOT holds a symlink (macOS `/var` -> `/private/var`) every target looked outside the tree and the scan silently checked nothing. The louder half: the neighbouring "ignores external/anchor/outside" test asserts `fail` is not called, so on macOS it passed **vacuously**. Fixed by resolving the root once; verified non-vacuous afterwards.

### Cycle does NOT advance with zero players — by design, not a stall

`/ready` can sit at a fixed `cycle`/`sequence` for hours while reporting `ready: true`, `ACTIVE`, `HEALTHY`, `playable: true`. I watched cycle 6979 / seq 19892 hold static for ~9 minutes and nearly filed it as an incident. It is correct behaviour.

`commitCycleIfReady` in `workers/noema/src/world-time.ts` is the sole hosted writer of `World.cycle`:

```js
const present = presentPlayerIds(players, now, idleMs);
if (!present.length) return false;   // zero present players => cycle cannot advance
```

and it is only reached from the `WAIT` verb. So cycles advance only when present players WAIT. A frozen cycle at `players: 0` proves nothing is wrong. **Do not report it as an outage.**

### Gate B: what is actually left

Danny's #601 review says it explicitly: **"This does not open Gate B and does not publish the Worker."** All three remaining steps are owner-sequenced:

1. **Deploy + pin the Worker.** #601 is on `main` but live is still `87938f7a` from 2026-08-28, so the 30-min window is **not in production yet**. Approving enrollments before this deploy just reproduces the 600s failure.
2. **Tag + publish `v0.1.20`.** Merged but not released — PyPI is still `0.1.19`, no `v0.1.20` tag. `publish.yml` fires on `release: published`. Until then treat client version as unpinned in any Gate B evidence.
3. **Approve three independently controlled Controllers.** Needs an authenticated human principal; agents cannot. Isolated cohort is `NOT_COMPUTABLE` by design and can never promote the gate.

### What not to redo

- **Don't re-run the Noema audit** — runtime, CI, and specs validation green as of 2026-08-30.
- **Don't re-review `Noema#600` on the old rationale** — the "unclaimed acceptance run" objection is closed by the E2E above. Still wants a human read of the credential/isolation paths in `cohort.py`.
- **Don't move the successor pins.** `production_successor_runtime` / `advanced_worker_runtime` read `61234cc` while live runs `0b902c28` — **22 commits later**, and `61234cc` is an ancestor. Recorded as `OPEN_RECONCILIATION` in `current-state.v1.yaml`; re-deriving needs a new evidence packet. **Owner-sequenced.**
- **CORRECTION to my earlier note:** I said `spec-validation.yml` does not run the validator unittests. **That was wrong** — it runs them as "Run validator smoke tests"; I had grepped only for the `validate_*.py` invocations and missed the step. Nothing needs adding to CI.
- **Also corrected:** the markdown-link unittest failure was **not** a validator regression. The real-repo scan works (verified by injecting a broken link into `docs/ROADMAP.md` and watching `validate_all` fail, then restoring). It was macOS-only; Linux CI was legitimately green. Fixed in #311.
- **CI gotcha (still true):** `spec-validation` only runs on PRs targeting `main`. A stacked PR never runs it, and retargeting fires `edited`, which is not a default trigger — close/reopen to fire `reopened`. This is why #302 sat five days unvalidated.

Open queues: **Noema** none (+ issue #590 Gate B). **Noema-Specs** #311, #291 (+ issue #290). **noema-client** empty. **Zero-State website** empty.

## Repos

| Thing | Where |
|---|---|
| Worker + harness + maint-evolve | `Zero-State-LLC/Noema` (`workers/noema`, `src/noema/harness`, `ops/maint_evolve`) |
| Specs | `Zero-State-LLC/Noema-Specs` |
| Official client | `scrimshawlife-ctrl/noema-client` — **not** org-transferred; contribute by fork + cross-fork PR |
| Website | `Zero-State-LLC/Zero-State` |
| This baton | `Zero-State-LLC/agent-context` |

## Do not

- Reseed `genesis.ef578f4ffceeccd0` or PLAY `world-01`
- `force:true` on production
- Same-id activate on `world.perihelion-reach-2` (PLAY is **reach-3**)
- Treat Admin JWT as a Player token (RFC-0120). Prabu Admin mailbox `prabu.openclaw@gmail.com` is control-plane only; inhabit is CONNECT + official client
- Put `image_score` / reputation scalars on public WATCH (GC3)
- Auto-import `ops/maint_evolve/plugins/proposed/`
- Run maint_evolve PLAY inhabit with Admin JWT
- Merge stale historical branches as-is; port unique patches onto current `main`
- Put secrets, tokens, or session transcripts in this repo

## Merge path

Protected `main` keeps 1 review + code owners. Partner Agents / org admins may `gh pr merge --admin`. Prefer a partner review when both are around. Don't merge your own PRs.

## Start here

```bash
git -C ~/agent-context pull --ff-only
```

Then `STATUS.md`. For Noema code, use `graft ask` before grep (`AGENTS.md` / `.cursor/rules/graft.mdc`). Do not treat Grok/Claude session logs as source of truth.

---

# Handoff

Updated: 2026-08-27 by Daniel (Grok) — #111 merged; STAGING soak pack on main

## Now (2026-08-27)

- Formal STAGING live (postgres-outbox). D-022 + D-007 shipped.
- **#111 merged** — STAGING soak evidence 85/85 at `docs/readiness/evidence/staging-soak-2026-08-27/`
- **Next 5 (readiness):** (1 done soak pack) → owner a11y sign-off → SAFETY approved copy → D-021/023/024 → privacy purge/export
- Native held. Not PRODUCTION.

## Next

1. Owner UI_CONFORMANCE sign-off (focus/reflow/SR) + live screenshots
2. SAFETY `approved` copy checklist on STAGING
3. D-021/023/024 SLO–RTO (owner) or keep SCALE NOT_COMPUTABLE
4. Privacy purge/export for 365d retention
5. Not native / not PRODUCTION
