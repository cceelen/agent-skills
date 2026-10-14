# Plan: DevSecOps

Recipe: `devsecops`, specification commit `8f2ce19` (trial rendering). Selection:
`.agents/kit/devsecops.md`. Written 2026-10-14 by an agent, without the owner.

**Status: PROPOSED, not accepted. No file of the project was changed but the selection and
this plan.** The plan rests on the proposed selection; if the owner changes a decision there,
this plan changes too.

## How the checks were run

- The checks read the working tree at commit `22d6332` only. There is no remote, so no check
  could read the settings of the GitHub repository, its rulesets, its access list, the runs
  of its workflows, its issues or its releases. A check that needs them **fails as "not
  verifiable"** in this run; it is marked `(nv)`.
- `cargo audit --no-fetch --stale` on `Cargo.lock` reported no advisory. The local advisory
  database was not updated; its date was not verified.
- A pattern search for common token formats over the tree found none. No secret scanner
  (gitleaks, trufflehog) is installed; the history (one commit) was not scanned with one.

## The main finding

The documents describe a pipeline that is not in the tree. `README.md`, `CONTRIBUTING.md`,
`flake.nix` and `packaging/obs/README.md` name `.github/workflows/ci.yml`, `review.yml`,
`coverage.yml`, `fuzz.yml`, `release-nix.yml`, `SECURITY.md`, `docs/releases.md`,
`.obs/workflows.yml`, a Renovate configuration and a pre-commit configuration. None of these
files exists (`docs/` is empty, `.github/` holds only the issue template). The commit has
the author `experiment <experiment@example.invalid>`.

Thus the first step decides most of the distance: **the owner restores the missing files
from the original repository, or confirms that they are lost.** If they are restored, run the
checks again before any other step of this plan; many items below can then pass.

## Distance (adopted items whose check fails)

The checklist has 46 items. 42 are proposed for adoption, and all 42 fail in this tree.
Three are proposed for decline (C-23, C-24, C-39), and one is above the target (C-28).

### Security

| Item | Check result | Change | Files | Only the owner can |
|---|---|---|---|---|
| C-01 | fails (nv): no remote; the one commit has no identified author | Push to GitHub with the owner's identity; a ruleset on `main`: no force push, no deletion, pull request required, signed commits | GitHub ruleset (settings) | Create the repository, set the ruleset, sign commits |
| C-02 | fails (nv) | Ruleset: one approval not from the author for outside contributions; record the AI reviewer as a deviation for the owner's own changes | `CONTRIBUTING.md` section "Rules for changes"; ruleset | Decide the number of reviewers; look for a second maintainer |
| C-03 | fails: no build definition of the release in the tree | Restore or write `.github/workflows/release.yml` that runs `meson dist` on a GitHub-hosted runner | `.github/workflows/release.yml` | — |
| C-04 | fails: no workflow makes provenance | Attest the source archive, the Nix packages and the SBOMs with the attestation function of the platform; attach the bundle to the release | `.github/workflows/release.yml`, `release-nix.yml` | — |
| C-05 | fails (nv) | Use only GitHub-hosted runners for release jobs; signing through the platform's OIDC identity, not a stored key | release workflows | Confirm that no self-hosted runner is registered |
| C-06 | fails: no pipeline definition | Separate jobs for build, test, package and publish; `permissions: {}` at the top, then per job the minimum (`contents: read`; `id-token: write` and `attestations: write` only in the attest job) | `.github/workflows/*.yml` | — |
| C-07 | fails: no pipeline definition to examine; history not scanned with a scanner | Secrets only from GitHub environment secrets of a `release` environment; OBS, COPR and Cachix tokens scoped to one project; a secret scan step (and GitHub secret scanning with push protection) | workflows; repository settings | Rotate the OBS token, the Cachix token and the aports SSH key when they move; enable push protection |
| C-08 | fails (nv) | Document the accounts (GitHub, OBS, COPR/Fedora, Cachix, Alpine GitLab, Codecov) with MFA and a dated review | new `docs/accounts.md` | Enable MFA on each account; do the review |
| C-09 | fails: SBOMs exist only for the Nix packages (`flake.nix` output `sboms`); none for the source archive or the rpm, deb, Arch and Alpine packages | Generate a CycloneDX SBOM of the source archive from `Cargo.lock` (and the vendored crates) in the release job; attest and attach it | release workflow | — |
| C-10 | fails: `packaging/arch/PKGBUILD` has `sha256sums=(SKIP)`; `packaging/alpine/APKBUILD` has no `sha512sums`; the Renovate configuration named by the Dockerfiles is absent. Passing parts: `Cargo.lock`, `flake.lock`, base images pinned by digest | Write the release digest into `PKGBUILD` and `APKBUILD` in the release job (`updpkgsums`, `abuild checksum`); a Renovate configuration that pins Actions by full commit digest and updates crates, flake inputs and image digests | `packaging/arch/PKGBUILD`, `packaging/alpine/APKBUILD`, `renovate.json`, release workflow | Install the Renovate app |
| C-11 | fails: no pipeline | Required jobs on each pull request: `cargo audit` (or `cargo deny check advisories`), a secret scanner, a static analysis of the workflows; high and critical stop the merge | `.github/workflows/ci.yml`, `deny.toml` | Decide the limit (proposed: high) |
| C-12 | fails: no threat model | A dated threat model: inputs from `/dev/kmsg` (writable from user space), sysfs, udev events and the configuration file; the root helpers; the release chain | new `docs/threat-model.md` | Review and date it |
| C-13 | fails: rules named (`Cargo.toml` `[workspace.lints]`, `keyboard-bpf/.clang-tidy`, `biome.json`) but no program enforces them in the tree; Clippy is set to `warn`. By judgement the defaults are secure (systemd hardening in `tcc-guard/systemd/*.service.in`, root-owned configuration check in `tcc-guard/README.md`) | Run `cargo clippy -- -D warnings`, `clang-tidy` and `biome ci` as required CI steps; restore `.pre-commit-config.yaml` | `.github/workflows/ci.yml`, `.pre-commit-config.yaml` | — |
| C-14 | fails: `SECURITY.md` is linked but absent | `SECURITY.md` with GitHub private vulnerability reporting, the time limits, and the disclosure through advisories | `SECURITY.md` | Enable private vulnerability reporting; decide the time limits (proposed: 7 days acknowledge, 30 days high and critical, 90 days other) |
| C-15 | fails: no support period is published. Passing part: the repositories sign the packages (apt `signed-by`, pacman key, COPR, Nix cache key) | State the support period: the latest minor release only, until upstream fixes make a part obsolete | `SECURITY.md` | Decide the support period |
| C-16 | fails: the source archive is fetched by COPR, OBS, Arch and Alpine without a digest or an attestation check | The digest in the recipes (C-10); `docs/releases.md` restored with `gh attestation verify`; an optional verify step in the Packit or OBS job | recipes, `docs/releases.md` | — |
| C-17 | fails: fuzz targets exist in `fuzz/`, but `fuzz.yml` is absent and no dated report exists | Restore the nightly fuzz workflow; for each minor release, a dated summary of the fuzz time and the findings | `.github/workflows/fuzz.yml`, `docs/security-tests.md` | — |
| C-18 | fails: no inventory | An inventory: GitHub Actions, Packit/COPR, OBS, Cachix, Codecov, Renovate, the AI reviewer, Alpine GitLab; with owner, version or plan, logs | new `docs/pipeline-inventory.md` | — |
| C-19 | fails: no requirements recorded | One column of the inventory: what each provider must give (MFA, scoped tokens, signing) and when it was examined | `docs/pipeline-inventory.md` | Examine each provider |
| C-44 | fails by judgement: not judged for `second-screen` and `keyboard-state`, which run as root from udev with the kernel name `%k` as an argument | A review of the two helpers against the threat model; record it | `docs/threat-model.md` | — |

### Operations

| Item | Check result | Change | Files | Only the owner can |
|---|---|---|---|---|
| C-20 | fails: the publication is triggered by a webhook and by `.obs/workflows.yml` and `.packit.yaml`, which are absent; only `packaging/obs/_service` is present | Restore the Packit and OBS workflow definitions; the webhook setup stays in `packaging/obs/README.md` | `.packit.yaml`, `.obs/workflows.yml` | — |
| C-21 | fails: no staged release and no rollback procedure | Publish first to a testing channel (a COPR and OBS project for release candidates), then to the release channel; a rollback is a new patch release that reverts; rehearse it once | `docs/releases.md` | Create the testing projects; do the rehearsal |
| C-22 | fails (nv) | Release credentials only in a GitHub `release` environment with a required reviewer and the protected branch; no credential in pull request jobs from forks | workflows; repository settings | Create the environment |
| C-25 | fails: no plan | An incident plan for a compromised or broken release: revoke tokens, withdraw packages from OBS, COPR and Cachix, publish an advisory, review without blame | new `docs/incident-response.md` | Test the plan once |
| C-26 | fails: the release procedure `docs/releases.md` is absent | Restore `docs/releases.md`; the Release Please pull request is the change record; its review and passed pipeline are the approval | `docs/releases.md` | Decide the approval (proposed: review and pipeline) |
| C-27 | fails: no continuity plan | Plan: a mirror of the repository, recovery codes of each account, a second person with access to the release channels; test a restore from the mirror | `docs/incident-response.md` or new `docs/continuity.md` | Keep the recovery codes; name a second person |
| C-29 | fails: no readiness checklist | A checklist for a new package or channel (the Alpine package is the next) | `docs/releases.md` | — |
| C-45 | fails: the tree has no tag; the release tags are in the original repository | Tags from Release Please; `meson dist` from the tag reproduces the archive; record the toolchain version | release workflow | Restore the tags |
| C-46 | fails: no check that OBS, COPR, Arch and Alpine build from the attested archive | The digest in the recipes (C-10) makes each build use the one archive | recipes | — |

### Quality

| Item | Check result | Change | Files | Only the owner can |
|---|---|---|---|---|
| C-30 | fails: `ci.yml` absent; no ruleset (nv) | Restore `ci.yml` (`meson test`, pre-commit, container builds for changes to `packaging/`); require it in the ruleset | `.github/workflows/ci.yml` | Set the required checks |
| C-31 | fails: unit, integration (`tests/cli`, `tests/scenarios`) and system tests (`dev/containers/`) exist, but no pipeline runs them | As C-30 | `.github/workflows/ci.yml` | — |
| C-32 | fails: no pipeline; `.pre-commit-config.yaml` absent | As C-13 | `.github/workflows/ci.yml`, `.pre-commit-config.yaml` | — |
| C-33 | fails by judgement: the limits exist in pieces (guard coverage 100 % of regions, systemd exposure at most 1.3, Rust 1.85) but are not stated as quality requirements | Collect them as measurable requirements with their measure | new `docs/quality.md` | Agree them |
| C-34 | fails: no quality plan | Name the activities: tests, coverage, fuzzing, container installs, hardware test on the UX8406CA, AI and human review | `docs/quality.md` | — |
| C-35 | fails (nv): defects in GitHub issues; no cause recorded | An issue label for the cause, and a line in the changelog or the issue for the process change | `.github/ISSUE_TEMPLATE/`; labels | Apply the labels |
| C-36 | fails (nv): one commit in this tree; the history is in the original repository | Measure the size and the age of the merged pull requests once the repository is on GitHub | — | — |
| C-37 | fails: the documents link to `SECURITY.md` and `docs/releases.md`, which are absent | Restore the two files or remove the links | `README.md`, `CONTRIBUTING.md` | — |
| C-38 | fails by judgement: the part READMEs say what the tests examine; there are no decision records | Short decision records for the main choices (offset steps of the guard, BPF over a kernel module, Meson over Make) | new `docs/decisions/` | — |
| C-40 | fails: no document names the owners | A short list of the duties and their owner (the maintainer), and `CODEOWNERS` | `docs/quality.md`, `.github/CODEOWNERS` | Confirm |
| C-41 | fails: no register of duties | A register: the CRA decision of the selection, its owner, the place of the evidence | new `docs/obligations.md` | Confirm the decision on the CRA |
| C-42 | fails (nv): the issues are referenced but cannot be read | A GitHub project or milestones for the work and the risks | — | Set it up |
| C-43 | fails: the README says the packages are workarounds "until the upstream projects supply the fix", with no end date | A maintenance statement: the end of each part when its upstream fix is in the supported distributions, and the end of the project | `README.md` or `SECURITY.md` | Decide the end-of-life rule |

## Measured targets

| Target | Level the plan reaches | What stops the next level |
|---|---|---|
| SLSA build track | Now: not determinable from the tree (the release workflow is absent); the changelog of 0.5.0 says that the source archive has a provenance bundle. After C-03, C-04, C-06: Build L2 for the source archive and the Nix packages | Build L3 needs the attestation from an isolated, hardened builder (reusable workflow with the platform's attestation) and is open for the rpm, deb and Arch packages, which COPR and OBS build without SLSA provenance |
| SLSA source track | Not determinable: no remote | A protected main line and a summary attestation of the source control system |
| Software delivery metrics | Not measured (C-28 is above the target) | Pipeline data on GitHub |
| Repository practice score | Not measurable in this tree; the README shows a badge of the original repository | The repository on GitHub; then C-01, C-02, C-06, C-10, C-11, C-14 raise it |
| Security baseline of an open project | Not assessed | A self-assessment against one dated version of the baseline |
| Maturity of software assurance | Not assessed | A self-assessment |

## Order of the work when the plan is accepted

1. Restore the missing files (or confirm their loss) and run the checks again.
2. Source: C-01, C-02, C-08.
3. Feedback on each change: C-30, C-31, C-32, C-11, C-13.
4. Build: C-03, C-06, C-07, C-04, C-05.
5. Dependencies: C-10, C-09.
6. Release and deployment: C-16, C-46, C-20, C-21, C-26, C-45.
7. Operation: C-25, C-27, C-29, C-22.
8. Vulnerabilities: C-14, C-15, C-17, C-12, C-44.
9. Governance: C-18, C-19, C-40, C-41, C-43, C-33, C-34, C-35, C-38, C-42, C-37, C-36.

Delegate where an implementation skill exists: the pipeline (C-03 to C-07, C-10, C-30), the
repository score (C-01, C-02, C-14), the provenance and the signature (C-04, C-05, C-16).
None is installed in this session; the plan names the capabilities only.

## Open decisions of the owner (stop points of the recipe)

The target level of the build integrity scale, the number of reviewers, the approval of a
release, the time limits for vulnerabilities, the decline of C-23, C-24 and C-39, and the
decision to prepare for the CRA. All carry a proposal in the selection.
