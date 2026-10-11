# Reading: do the requirement lines of ST-13 say what the page says

This is a reading of recorded reports. It did not go through the gate of the experiments: it
has no registration and no seal. The agent stated its expectation to the owner before the
marks came back: the reports of the arm `text` have a smaller share of lines with the mark
`more` or `absent` than the reports of the arm `web`.

## Input

- The requirement lines of the ten reports of the stage test ST-13: five of the arm `web`,
  five of the arm `text`.
- The converted text of the page, written by `web.py` on 2026-10-11. It is in the work folder
  and is not committed.

## Method

- A program gave each report a code in a random sequence. A judge did not see the arm.
- Four judges of the mid-size model marked each line as `same`, `more` or `absent`, with the
  task `judge-task.md`. Each judge had two or three reports.
- Each mark `same` or `more` needs a quote from the text. A program compared each quote with
  the text, with the spaces and the case made equal.

## Result

| Arm | Lines | `same` | `more` | `absent` | Quotes not in the text |
|---|---|---|---|---|---|
| web | 159 | 159 | 0 | 0 | 0 |
| text | 176 | 172 | 4 | 0 | 0 |

The expectation was wrong. The lines of the readers that used the web tool are as true to the
page as the lines of the readers that had the text.

The four lines with the mark `more`, all of the arm `text`:

- One line gives a duty to the build platform. The page gives it to all implementations.
- One line has the strength MUST. The page states that requirement with no keyword.
- Two lines (two reports) make a duty to document wider than the page makes it.

## Limits

- One page of one specification. The page has clear headings and keywords for the strength.
  A long page, a page that the web tool cuts, or a page without such keywords can give a
  different result.
- The judges are agents. No person examined the marks.
- A first pass with a task that asked only for the heading of the page as evidence was not
  valid: one judge marked each of its 165 lines `same` with one text of evidence for all. The
  marks above are from the second pass, with the quote. A judge that must quote can be
  examined by a program; a judge that must not, cannot.

## What follows

- The procedure stays as it is after ST-13: a web page is converted only when it came back
  empty or in part, or when its words must be examined.
- The statement of the trial I-14, that the web tool returns a summary and not the text, is
  true for the tool, but on this page it did not make the lines less true.
