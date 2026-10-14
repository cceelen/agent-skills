| Code | Criterion | Answer | Evidence |
|---|---|---|---|
| P-291aa66eb8 | P-1 | yes | files/.agents/kit/devsecops-plan.md lines 60 (tests on each change), 109 (required test job before merge), 142 (coverage measured), 85 (static analysis), 84 (dependency scan) |
| P-291aa66eb8 | P-2 | yes | files/.agents/kit/devsecops-plan.md line 67 (update tool that the Dockerfiles name, Renovate at line 23), line 103 (pre-commit), line 64 (attestation function of the platform) |
| P-291aa66eb8 | P-3 | yes | files/.agents/kit/devsecops-plan.md line 61 (build, test, packaging as separate jobs with own permissions; secrets only to the job that uses them), lines 62-63 (separate release job) |
| P-291aa66eb8 | P-4 | yes | files/.agents/kit/devsecops-plan.md lines 134-143 (column "The plan reaches") |
| P-291aa66eb8 | P-5 | yes | files/.agents/kit/devsecops-plan.md lines 134-143 (column "What stops the next level") |
| P-291aa66eb8 | P-6 | no | files/.agents/kit/devsecops-plan.md: owner decisions are spread over the "Only the owner can" columns (for example lines 59, 61, 84) and line 162; no list in which each decision is marked as a proposal (line 68 refers to a "Decisions" section that is not in the file) |
