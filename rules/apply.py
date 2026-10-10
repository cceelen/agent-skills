"""Put the rules of this kit into an instruction file of an agent, or remove them.

  apply.py FILE            show the change to FILE, and change nothing
  apply.py --write FILE    add the rules to FILE, or replace an earlier version of them
  apply.py --remove FILE   remove the rules from FILE
  apply.py --print         print the rules (the plugin does this at the start of a session)

The rules go between two marker lines. The program changes only the text between the markers.
"""

import difflib
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
START = "<!-- agent-skills:evidence-before-action:start -->"
END = "<!-- agent-skills:evidence-before-action:end -->"


def block():
    """The rules with their markers, as they are in an instruction file and in each SKILL.md."""
    return f"{START}\n{(HERE / 'evidence-before-action.md').read_text()}{END}\n"


def removed(text):
    """The text without the block.

    >>> removed("a\\n\\n" + START + "\\nold\\n" + END + "\\n\\nb\\n")
    'a\\n\\nb\\n'
    >>> removed("a\\n")
    'a\\n'
    """
    if START not in text or END not in text:
        return text
    before, rest = text.split(START, 1)
    after = rest.split(END, 1)[1].lstrip("\n")
    before = before.rstrip("\n")
    return "\n\n".join(part for part in (before, after) if part) + ("" if after else "\n" if before else "")


def merged(text, new):
    """The text with the block at its end; an earlier block is replaced.

    >>> merged("", "B\\n")
    'B\\n'
    >>> merged("a\\n", "B\\n")
    'a\\n\\nB\\n'
    >>> merged(merged("a\\n", block()), block()) == merged("a\\n", block())
    True
    """
    rest = removed(text).rstrip("\n")
    return (rest + "\n\n" if rest else "") + new


def main(arguments):
    if arguments == ["--print"]:
        sys.stdout.write(block())
        return 0
    if arguments == ["--selftest"]:
        import doctest

        return doctest.testmod()[0]
    if not arguments or arguments[-1].startswith("--") or len(arguments) > 2:
        print(__doc__)
        return 2
    path = pathlib.Path(arguments[-1]).expanduser()
    old = path.read_text() if path.exists() else ""
    new = removed(old) if arguments[0] == "--remove" else merged(old, block())
    if arguments[0] in ("--write", "--remove"):
        if new != old:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(new)
        print(f"{'changed' if new != old else 'no change'}: {path}")
        return 0
    sys.stdout.writelines(
        difflib.unified_diff(old.splitlines(True), new.splitlines(True), str(path), str(path))
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
