# Integrity review of `.agents/kit/devsecops-plan.md`

Only the viewpoint `integrity` was done. All paths are in the trial project.

## Table: assets, questions 1 to 3

Question 1 asks who can change the asset and leave no trace. Question 2 asks what shows a change. Question 3 asks if that check is tied to the asset. "Plan" means `.agents/kit/devsecops-plan.md`.

| # | Asset | Q | Result | Evidence | Sentence |
|---|---|---|---|---|---|
| A1 | Source | 1 | yes | Plan:74 | The owner can push, force-push or delete on the primary branch, because rule C-02 is not set and there is no remote. |
| A1 | Source | 2 | partly | Plan:74-76 | A branch rule and the platform record are planned, but only after the repository is on GitHub; today nothing shows a change. |
| A1 | Source | 3 | partly | Plan:76 | The planned platform record covers each revision, but Source L3 (signed summary) is not planned (Plan:137). |
| A2 | Input from outside: crates, Nix inputs, base images, tools | 1 | partly | `Cargo.lock`, `flake.lock`, `dev/containers/alpine.Dockerfile:9` | The crates, the Nix inputs and the base images are locked by digest, but the pipeline tools are not pinned (Plan:67). |
| A2 | Input from outside | 2 | yes | Plan:128 | `Cargo.lock` checksums, `--locked` (`meson.build:99`), `narHash` and image digests show a change of these inputs. |
| A2 | Input from outside | 3 | yes | Plan:128 | These checks are tied to each input by checksum or digest. |
| A2b | Input from outside: build and CI tools, actions, `cargo-llvm-cov`, `cargo-about`, `cargo-fuzz` | 1 | yes | Plan:67 | A moving tag of an action or tool changes silently; the plan pins by digest only after the files are brought in. |
| A2b | Build and CI tools | 2 | partly | Plan:67 | A pin by digest and a Renovate configuration are planned, but both are conditional on the missing files. |
| A2b | Build and CI tools | 3 | partly | Plan:67 | A digest pin is tied to the tool, but the plan does not say that the pin is checked. |
| A3 | Build (definition and run) | 1 | yes | Plan:59 | No pipeline definition is in the tree, so a build on any machine leaves no trace. |
| A3 | Build | 2 | partly | Plan:60-64 | Hosted jobs and provenance are planned for Build L2; nothing is measured today (Plan:136). |
| A3 | Build | 3 | partly | Plan:64 | Build provenance is tied to the source repository by design, but the plan names no commit or digest binding for the build. |
| A4 | Tests (code and fixtures) | 1 | yes | `CONTRIBUTING.md:163`, Plan:74 | Tests are in the tree, so the owner can change or delete them without review. |
| A4 | Tests | 2 | partly | Plan:109 | The plan only proposes a rule that requires the test job; it is not measurable and is the owner's to set. |
| A4 | Tests | 3 | no | Plan:63 | No link ties a test run to a commit or to the archive; only the digest of the archive is compared. |
| A5 | Results of tests and other checks | 1 | yes | Plan:102-103 | Plan:102 only reports flaky tests, and Plan:103 only runs the pre-commit job. No result is stored; anyone can re-run and replace a log. |
| A5 | Check results | 2 | no | Plan:139, Plan:142 | The plan keeps results only in the run summary and the coverage service; "check scores" is "after the first push". |
| A5 | Check results | 3 | no | `CONTRIBUTING.md:125` | A coverage upload to an outside service names no commit or digest in the plan. |
| A6 | Released result (source archive) | 1 | yes | Plan:62-63, Plan:65 | The release asset on the platform can be replaced by a maintainer; immutable releases (C-34) are not measurable and are the owner's to set. |
| A6 | Released archive | 2 | partly | Plan:64-65, Plan:95 | A digest file, signed provenance and immutable releases are planned. No such file exists today (Plan:65). |
| A6 | Released archive | 3 | partly | Plan:63 | One digest of the tested archive is compared before the upload, but the plan does not say that provenance names this digest. |
| A7 | What the user installs: distribution packages, the Nix packages and the cache | 1 | yes | Plan:63 | The distribution build services rebuild from the archive, outside the check, so packages can differ from the archive without a trace. |
| A7 | Distribution packages | 2 | partly | `README.md:259-260`, Plan:66 | The package manager checks the repository keys, and attestations for Nix are stated in the README, but `docs/releases.md` is absent. |
| A7 | Distribution packages | 3 | no | `packaging/obs/_service:7`, `packaging/obs/_service:20` | OBS takes `@PARENT_TAG@` and a downloaded file, and no digest ties the package to the verified archive. |
| A7b | Packaging recipes (`PKGBUILD`, `APKBUILD`, spec, dsc) | 1 | yes | `packaging/arch/PKGBUILD:20`, `packaging/alpine/APKBUILD:34` | Arch skips the checksum and Alpine has no checksum line, so a swapped archive builds without a trace. |
| A7b | Packaging recipes | 2 | partly | Plan:65 | The plan sets the digest in the two recipes at release, but the plan does not cover the spec or the dsc. |
| A7b | Packaging recipes | 3 | partly | Plan:65 | The digest would be tied to the archive, but the plan says nothing on the Debian and RPM recipes, or about who edits them after the build. |
| A8 | System on which it runs (root guard, udev helpers, HID-BPF in the kernel) | 1 | yes | `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in:12`, `README.md:42-44` | A malicious package runs as root and as a kernel BPF program, and nothing in the plan checks what the result does to the machine. |
| A8 | System of the user | 2 | partly | Plan:129 | The hardening of the guard unit is judged (C-30), but the helpers and the BPF program are not judged. |
| A8 | System of the user | 3 | not applicable | `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in:12` | The hardening is a property of the unit, not a check tied to an artifact digest, so question 3 does not apply. |
| A9 | Data read and written (sysfs, `/dev/kmsg`, `/run` notes, TCC offset, config) | 1 | yes | `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in:13-14`, `:23-26` | A change of the offset or of the notes in `/run` leaves no trace beyond the guard's own restore. |
| A9 | Data read and written | 2 | partly | Plan:130, Plan:142 | Fuzz and tests cover the parsers (Plan:130), and the plan names no check that the guard restores the offset. |
| A9 | Data read and written | 3 | not applicable | `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in:23` | The data is machine state at run time, so tying a check to a digest does not apply. |
| A10 | The pipeline itself (workflows, secrets, webhook, AI reviewer, OBS token) | 1 | yes | Plan:94, `packaging/obs/README.md:80-86` | A change to a workflow, a secret or the webhook takes effect with no record beyond the repository history. |
| A10 | Pipeline | 2 | no | Plan:94 | C-23 is not measurable until the definition exists, and C-32 (pipeline log) is above the target (`devsecops.md:126`). |
| A10 | Pipeline | 3 | no | Plan:61, Plan:67 | Nothing ties a run to the reviewed workflow commit beyond the pin by digest; the plan does not address this. |
| A11 | Records of the project (changelog, issues, advisories, selection, plan, tags) | 1 | yes | `devsecops.md:11-12` | The repository has no tag and no remote, so the history, the changelog and the selection can be rewritten. |
| A11 | Records | 2 | partly | Plan:76, Plan:96, Plan:110 | The platform record, issue records and `CHANGELOG.md` are planned or exist, but none is signed. |
| A11 | Records | 3 | no | `CHANGELOG.md:8` | The changelog links to commits, but the tags are not in this repository, so no release is tied to a commit (Plan:59). |

## Table: questions 4 to 7

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 4. Where does the chain of evidence end before the user? | yes | Plan:63, `packaging/obs/_service:20` | The chain ends at the archive: the packages are rebuilt by four outside services, and this is "outside the check". |
| 5. Which results are kept, which are lost? | partly | Plan:64-65, Plan:142 | Provenance and the digest file stay with the release, while test, lint, scan and fuzz results are not kept as evidence. |
| 6. Can one change weaken a check and pass? | yes | Plan:86, `Cargo.toml:17`, `CONTRIBUTING.md:172` | Lints are `warn` and the coverage limit is a rule in a document, and a change can weaken both together with the workflow. |
| 7. Does the risk analysis ask what the result can do to the system and the data? | no | `.agents/kit/devsecops.md:34` | The questions cover users' harm and exposure, not what a root daemon, udev helpers and a BPF program can do to the machine. |

For question 6, the planned approval cannot hold for the owner's own changes (Plan:75). No rule on the files of the checks, such as CODEOWNERS, is planned.

## Findings

1. **The plan has no tie from distribution packages to the verified archive.** OBS fetches by `@PARENT_TAG@` and a downloaded file with no digest (`packaging/obs/_service:7`), and the plan calls it "outside the check" (Plan:63). Viewpoint: `integrity`. Route: `recipe`.
2. **The Arch and Alpine recipes check no digest of the archive.** `PKGBUILD` has `SKIP` and `APKBUILD` has no checksum line. Plan:65 plans only the release-time fix, and the spec and dsc recipes are not covered. Viewpoint: `integrity`. Route: `tooling`.
3. **No check result is kept as evidence.** Plan:102-103 gives no store for test, lint, scan or fuzz results (`CONTRIBUTING.md:125` shows a coverage upload to an outside service). The recipe items C-33 and C-32 are above the target (`devsecops.md:121`, `:126`). Viewpoint: `integrity`. Route: `recipe`.
4. **One change can weaken a check and pass.** Lints are `warn` (`Cargo.toml:17`) and the coverage limit is only a rule (`CONTRIBUTING.md:172`). The plan has no protection of the check files (Plan:86, Plan:109). Viewpoint: `integrity`. Route: `recipe`.
5. **The risk analysis does not ask what the result does to the machine and the data.** The three questions (`devsecops.md:31-35`) skip root daemons, udev helpers and a BPF program. The plan judges only the guard unit (Plan:129). Viewpoint: `integrity`. Route: `recipe`.
6. **The pipeline is not protected as an asset.** C-23 is not measurable (Plan:94) and C-32 is above the target. The OBS token and webhook are set by hand (`packaging/obs/README.md:80-86`), so nobody gets a signal when the pipeline is defective. Viewpoint: `integrity`. Route: `recipe`.
7. **The source has no signed record of identity or approval before the remote exists.** C-02, C-03 and C-15 are not measurable (Plan:74-76), and Source L3 has no implementation skill (Plan:137). Viewpoint: `integrity`. Route: `implementation skill`.
8. **The plan does not tie releases to a commit in the records.** No tag exists (`devsecops.md:12`), so the changelog links (`CHANGELOG.md:8`) cannot be tied to a release (Plan:59). Viewpoint: `integrity`. Route: `tooling`.
9. **The plan does not tie test results to the archive that is released.** Plan:63 compares one digest of the archive, but nothing says that the test job tested that exact archive (Plan:102). Viewpoint: `integrity`. Route: `tooling`.

## Files read

- `review-task/plan-review.md`
- `.agents/kit/devsecops-plan.md`
- `.agents/kit/devsecops.md`
- `.claude/skills/devsecops/SKILL.md`
- `.claude/skills/devsecops/references/checklist.md`
- `CONTRIBUTING.md` (lines 55-204)
- `packaging/obs/_service`
- `packaging/alpine/APKBUILD`
- `packaging/nix/package.nix`
- `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in`
- Grep results only: `README.md`, `CHANGELOG.md`, `dev/containers/*`, `meson.build`, `packaging/obs/README.md`, `packaging/arch/PKGBUILD`, `Cargo.toml`
- Glob results: file lists of the project and of `build-aux/`

## Not verified

- I did not verify the Rust, C and JavaScript sources, `Cargo.lock`, `flake.lock`, `build-aux/dist-vendor.sh` or the spec, dsc and Debian recipes.
- I did not verify claims about workflows or GitHub settings. I did not verify the other viewpoints. No reference state was given.
