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
| Probability | How probable is that harm in a project that does not have the item? |
| Breadth | In how many contexts does the item apply? |
| Adopt | How much effort is necessary to adopt the item? |
| Keep | How much effort is necessary to keep the item? |
| Own risk | Which risk does the item itself bring? |

## Rules

- Write each answer as a number, then its source in parentheses: `3 (S-02 section 4)`. Use
  the evidence record to find the source.
- If no source gives the answer, write `(judgement)` after the number. Do not invent a source.
- Answer for a typical project. Do not answer for one project that you know.
- If the return of an item depends on the risk of a project, write the name of the risk
  dimension from section 1 of `spec.md` in the cell Dimension. Examples are an item that only
  a regulated project needs, and an item with a high cost.
- If you cannot answer a question, leave the cell empty. The item then stays pending, and the
  owner sees it.

Then run `scripts/place.py <folder>`. If the program reports that an item is above level 1 and
has no dimension, record the dimension and run the program again. When no item is pending, run
it with `--write`.

Give the table to the owner for the review. The owner can correct each answer.
