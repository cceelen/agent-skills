I've read the plan, the selection, the skill and the packaging files. Next I'm writing the integrity report.

**Integrity review of `.agents/kit/devsecops-plan.md`: viewpoint `integrity`**

Paths are relative to the trial project. Line numbers for the plan and the selection are from my reads. Where a project file was read through a search, the line is the one the search returned.

### Assets

The assets are:
- A1 source
- A2 inputs from outside: crates, the Nix flake inputs, base images, tools of the pipeline
- A3 build
- A4 tests
- A5 results of tests and checks
- A6 released result (the source archive)
- A7 what the user gets: distribution packages built from the archive
- A8 the system on which it runs: root guard, udev helpers, BPF program
- A9 data read and written: `/dev/kmsg`, sysfs, the guard's config and store
- A10 the pipeline itself
- A11 records of the project: `CHANGELOG.md`, tags, the review record, issues and advisories

### Questions 1 to 3, one row per asset

Question 1 asks who can change the asset and leave no trace. Question 2 asks what shows a change. Question 3 asks whether that check is tied to the asset.

| Asset | Q1: untraced change | Q2: what shows it (result) | Q3: tied to the asset? (result) |
|---|---|---|---|
| A1 source | The owner can force-push or delete `main`, and no rule exists. The repository has one commit and no remote (`.agents/kit/devsecops.md:11`). The plan defers the rule to the owner (`.agents/kit/devsecops-plan.md:74`). | `partly`. C-02 and C-15 are "not measurable" and left to the platform (`devsecops-plan.md:74-76`). No signed summary is planned (`devsecops-plan.md:137`). | `no`. No check exists yet. Tags are absent (`devsecops-plan.md:59`). |
| A2 inputs from outside | A crate, base image or flake input can change. This is mostly covered: `Cargo.lock` has checksums, `--locked` is used and the base images have digests (`devsecops-plan.md:128`). The pipeline tools have no pins (`devsecops-plan.md:67`). The OBS service takes the source by tag (`packaging/obs/_service:7`), and a tag can move. | `partly`. C-28 passes (`devsecops-plan.md:128`). The update tool and action pins are only proposed (`devsecops-plan.md:67`). | `partly`. Digests and checksums tie the crates and images. The tag in `packaging/obs/_service:7` ties nothing. `fuzz/Cargo.lock` is ignored on purpose (`devsecops-plan.md:67`). |
| A3 build | A build on a personal computer leaves no trace. No hosted build exists (`devsecops-plan.md:62`). | `partly`. Signed provenance is planned (`devsecops-plan.md:64`). It is not yet in place. | `partly`. The plan binds the provenance to the repository (`devsecops-plan.md:64`). It does not say that the provenance names a commit. C-01 expects a release "built from a commit" (`.claude/skills/devsecops/references/checklist.md:13`). |
| A4 tests | A commit can delete or weaken a test or fixture. Nothing guards them: the fixtures are in the tree (`tcc-guard/tests/fixtures/README.md`), and the test requirement is left to the platform (`devsecops-plan.md:109`). | `partly`. A coverage limit exists for the guard only (`CONTRIBUTING.md:127`). The pipeline that holds it is absent (`devsecops-plan.md:142`). | `no`. The coverage result is not bound to a commit or an archive digest. |
| A5 results of tests and checks | A run summary or an upload to Codecov can be edited or lost. No pipeline exists (`devsecops-plan.md:19`). | `no`. C-33 (keep results as evidence) is above the target (`.agents/kit/devsecops.md:121`). The plan stores nothing. | `no`. Nothing is stored, so nothing is tied. |
| A6 released result | A person can upload a different archive. No immutable releases exist and the plan leaves this to the owner (`devsecops-plan.md:95`). The digest and the provenance are not reachable (`devsecops-plan.md:65`). | `partly`. The plan adds a digest file, provenance and a compare-before-upload step (`devsecops-plan.md:63-65`). | `partly`. The digest check is tied to the archive (`devsecops-plan.md:63`). It is not tied to a commit, because there is no tag. |
| A7 what the user gets: packages | The distribution services rebuild from the archive. The plan itself says this is "outside the check" (`devsecops-plan.md:63`). Arch skips the checksum (`packaging/arch/PKGBUILD:20`). Alpine has no checksum line (`packaging/alpine/APKBUILD:34`). | `partly`. Package-manager signatures cover the repositories (`devsecops-plan.md:66`). | `no`. The package signature is not tied to the project's archive digest or provenance. |
| A8 the system on which it runs | The guard runs as root and the BPF program runs in the kernel (`.agents/kit/devsecops.md:22`). Nothing shows a change of the host it touches. | `no`. The plan has no check on this asset. | `not applicable`. There is no check to tie. |
| A9 data read and written | The guard reads kernel-log input that user space can write (`.agents/kit/devsecops.md:45`). The plan records no change of that data. | `partly`. The tests and fuzz targets examine the parsers (`devsecops-plan.md:130`). The nightly fuzz job is not in the tree (`CONTRIBUTING.md:144`). | `no`. The checks are not tied to the data or to a release. |
| A10 the pipeline itself | The pipeline is absent. A change to a workflow, a secret or a webhook leaves no trace. No branch rule covers it (`devsecops-plan.md:19`). C-23 is not examinable (`devsecops-plan.md:94`). | `partly`. The plan lists per-job permissions and action pins (`devsecops-plan.md:61,67`). Pipeline logs (C-32) are above the target (`.agents/kit/devsecops.md:126`). | `no`. Nothing ties the pipeline definition to a run or to a release. |
| A11 records | `CHANGELOG.md`, the tags and the review record can be rewritten. The changelog claims a provenance bundle that does not exist (`devsecops-plan.md:64`). The advisories and issues are not reachable. | `partly`. Platform records are expected after C-02 and C-03 (`devsecops-plan.md:76`). The "not verified" list says these claims cannot be checked (`devsecops-plan.md:151`). | `no`. Records are not tied to a commit. The selection stamps the recipe, but not the plan's own sources. |

### Questions 4 to 7

| Question | Result | Evidence | Sentence |
|---|---|---|---|
| 4. Where does the chain of evidence end before the thing the user gets? | `yes` | `devsecops-plan.md:63`; `packaging/arch/PKGBUILD:20`; `packaging/obs/_service:7` | It ends at the release archive. The distribution rebuild and the packages are outside the check, Arch skips the digest, and the OBS service fetches by a movable tag. |
| 5. Which results are kept as evidence, and which are lost after the run? | `no` | `.agents/kit/devsecops.md:121`; `devsecops-plan.md:142` | The plan keeps no test, coverage, scan or analysis result. C-33 is above the target, and the coverage is only shown in the run summary and sent to Codecov. |
| 6. Can one change weaken a check and pass? | `yes` | `devsecops-plan.md:86`; `CONTRIBUTING.md:127`; `devsecops-plan.md:109` | A change can lower the guard's coverage limit, drop a test or edit the lint job. The plan has no protection or review for the checks themselves. |
| 7. Does the risk analysis ask what the result can do to the system on which it runs and to the data it changes? | `no` | `.agents/kit/devsecops.md:33-35`; `.claude/skills/devsecops/SKILL.md:57-61` | The three questions cover exposure, harm to users and evidence duty. The root guard's effect on the host is only noted in prose. |

For question 6, the plan does say the lint job will deny warnings (`devsecops-plan.md:86`). That job, the coverage limit and the pins can all be changed in the same commit as the code they check.

### Findings

1. The plan does not require the signed provenance or the digest to name the commit and tag. No tag exists, and the plan's own table shows this (`devsecops-plan.md:59,64`). Viewpoint: `integrity`. Route: `recipe`.
2. The chain of evidence ends at the source archive. The distribution rebuild is "outside the check", Arch skips the checksum and Alpine has none (`devsecops-plan.md:63`, `packaging/arch/PKGBUILD:20`). Viewpoint: `integrity`. Route: `recipe`.
3. The OBS service fetches the source by a tag, not by a commit or a digest (`packaging/obs/_service:7`). The plan does not name this input. Viewpoint: `integrity`. Route: `implementation skill`.
4. No result of any check is stored as evidence. C-33 is above the target, and the coverage is only shown in the run summary and sent to Codecov (`.agents/kit/devsecops.md:121`, `devsecops-plan.md:142`). Viewpoint: `integrity`. Route: `recipe`.
5. One change can weaken a test, the coverage limit, a lint level or a pipeline setting and still pass. The plan has no rule that protects the checks (`devsecops-plan.md:86,109`, `CONTRIBUTING.md:127`). Viewpoint: `integrity`. Route: `recipe`.
6. The selection's risk questions do not ask what the root guard, the udev helpers and the BPF program can do to the host or to the data they change (`.agents/kit/devsecops.md:33-35`). Viewpoint: `integrity`. Route: `recipe`.
7. The pipeline has no integrity control. The log item C-32 and the separated-environments item C-31 are above the target, and the plan only checks the pipeline permissions (`.agents/kit/devsecops.md:126-127`, `devsecops-plan.md:61`). Viewpoint: `integrity`. Route: `recipe`.
8. The plan gives no check for the data the guard reads. The fuzz job named in `CONTRIBUTING.md:144` is not in the tree, and the plan does not add it (`devsecops-plan.md:19`). Viewpoint: `integrity`. Route: `tooling`.
9. The records of the project can be rewritten without a trace. `CHANGELOG.md` states a provenance bundle that does not exist, and the tags are missing (`devsecops-plan.md:64`). Viewpoint: `integrity`. Route: `tooling`.

### Files read

- `review-task/plan-review.md`
- `.agents/kit/devsecops-plan.md`
- `.agents/kit/devsecops.md`
- `.claude/skills/devsecops/SKILL.md`
- `.claude/skills/devsecops/references/checklist.md`
- `CONTRIBUTING.md` (lines 60-195, plus a search)
- `Cargo.toml` (search only)
- `packaging/arch/PKGBUILD`
- `packaging/obs/_service`
- `packaging/alpine/APKBUILD` (search only)
- `packaging/rpm/asus-zenbook-duo-ux8406.spec` (search only)
- `packaging/nix/package.nix` (search only)
- `README.md` (search only)
- A file listing of the project

### Not verified

- I did not read the Rust, C and JavaScript sources, `flake.nix`, `meson.build`, `Cargo.lock`, the container files or the CHANGELOG.
- I did not check any remote setting, since none exists.
- I did not run any command.
- I did not check the plan's counts of passed and failed items.
