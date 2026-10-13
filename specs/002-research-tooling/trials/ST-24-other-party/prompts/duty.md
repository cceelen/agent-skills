The folder specs/001-devsecops holds an aspect specification after its research: spec.md, evidence.md and vetting.md. The file step.md holds a part of the step "Distil" of the procedure in factory/sota-research/references/procedure.md.

Do the last rule of step.md for the table "Requirements" of vetting.md: for each requirement of a source of the class `regulation` or `governance`, find who has the duty, and write the exit that step.md gives into the cell "Goes to". Section 2 of spec.md gives the class of each source. Do not change a different cell of a row. Do not change a row of a different source. Do not remove a row.

Then run `uv run factory/sota-research/scripts/check.py specs/001-devsecops`. Correct each line that starts with `FAIL`, in the way that the procedure gives. Then do the part "The value and the level of an item" of the procedure.

Run the check again and write its full output into the file check.out in the current folder.

The owner is not in this session. Do not ask a question. Give as your final report: the number of rows that you changed, for each source, and each item that changed its level or its strongest source.
