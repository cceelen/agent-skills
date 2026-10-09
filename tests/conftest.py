"""Settings for all tests of the repository."""

import os

# Git gives these variables to a hook, for example to the hook that runs the tests before a
# commit. A test that runs git in a temporary folder must not get them: its commands would then
# write to the index of this repository, not of the temporary one.
for _name in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_PREFIX", "GIT_OBJECT_DIRECTORY"):
    os.environ.pop(_name, None)
