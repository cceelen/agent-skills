| Code | Criterion | Answer | Evidence |
|---|---|---|---|
| P-fac6505c17 | K-1 | yes | files/specs/001-devsecops/spec.md line 135 (S-27 OSV.dev, documentation of the service); line 183 (decision row "Which data service gives the known vulnerabilities": a public service that collects the databases of the ecosystems) |
| P-fac6505c17 | L-4 | yes | final-1.md lines 203-259 (checklist in the order of place.py with level and strongest source); lines 264-286 (ladder values, version 5) |
| P-fac6505c17 | L-5 | no | final-1.md lines 205-259 hold no judgement of severity, probability or cost for an item; lines 45-51 only report checks; no such judgement found in final-1.md |
| P-fac6505c17 | B-1 | yes | files/specs/001-devsecops/spec.md line 260 (C-37, level 1: "An automated test suite runs on each change") |
| P-fac6505c17 | B-2 | yes | files/specs/001-devsecops/spec.md line 260 (C-37, level 1: "a failed run stops the change") |
| P-fac6505c17 | B-3 | no | files/specs/001-devsecops/spec.md line 262 (C-39, the only item on test measures, is level 2, harm of a failure); no level 1 item asks for coverage |
| P-fac6505c17 | B-4 | yes | files/specs/001-devsecops/spec.md line 237 (C-14, level 1: "Static analysis and security tests run automatically on each change") |
| P-fac6505c17 | B-5 | yes | files/specs/001-devsecops/spec.md line 234 (C-11, level 1: known vulnerabilities in the dependencies found by automated scans) |
| P-fac6505c17 | B-6 | no | files/specs/001-devsecops/spec.md lines 222-274: no item asks for robustness tests or fuzzing; "fuzz" appears only as a source unit name in the Source cell of C-14 (line 237); C-15 (line 238) is about pipeline inputs, not tests |
