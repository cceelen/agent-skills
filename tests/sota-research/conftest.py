"""The tooling of the factory needs the latest stable Python. Older versions skip this folder."""

import sys

if sys.version_info < (3, 14):
    collect_ignore_glob = ["test_*.py"]
