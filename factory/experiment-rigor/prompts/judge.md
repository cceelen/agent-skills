# Task of the judge

You get the path of one folder. It holds one folder for each packet.

1. Open only this folder. Do not open a different folder.
2. Do not ask what the experiment tests.
3. In each packet, read `criteria.md` first. It lists the criteria of the packet.
4. Read what the column `Where` names. `final` is each file `final-<number>.md` of the packet.
   `file:<path>` is the file `files/<path>` of the packet.
5. Answer each criterion of each packet with `yes` or `no`. If the file that a criterion names
   is absent, answer `no`.
6. Give the evidence for each answer: a file of the packet and a line number.
7. Examine each packet alone. Do not compare a packet with a different packet. Do not guess the
   group of a packet.
8. Write this table into the file `judgements.md` in the folder that you got. Write one row for
   each packet and each criterion. The code is the name of the folder of the packet.

```markdown
| Code | Criterion | Answer | Evidence |
|---|---|---|---|
| P-0123456789 | C-1 | yes | final-1.md line 3 |
```

9. If you cannot write a file, return the table as your answer, and no other text.
