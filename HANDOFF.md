# Handoff

**2026-09-04 — templates canon (pointer only; not the baton).** Product-repo collab files live in [`templates/`](templates/) (`intent.md` stage-0, slim `AGENTS.md`, Workflows). Dated lock in `DECISIONS.md`. Live team baton below is unchanged.

Updated: 2026-10-01 (later) by Prabu (Claude Opus 5.5). **SS: the stealth reward is merged (D-101, "quiet approach").** Runtime main `0b433de`, pinned SS-specs `01f9c89` (`ss-rules-006`, content-006).

- **Rule:** a latched `quietApproach` flag clears in phase 14 if the Detection State reaches `tracked` before M-C activates. M-C's forced Lockdown resolves on the same tick and never costs it. If it holds at boss activation, the court restore is 60% (90), not 50% (75).
- **HUD:** a `( ) QUIET` tag beside the state label, plus the `QUIET APPROACH LOST` and `QUIET APPROACH • INTEGRITY 90` captions, all read from the latch.
- **Probe** (540 runs): legal wins 57/65/53% (competent/stealth/loud); stealth is +12 over loud, at the ~65% cap. Loud and competent are unchanged. Quiet kept in 73% of stealth runs and 2% of loud. Medians 5:06–5:36.
- **GHOST fix:** the D-095 event-based GHOST was unearnable, because the forced Lockdown's phase-14 `detectionStateChanged` is published before M-C's phase-15 `waveStarted`. It now reads the latch (RS-024).
- **Traps:**
  - A `gh` network reset mid-script left an empty variable, which wrote an empty pin. Check the merge commit is non-empty before sed-replacing pins.
  - Presentation structs used by the app target need public inits; build the app locally before pushing.
- **Next:** Luna's on-device playtest. Also, the `QUIET APPROACH LOST` caption is tested but has not been seen on screen.

Prior: Updated: 2026-10-01 by Prabu (Claude Opus 5.5). **SS: the "make this one level dope" program is merged (D-094 to D-100).** Runtime main `902f4ef`, pinned SS-specs `a674ac0` (`ss-rules-005`, content-005, arena-004); spec and runtime are fully in sync (#110 pinned D-100 and added tests for its clarifications).

- **D-094, readability (#107):** the camera shows 704 × 326, actors get ground shadows and faction outlines, fog thins while an aware enemy is on screen, and captions are capped.
- **D-095 medals and D-097 to D-099 feel pass 2 (#109):**
  - medals GHOST, SHADOW, BLACKOUT, SURGICAL and SWIFT, stored per day, on the run card and the title;
  - takedowns (hit-stop, desaturating ring, pitched impact, streak);
  - patrol near-miss edges, in the cone's blue, never pickup gold;
  - a 2 s intro with no tick, and tutorial lines one at a time;
  - a daily grade, fog and headline.
  - All presentation only; a test proves digests and receipts are identical with and without it.
- **D-096, Captain Court climax (#108):**
  - on boss activation the Player is raised to at least 50% Integrity (75);
  - boss contact damage is 10 DPS;
  - each phase gets its own court lighting, and telegraphs get countdown rings.
  - **Final probe** (540 runs): legal wins 56/52/53%, medians 5:32/5:03/5:35. Boss-fight damage is cone 64–67%, bolts 27–29%, contact 6–9%.
  - The first probe at 60% won 58/68/66%, over the ~65% cap. The D-093 "contact 32%" figure had included cone hits; the probe now books them apart.
- **D-100 (SS-specs #58):** the spec records 7 choices #109 made where D-097 to D-099 were silent.
- **Process:** Danny's Cursor agent superseded SS-specs #55 with #57 (rebased, but still at 60%). I pushed the 50% commit and the probe onto #57 and merged it.
- **Traps:**
  - **A background sweep's `git checkout` can abort on local edits and silently test the old build.** Check `git log -1` in the sweep tree before trusting a sweep.
  - App CI uses an older Swift with stricter actor checks than local Xcode 26. SpriteKit node builders in static helpers need `@MainActor`.
  - Agents killing `xcodebuild` or `swift-frontend` by pattern can kill another agent's build.
- **Next:**
  1. Luna's on-device playtest. This is the evidence for the stealth targets D-093 left open: stealth should win more than loud, and stealth should slip past the patrol.
  2. (Correction 2026-10-02: art pack 2 was already delivered and merged in SS-runtime #97 on 2026-09-28; the deliverables are byte-identical. No art is outstanding.)
  3. A stealth reward, if the playtest confirms stealth doesn't pay.

Prior: Updated: 2026-09-30 by Prabu (Claude Opus 5.5). **SS: awareness, pacing and the Transit Patrol are merged; the build is ready for Luna's first playtest.** Runtime main `f635be4`, pinned SS-specs `92460a2` (`ss-rules-004`, content-004, arena-003).

- **D-089, awareness and ambush:** enemies start unaware; the first hit is an ambush (now ×3); surveillance (`tracked`+) alerts everyone.
- **D-090, pacing:** sight 320, unaware drift 25%, enemy Integrity ×1.5 (boss 1600), the Player takes 50% damage (exact remainder carried). The § 5 windows fit the arena as built (it crosses in about 10 s).
- **D-091 to D-093, Transit Patrol:** three members in Z-02 with visible 45°/240-unit cones and 200% Integrity. They are targeted only within 240 units and only while the Player moves toward them, so walking past holds fire. Fairness is proven over one hour of joint simulation for every legal Camera subset. Player Integrity is 150.
- **Final probe** (540 runs): competent wins have a median of 5:07; win rates are about 40%; stealth's ambush share is 35% against loud's 2%; sight causes 34–54% of alerts.
  - Short: the stealth win rate is roughly equal to loud's, and the stealth pilot cannot slip past the patrol.
  - Luna accepted merging and judging these by playtest (recorded in D-093).
- **CI fix (#104):** the SwiftPM job runs on Xcode 26.3. The runner default (Xcode 16.4 / Swift 6.1) needed over 5× the debug stack and crashed Swift Testing workers with SIGBUS.
- **Traps:**
  - Long-running subagents stall on 10-minute silent tool calls. Run sweeps in the background and poll; checkpoint-push often.
  - Git identity is set repo-locally in the SS repos, because hostname detection broke.
  - **Specs first, then runtime** (standing owner rule).
- **Next:** Luna plays daily runs (sneaky, loud, natural), then tuning from feel; T903/T904 external playtests; devices / D-020.

Prior: Updated: 2026-09-29 by Prabu (Claude Opus 5.5). **SS: bets 1 and 2 and the game-feel pass are merged.** Runtime main `a01d8a4`, pinned SS-specs `b79df66`. 561 tests and 26 app tests pass.

- **Bet 2 (D-081, #100):** a Daily Run (UTC-date seed, so the same Camera layout for everyone that day), a presentation-only ghost of today's best, and a run card with Share.
- **Bet 1 (D-082–D-087, #101), `ss-rules-002`, content-002, arena-002:**
  - Cameras are shot only when you move toward them.
  - Heat reinforcements in M-A/M-B: tracked +1, hunted/lockdown +2.
  - Tamper is +150 per destroyed Camera, with a recovery floor of 150 × Cameras destroyed.
  - A Camera's own mount never blocks shots at it.
  - `cam-z02-d` moved off the transit kiosk.
  - Probes: stealth 0.55 reinforcements per run (0.38 without Ricochet, the loud build), loud 4.58. #102 is closed.
- **Game feel (D-088, #103):** the 10 specified VFX recipes now render (they never had), plus hit-stop and shake. New big moments: Camera kill, Network Blackout (dim, cascade, music drop), boss phase break, heat chevrons. The Captain telegraph has no freeze.
- **Traps:**
  - `SSRuntime.xcodeproj` is generated. Run `xcodegen generate` before a local `xcodebuild`, or new files look missing.
  - Resolving pin conflicts with `--theirs` can drop real changes in `ContractVersions.swift`. Diff that file after taking a side.
  - Scenario tests must move toward a Camera to shoot it (D-082).
- **Open:**
  1. Runs are still 3–3.5 min against the 5–8 target.
  2. Luna's first playtest (3 daily runs: sneaky, loud, natural).
  3. Option B, awareness AI.
  4. T903/T904 playtests, devices / D-020, #31.

Prior: Updated: 2026-09-28 by Prabu (Claude Opus 5.5). **SS: every open PR is merged; the run target is now 5–8 minutes; all art and audio IDs are delivered.**

- **Merged today (Luna directed each merge in chat):**
  - SS-specs #43 (D-077 boss telegraph cues from Hexwire).
  - SS-specs #44 (D-078: Captain Camera, trolley wires, rooftop kit = solid art; **T507 and T800 done**).
  - SS-specs #45 (T305/T901 evidence, both PARTIAL).
  - SS-specs #46 (**constitution 1.2.0**: run target 5–8 min, D-079; supported architecture = arm64 on a D-020 device, D-080. Luna gave owner approval on the PR).
  - SS-specs #47 (intent accepted).
  - SS-runtime #96 (boss telegraph audio), #97 (Captain Camera and wires), #98 (pacing probes and long replay), #99 (`PacingSegment`/`PacingTimeline`: the arena § 5 table as data, reported not enforced).
- **Runtime:** main `feada63`, pinned SS-specs `a03c847`. 479 tests and 19 app tests pass, parity OK.
- **Audio:** all 32 cue IDs play.
  - The Hexwire SFX (`trace_warning`, `mech_autocannon`, `agi_attack_burst`) ship **level-matched**: gain −4.7/−11.2/−9.6 dB to a −15 dBFS loudest 400 ms, zero clipping. The masters are 10–15 dB hot and partly clipped.
  - `AudioEngine` previously played only `adaptedAdmitted` audio. The playable set is now `AssetCatalog.deliveredAudioPaths` (tested).
- **Captain Camera:** its own env group, `captain`, matched by longest prefix. First-prefix matching would have unbacked all 5 standard housings.
- **Pacing (T305 probes):** a perfect-route bot run takes 3:43 median; the content floor is about 2:20. That drove the retarget; playtests confirm it.
- **Art packs:** pack 2 is at `~/Documents/claude/SS-art-pack-2`.
  - **Codex saves output in its own folder** (`~/Documents/Codex/2026-09-27/plea/{work,outputs}/`), not ours. Look there first.
- **Traps:**
  - `git add -A` in SS-runtime stages the agent worktree under `.claude/worktrees/` as a gitlink. Add explicit paths.
  - The auto-mode classifier blocks `gh pr merge --auto` and merges without explicit direction.
  - Constitution changes need explicit owner approval (Governance 5).
- **Next (none of it is agent code):**
  1. T903/T904 playtests. `PacingTimeline` makes each recording show segment and run times against the table.
  2. Physical-device rows (T406/T606/T901/T905), blocked on D-020 device classes.
  3. SS-specs #31 lethal warning: Danny's call.
  4. Hexwire audio-rights evidence (plan-on-date), which also covers the 3 boss telegraph cues.

Prior: Updated: 2026-09-27 (end of day) by Prabu (Claude Opus 5.5). **SS: everything opened today is merged, T602 art is in, and T602 is done.**

- **Merged at Luna's direction:**
  - SS-specs #40 (D-075 legacy boss cues), #41 (D-074 fog-band correction), #42 (D-076 T602 acceptance).
  - SS-runtime #85, #86, #90 (vertical facing), #93 (D-072 commit clips), #94 (boss cues, `presentation-assets-002`), #95 (T602 art).
- **Runtime pin is SS-specs `14a042f`.** 467 tests, 19 app tests, parity OK.
- **T602 art:** Luna generated it via Codex, which saved into its own copy at `~/Documents/Codex/2026-09-27/plea/work/SS-art-generation-pack/`, not our pack.
  - The canonical pack is `~/Documents/claude/SS-art-generation-pack` (START_HERE.md, PROMPTS.md, `process_all.py`).
  - Admitted: 368 frames, 50 redrawn attack `n`/`s` frames (closes #89), and both fog layers. Clip-frame coverage is 956/956.
  - The review packet is `docs/review/T602`.
- **Script fix in #95:** `admit_environment_art.py` left the `plannedOriginal` record beside a first delivery, a duplicate ID that breaks every catalog test. It now drops it.
- **Stacked-PR trap:** merging a base PR with `--delete-branch` *closes* the PRs stacked on it (#91 and #92 were replaced by #93 and #94). Retarget stacked PRs to main before merging the base.
- **zsh trap:** `"$P:contracts/..."` expands `:c` as a history modifier and writes empty files. Use `"${P}:..."`.
- **Merge permission:** the auto-mode classifier blocks merges without review. Merges succeed when Luna directs them explicitly in chat; auto-merge (`--auto`) stays blocked.
- **Next:**
  1. Original sounds for 3 boss telegraphs (safetyRationale, narrowTailoring, independentReview), still `plannedOriginal`.
  2. Remaining T800 art: trolley wires, rooftop kit, Captain Camera housing (T507).
  3. SS-specs #31 lethal-warning trigger: Danny's call.
  4. Playtest gates T903/T904.

Prior: Updated: 2026-09-27 (later) by Prabu (Claude Opus 5.5) — **SS: facing bug fixed, commit clips play, boss cues get legacy sounds.**

- **Merged since:** SS-specs #36–#39 (D-072, lethal-warning intent, D-073, D-074).
- **Lost correction:** #39 merged *without* its fog-band fix. The commit (111a5da) was dropped during a rebase, although a PR comment said it had been pushed. Re-applied as **SS-specs #41**: the band is rejected because runtime fog is a seamless 512² tile. **Lesson: after a rebase, check `gh pr view --json commits` before announcing a push.**
- **Open, runtime:**
  - **#90** vertical facing (closes #88). `direction(forFacing:)` mapped +y to `s`, but world +y is north. Cordic `headingUnit` is y = −sin; 270_000 is +y, which is `n`.
  - **#86** now pinned at `878cb9f`.
  - **#91** D-072 commit clips via `ReactionClipTracker`. Stacked on #86 and merges in #85. Closes #87.
  - **#92 (draft)** boss cues. Pins SS-specs #40's head `911a3a7`; **re-pin to #40's merge commit, then mark ready.**
- **Open, specs:** **#40** `presentation-assets-002` + D-075.
  - `boss_phase_*` ×4 use `sfx_boss_activated`.
  - `boss_telegraph_temporaryOrder` uses `sfx_camera_scan_sweep`.
  - The other 3 telegraphs are `plannedOriginal`, because approximate substitution is closed (legacy-admission.md).
- **Merge order:** #85 → #86 → #91; #40 → re-pin #92 → #92; #41 → then a re-pin changes the SF-candidate test from 3 to 2 (AssetCatalogTests). #90 is independent.
- **zsh trap:** `"$P:contracts/..."` expands `:c` as a history modifier and writes empty files. Use `"${P}:..."`.

Prior: Updated: 2026-09-27 by Prabu (Claude Opus 5.5) — **SS: review is the bottleneck; owner decisions turned into merge-to-accept PRs.**

- **Nothing moved Sep 23→27.** SS-runtime #85 (hurt/stagger/defeat play) and #86 (pin `c15a6f5` + standard-enemy idle/move/recover) green and unreviewed. Pinged Danny on both and asked whether I may merge my own green PRs after a 48 h window, like the org admin-bypass in DECISIONS 2026-08-21. **No answer yet.**
- **Four decision PRs on SS-specs (merge = accept):** #36 D-072 commit clips reachable (state-derived, no new event; Informant commit on its contact hit); #37 lethal-warning intent (3 triggers, recommends presentation-derived lethal-threat); #38 D-073 approve 42 delivered P0 env assets — and records P0 gaps: `env_fog_low/high` were declared with **no catalog record**, rooftop kit, trolley wires, Captain Camera; #39 D-074 disposes of 12 SF legacy sprites (fog band → candidate for `env_fog_low`, 2 deferred, 9 rejected for no role), closes #3.
- **Corrections to my own earlier records:** #33 said T800 was "33 assets awaiting approval" — it missed the P0 gaps. My #31 note said the lethal warning needs a new event — it doesn't under two of three options.
- **Still silent:** 8 boss audio cues (`boss_telegraph_*`, `boss_phase_*`) emitted with no contract slot or asset. Adding them needs `presentation-assets-002` (D-060 bump rule) — not yet drafted.
- D-072/073/074 all follow D-071; whichever merges out of order needs a trivial rebase.

Prior: Updated: 2026-09-23 by Prabu (Claude Opus 5.5) — **SS art pipeline: three spec questions decided, T602 production order specified, and delivered art that never played is fixed.**

- **Merged (all approved by Danny):** SS-runtime #83 (T301/T700 verification), #84 (pin `ef5edad`); SS-specs #32 (close T301/T700), #33 (art ledger reconciled with the catalog: T509/T601/T603 closed), #34 (**D-068** boss attack names = `bosses.md`; **D-069** a clip may self-reference as its reduced-motion clip; **D-070** Guard/Interceptor retired from T405/T503/T602, A-006/D-003/G-007, arena.md), #35 (**D-071** T602 order: 20 standard-enemy clips, 368 `plannedOriginal` frames; no `acquire` clip, `recover` only for the Correlator, no `move` for the Informant).
- **Open:** **SS-runtime #85** — `ReactionClipTracker`: hurt/stagger/defeat clips from authoritative events. Before it, *no hurt clip was ever selected* and dead enemies left the snapshot on death, so delivered `player_hurt`, Daemon hurt/defeat, Moderate stagger/defeat never played. Marker-driven, honours `cancelWindows`, 6 mutations caught. **SS-runtime #86** — pin `c15a6f5` + projection shows idle/move/recover for standard enemies; pinned "every clip backed" tests restated as invariants that survive batched delivery (956 total / 588 backed). A watcher merges both on Danny's approval (4h).
- **Filed:** SS-runtime **#87** — 4 of 5 enemies' delivered *commit* clips never play (Fog/Witch/Vendor resolve inside telegraph→cooldown; Informant never enters `charge`). Needs a spec decision on commit markers. SS-specs **#31** lethal warning still undefined.
- **T602 art itself** is the remaining production job: 368 frames, IDs are the `plannedOriginal` records in `asset-catalog-001`. Source pipeline `original://Surveillance-Survivor-Art/` is not on this machine.
- `prabu-openclaw` now has **write** on SS-specs/SS-runtime (+6 more Danny repos). 22 other invitations expired; Danny must re-send if wanted.

Prior: Updated: 2026-09-22 by Prabu (Claude Opus 5.5) — **Surveillance Survivor reboot: audited SS-runtime against SS-specs `ef5edad`; two runtime PRs + one spec issue open.**

- **Spec update since the runtime pin (`fb60046` → `ef5edad`, Danny's SS-specs #29/#30, D-067) is process-only**: `git diff fb60046 ef5edad -- contracts/ fixtures/` is empty; no FR or version identity moved. Parity at `ef5edad`: 20 files byte-identical, the one diff is the asserted `asset-catalog` `specificationCommit` exception.
- **`SS-runtime#84`** re-pins to `ef5edad` at all six pin sites; `spec_parity.sh` OK, `swift test` 430/73, `xcodebuild test` 19/2.
- **`SS-runtime#83`** closes **T301/T700** (converge.md's "runtime-implemented, awaiting a citing PR"). Real gap, not paperwork: with the neutral-movement/Dodge guards deleted, or selection opened after M-B, **all 420 existing tests passed** — every test opened selection through `testing_armUpgradeSelection`. New tests drive genuine M-A completion through `step()` and pin the seven canonical zone rectangles; 5 mutations each caught; suite 440/75. After merge, the SS-specs `tasks.md` rows T301/T700 can be checked against #83.
- **`SS-specs#31`**: G-04 lethal warning is **undefined**, not just missing copy — audio priority 1 in 4 spec files, but no trigger, no event-catalog entry, no audio ID. Runtime rightly emits nothing. G-08 is spec wording only (runtime has exactly 5 families).
- Everything else in converge.md is owner/device/art (T306/T506/T802/T804/T806/T907/T908, D-020/D-021, T503–T509, T601–T603, T800) — not agent-actionable.

Prior: Updated: 2026-09-07 by Prabu (Claude Sonnet 5) — Continued the agent-doable Noema slice queue. **`Noema#637`** merged (2026-09-07T06:04Z), closing #622. Took the next open slice, **`Noema#633`** (WATCH reconstruction fallback can pick private fidelity over public zero): independently verified — not rubber-stamped — that PR#636 satisfies all six of #633's acceptance criteria against fresh-clone source/tests at `main` `2343222` (`watch-live.ts:710-714` public-only fidelity selection, `world-do.ts:288-296` matching Worker→DO adapter, `watch-reconstruction-projection.test.ts` 12-case table incl. reversed-order leak checks, `watch-phosphor.test.ts` real color assertions replacing prior `expect(true).toBe(true)` tautologies). 60/60 on cited files, 1681/1681 full `workers/noema` suite (21 skipped, 0 failed), typecheck clean. No source changes needed — closed **`#633`** directly with the evidence trail in the closing comment (https://github.com/Zero-State-LLC/Noema/issues/633#issuecomment-5578451482). Posted to Buzz `general`. Remaining agent-doable open item: **#634** (canonical JSON — `RECONSTRUCT` optional fields with `undefined` break `noema-jcs/1`/RFC-0003 compliance, shared-serializer risk flagged, needs careful digest-compat review before touching — haven't started). Gate B itself remains owner-blocked (deploy + human enrollment of 3 independent Controllers) — not agent-actionable.

Prior: Updated: 2026-09-06 by Prabu (Claude Opus) — Picked up zero.zero's Buzz handoff request. Resynced Noema to `origin/main` (`11f20a3`): the specs-runtime gap closure plan (`docs/evidence/SPECS-RUNTIME-GAP-CLOSURE-2026-09-07.md`, PR#631) had already had P0/P1/most of P2 merged via PR#635/#636. Next dependency-ordered agent-doable item was issue #622 (Gate B controller-count provenance). Investigation found the actual contract was already shipped in PR#621 (2026-09-02) — #622 just never got closed by it. Opened **`Noema#637`** (tests-only, not merged): two lock-in regression tests (digest changes with controllers/fidelity; registry round-trip preserves both without caller mutation), closes #622. 57/1 acceptance-slice pass, 560/32 full suite pass, no regressions. Remaining agent-doable open items from the plan: **#634** (canonical JSON — `RECONSTRUCT` optional fields with `undefined` break `noema-jcs/1`/RFC-0003 compliance, shared-serializer risk flagged, needs careful digest-compat review before touching) and **#633** (WATCH reconstruction fallback private-fidelity selection — PR#636 claims this fixed but issue is still open, needs verification/closing). Gate B itself remains owner-blocked (deploy + human enrollment of 3 independent Controllers) — not agent-actionable.

Prior: Updated: 2026-09-01 by Prabu (Claude Sonnet 4.6) — Gate B tasks 1-3 done: Noema#620 open (reconstructionLines fidelity/contention, requestAgentEnrollment batch 3+ controllers, reduce_INSPECT fidelity + patch_entity seam); 1613 TS + 535 Python pass. Earlier: WATCH answered, DNS verified, SS#164 merged. ASC Connect UI entry needs Danny/Aaron login.

## Now (2026-09-01) — Surveillance Survivor reboot (`scrimshawlife-ctrl/SS-specs` + `SS-runtime`)

**The reboot is real and the kernel is strong; the governance loop and the app target were broken. Four PRs open, all green locally; none merged.**

### `SS-runtime#42` — the iOS app had never compiled

`xcodegen generate` + `xcodebuild` on `main` fails before any App file: `BundledResource.swift:5: type 'Bundle' has no member 'module'`. `project.yml` rebuilt `SurveillanceCore` as an Xcode framework target; `Bundle.module` only exists for SwiftPM resource targets, and the framework target would not have shipped `Resources/contracts` anyway. CI only ran `swift test`, so this survived **41 merged PRs**. Two access-level errors hid behind it (`RunInstrumentation.swift` never imported `SurveillanceCore`; `CameraHUDProjection` had no public init). Fix: consume the package via `packages:`; CI gains an `app` job. **Evidence:** BUILD SUCCEEDED (simulator + signed `iphoneos` for team `7FRK8RHAL5`), app runs in the simulator (stable pid, renders a scene, 56 colours), `swift test` 272/47 pass.

**Fork PR — CI shows no checks. Danny must click *Approve and run* for a first-time fork contributor.**

### `SS-specs#1` — contract drift, stale task ledger, wrong repo identity, no CI

- Runtime bundles **five contracts the spec never owned** (`clip-metadata`, `procedural-vfx`, `ambient-motion`, `visual-language`, `asset-catalog` — 509 records) + two golden fixtures, none in `versions.json`; and **amended `presentation-assets-001` in place** (`camera_field_off`) so both repos shipped different bytes under one ID. Adopted as D-060/D-061.
- `tasks.md` had Phases 2–9 **entirely unchecked** against 41 citing PRs. 56 tasks now checked with an Evidence table; run/record/measure/decide tasks left open (a harness is not evidence).
- D-014 said `scrimshawlife-ctrl/SS`; reality is `SS-runtime`. Amended. **T004/D-013 tag `legacy-multicity-2026-08-24` created** on the legacy repo (`e085ea8` → `3b20d88`).
- New `scripts/validate_specs.py` + workflow: JSON/schema validity, arena/replay/asset-record conformance, `versions.json` resolution, README index completeness. First run found `camera-placement-001.schema.json` un-indexed — and it has **no instance in either repo**; decision needed.

### What is conformant (verified, not assumed)

Pin `39b04bb` = SS-specs HEAD in `SPEC_BASELINE.md`, `SPEC_PIN.txt`, `ContractVersions.swift`. 11 spec-owned contracts byte-identical. Zero forbidden imports in Core; zero `Double`/`Float` in authority dirs; the four dictionary-iteration sites are arrays or sorted. D-038/040/041/053/027/029 constants match; `combat-content-001` byte-identical (boss 800, waves 14/17/25).

### Next (in order)

1. Danny: approve-and-run CI on `SS-runtime#42`; review `SS-specs#1`.
2. After `SS-specs#1` merges: runtime PR bumping the pin and adding a CI step that byte-compares bundled `contracts/`+`fixtures/` against SS-specs at the pinned SHA — the check that would have caught all of §SS-specs#1.
3. Device run for Gate C: a signed `SSRuntime.app` is built; install needs the phone unlocked. **Same bundle ID as the legacy app** — installing replaces it. `ReleaseEvidenceStore` exports device-run JSON to the app's Documents; pull with `devicectl`.
4. `CombatContent.swift` decodes spec JSON with 25× `as!` — crash, not typed fail-closed. S3 hygiene.

## Also this session — org `Zero-State-LLC/Surveillance-Survivor`

- **`#16` merged** (`0721cc8`): Cloud Agent env, core tests off the iOS host (468→194 simulator-hosted is de-duplication, not lost coverage).
- **`#17` open** — nightly was red 12 days straight *with all tests green*: `Failed to CreateArtifact: Artifact storage quota has been hit` — 17 `simulator-artifacts` bundles on 90-day retention = 1.1 GB of the repo's 1.19 GB. Short retention + `continue-on-error` on evidence bundles; test-count logs stay strict.
- **`#18` open** — port of Danny's art remediation `f6410a3` (#161; 106 PNGs; all asset validators pass). **Needs eyes on an LPR-dense panel** — it removes baked beams under the same masts org #12 re-drew cones on (A-02). Store-docs `3b20d88` deliberately *not* ported: it hardcodes `life.zerostate.*` personal bundle IDs.
- **`#14` closed** as superseded. CodeQL default setup fails on `ubuntu-latest`: *"recent account payments have failed or your spending limit needs to be increased"* — billing, not code.
- `luna-mac-ios` self-hosted runner (Luna's Mac, `[self-hosted, macOS, ARM64, ios]`) drained the queued simulator jobs; it is the only `ios` runner that has been online since Aug 19.
- **`#19` open** — boards refreshed to tip `0721cc8` (counts 289/194/14, nightly root cause, runner, personal-repo reconcile) + `CONTINUATION_REPORT_2026-09-01_org_reconcile.md`; `repo-status-check`/`release-docs-check`/`launch-gate-check` pass.

---

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

### `Noema#619` — the Python suite had the same silent-skip hole as the Worker

`#609` closed this on the Worker side; the Chamber suite still carried it. **With Noema-Specs absent the Python suite reports `531 passed, 7 skipped` and exits zero** — and three of those are the cross-repo **ADR-005 conformance** tests: seed replay against the published v0.1 fixtures, published-vs-local fixture comparison, and the event-catalog check. The tests that prove the offline Chamber still agrees with Specs can go quiet behind a green run.

`require_specs()` keeps the local skip, fails under `CI`, and names the likely cause — **CI pins Specs to `spec-compat.json specs.commit`, not main**, so a lagging pin can make an artifact vanish even when the clone succeeds (how #608 would have skipped). Mutation-verified; 538 passed / 4 skipped with Specs present.

The other four skips are legitimate: 2 Postgres, 1 Postgres ops, and the cohort E2E needing an official-client checkout.

**Both suites are now loud.** If you add a cross-repo fixture on either side, CI tells you instead of skipping.

### `noema-client#33` — the client had no check against the Worker

The client's fixture pins all 42 Worker `cmd:` templates and the suite checks the client against it — but **nothing checked the fixture against the Worker**, so a command added or renamed in Noema drifts silently while client CI stays green. Same shape as `Noema#609` / `Specs#310`/`#311`. Matters because **Gate B runs three Controllers on this client against the live Worker**, and the affordance contract is what they exercise.

`scripts/check_worker_contract.py` compares both directions (a gained command must be classified `parsed` vs `structured_only`; a dropped one must be removed) and rejects a template listed in both halves. Mutation-verified: adding a template and renaming one each exit 1 with the right message; unmodified exits 0. Trigger mirrors `pin-currency` — scheduled watch + narrow `pull_request` on the fixture/parser/script only, so a normal PR isn't failed by another repo moving.

Contract was 42/42 clean today against both Worker main and the live build.

### Also verified, no findings: the public door

Contrast **passes AA and AAA everywhere** (7.55–14.93 across headline, prose, tags, feed, site list, nav). Tier markers are not colour-only (`·` mark elements, `>` on the headline); older rows get `quiet` = visual fade, no deletion. Low-noise applies `is-low-noise` and persists client-local. **No slice needed here — do not re-audit.**

**Gate D is not evidenceable yet.** Its test is blind human comprehension of a populated WATCH; with `players: 0` there is nothing to comprehend. Only its redaction clause is already evidenced (`#614`/`#618`).

### `Noema#618` — C5 verification finished; **do not re-run it**

`#616`, `#617`, `Specs#320` merged. `#618` closes the C5 items my first pass left open *without listing them as uncovered*: WebSocket 101, TEXT/PIXEL, low-noise, reduced-motion behaviour, MAJOR banner. **All pass — no further findings.** C5's read-only half is complete.

**Useful:** `/v1/watch/live` and the WS stream both render through `watchSnapshot()` → `buildWatchLive`, so **#617's entity-id fix covers both surfaces**. The live stream still shows `entity_id` only because live runs `02fd112`, predating #617.

**Three measurement traps, each of which looked like a defect** — recorded so nobody files them:
1. *Semantic site list empty* — queried before the first poll; 10 items after ~3s.
2. *TEXT doesn't disable the canvas* — `canvas.hidden` false and `display:block`, but the **parent** is hidden so the rendered box is `0x0`. Test `clientWidth`/`offsetParent`, not the element's own `hidden`.
3. *WS upgrade returns 405* — curl defaults to **HTTP/2**, where upgrade doesn't apply. Use `--http1.1` → 101.

### `Noema#617` + `Specs#320` — entity ids off the spectator wire; all three C5 findings closed

**My C5 finding 3 was wrong about the doctrine.** I called it an ambiguity ("no rule covers `rooms[].entities[]`"). The WATCH **field table** pins that row to `label`, `entity_type` — I'd read §8/§9 and missed it. So it was the runtime shipping two fields beyond contract, with `rooms[].traces[]` forbidding entity ids one row away.

- **`entity_id` dropped** (#617). Its only consumer was `watch.ts`'s `label || entity_id` fallback, which **cannot fire** — `label` is required on EntityRuntime. It published an internal id to satisfy an unreachable branch, and would have rendered a raw `entity.relay.15ec525b` to spectators if it had.
- **`glyph` kept** — §18 pins the glyph catalog and both renderers read it; the field row was just stale. Corrected in `Specs#320`.
- **Scope:** only *public* entities were ever projected (`isPublicEntity` filters hidden), so this narrowed a bounded exposure, not a hidden-entity leak. Don't over-read it.

**Lesson worth keeping: read the field table before concluding WATCH doctrine is silent.** §8/§9 are prose; the per-field contract is a table further up.

### `Noema#616` — CSP now allows the font hosts the chrome asks for

Closes C5 finding 1. The public door rendered in **system fallback**: HOSTED-FIRST-ENTRY pins Syne / IBM Plex, `theme/tokens.ts` requests them from Google Fonts, and the CSP allowed neither host. Pre-existing, present at the prior live build.

**Two hosts, not interchangeable:** `fonts.googleapis.com` serves the stylesheet (`style-src`); `fonts.gstatic.com` serves the woff2 files (`font-src`). **`font-src` was absent entirely** and inherited `default-src 'self'` — so allowing only the stylesheet host leaves the fonts blocked. That half-fix is now guarded by a test.

Verified on a local Worker, not asserted: display stack 287.02 == system before → **331.88 ≠ 287.02** after; mono 325.11 == before → **324.00 ≠ 325.11** after. Six tests where there were none — an untested header is how this stayed live. Widening is narrow: `default-src` still `'self'`, no third-party script/img origin, no wildcard in the touched directives.

Owner note: this makes a per-pageload request to a Google host. Self-hosting the two families would avoid it and need no CSP widening — larger change, not done.

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
