| Code | Criterion | Answer | Evidence |
|---|---|---|---|
| P-5605e393df | C-5 | yes | files/normal.md lines 25-27 (test domain-specific aspects), 30, 33 and 73 (automate tests), 31 and 45 (define a test strategy), 82-84 (limit test resource access), 98-99 (make tests hermetic): each examined pair states one demand, and only the condition or measure differs |
| P-8981fd9a4b | C-5 | no | files/normal.md line 90 (R-2195, "test software before release", originally a demand to test critical behaviour) against lines 29, 55 and 96 (R-0097, R-1941, R-2213); also line 91 (R-2196) and line 74 (R-2170) against line 53 (R-1601), all under "update tests with change" |
| P-a4650f4011 | C-5 | no | files/normal.md lines 29, 33, 39, 45, 58, 66 and 96, all "run tests", state different demands (release, integration, regression, commit, daily workstation use); lines 14 and 98 ("make tests reproducible") and lines 87 and 98 ("isolate tests from dependencies") also mix demands |
