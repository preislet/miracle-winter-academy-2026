"""MkDocs hook: build iCalendar files for each track from docs/programme.md.

The programme page is the single source of truth. Every build parses its day tabs
and tables and publishes calendar/miracle-basic.ics and calendar/miracle-advanced.ics.
"""

import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

from mkdocs.structure.files import File

try:
    from zoneinfo import ZoneInfo

    PRAGUE = ZoneInfo("Europe/Prague")
except Exception:  # no tz database: the course runs in winter (CET, UTC+1)
    PRAGUE = timezone(timedelta(hours=1))

YEAR = 2026
MONTHS = {"Nov": 11, "Dec": 12}
LOCATION = (
    "Simulation Centre (SCIM)\\, pavilion 40\\, Motol University Hospital\\, "
    "V Úvalu 84/1\\, 150 06 Praha 5\\, Czech Republic"
)
TRACKS = {"basic": "Basic", "advanced": "Advanced"}

DAY_RE = re.compile(r'^=== "\w+ (\d+) (\w+)"')
TIME_RE = re.compile(r"^(\d\d:\d\d)–(\d\d:\d\d)$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
TAG_RE = re.compile(r"<[^>]+>")


def _plain(text):
    text = LINK_RE.sub(r"\1", text)
    return TAG_RE.sub("", text).replace("**", "").strip()


def _escape(text):
    return text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def _fold(line):
    """Fold a content line to at most 75 octets without splitting UTF-8 characters."""
    out, chunk = [], ""
    for ch in line:
        limit = 75 if not out else 74
        if len((chunk + ch).encode()) > limit:
            out.append(chunk)
            chunk = ""
        chunk += ch
    out.append(chunk)
    return "\r\n ".join(out)


def _utc(day, hhmm):
    h, m = map(int, hhmm.split(":"))
    local = datetime(day.year, day.month, day.day, h, m, tzinfo=PRAGUE)
    return local.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def parse_programme(path):
    sessions, day = [], None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if m := DAY_RE.match(line):
            day = datetime(YEAR, MONTHS[m.group(2)], int(m.group(1)))
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not day or len(cells) != 4 or not (t := TIME_RE.match(cells[0])):
            continue
        start, end = t.groups()
        session, track_cell, speaker = cells[1:]
        if 'class="break"' in session:
            continue
        title_md, _, detail = session.partition("<br>")
        link = LINK_RE.search(title_md)
        track = next((t for t in ("basic", "advanced") if f"pill {t}" in track_cell), None)
        sessions.append({
            "day": day, "start": start, "end": end,
            "title": _plain(title_md), "detail": _plain(detail),
            "speaker": _plain(speaker), "track": track,
            "page": link.group(2) if link else None,
        })
    return sessions


def build_calendar(sessions, track, site_url):
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//MIRACLE Winter Academy 2026//Programme//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        f"X-WR-CALNAME:MIRACLE Winter Academy 2026 ({TRACKS[track]} track)",
        "X-WR-TIMEZONE:Europe/Prague",
    ]
    for s in sessions:
        if s["track"] not in (None, track):
            continue
        summary = s["title"] + (f" ({TRACKS[track]})" if s["track"] else "")
        description = "\n".join(filter(None, [s["speaker"], s["detail"]]))
        url = ""
        if s["page"] and site_url:
            page, _, anchor = s["page"].partition("#")
            url = site_url.rstrip("/") + "/" + page.removesuffix(".md") + "/" + (f"#{anchor}" if anchor else "")
            description = "\n\n".join(filter(None, [description, url]))
        slug = re.sub(r"[^a-z0-9]+", "-", s["title"].lower()).strip("-")[:40]
        uid = f"{s['day']:%Y%m%d}-{s['start'].replace(':', '')}-{slug}-{track}@miracle-winter-academy-2026"
        lines += [
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTAMP:{stamp}",
            f"DTSTART:{_utc(s['day'], s['start'])}",
            f"DTEND:{_utc(s['day'], s['end'])}",
            f"SUMMARY:{_escape(summary)}",
            f"LOCATION:{LOCATION}",
        ]
        if description:
            lines.append(f"DESCRIPTION:{_escape(description)}")
        if url:
            lines.append(f"URL:{url}")
        lines.append("END:VEVENT")
    lines.append("END:VCALENDAR")
    return "\r\n".join(_fold(line) for line in lines) + "\r\n"


def on_files(files, config):
    sessions = parse_programme(Path(config["docs_dir"]) / "programme.md")
    for track in TRACKS:
        content = build_calendar(sessions, track, config.get("site_url"))
        files.append(File.generated(config, f"calendar/miracle-{track}.ics", content=content))
    return files
