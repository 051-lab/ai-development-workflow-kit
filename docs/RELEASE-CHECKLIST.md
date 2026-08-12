# V1.2 Release Checklist

Maintainer checklist for releasing the workflow kit. This is not project runtime state and does not add to the five-file `docs/ai` model.

## Source state

- [ ] Release work comes from an explicitly reviewed branch and commit.
- [ ] Working tree is clean before packaging.
- [ ] `main` and its remote state are verified as appropriate.
- [ ] Use actual Git evidence rather than stale narrative.

## Verification

- [ ] Unit tests pass.
- [ ] Bash syntax checks pass.
- [ ] PowerShell contract/smoke checks pass where available.
- [ ] `git diff --check` passes.
- [ ] Initializer fresh, rerun, force, and launcher behavior are verified.

## Version consistency — final release only

- [ ] `VERSION` contains the intended release version.
- [ ] Visible documentation version is consistent.
- [ ] Reference filename/version is consistent where applicable.

Version and reference alignment belongs exclusively to finalization, before packaging.

## Package hygiene

- [ ] Final package contains only intentional distributable kit files.
- [ ] Exclude `.git/`, `__pycache__/`, `*.pyc`, temporary test directories, editor/OS junk, and unrelated generated files.

## Manifest — final release only

- [ ] Regenerate `MANIFEST.txt` from the exact final package contents.
- [ ] Verify every recorded hash corresponds to its packaged file.
- [ ] Regenerate the manifest only after all distributable release contents are final; historical release artifacts remain separate evidence.

Regenerate the current manifest only after the final distributable inventory is frozen.

## Final artifact validation

- [ ] Inspect the ZIP inventory.
- [ ] Extract the ZIP into a temporary directory.
- [ ] Run applicable tests and checks from the extracted artifact.
- [ ] Confirm initializers work from the extracted package.
- [ ] Verify VERSION and final MANIFEST contents.
- [ ] Confirm no cache or transient artifacts are present.

## Release boundary

- [ ] Treat final release preparation as separate from P2.
- [ ] Create a tag/release only after artifact verification.
- [ ] Perform EELForge migration only after V1.2 release acceptance.
