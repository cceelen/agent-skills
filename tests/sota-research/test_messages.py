"""The text for the person in the loop is in Simplified Technical English: short sentences."""

import ast
import re

from helpers import SCRIPTS

TOOLING = SCRIPTS.parent
PROGRAMS = sorted(p for p in SCRIPTS.glob("*.py"))


def messages(path):
    """The values of the table MESSAGES of one program."""
    for node in ast.parse(path.read_text()).body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "MESSAGES" for t in node.targets):
            return list(ast.literal_eval(node.value).values())
    return []


def test_each_sentence_of_a_message_has_25_words_or_less():
    long = []
    for program in PROGRAMS:
        for text in messages(program):
            for sentence in re.split(r"(?<=[.:;])\s+", text):
                if len(sentence.split()) > 25:
                    long.append(f"{program.name}: {sentence}")
    assert not long


def test_no_model_name_in_the_text_for_agents():
    table = SCRIPTS / "models.py"
    if not table.is_file():
        return
    names = set(re.findall(r'"((?:claude|gpt|gemini|o\d)[a-z0-9.\-]*)"', table.read_text()))
    texts = [TOOLING / "SKILL.md", *TOOLING.glob("prompts/*.md"), *TOOLING.glob("agent-templates/*.md")]
    found = [f"{t.name}: {n}" for t in texts for n in sorted(names) if n in t.read_text()]
    assert not found
