# Changelog

This file shows the changes of each version. A change of the major number means that earlier
reports are not comparable with new reports.

## Next version

- The kit gives the agent five rules for evidence before action. The rules are in each skill.
  The plugin puts them into each session. `install.sh` adds them to the instruction file of the
  user. The section "The rules of the kit" in `README.md` tells you how to prevent this.
- The repository gets the tooling of the factory in `factory/sota-research/`. It distils the
  state of the art of one aspect of software engineering into a recipe skill. Users of the
  kit do not install it.
- The tooling uses the latest stable Python and runs with `uv`.

## 1.0.3

The skill did not change.

- A published release cannot be changed. The files and the tag of the release are permanent.
- The tags `v1.0.1` and `v1.0.2` have no release. Do not use them.

## 1.0.0

The first public version. It contains one skill, `library-vetting`, with the rubric
`library-vetting v1`.

- The skill examines an open source library in 15 dimensions and gives a tier.
- `collect.py` collects the facts: the registry record, the history, the files, the CI
  configuration, the advisories, the OpenSSF Scorecard and the base stack.
- `score.py` calculates the scores, the tier and the SLSA levels for the Build track, the
  Source track and the Dependency track.
- `models.py` saves the model for each role of the skill.
- The skill can use the programs pipeline-check and Plumber if they are installed.
