The file spec.md holds two parts of a specification: the decisions that depend on context (3.3) and the checklist (4).
The file vetting.md holds a table "Requirements". Each requirement comes from a source. The cell "Goes to" of each row is empty.

Write the cell "Goes to" of each row. A requirement does not go to a decision of 3.3: a decision tells how a practice is done, not if it is done. Use one of these forms:

- `C-nn`: the checklist item that holds the practice of the requirement. Use it only if the words of the item name that practice.
- `new: <one sentence>`: a new checklist item, if no item names the practice of the requirement. Two rows with the same practice get the same sentence.
- `5`: the requirement names a product, or it is a task for a skill of one product.
- `duplicate: R-nn`: a different row of the table says the same.

Do not change spec.md. Do not change another cell. Do not make another file.
