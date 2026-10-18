# Cut Club 0.3.20 — review candidate

Native edit batches now construct every action before registering any of them with Premiere. A controlled native probe showed that incremental registration can leave the first action applied when a later factory throws. The new shared helper prevents that construction-failure case, preserves action order and existing Undo stages, and never retries. Registration or commit failures still require the existing ownership-based cleanup.

This is a narrow safety correction, not a solution to Premiere's intermittent invalid-script-object errors. Fresh-session and accumulated-session testing still reproduced failures at clone factories, including ordinary separate QA-button clicks. Cleanup preserved the prior QA timeline; long-session production acceptance remains blocked. No unproven carrier-retention, wrapper-refresh or bounded-retry experiment ships.

Includes the prior export/recovery and grid fixes, 25 original cards, 60 editable MOGRT files, six alpha movies and six supported formats. No new effect family, network permission or updater ships.

Regression tests and the native construction-failure probe passed. Official package, installed acceptance and file-integrity results are recorded separately when complete. This remains a prerelease: reference sign-off, sustained physical hover, native insertion stability, second-machine/fonts and update migration need review.

Release hygiene: local last-known-project paths and unrelated QA media were removed from our native source containers. MOGRT preview movies have their authoring XMP removed without changing encoded frames, sample tables or offsets. All editable project payloads and definitions remain byte-exact. Packaging now checks local home-path metadata in compressed native sources and nested MOGRT containers. This bounded hygiene check is not a general sensitive-data detector. Native acceptance is recorded separately.

Native hygiene acceptance: all six regenerated source formats placed with independent native values and full-white flash peaks; all 60 MOGRT variants inserted and produced correctly sized hold frames, reviewed with alpha compositing. Original and sanitized Character Rise exports from fresh projects were pixel-identical. These checks do not establish exhaustive animation/control acceptance. The official Adobe CCX is built and installed; 3,663 source/archive/installed files match. Initial installed startup was observed; repeat-insertion and panel-reopening acceptance for this installed version remain pending.
