| Code | Criterion | Answer | Evidence |
|---|---|---|---|
| P-e9f3d1ab1b | P-1 | yes | files/.agents/kit/devsecops-plan.md lines 63-64 (C-11 dependency scan, secret scan, stops the merge), 69 (C-13 static analysis), 85-86 (C-30 tests per change, C-31); coverage in line 12 area/C-33 (guard coverage) and line 26 (coverage.yml named) |
| P-e9f3d1ab1b | P-2 | yes | files/.agents/kit/devsecops-plan.md C-11 row (cargo audit, cargo deny), C-13 row (clippy, clang-tidy, biome), C-10 row (Renovate), C-04 row (platform attestation) |
| P-e9f3d1ab1b | P-3 | yes | files/.agents/kit/devsecops-plan.md C-06 row (separate jobs for build, test, package, publish; permissions per job, id-token only in attest job) |
| P-e9f3d1ab1b | P-4 | yes | files/.agents/kit/devsecops-plan.md "Measured targets" table, column "Level the plan reaches" |
| P-e9f3d1ab1b | P-5 | yes | files/.agents/kit/devsecops-plan.md "Measured targets" table, column "What stops the next level" |
| P-e9f3d1ab1b | P-6 | yes | files/.agents/kit/devsecops-plan.md last section "Open decisions of the owner" (last lines: "All carry a proposal in the selection"); status line 6 "PROPOSED"; proposals marked in rows such as C-14 and C-26 |
| P-e9f3d1ab1b | P-8 | yes | files/.agents/kit/devsecops.md lines 33-45 ("Regulation and governance" table; owner cannot know where the product is used) |
| P-e9f3d1ab1b | P-9 | yes | files/.agents/kit/devsecops.md C-39 line (declined, note that the CRA asks for it so the decline is a deviation) and the "(prepared: Regulation (EU) 2024/2847)" marks on items; weak evidence, no ordering by source class |
| P-e9f3d1ab1b | P-11 | yes | files/.agents/kit/devsecops.md lines 35-43 (columns "Binds the project?" and "Binds a user of the product?" with reasons based on non-commercial open source) |
