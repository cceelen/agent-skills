#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Vetting of the independent sources of an aspect specification. Standard library only.

  vet.py collect SPEC --work DIR --today DATE [SOURCE-ID ...]
  vet.py score   SPEC --work DIR [--write] [--max-age DAYS] [--rubric FILE]

  collect  measures the signals of each independent source of section 2 (or of the named ones)
           and writes DIR/<source-id>.json. It uses the network. A signal that it cannot
           measure is recorded as not measured, with the error, and the run continues. For a
           repository it runs the collector of the skill library-vetting. --today is the date
           for the age (YYYY-MM-DD); the program does not read the clock.
  score    reads the signal files and the answers in the table "Sources" of vetting.md, applies
           the gates and computes the score. It uses no network. --write fills the cells Kind,
           Gates, Signals, Score and Date. It never fills the cell "Confirmed by": only the
           owner confirms a source.

DIR is a work folder outside the repository. Do not commit it. The rubric is rubric-sources.txt
beside this program. Result code 0: each source is scored and confirmed. Result code 1: a source
is not scored, is rejected or is not confirmed. Result code 2: the input cannot be read.
"""

import datetime
import html.parser
import http.client
import ipaddress
import json
import pathlib
import re
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import aspect
import check

COLLECTOR = 1  # increase when the signals change
MAX_BYTES = 2_000_000
TIMEOUT = 20  # seconds for one network operation
DEADLINE = 60  # seconds for one page
SOURCE = re.compile(r"S-\d+")
FIRST_YEAR = 1990
FORGES = ("github.com", "gitlab.com", "codeberg.org", "bitbucket.org", "sr.ht")
DATE = re.compile(r"(?<!\d)(\d{4})-(\d{2})-(\d{2})(?!\d)")
LOOSE_DATE = re.compile(r"(?<![\w.-])(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?(?![\w.-])")
AUTHOR_META = (
    "author",
    "article:author",
    "dc.creator",
    "dcterms.creator",
    "citation_author",
    "parsely-author",
)
DATE_META = (
    "article:published_time",
    "article:modified_time",
    "date",
    "dc.date",
    "dcterms.date",
    "dcterms.modified",
    "citation_publication_date",
    "datepublished",
    "datemodified",
    "last-modified",
)
WEIGHT = re.compile(r"^weight (\S+):\s*(.+)$")
SETTING = re.compile(r"^(version|gate \S+|pass score):\s*(\d+)\s*$")
RECORD = re.compile(r"(?:^|;)\s*record:\s*(yes|no)\b", re.I)
REFERENCES = re.compile(r"(?:^|;)\s*fast-lane references:\s*(\d+)", re.I)
COLLECTOR_PROGRAM = pathlib.Path(__file__).resolve().parents[3] / "skills/library-vetting/scripts/collect.py"

MESSAGES = {
    "collected": "{0}: the signals are in {1}.",
    "not-measured": "{0}: the signal '{1}' was not measured: {2}",
    "no-url": "{0}: the source has no address with http or https.",
    "bad-id": "The identifier '{0}' is not of the form S-<number>. The source was not vetted.",
    "unknown-id": "Section 2 has no independent source with the identifier '{0}'.",
    "bad-max-age": "Give the age limit as a whole number of days.",
    "scored": "{0}: {1}, gates pass, score {2} of 10. Confirmed by: {3}.",
    "low-score": "{0}: {1}, rejected: the score {2} is below {3}.",
    "gate": "{0}: {1}, rejected by a gate: {2}.",
    "no-signals": "{0}: not scored. Run the collection for this source first.",
    "no-row": "{0}: not scored. Add a row for this source to the table Sources of vetting.md.",
    "no-answer": "{0}: not scored. The answer '{1}' is missing in the cell Answers.",
    "incomplete": "{0}: not scored. The signal '{1}' was not measured. Run the collection again.",
    "summary": "Rubric version {0}. Confirmed: {1}. Wait for the owner: {2}. Rejected: {3}. Not scored: {4}.",
    "written": "The program wrote the results to vetting.md.",
    "not-written": "The program cannot write the cell '{0}' in line {1} of vetting.md. Correct the table.",
    "bad-date": "Give the date of today as --today YYYY-MM-DD.",
    "no-work": "Give the work folder with --work DIR.",
    "rubric": "The rubric cannot be read: {0}",
    "unreadable": "The input cannot be read: {0}",
}


# ---- collect ----


class PageFacts(html.parser.HTMLParser):
    """The author, the dates and the links of one HTML page."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.author, self.dates, self.links = None, [], []

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "meta":
            name = (a.get("name") or a.get("property") or a.get("itemprop") or "").lower()
            content = a.get("content", "").strip()
            if name in AUTHOR_META and content and not self.author:
                self.author = content
            if name in DATE_META and DATE.search(content):
                self.dates.append(DATE.search(content).group(0))
        elif tag == "time" and DATE.search(a.get("datetime", "")):
            self.dates.append(DATE.search(a["datetime"]).group(0))
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])


def valid_date(text, today=None):
    """The date as YYYY-MM-DD, or None for a date that does not exist or is after today."""
    try:
        date = datetime.date.fromisoformat(str(text)[:10])
        if date.year < FIRST_YEAR or (today and date > datetime.date.fromisoformat(today)):
            return None
    except ValueError:
        return None
    return date.isoformat()


def page_signals(text, url, header_date=None, today=None):
    """The signals that the text of one page gives. A page cannot give a date after today."""
    facts = PageFacts()
    facts.feed(text)
    own = urllib.parse.urlsplit(url).hostname or ""
    hosts = set()
    for link in facts.links:
        try:
            hosts.add(urllib.parse.urlsplit(link).hostname)
        except ValueError:
            continue
    others = sorted(h for h in hosts if h and h != own and not h.endswith("." + own))
    dates = sorted(d for d in (valid_date(x, today) for x in [*facts.dates, header_date]) if d)
    return {"author": facts.author, "date": dates[-1] if dates else None, "links_out": len(others)}


def public_host(url):
    """True if the address uses http or https and its host is not a local or private address."""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        return False
    try:
        found = socket.getaddrinfo(parts.hostname, None)
    except OSError:
        return False
    addresses = {ipaddress.ip_address(info[4][0].split("%")[0]) for info in found}
    return bool(addresses) and all(a.is_global for a in addresses)


class OnlyHttp(urllib.request.HTTPRedirectHandler):
    """A redirect must stay on http or https and on a public host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not public_host(newurl):
            return None
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(url):
    """(text, date of the header Last-Modified). No cookies, no credentials, a size and a time limit."""
    if not public_host(url):
        raise OSError("the address is not a public http or https address")
    opener = urllib.request.build_opener(OnlyHttp)
    request = urllib.request.Request(url, headers={"User-Agent": "sota-research-vetting/1"})
    end = time.monotonic() + DEADLINE
    chunks, size = [], 0
    with opener.open(request, timeout=TIMEOUT) as response:
        while size < MAX_BYTES:
            if time.monotonic() > end:
                raise OSError("the page took too long")
            chunk = response.read(min(65536, MAX_BYTES - size))
            if not chunk:
                break
            chunks.append(chunk)
            size += len(chunk)
        modified = response.headers.get("Last-Modified")
    header_date = None
    if modified:
        try:
            header_date = datetime.datetime.strptime(modified[5:16], "%d %b %Y").date().isoformat()
        except ValueError:
            header_date = None
    return b"".join(chunks).decode("utf-8", errors="replace"), header_date


def age_days(date, today):
    """The age in days, or None for a date that does not exist or is after today."""
    date = valid_date(date, today) if date else None
    if not date:
        return None
    return (datetime.date.fromisoformat(today) - datetime.date.fromisoformat(date)).days


def collect_page(url, today):
    signals = {"reachable": None, "date": None, "age_days": None, "author": None, "links_out": None}
    errors = {}
    try:
        text, header_date = fetch(url)
    except urllib.error.HTTPError as e:
        if e.code in (404, 410):
            signals["reachable"] = False
        else:
            errors["reachable"] = f"HTTP {e.code}"
        return signals, errors
    except (OSError, ValueError, http.client.HTTPException) as e:
        errors["reachable"] = str(e) or type(e).__name__
        return signals, errors
    signals["reachable"] = True
    signals.update(page_signals(text, url, header_date, today))
    signals["age_days"] = age_days(signals["date"], today)
    return signals, errors


def collect_repository(url, today, work, ident):
    signals = {"reachable": None, "date": None, "age_days": None, "commits_12m": None, "authors_24m": None}
    errors = {}
    out = work / f"{ident}-facts"
    if not COLLECTOR_PROGRAM.is_file():
        errors["reachable"] = "the collector of library-vetting is absent"
        return signals, errors
    try:
        (out / "facts.json").unlink(missing_ok=True)  # facts of an earlier run must not be used
        done = subprocess.run(
            [sys.executable, str(COLLECTOR_PROGRAM), url, "--out", str(out)],
            capture_output=True,
            timeout=900,
            check=False,
        )
        if done.returncode != 0:
            raise OSError(f"the collector ended with the result code {done.returncode}")
        facts = json.loads((out / "facts.json").read_text(encoding="utf-8"))
        if not isinstance(facts, dict):
            raise ValueError("the collector gave no facts")
    except (OSError, ValueError, subprocess.TimeoutExpired) as e:
        errors["reachable"] = str(e)
        return signals, errors
    history = facts.get("history") or {}
    if not history:
        errors["reachable"] = str((facts.get("errors") or {}).get("clone", "the collector gave no history"))
        return signals, errors
    last = DATE.search(str(history.get("last_commit", "")))
    signals.update(
        reachable=True,
        date=valid_date(last.group(0), today) if last else None,
        commits_12m=history.get("commits_12m"),
        authors_24m=history.get("authors_24m"),
    )
    signals["age_days"] = age_days(signals["date"], today)
    return signals, errors


def kind_of(row, url):
    kind = (row or {}).get("kind", "").strip().lower()
    if kind in ("page", "repository"):
        return kind
    parts = urllib.parse.urlsplit(url)
    path = [p for p in parts.path.split("/") if p]
    return "repository" if (parts.hostname or "") in FORGES and len(path) == 2 else "page"


def independent_sources(data, only=()):
    """The independent sources with an identifier of the right form, and the wrong identifiers."""
    rows = [s for s in data["sources"] if s.get("class") == "independent"]
    bad = sorted(s.get("id", "") for s in rows if not SOURCE.fullmatch(s.get("id", "")))
    good = [s for s in rows if SOURCE.fullmatch(s.get("id", "")) and (not only or s["id"] in only)]
    return good, bad


def cmd_collect(data, args):
    work, today = check.option(args, "--work"), check.option(args, "--today")
    if not work:
        print(MESSAGES["no-work"], file=sys.stderr)
        return 2
    if not today or not DATE.fullmatch(today) or not valid_date(today):
        print(MESSAGES["bad-date"], file=sys.stderr)
        return 2
    work = pathlib.Path(work)
    work.mkdir(parents=True, exist_ok=True)
    only = [a for a in args[1:] if not a.startswith("--")]
    rows = {r.get("source"): r for r in data["vetting_sources"]}
    sources, bad = independent_sources(data, only)
    unknown = sorted(set(only) - {s["id"] for s in sources})
    for ident in bad:
        print(MESSAGES["bad-id"].format(ident))
    for ident in unknown:
        print(MESSAGES["unknown-id"].format(ident))
    for source in sources:
        ident, url = source["id"], source.get("url", "")
        kind = kind_of(rows.get(ident), url)
        if urllib.parse.urlsplit(url).scheme not in ("http", "https"):
            signals, errors = {"reachable": None}, {"reachable": "no address with http or https"}
            print(MESSAGES["no-url"].format(ident))
        elif kind == "repository":
            signals, errors = collect_repository(url, today, work, ident)
        else:
            signals, errors = collect_page(url, today)
        record = {
            "collector": COLLECTOR,
            "errors": errors,
            "kind": kind,
            "signals": signals,
            "source": ident,
            "today": today,
            "url": url,
        }
        path = work / f"{ident}.json"
        path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        for name, error in sorted(errors.items()):
            print(MESSAGES["not-measured"].format(ident, name, error))
        print(MESSAGES["collected"].format(ident, path))
    return 1 if bad or unknown else 0


# ---- score ----


def read_rubric(path):
    rubric = {"weights": {}}
    for line in aspect.read_text(path).splitlines():
        if m := SETTING.match(line):
            rubric[m.group(1)] = int(m.group(2))
        elif m := WEIGHT.match(line):
            rubric["weights"][m.group(1)] = [tuple(step.rsplit(":", 1)) for step in m.group(2).split()]
    needed = ("version", "gate max-age-days", "pass score")
    names = ("age-days", "record", "links-out", "commits-12m", "fast-lane-references")
    absent = [k for k in needed if k not in rubric] + [n for n in names if n not in rubric["weights"]]
    if absent:
        raise ValueError("missing: " + ", ".join(absent))
    return rubric


def points(steps, value):
    """The points of the first step that the value meets."""
    for condition, pts in steps:
        if condition == "else" or condition == str(value):
            return int(pts)
        if condition.startswith("<=") and isinstance(value, int) and value <= int(condition[2:]):
            return int(pts)
        if condition.startswith(">=") and isinstance(value, int) and value >= int(condition[2:]):
            return int(pts)
    return 0


def recorded_date(source, today=None):
    """A date in the cell "Version or date" of section 2, as YYYY-MM-DD."""
    for m in LOOSE_DATE.finditer(source.get("version or date", "")):
        date = valid_date(f"{m.group(1)}-{m.group(2) or '01'}-{m.group(3) or '01'}", today)
        if date:
            return date
    return None


def usable_signals(signal_file, source):
    """True for a signal file of the right form that belongs to the address of the source."""
    if not isinstance(signal_file, dict) or not isinstance(signal_file.get("signals"), dict):
        return False
    return (
        signal_file.get("kind") in ("page", "repository")
        and bool(valid_date(signal_file.get("today")))
        and signal_file.get("url") == source.get("url", "")
    )


def score_source(source, row, signal_file, rubric, max_age):
    """The result for one source: state confirmed, wait, rejected or not scored."""
    ident = source["id"]
    if row is None:
        return {"id": ident, "state": "not scored", "text": MESSAGES["no-row"].format(ident)}
    if not usable_signals(signal_file, source):
        return {"id": ident, "state": "not scored", "text": MESSAGES["no-signals"].format(ident)}
    kind, signals, today = signal_file["kind"], signal_file["signals"], signal_file["today"]
    result = {"id": ident, "kind": kind, "date": today}
    if signals.get("reachable") is None:
        return result | {"state": "not scored", "text": MESSAGES["incomplete"].format(ident, "reachable")}
    answers = row.get("answers", "")
    record, references = RECORD.search(answers), REFERENCES.search(answers)
    for name, found in (("record", record), ("fast-lane references", references)):
        if not found:
            return result | {"state": "not scored", "text": MESSAGES["no-answer"].format(ident, name)}
    # A date after the day of the collection is not a date: a page cannot make itself new.
    date = valid_date(signals.get("date"), today) or recorded_date(source, today)
    age = age_days(date, today)
    has_author = bool(signals.get("author")) or source.get("issuer", "").strip().lower() not in (
        "",
        "unknown",
    )
    activity = "commits_12m" if kind == "repository" else "links_out"
    shown = [
        f"reachable {'yes' if signals['reachable'] else 'no'}",
        f"date {date or 'none'}",
        f"age {age} d" if age is not None else "age not known",
        f"author {'yes' if has_author else 'no'}",
        f"{activity.replace('_', ' ')} {signals.get(activity) if signals.get(activity) is not None else 0}",
    ]
    result["signals"] = "; ".join(shown)
    gate = None
    if not signals["reachable"]:
        gate = "not reachable"
    elif not has_author:
        gate = "no author or issuer"
    elif not date:
        gate = "no date"
    elif age > max_age:
        gate = f"older than {max_age} days"
    if gate:
        text = MESSAGES["gate"].format(ident, kind, gate)
        return result | {"state": "rejected", "gates": f"rejected: {gate}", "score": "", "text": text}
    weights = rubric["weights"]
    total = (
        points(weights["age-days"], age)
        + points(weights["record"], record.group(1).lower())
        + points(weights["commits-12m" if kind == "repository" else "links-out"], signals.get(activity) or 0)
        + points(weights["fast-lane-references"], int(references.group(1)))
    )
    result |= {"gates": "pass", "score": f"{total} of 10"}
    if total < rubric["pass score"]:
        text = MESSAGES["low-score"].format(ident, kind, total, rubric["pass score"])
        return result | {"state": "rejected", "gates": "rejected: score", "text": text}
    confirmed = row.get("confirmed by", "").strip()
    state = "confirmed" if confirmed.lower() not in check.NOT_CONFIRMED else "wait"
    if confirmed.lower() == "rejected":
        state = "rejected"
    text = MESSAGES["scored"].format(ident, kind, total, confirmed or "pending")
    return result | {"state": state, "text": text}


def write(data, results):
    """Fill the cells of the table Sources. Returns a message for each cell that is absent."""
    path = pathlib.Path(data["folder"]) / "vetting.md"
    rows = {r.get("source"): r for r in data["vetting_sources"]}
    failed = []
    for result in results:
        row = rows.get(result["id"])
        if row is None or "kind" not in result:
            continue
        cells = {
            "kind": result["kind"],
            "gates": result.get("gates", ""),
            "signals": result.get("signals", ""),
            "score": result.get("score", ""),
            "date": result["date"],
        }
        for name, text in cells.items():
            if not aspect.set_cell(path, row["_line"], aspect.column_of(row, name), text):
                failed.append(MESSAGES["not-written"].format(name, row["_line"]))
    return failed


def cmd_score(data, args):
    work = check.option(args, "--work")
    max_age = check.option(args, "--max-age")
    rubric_file = check.option(args, "--rubric") or pathlib.Path(__file__).with_name("rubric-sources.txt")
    if not work:
        print(MESSAGES["no-work"], file=sys.stderr)
        return 2
    try:
        rubric = read_rubric(rubric_file)
    except (aspect.Unreadable, OSError, ValueError) as e:
        print(MESSAGES["rubric"].format(e), file=sys.stderr)
        return 2
    if max_age is not None and not max_age.isdecimal():
        print(MESSAGES["bad-max-age"], file=sys.stderr)
        return 2
    limit = int(max_age) if max_age else rubric["gate max-age-days"]
    rows = {r.get("source"): r for r in data["vetting_sources"]}
    results = []
    sources, bad = independent_sources(data)
    for ident in bad:
        print(MESSAGES["bad-id"].format(ident))
    for source in sources:
        path = pathlib.Path(work) / f"{source['id']}.json"
        try:
            signal_file = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None
        except OSError, ValueError:
            signal_file = None
        results.append(score_source(source, rows.get(source["id"]), signal_file, rubric, limit))
    results.sort(key=lambda r: r["id"])
    print("\n".join(r["text"] for r in results))
    count = {
        s: sum(1 for r in results if r["state"] == s) for s in ("confirmed", "wait", "rejected", "not scored")
    }
    print(MESSAGES["summary"].format(rubric["version"], *count.values()))
    if "--write" in args:
        failed = write(data, results)
        path = pathlib.Path(data["folder"]) / "vetting.md"
        text = aspect.read_text(path)
        text = re.sub(r"(Rubric for sources: version )\d+", rf"\g<1>{rubric['version']}", text)
        aspect.write_text(path, text)
        print("\n".join([*failed, MESSAGES["written"]]))
        if failed:
            return 1
    return 0 if count["confirmed"] == len(results) and not bad else 1


def main():
    args = sys.argv[1:]
    if len(args) < 2 or args[0] not in ("collect", "score"):
        sys.exit(__doc__)
    try:
        data = aspect.load(args[1])
    except (aspect.Unreadable, OSError) as e:
        print(MESSAGES["unreadable"].format(e), file=sys.stderr)
        sys.exit(2)
    rest = args[2:]
    sys.exit(cmd_collect(data, ["collect", *rest]) if args[0] == "collect" else cmd_score(data, rest))


if __name__ == "__main__":
    main()
