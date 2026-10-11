# Result of the experiment: stage test of a reader that gets the text of a web source

- Registration: seal bccda5b0f99f, sealed on 2026-10-11, commit (none)
- Valid runs: 10 of 10

## Counts

| Criterion | Arm | Yes | Runs | Share | Wilson 95 % interval | Predicted count |
|---|---|---|---|---|---|---|
| C-1 | web | 5 | 5 | 100 % | 57 % to 100 % | 0 |
| C-1 | text | 5 | 5 | 100 % | 57 % to 100 % | 5 |
| C-2 | web | 5 | 5 | 100 % | 57 % to 100 % | 0 |
| C-2 | text | 5 | 5 | 100 % | 57 % to 100 % | 5 |
| C-3 | web | 5 | 5 | 100 % | 57 % to 100 % | 5 |
| C-3 | text | 5 | 5 | 100 % | 57 % to 100 % | 5 |

## Comparison of the arms

| Criterion | Arms | Exact test of Fisher, two sides |
|---|---|---|
| C-1 | web, text | p = 1.0000 |
| C-2 | web, text | p = 1.0000 |
| C-3 | web, text | p = 1.0000 |

## Verdict

- Hypothesis: A reader that gets the text of a web page as a converted file reports 25 or more requirements of the page in more runs than a reader that fetches the same page with its web tool.
- Criterion: C-1
- Confirmed when: `text - web >= 3`
- Refuted when: `text - web <= 0`
- Counts: web = 5, text = 5
- Verdict: refuted

## Runs that were not valid

(none)

## Explanations after the fact

Each explanation written here is a guess. No next step rests on it.

## What the files show (seen after the run)

- Requirement lines of each run: with the web tool 28, 39, 36, 25, 31; with the text 33, 41, 36, 32, 34.
- The one reading before the registration gave 13 lines with the web tool. No registered run gave fewer than 25. The limit of C-1 came from one reading, and that reading was not typical.
- The test counts lines. It does not measure if a line says what the page says, and it does not measure if a second reader or a program can examine a line against the text. The statement of the research trial I-14, that the web tool returns a summary, was not examined here.

Predictions: 3 of 6 were correct. Wrong: the two for the arm `web` on C-1 and C-2.
