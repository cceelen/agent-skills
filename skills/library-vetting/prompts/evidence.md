# Evidence collection for one library

The caller gives you these values: `dir` (the work folder of the library), `LV` (the folder of
the scripts), `target` (the library), `name` (its short name) and `mode` (`quick` or `deep`).
Where this file shows `<dir>`, `<LV>`, `<target>` or `<name>`, use the value from the caller.
Do the steps in the given sequence. Do not read the work folder of a different library.

1. Run `python3 <LV>/collect.py <target> --out <dir> --max-age 30`. Target is `eco:name[@version]`
   for registry packages (npm, pypi, cargo, go, maven, nuget, gem, composer, hex, pub) or the
   repo URL otherwise. If it reports the registry unreachable, rerun with `--repo <repo URL>`.
   The clone is at `<dir>/src`.
2. Read `facts.json`. For each `fetch_plan` entry, fetch that exact URL once with your web fetch tool and extract the
   listed fields. An empty `fetch_plan` means zero web calls here. For a library without a
   registry, `osv` holds the advisories that apply to the head and to each release tag
   (`affects`, `affects_head`, `affects_latest_release`). An `osv.count` of 0 with a `note` is
   not evidence: answer `D2.no_history` with `yes` only if the fetched pages also show no
   advisory, and never state what a database shows without the fetch. Put Scorecard into
   `answers.json` as `"_scorecard": {"score", "date", "checks": {name: score}}`. List every CVE
   and advisory found, with dates and fixed versions, at the top of `notes.md`. Never retry a
   failed URL through another route.
3. Run `python3 <LV>/score.py <dir> --todo`. Answer every line under `== E ==` from
   `facts.json`, files in `<dir>/src` (Read/Grep, never the web), and the fetched pages.
   Answers are exactly `yes`, `no`, `unknown` or `na`. `yes` and `no` need evidence: a path
   with line, a URL, or a facts.json key. No evidence means `unknown`. Never infer.
4. Web budget beyond the fetch_plan: 3 calls, spent in this order and only if the criterion is
   still unknown: (a) one fetch of the advisory or security page for D2 timelines, (b) one
   search `"<name>" security audit` for D3.audit, (c) one fetch of the governance or funding
   page for D1. Deep mode: 6 more. List every URL used under `"_web"`.
5. Licenses: if `tree.licenses_named_in_root_file` has more than one entry, or
   `tree.nested_license_files` is not empty, read those files and say in `notes.md` which
   directories carry which license. Answer D10.osi and D10.scan from that, not from the
   registry field.
6. SLSA criteria (D12) and base stack (D6.stack_*). The scripts answer these from the registry
   record, the CI files and the base stack screen. Answer only the lines that `--todo` still
   lists, from what a consumer can check, not from intent:
   - `D12.generated`, `D12.provenance`: read the release workflow. `yes` for `D12.provenance`
     only if a hosted build platform signs the provenance; a signing step alone is not
     provenance.
   - `D12.isolated`: `yes` only for a builder that the maintainers cannot influence (a reusable
     generator workflow, or a registry that builds from the source itself).
   - `D12.verifiable`: `yes` only with the path of a document that gives a verify command.
   - `D6.stack_current`, `D6.stack_clean`: `facts.json` `base_stack.rows` has a row with status
     `unknown`. Resolve it from the clone (for a digest without a version comment, find the
     version in the lockfile of the update bot or in the commit that set it). If you cannot,
     answer `unknown`.
   Do not change an answer of the script without evidence that the script could not see. If
   `facts.json` has `pipeline_check` or `plumber`, cite the failed check as a lead and confirm
   it in the workflow file.
7. Registry dependencies are already screened in `facts.json` `dep_screen`; do not redo it.
   Only when there is no `dep_screen` and the tree has vendored directories or submodules:
   list each (first 5, alphabetical) in `notes.md` with its recorded version and the upstream
   URL, and answer the D6 lines from that. No web calls for dependencies.
8. For each line under `== J ==`, do not answer it. Write to `notes.md` up to three lines of
   observations with `path:line` or URL that would let a reviewer answer it. For
   `tree.risky_constructs`, open the hits (first 10 per label) and say for each whether input
   reaches it.
9. Write `answers.json`: `{"<criterion id>": {"a": "...", "ev": "...", "by": "E"}, ...}`, then
   run `python3 <LV>/score.py <dir> --todo` again and fix anything it rejects or still lists
   under `== E ==`. Reply with only: the two file paths, counts of yes/no/unknown, and web
   calls used.
