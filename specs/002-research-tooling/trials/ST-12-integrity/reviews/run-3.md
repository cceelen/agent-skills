# Report: plan review, viewpoint `integrity`, recipe `devsecops`

Paths are relative to the trial project. `plan` is `.agents/kit/devsecops-plan.md`. `sel` is `.agents/kit/devsecops.md`. `CONTRIB` is `CONTRIBUTING.md`.

## Assets

The plan is a proposal. It changes no file but the selection and itself (plan:3-5). Thus "what shows a change" means what the plan would add. At present the tree has no pipeline, no remote and no tag (plan:19, sel:12).

## Table: integrity, questions 1 to 3 for each asset

| Asset | Q | Result | Evidence | Sentence |
|---|---|---|---|---|
| Source | 1 | partly | plan:74 | Until the owner sets a branch rule, a direct push, a forced push or a deletion leaves no trace. |
| Source | 2 | partly | plan:74-76 | Only C-02 and C-15 would show it, and both depend on settings that the owner has not made. |
| Source | 3 | partly | plan:76 | The platform record is per revision, but the plan names no signed commits. A sole maintainer can still approve their own change (plan:75). |
| Inputs from outside (crates, flake inputs, base images, tools, actions) | 1 | partly | plan:128 | Crates, flake inputs and base images are pinned. The plan gives no pin for the pipeline's tools and actions, which do not exist yet (plan:67). |
| Inputs from outside | 2 | yes | plan:128 | `Cargo.lock` checksums, `--locked`, `narHash` and image digests show a change of these inputs. |
| Inputs from outside | 3 | partly | plan:128 | Digests tie the checks to the inputs, but the update tool is not configured (plan:67), and the plan does not name `udev-hid-bpf`, which the keyboard package needs (README.md:89). |
| Build | 1 | yes | plan:19 | No pipeline exists. A person builds on their machine, and the result carries no record. |
| Build | 2 | partly | plan:64 | Only C-08, signed provenance, would show a build, and it is not yet written or run. |
| Build | 3 | partly | plan:64 | The plan says "tied to the source repository" but does not say that the provenance must name the archive digest and the commit. |
| Tests | 1 | yes | plan:102 | Without a pipeline or a branch rule, a test can be removed or weakened in a change with no required check. |
| Tests | 2 | partly | plan:109 | C-39 (a required test job) is "not measurable" and rests on the owner's setting. C-50 is only a tree check (plan:130). |
| Tests | 3 | no | plan:109 | The plan does not tie a test run to a commit or to the tested archive. |
| Results of the tests and other checks | 1 | yes | plan:142 | The plan keeps no result. The coverage summary lives in the run, and the other results have no store. |
| Results | 2 | no | sel:121 | C-33 (stored release evidence) is above the target, so nothing shows a change of a result. |
| Results | 3 | no | plan:63 | The digest compare in C-12 is inside one job. No stored result carries a digest or a commit. |
| Released result (source archive) | 1 | yes | plan:87 | Releases can be replaced after publication, because immutable releases (C-34) are "not measurable" and rest on the owner (plan:95). |
| Released result | 2 | partly | plan:64-65 | The plan adds a provenance bundle and a digest file. Neither exists in the tree. |
| Released result | 3 | partly | plan:63 | The digest compare happens before the upload only. After the upload, the digest file and the provenance sit beside the archive with no pin. |
| What the user installs (distribution packages) | 1 | yes | plan:63 | The services of the distributions build the packages again from the archive. The plan calls this "outside the check". |
| Packages | 2 | partly | README.md:199 | Package-manager keys of the project's own repositories sign the packages. The plan sets no check on how those packages were built. |
| Packages | 3 | no | packaging/arch/PKGBUILD:20 | `sha256sums=(SKIP)` and no checksum in `packaging/alpine/APKBUILD:34` let a different archive pass. The plan sets the digest "at the release step" (plan:65), a step with no definition. |
| System on which it runs (root guard, udev helpers, BPF in kernel) | 1 | yes | tcc-guard/systemd/asus-ux8406-tcc-guard.service.in:12 | A package that is changed runs as root on the user's machine, so an unseen change reaches the kernel and the system. |
| System | 2 | partly | plan:129 | Only the hardening of the guard is examined (C-30). The other parts have none (plan:129). |
| System | 3 | no | plan:129 | The hardening check reads files of the tree. Nothing ties it to the installed package. |
| Data read and written | 1 | not applicable | sel:34 | The selection says the project holds no data of users. The files that the guard changes are not examined (see question 7). |
| Data | 2 | not applicable | sel:34 | The plan names no check on what the programs write on the machine. |
| Data | 3 | not applicable | sel:34 | Same reason. |
| Pipeline itself | 1 | yes | plan:94 | The pipeline does not exist yet. Later, a change by the sole maintainer, the AI reviewer or a pull request can alter the workflow with no second person (plan:75). |
| Pipeline | 2 | partly | plan:94 | C-23 asks that someone examine the pipeline, and the plan names three points, but no check runs against changes of the workflow files. |
| Pipeline | 3 | no | plan:67 | Pinning of actions by digest is planned (C-14). Nothing ties a run to the workflow definition that ran it. |
| Records of the project (changelog, issues, advisories, tags) | 1 | yes | plan:59 | No tag exists, and the changelog lists releases with no tags to check them. |
| Records | 2 | partly | plan:110 | C-49 and C-36 rest on an issue tracker that is not reachable. Releases are not tied to tags until the owner provides them (plan:59). |
| Records | 3 | no | plan:76 | The plan ties no record to a commit or digest, except the platform's own change record (C-15). |

## Table: integrity, questions 4 to 7

| # | Question | Result | Evidence | Sentence |
|---|---|---|---|---|
| 4 | Where does the chain of evidence end? | yes | plan:63 | It ends at the source archive. The distribution builds, `PKGBUILD:20` (SKIP) and `APKBUILD:34` (no checksum) lie after it. |
| 5 | Which results are kept, which are lost? | no | sel:121 | Only the provenance bundle and digest file are kept. Test, coverage, scan and lint results are lost after the run, and C-33 is declined. |
| 6 | Can one change weaken a check and pass? | yes | plan:86 | The lint denial, the 100 % coverage limit (`CONTRIBUTING.md:120`) and the policy limits (plan:84) live in editable files, and the plan has no protection on them. |
| 7 | Does the risk analysis ask what the result can do to the system and its data? | partly | sel:34 | The question asks about harm to users. The root and BPF risk appears only in the opinion text (sel:46). |

## Findings

1. **Distro packages are outside the chain.** The plan accepts packages being rebuilt "outside the check" (plan:63), and `PKGBUILD:20` skips the checksum while `APKBUILD:34` has none. Viewpoint: integrity. Route: recipe.
2. **No result is kept as evidence.** C-33 is above the target (sel:121), so test, coverage and scan results are lost after each run (plan:142). Viewpoint: integrity. Route: recipe.
3. **A change can weaken a check unseen.** The lint, coverage and policy limits are plain files (plan:86, plan:84, `CONTRIBUTING.md:120`), and the plan adds no protection for them or for the workflow files. Viewpoint: integrity. Route: recipe.
4. **Provenance is not required to name the archive digest and commit.** The plan says only "tied to the source repository" (plan:64), and the digest compare is inside one job (plan:63). Viewpoint: integrity. Route: tooling.
5. **Source and pipeline protections depend on owner settings.** C-02, C-39 and C-34 are "not measurable" (plan:74, plan:109, plan:95). With one maintainer, a change of the owner has no second person (plan:75). Viewpoint: integrity. Route: recipe.
6. **The risk analysis does not ask what the result does to the system and data.** The `criticality` question asks about harm to users (sel:34), although the guard runs as root (`tcc-guard/systemd/asus-ux8406-tcc-guard.service.in:12`). Viewpoint: integrity. Route: recipe.
7. **Only the guard has a hardening check.** The other root or kernel parts (udev helpers, BPF) have no check on the installed system (plan:129). Viewpoint: integrity. Route: implementation skill.
8. **The chain has no tags to start from.** The plan relies on the owner to provide tags for the releases that `CHANGELOG.md` lists (plan:59), and nothing else ties a release to a commit. Viewpoint: integrity. Route: tooling.

## Files read

- `review-task/plan-review.md`
- `.agents/kit/devsecops-plan.md`
- `.agents/kit/devsecops.md`
- `.claude/skills/devsecops/SKILL.md`
- `.claude/skills/devsecops/references/checklist.md`
- Grep matches, not whole files, of these:
  - `README.md`
  - `CONTRIBUTING.md`
  - `packaging/arch/PKGBUILD`
  - `packaging/alpine/APKBUILD`
  - `packaging/obs/_service`
  - `tcc-guard/systemd/asus-ux8406-tcc-guard.service.in`
- File listings of `packaging/` and `.github/`.

## Not verified

I did not read the Rust, C or JavaScript sources, `Cargo.lock`, `flake.nix`, `flake.lock`, `CHANGELOG.md` or the other packaging files. I did not check the claim of "115 packages" or the digests in the Dockerfiles, and I did not run any command. I left the viewpoints other than `integrity` undone, as instructed.
