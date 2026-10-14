# Seeds

A seed is a document or a standard that the factory starts from. This file names where each
one is. It does not hold the content. The program `scripts/seed.py` reads the two tables.

## The seeds

| Id | Document | Issuer | Version or date | Kind | Address | sha256 | Terms | Row read on |
|---|---|---|---|---|---|---|---|---|
| swebok | Guide to the Software Engineering Body of Knowledge (SWEBOK Guide) | IEEE Computer Society | 4.0a, 2025-09-25 | owner file | https://www.computer.org/education/bodies-of-knowledge/software-engineering | 0c9db4da0b2425c58cf778b99131eb31bb6c188e98b67163a549a1366d96e511 | Individual use that is not commercial. Quotes of a reasonable length with the citation. No copy for other persons. | 2026-10-10 |

The cells:

- `Id`: lowercase letters, digits and hyphens. The files of the seed get this name.
- `Kind`: one of these three values.
  - `pdf`: the address is the public address of a PDF file.
  - `page`: the address is a public web page.
  - `owner file`: the address is the page where a person gets the file.
- `sha256`: the digest of the file when the row was written. Leave the cell empty if the file
  was not retrieved yet.
- `Terms`: what the issuer permits.

## Bodies of knowledge

A body of knowledge divides a whole field into knowledge areas.

| Field | Seed |
|---|---|
| software engineering | swebok |

## How to retrieve the seeds

1. Run `uv run factory/sota-research/scripts/seed.py get <work folder>`. The work folder is
   outside each git repository.
2. For a seed with the kind `owner file`, ask the owner to get the file from the address. Then
   add `--file <id>=<path>` to the command.
3. For a seed with the kind `page`, give the address to a web reader.
4. Do not read a file of `<work folder>/converted/` yourself. Give its path to a file reader.
5. If the program reports the state `changed`, tell the owner. Do the steps of "How to add a
   row" for that seed.
   - To find a seed that changed at its address, add `--fresh`. The program then downloads
     each file again.
6. If the manifest has no digest for a seed, write the digest that the program prints into the
   row.

## How to read the SWEBOK Guide

- The guide is a PDF file behind a form on the page of the issuer. A reader cannot get it.
  Ask the owner to get the file and to give its path.
- Retrieve it with `scripts/seed.py get <work folder> --file swebok=<path>`. Give the file
  `<work folder>/converted/swebok.md` to a file reader.
- Keep the file and its converted text out of each repository and out of each kit.
- Do not give the file or its converted text to a different person.
- Write the evidence record in the words of this kit.
- If the owner cannot give the file, let a web reader read the page of the issuer for the
  list of the knowledge areas. Record in section 7 that the guide was not read.

## How to add a row

1. Read the page of the issuer in the same turn.
2. Write the version and the date that the page gives. Write the date of today into the cell
   `Row read on`.
3. Do not write a row from your memory.
4. If the seed is a body of knowledge, add one row to the table "Bodies of knowledge".
5. Run `uv run factory/sota-research/scripts/seed.py list`. Correct each line that it reports.
6. Stop. Give the row to the owner. The row enters the manifest only after the owner accepts
   it.
