# Aspect specification: Backups of project data

**Branch**: `900-backups` | **Research date**: 2026-01-10 | **Supersedes**: none | **Accepted**: A. Person, 2026-01-15

A small specification for the tests of the tooling. Its sources are invented.

## 1. Aspect

- **Aspect**: backups of the data of a software project.
- **Field and disciplines**: operations; it cuts across development and support.
- **Contexts**: the size of the data; who operates the software; the place where the data
  is.
- **Risk dimensions**: the dimensions on which the risk of a project differs for this aspect.
  - `operative`: Can a lost record be made again? Opinion: if not, go past level 1.
  - `regulatory`: Is personal data in the backup? Opinion: if yes, aim for level 3.
- **Boundaries**: the recovery of a complete site belongs to a different aspect.
- **Agreed with the owner on**: 2026-01-05; a recipe for small teams.

## 2. Sources

| Id | Source | Issuer | Version or date | Class | License | Read | URL |
|---|---|---|---|---|---|---|---|
| S-01 | Guide to backups | Example Standards Body | 2.0, 2025-03 | standard | public | full | https://standards.example/backups |
| S-02 | A study of restore failures | Example Journal | 2024 | research | CC BY 4.0 | full | https://journal.example/restore |
| S-03 | Notes on restore drills | A. Writer | 2025-06-01 | independent | all rights reserved | full | https://writer.example/drills |
| S-04 | backup-examples | example-org | commit of 2025-11-02 | independent | MIT | part | https://forge.example/example-org/backup-examples |

## 3. Strategy

### 3.1 Goals

A lost record can be made again in the time that the project agreed on.

### 3.2 Order of the work

1. Find out which data cannot be made again.
2. Make the first backup, then do one restore.

### 3.3 Decisions that depend on context

| Decision | Depends on | Options | Sources |
|---|---|---|---|
| How frequently to make a backup | how much work a lost day is | each day, or after each change | S-01 section 3 |

### 3.4 Where the sources disagree

| Question | Positions | How this recipe handles it | Sources |
|---|---|---|---|
| Whether one copy is sufficient | One source accepts one copy with a restore test. One source wants a second place. | One copy is level 1; the second place is above it. | S-01, S-02 |

## 4. Checklist

| Id | Item | Why | Level | Admitted by | Check | Source |
|---|---|---|---|---|---|---|
| C-01 | A backup of the data that cannot be made again exists. | Risk: a lost record stays lost. | 1 | authority (2) | the newest backup is younger than the agreed interval | S-01 section 2; S-02 abstract |
| C-02 | A restore from the backup was done and recorded. | Risk: a backup that cannot be restored is found too late. | 2, operative | authority (1) | the record of the last restore has a date | S-02 section 4 |
| C-03 | A copy of the backup is kept in a second place with a different access. | Risk: one event destroys the data and its backup. | 3, regulatory | authority (1) | the list of copies names two places | S-01 section 5 |
| C-04 | Each restore drill ends with a written review. | Risk: the same restore error occurs again. | not admitted | practice | judgement | S-03 "After the drill" |
| C-05 | The backup is made by a program, not by hand. | Risk: a person forgets the backup. | 1 | practice | the schedule of the program is in the repository | S-04 README; S-01 section 3 |

**Selection.** The kit recommends; the user decides.

## 5. Skill set to define

### Recipe skill and agent: backups

- **Goal**: Each record that cannot be made again has a backup that was restored one time.
- **Reads first**: the size of the data, who operates the software, and where the data is;
  the selection of the project.
- **Applies**: the order of the work below; it judges C-04.
- **Delegates**: The making and the restore of a backup go to an implementation skill.
- **Stops when**: the goal is reached, or a decision that depends on context needs a person.

### Implementation skills (layer two)

| Product or tool | Capability | Checklist items it implements | Helper software it needs |
|---|---|---|---|
| A backup tool | make and restore a backup | C-01, C-02, C-05 | none |

## 6. Watch list

| Signal | Where to read it | Cadence |
|---|---|---|
| A new version of S-01 | the page of the issuer | at each refresh |

## 7. Decisions and changes

| Date | Decision or change | Reason | Revisit when |
|---|---|---|---|
| 2026-01-05 | The recipe is for small teams. | Owner. | a large team uses it |
| 2026-01-10 | Models used: a small model read the sources; the session model wrote this file. Accepted by: A. Person. | C-11. | |

## 8. Glossary

| Term | Meaning here | Other meanings in the sources |
|---|---|---|
| backup | a copy that is kept to make lost data again | S-02 uses it for a second server also |
