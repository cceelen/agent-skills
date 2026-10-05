# How to contribute

Thank you for your help. Use the GitHub issues of this repository for each contribution.

## Report a defect or propose a change

1. Look for an issue that describes the same subject.
2. If there is none, open an issue.
3. For a defect, give the command, the result that you got and the result that you expected.
4. For a wrong score, give the library, the criterion and the evidence.

To report a vulnerability, obey [SECURITY.md](SECURITY.md). Do not open a public issue.

## Change the code

1. Open an issue first, and wait for an answer. This prevents work that cannot be merged.
2. Read [AGENTS.md](AGENTS.md). It contains the rules for the programs, the tests and the
   documentation.
3. Install [uv](https://docs.astral.sh/uv/).
4. Use the command `uv run pre-commit install` one time.
5. Make the change, and add a test for it.
6. Use the command `uv run pre-commit run --all-files`. All checks must pass.
7. Open a pull request that refers to the issue.

## Rules that are frequently missed

- The programs use only the standard library of Python 3.9.
- The tests do not use the network.
- If you change the scoring, increase the rubric version and update the expected values in the
  tests.
- Do not change the identifier of a criterion.

## License

Your contribution has the license of this repository, the MIT license.
