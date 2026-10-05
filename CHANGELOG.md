# Changelog

This file shows the changes of each version. A change of the major number means that earlier
reports are not comparable with new reports.

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
