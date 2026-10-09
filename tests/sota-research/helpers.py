"""Shared paths and loaders for the tests of the research tooling."""

import importlib.util
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "factory" / "sota-research" / "scripts"
FIXTURE = pathlib.Path(__file__).resolve().parent / "fixture"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def module(name):
    """Load one program of the tooling as a module."""
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(program, *args):
    """Run one program. Returns (result code, standard output, standard error)."""
    done = subprocess.run(
        [sys.executable, str(SCRIPTS / f"{program}.py"), *map(str, args)],
        capture_output=True,
        text=True,
        check=False,
    )
    return done.returncode, done.stdout, done.stderr
