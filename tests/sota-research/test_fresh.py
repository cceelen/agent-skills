"""Each rendered recipe skill in the repository is the same as a fresh rendering.

The folder specs/ is only on the branch of a specification. On the main branch this test checks
only the form of each stamp.
"""

from helpers import ROOT, module, run

aspect = module("aspect")
render = module("render")


def accepted_aspect_specifications():
    found = []
    for spec in sorted(ROOT.glob("specs/*/spec.md")):
        data = aspect.load(spec.parent)
        if data["is_aspect"] and data["head"].get("accepted", "pending") != "pending":
            found.append(spec.parent)
    return found


def test_rendered_skills_are_fresh():
    stale = []
    for folder in accepted_aspect_specifications():
        code, out, _ = run("render", folder, "--check", "--out", ROOT)
        if code != 0:
            stale.append(f"{folder.name}: {out.strip()}")
    assert not stale


def test_each_stamp_has_the_right_form():
    wrong = []
    for kind in ("skills", "factory"):
        for skill in sorted((ROOT / kind).glob("*/SKILL.md")):
            text = skill.read_text()
            if "Rendered from the specification" in text and not render.STAMP.search(text):
                wrong.append(str(skill.relative_to(ROOT)))
    assert not wrong
