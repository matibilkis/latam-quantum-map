#!/usr/bin/env python3
"""Deterministic add-entity pipeline — no LLM.

Reads a structured `entity-add` issue (from env vars), builds a validated
entity object, and opens a data-only PR. If the issue can't be turned into a
valid entity, it comments on the issue explaining what's missing and stops.

Because there is no language model and the issue text is only ever treated as
data (never as instructions, never passed through a shell), this is free and
has no prompt-injection surface. Stdlib only.

Env in: ISSUE_NUMBER, ISSUE_TITLE, ISSUE_BODY, GH_TOKEN, GITHUB_REPOSITORY.
"""
import json
import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

# ── Schema (mirror of scripts/validate_data.py) ─────────────────────────────
TYPES = {"research", "startup", "corporate", "government", "training", "infrastructure", "network"}
FOCUS = {"computing", "sensing", "communication", "cryptography", "optimization", "education", "other"}
COUNTRIES = {
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Costa Rica", "Cuba",
    "Dominican Republic", "Ecuador", "El Salvador", "Guatemala", "Honduras",
    "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Uruguay", "Venezuela",
    "Regional",
}
# Common Spanish/Portuguese country names → canonical
COUNTRY_ALIASES = {
    "brasil": "Brazil", "méxico": "Mexico", "mexico": "Mexico", "perú": "Peru",
    "panamá": "Panama", "costa rica": "Costa Rica", "uruguay": "Uruguay",
}
URL_RE = re.compile(r"https?://\S+")

# Coordinate table for known LATAM cities (from agent_instructions.md); Nominatim is the fallback.
CITY_COORDS = {
    "são paulo": (-23.55, -46.63), "sao paulo": (-23.55, -46.63),
    "rio de janeiro": (-22.91, -43.17), "campinas": (-22.82, -47.07),
    "brasília": (-15.77, -47.92), "brasilia": (-15.77, -47.92),
    "salvador": (-12.97, -38.50), "recife": (-8.05, -34.88),
    "belo horizonte": (-19.92, -43.94), "buenos aires": (-34.60, -58.38),
    "bariloche": (-41.15, -71.31), "córdoba": (-31.42, -64.18), "cordoba": (-31.42, -64.18),
    "la plata": (-34.92, -57.95), "gonnet": (-34.88, -57.99),
    "santiago": (-33.45, -70.67), "concepción": (-36.82, -73.04), "concepcion": (-36.82, -73.04),
    "bogotá": (4.71, -74.07), "bogota": (4.71, -74.07), "medellín": (6.25, -75.56), "medellin": (6.25, -75.56),
    "cali": (3.45, -76.52), "mexico city": (19.43, -99.13), "ciudad de méxico": (19.43, -99.13),
    "monterrey": (25.65, -100.29), "guadalajara": (20.66, -103.35),
    "montevideo": (-34.90, -56.19), "lima": (-12.05, -77.04), "heredia": (10.00, -84.12),
    "panama city": (8.99, -79.52), "ciudad de panamá": (8.99, -79.52),
    "la paz": (-16.50, -68.15), "quito": (-0.22, -78.51), "guayaquil": (-2.19, -79.89),
    "havana": (23.13, -82.38), "la habana": (23.13, -82.38), "caracas": (10.48, -66.88),
    "asunción": (-25.29, -57.65), "asuncion": (-25.29, -57.65),
}

REPO = os.environ.get("GITHUB_REPOSITORY", "")
ISSUE = os.environ.get("ISSUE_NUMBER", "")
ROOT = Path(__file__).resolve().parent.parent
ENTITIES = ROOT / "data" / "entities.json"


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-+", "-", s)


def parse_form(body: str) -> dict:
    """GitHub issue-form bodies render as `### Label\\n\\nvalue` blocks."""
    sections, cur, buf = {}, None, []
    for line in (body or "").splitlines():
        if line.startswith("### "):
            if cur is not None:
                sections[cur] = "\n".join(buf).strip()
            cur, buf = line[4:].strip(), []
        else:
            buf.append(line)
    if cur is not None:
        sections[cur] = "\n".join(buf).strip()
    return sections


def clean(v: str) -> str:
    v = (v or "").strip()
    return "" if v.lower() in ("_no response_", "no response", "n/a", "-") else v


def geocode(city: str, country: str):
    key = city.strip().lower()
    if key in CITY_COORDS:
        return CITY_COORDS[key]
    q = urllib.parse.urlencode({"q": f"{city}, {country}", "format": "json", "limit": "1"})
    req = urllib.request.Request(
        f"https://nominatim.openstreetmap.org/search?{q}",
        headers={"User-Agent": "latam-quantum-map-bot/1.0 (hello@qutsur.com)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.load(r)
        if data:
            return round(float(data[0]["lat"]), 3), round(float(data[0]["lon"]), 3)
    except Exception:
        pass
    return None


def gh(*args: str):
    subprocess.run(["gh", *args], check=True)


DRY_RUN = os.environ.get("DRY_RUN") == "1"


def comment(msg: str):
    if DRY_RUN:
        print("[dry-run comment]\n" + msg)
        return
    if ISSUE and REPO:
        subprocess.run(["gh", "issue", "comment", ISSUE, "--repo", REPO, "--body", msg], check=False)


def fail(msg: str):
    """Comment what's missing and exit cleanly (no PR)."""
    comment(f"🤖 No pude armar la entrada automáticamente.\n\n{msg}\n\n"
            "Editá el issue con esa info y se reintenta solo, o un mantenedor puede comentar `@claude` para que lo arme.")
    print("STATUS: needs-info —", msg)
    sys.exit(0)


def main():
    body = os.environ.get("ISSUE_BODY", "")
    f = parse_form(body)

    name = clean(f.get("Name", ""))
    typ = clean(f.get("Type", "")).lower()
    loc = clean(f.get("Country and city", ""))
    desc = clean(f.get("Description", ""))
    sources = f.get("Sources (required)", "") or ""
    focus_block = f.get("Focus (pick 1-4)", "") or ""

    if not name:
        fail("Falta el **nombre**.")
    if typ not in TYPES:
        fail(f"El **tipo** debe ser uno de: {', '.join(sorted(TYPES))}.")

    # country + city
    parts = re.split(r"\s*[,—\-–;|]\s*", loc, maxsplit=1)
    if len(parts) < 2 or not parts[0] or not parts[1]:
        fail("Poné **país y ciudad** separados por coma. Ej: `Argentina, La Plata`.")
    country_raw, city = parts[0].strip(), parts[1].strip()
    country = COUNTRY_ALIASES.get(country_raw.lower(), country_raw)
    if country not in COUNTRIES:
        fail(f"El **país** «{country_raw}» no está en la lista admitida ({', '.join(sorted(COUNTRIES))}).")

    # focus
    focus = [t for t in FOCUS if re.search(rf"- \[x\]\s*{re.escape(t)}\b", focus_block, re.I)]
    if not (1 <= len(focus) <= 4):
        fail("Marcá entre **1 y 4** áreas de foco.")

    # description
    if len(desc) < 30:
        fail("La **descripción** es muy corta (mínimo 30 caracteres). Agregá hechos concretos.")
    if len(desc) > 600:
        desc = desc[:597].rstrip() + "…"

    # url
    m = URL_RE.search(sources)
    if not m:
        fail("Falta una **fuente** con URL (`https://…`). Es obligatoria.")
    url = m.group(0).rstrip(").,;")

    # coords
    coords = geocode(city, country)
    if not coords:
        fail(f"No pude ubicar **{city}, {country}** automáticamente. Agregá lat/lng aproximadas en el issue.")
    lat, lng = coords
    if not (-60 <= lat <= 35 and -120 <= lng <= -25):
        fail(f"Las coordenadas de {city} ({lat}, {lng}) caen fuera de LATAM. Revisá el nombre de la ciudad.")

    slug = slugify(name)
    if not slug:
        fail("No pude generar un id a partir del nombre.")

    entities = json.loads(ENTITIES.read_text(encoding="utf-8"))
    norm = lambda s: re.sub(r"[^a-z0-9]+", "", s.lower())
    for e in entities:
        if e["id"] == slug or norm(e["name"]) == norm(name):
            comment(f"🤖 «{name}» ya parece estar en el mapa (`{e['id']}`). No abrí PR. "
                    "Si querés corregirla, usá el template de *fix*.")
            print("STATUS: duplicate —", e["id"])
            sys.exit(0)

    # avoid offset collisions with an existing same-city pin
    for e in entities:
        if abs(e["lat"] - lat) < 0.01 and abs(e["lng"] - lng) < 0.01:
            lat = round(lat + 0.03, 3)
            break

    entity = {
        "id": slug, "name": name, "type": typ, "country": country, "city": city,
        "lat": lat, "lng": lng, "focus": focus, "description": desc, "url": url,
    }

    # insert before the QutSur sentinel if present, else append
    idx = next((i for i, e in enumerate(entities) if e["id"] == "qutsur"), len(entities))
    entities.insert(idx, entity)
    ENTITIES.write_text(json.dumps(entities, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # validate before opening anything
    r = subprocess.run([sys.executable, "scripts/validate_data.py"], cwd=ROOT)
    if r.returncode != 0:
        fail("La entrada generada no pasó la validación de schema (revisá los campos del issue).")

    if DRY_RUN:
        print("[dry-run] entity built + schema OK:")
        print(json.dumps(entity, ensure_ascii=False, indent=2))
        sys.exit(0)

    branch = f"auto/add-{slug}"
    # idempotent: don't open a second PR if this entity already has one in flight
    exists = subprocess.run(["git", "ls-remote", "--exit-code", "origin", f"refs/heads/{branch}"],
                            cwd=ROOT, capture_output=True)
    if exists.returncode == 0:
        comment(f"🤖 Ya hay un PR en curso para esta entrada (`{branch}`). No abrí otro.")
        print("STATUS: pr-exists —", branch)
        sys.exit(0)

    pr_body = (
        "## Review\n"
        f"- **Change**: add entity `{slug}` _(auto, deterministic — no LLM)_\n"
        f"- **Name · Type · Country · City**: {name} · {typ} · {country} · {city}\n"
        f"- **Focus**: {', '.join(focus)}\n"
        f"- **Coords**: {lat}, {lng} ({'tabla' if city.lower() in CITY_COORDS else 'OpenStreetMap'})\n"
        f"- **Source**: {url}\n"
        f"- **Note**: built verbatim from the issue form; description not rewritten. Schema-validated.\n\n"
        "_Approve = merge · Reject = close._\n\n"
        f"Closes #{ISSUE}\n"
    )
    Path(ROOT / "pr_body.md").write_text(pr_body, encoding="utf-8")

    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=ROOT, check=True)
    subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], cwd=ROOT, check=True)
    subprocess.run(["git", "checkout", "-b", branch], cwd=ROOT, check=True)
    subprocess.run(["git", "add", "data/entities.json"], cwd=ROOT, check=True)
    subprocess.run(["git", "commit", "-m", f"[add] {name} (auto from #{ISSUE})"], cwd=ROOT, check=True)
    subprocess.run(["git", "push", "-u", "origin", branch], cwd=ROOT, check=True)
    gh("pr", "create", "--repo", REPO, "--base", "main", "--head", branch,
       "--title", f"[add] {name}", "--body-file", str(ROOT / "pr_body.md"))
    print("STATUS: ok —", slug)


if __name__ == "__main__":
    main()
