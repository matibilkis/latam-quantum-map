#!/usr/bin/env python3
"""Schema validation for the LATAM quantum map data files.

Run from the repo root: python3 scripts/validate_data.py
Exits non-zero on any violation. No dependencies beyond the stdlib.
"""
import json
import re
import sys
from pathlib import Path

TYPES = {"research", "startup", "corporate", "government", "training", "infrastructure", "network"}
FOCUS = {"computing", "sensing", "communication", "cryptography", "optimization", "education", "other"}
COUNTRIES = {
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Costa Rica", "Cuba",
    "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Honduras",
    "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Uruguay", "Venezuela",
    "Regional",
}
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
URL = re.compile(r"^https?://\S+$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

errors = []


def err(msg):
    errors.append(msg)


def load(name):
    path = Path("data") / name
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        err(f"{path}: cannot parse JSON — {e}")
        return None


def check_url(value, where, allow_empty=True):
    if value == "" and allow_empty:
        return
    if not isinstance(value, str) or not URL.match(value):
        err(f"{where}: invalid url {value!r}")


def check_latlng(obj, where):
    lat, lng = obj.get("lat"), obj.get("lng")
    if not isinstance(lat, (int, float)) or not -60 <= lat <= 35:
        err(f"{where}: lat {lat!r} out of range [-60, 35]")
    if not isinstance(lng, (int, float)) or not -120 <= lng <= -25:
        err(f"{where}: lng {lng!r} out of range [-120, -25]")


def validate_entities(entities):
    if not isinstance(entities, list):
        err("entities.json: top level must be a list")
        return set()
    ids = set()
    required = {"id", "name", "type", "country", "city", "lat", "lng", "focus", "description", "url"}
    optional = {"inactive"}  # optional flags: e.g. "inactive": true for dormant/proposed efforts
    for i, e in enumerate(entities):
        where = f"entities[{i}] ({e.get('id', '?')})"
        if not isinstance(e, dict):
            err(f"{where}: not an object")
            continue
        missing = required - e.keys()
        if missing:
            err(f"{where}: missing fields {sorted(missing)}")
        extra = e.keys() - required - optional
        if extra:
            err(f"{where}: unknown fields {sorted(extra)}")
        if "inactive" in e and not isinstance(e["inactive"], bool):
            err(f"{where}: inactive must be a boolean")
        eid = e.get("id", "")
        if not isinstance(eid, str) or not SLUG.match(eid):
            err(f"{where}: id must be a lowercase hyphen slug")
        if eid in ids:
            err(f"{where}: duplicate id {eid!r}")
        ids.add(eid)
        if not isinstance(e.get("name"), str) or not e.get("name", "").strip():
            err(f"{where}: empty name")
        if e.get("type") not in TYPES:
            err(f"{where}: type {e.get('type')!r} not in {sorted(TYPES)}")
        if e.get("country") not in COUNTRIES:
            err(f"{where}: country {e.get('country')!r} not in allowed list")
        check_latlng(e, where)
        focus = e.get("focus")
        if not isinstance(focus, list) or not 1 <= len(focus) <= 4 or not set(focus) <= FOCUS:
            err(f"{where}: focus must be 1-4 tags from {sorted(FOCUS)}")
        desc = e.get("description", "")
        if not isinstance(desc, str) or not 30 <= len(desc) <= 600:
            err(f"{where}: description must be 30-600 chars (got {len(desc) if isinstance(desc, str) else type(desc)})")
        check_url(e.get("url", ""), where)
    return ids


def validate_networks(networks, entity_ids):
    if not isinstance(networks, dict):
        err("networks.json: top level must be an object")
        return
    required = {"name", "color", "hub", "members", "blurb", "url"}
    for key, n in networks.items():
        where = f"networks[{key}]"
        if not SLUG.match(key):
            err(f"{where}: key must be a slug")
        missing = required - n.keys()
        if missing:
            err(f"{where}: missing fields {sorted(missing)}")
        if not re.match(r"^#[0-9a-fA-F]{6}$", n.get("color", "")):
            err(f"{where}: color must be a #rrggbb hex")
        members = n.get("members", [])
        if not isinstance(members, list) or len(members) < 2:
            err(f"{where}: members must list at least 2 entity ids")
        for m in members:
            if m not in entity_ids:
                err(f"{where}: member {m!r} is not an entity id")
        if n.get("hub") and n["hub"] not in entity_ids:
            err(f"{where}: hub {n['hub']!r} is not an entity id")
        check_url(n.get("url", ""), where)


def validate_events(events):
    if not isinstance(events, list):
        err("events.json: top level must be a list")
        return
    required = {"name", "kind", "city", "country", "lat", "lng", "start", "end", "url"}
    for i, e in enumerate(events):
        where = f"events[{i}] ({e.get('name', '?')[:30]})"
        missing = required - e.keys()
        if missing:
            err(f"{where}: missing fields {sorted(missing)}")
        for f in ("start", "end"):
            if not DATE.match(str(e.get(f, ""))):
                err(f"{where}: {f} must be YYYY-MM-DD")
        if str(e.get("start", "")) > str(e.get("end", "")):
            err(f"{where}: start after end")
        check_latlng(e, where)
        check_url(e.get("url", ""), where)


def main():
    entities = load("entities.json")
    networks = load("networks.json")
    events = load("events.json")
    if errors:
        report()
    ids = validate_entities(entities)
    validate_networks(networks, ids)
    validate_events(events)
    report()


def report():
    if errors:
        print(f"FAIL — {len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("OK — all data files valid.")
    sys.exit(0)


if __name__ == "__main__":
    main()
