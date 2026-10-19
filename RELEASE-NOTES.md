# Cut Club 0.3.21 — source-less graphics hotfix prerelease

Native text/graphic clips may exist on a sequence without a ProjectItem. Previously, taking the placement preservation snapshot dereferenced getId on null and rejected every insertion into that sequence. Source-less clips now remain in the snapshot with their native name, match name, type and full timing; they are not skipped or assigned a fabricated project ID. Selecting a source-less clip no longer breaks readiness polling either.

Preflight failures now remain visible through the immediate refresh instead of disappearing behind Ready. A changed sequence/playhead/selection or new user input may update readiness, while committed-operation feedback retains its previous behavior.

Collision checks, real source identity for Cut Club assets, ownership checks before transfer/removal, serialized native work and Undo stages remain in place. No effect content or permissions changed.

Validation: the exact reported null-getId failure and the overwritten-error case failed before the patch and pass afterward. Thirty JavaScript test runners pass, including a complete simulated configured-transition workflow with an unrelated source-less graphic and tests that snapshot changes and unreadable owned sources remain rejected. Package integrity and installed/native usability are separate gates.

This is a review candidate. Native testing on the reported macOS 27.0 / Premiere 26.5.2 machine is still required. Other previously documented native handle/insertion reliability issues remain unresolved; this patch does not claim to fix those.

Install using Adobe UPIA or Creative Cloud with Premiere saved and closed. Do not edit installed plugin folders. Keep 0.3.20 for rollback. Test a saved duplicate project containing plain Premiere text/graphics: insert twice, inspect preservation of text and prior edits, and verify Undo/Redo.

## Guided installation

Download Cut-Club-0.3.21-Direct-Install.zip, fully extract it, and open START-HERE.html. A guided Terminal script invokes Adobe’s official UPIA installer after local checks and a typed INSTALL confirmation. The exact same CCX is also available separately. No custom Apple-signed app or Developer Mode is required for this route. No automatic updater ships.
