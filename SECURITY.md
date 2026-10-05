# Security policy

## Supported versions

Only the latest release gets corrections.

## How to report a vulnerability

Do not open a public issue for a vulnerability.

1. Open the tab "Security" of this repository on GitHub.
2. Select "Report a vulnerability".
3. Give the version, the steps to get the result, and the effect.

You get an answer in a maximum of 14 days. After a correction is released, the repository
publishes a security advisory that gives the affected versions and the corrected version.

## Scope

The programs in `skills/*/scripts/` read data from other parties: repositories, registries and
advisory databases. A report is in scope if such data can make a program do one of these things:

- Run a command that the data contains.
- Write a file outside the work folder.
- Send a token to a host that is not the host of the examined repository.

A wrong score or a wrong tier is a defect, not a vulnerability. Use a public issue for it.
