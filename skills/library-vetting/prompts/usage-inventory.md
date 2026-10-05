# Usage inventory

The caller gives you `name` (the library) and `repo` (the consumer repository).

Find every use of `name` in `repo`: manifest or lockfile entry with the pinned version or commit, files that include or import it, the functions and types called, and build flags or defines set for it. Write `usage.md` with counts and `path:line`. No web calls.
