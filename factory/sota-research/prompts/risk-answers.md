# Task: record the answers of risk and reward for the checklist items

You get the folder of one aspect specification. For each item of the checklist in `spec.md`
that is not retired, write one row in the table "Items" of `vetting.md`.

A program computes the admission, the order and the level from your answers. Do not write a
level, a score or an admission result. Leave those cells empty.

## The answers

Read the questions and the meaning of each value in `scripts/rubric-items.txt`. Use only the
values of the scale.

| Cell | Question |
|---|---|
| Severity | How bad is the harm that the item prevents? |
| Probability | How strongly do regulations and standards ask for the item? |
| Breadth | In how many contexts does the item apply? |
| Adopt | How many elements does a project add or change to adopt the item? |
| Keep | How many elements does a project change to keep the item? |
| Own risk | Which risk does the item itself bring? |

## Rules

- Write each answer as a number, then its source in parentheses: `3 (S-02 section 4)`. Read
  `evidence.md` in this turn to find the source. Do not use a summary of it or your memory.
- A source is a row of section 2 of `spec.md`, with the location in that source. A context, a
  view, a risk dimension or a different part of the specification is not a source.
- For Probability, read each row of the table "Requirements" of `vetting.md` that names the
  item in its last cell. A row gives the answer when it asks for the item and its source has
  the class `standard` or `foundation` in section 2 of `spec.md`. A source of the class
  `standard` is a regulation or a standard. Words such as "shall" and "must" require. Words
  such as "should" recommend. Write the row and its source: `3 (R-0123, S-04 page 26)`.
- For Adopt and Keep, count the elements: the settings, the steps, the files and the
  integrations. Take them from a source that shows them, for example a sample of a maintained
  component that does the item. Do not estimate a time. Do not use a statement of a source
  about hours, days or the size of a team.
- If no source gives the answer, write `(judgement)` after the number. Do not invent a source.
- The check names each item whose severity and probability have no source. Give each one to
  the owner as a question. A decision of the owner is not a source: record it with its date
  in section 7 of `spec.md`.
- Answer for a typical project. Do not answer for one project that you know.
- If the return of an item depends on the risk of a project, write the name of the risk
  dimension from section 1 of `spec.md` in the cell Dimension. An example is an item with a
  high cost.
- If you cannot answer a question, leave the cell empty. The item then stays pending, and the
  owner sees it.

Then run `scripts/place.py <folder>`. If the program reports that an item is above level 1 and
has no dimension, record the dimension and run the program again. When no item is pending, run
it with `--write`.

Give the table to the owner for the review. The owner can correct each answer.
