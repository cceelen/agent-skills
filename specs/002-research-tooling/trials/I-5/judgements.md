| Code | Criterion | Answer | Evidence |
|---|---|---|---|
| P-731cdd054a | C-1 | no | files/specs/001-devsecops/spec.md lines 206 to 244: level 1 has static analysis (line 221) and a scripted release build (line 212), but no coverage item and no robustness item; two of four |
| P-731cdd054a | C-2 | no | files/specs/001-devsecops/spec.md lines 227 to 234: the quality items on level 1 ask for tests (lines 227 and 228), no item asks for a measure of coverage |
| P-731cdd054a | C-3 | yes | files/specs/001-devsecops/spec.md line 221 (C-16, level 1) |
| P-731cdd054a | C-4 | no | files/specs/001-devsecops/spec.md lines 206 to 244: no item for robustness tests; fuzzing is only an option of a decision (line 159), and dynamic security tests are on level 2 (line 225) |
| P-731cdd054a | C-5 | yes | files/specs/001-devsecops/spec.md line 212 (C-07, level 1: the release build runs from a script on a hosted build platform) |
| P-731cdd054a | C-6 | no | files/specs/001-devsecops/spec.md lines 34 to 42 and 49 to 52: no stakeholder and no view for the architecture |
| P-731cdd054a | C-7 | yes | files/specs/001-devsecops/spec.md line 35 (operations engineers); line 49 (view operations) |
| P-731cdd054a | C-8 | yes | files/specs/001-devsecops/spec.md line 37 (quality and test staff); line 51 (view quality) |
| P-731cdd054a | C-9 | yes | files/specs/001-devsecops/spec.md line 34 (developers) |
| P-731cdd054a | C-10 | yes | files/specs/001-devsecops/spec.md line 40 (consumers: users, customers and acquirers) |
| P-731cdd054a | C-11 | no | files/specs/001-devsecops/spec.md lines 206 to 244: the column Level holds only 1, 2 and not admitted; final-2.md line 114 says none on level 3 |
| P-731cdd054a | C-12 | yes | files/specs/001-devsecops/spec.md line 84 (SLSA build level, Build L0 to Build L3); line 85 (SLSA source level) |
