# CLAUDE.md — LATAM Quantum Map

This repo powers an interactive open map of the Latin American quantum ecosystem.
The **source of truth is the data files** in `data/`:

- `data/entities.json` — array of entities (labs, startups, programs, infra, networks…)
- `data/networks.json` — collaboration networks (object keyed by slug)
- `data/events.json` — events (array)

`index.html` renders these with Leaflet. The same data is mirrored into the live
site at qutsur.com/LATAM-quantum-map.

## Rules for any change

- **Data-only.** Community and automated changes may only edit `data/entities.json`,
  `data/networks.json`, `data/events.json`. A CI guard (`.github/workflows/validate.yml`)
  rejects any PR touching code or workflows — those are authored by the maintainer.
- **Schema is enforced.** The exact rules live in `scripts/validate_data.py`. Always run
  `python3 scripts/validate_data.py` before committing; the PR must pass it.
- **Field guidance & coordinates**: see `agent_instructions.md` — allowed types/focus/countries,
  the city coordinate table, the quality bar, and the automatic-reject list.
- **No invention.** Never fabricate facts, URLs, or coordinates. Every claim in a `description`
  must trace to a primary source cited in the issue/PR. If you can't verify it, leave it out.
  Prefer "research directions include…" over stating unverified claims as fact.
- **Dedupe.** Before adding an entity, confirm it isn't already in `data/entities.json` under a
  different id or name.

## Quick schema (entities)

`{ id, name, type, country, city, lat, lng, focus[], description, url }`

- `type` ∈ research · startup · corporate · government · training · infrastructure · network
- `focus` ⊆ computing · sensing · communication · cryptography · optimization · education · other (1–4 tags)
- `country` ∈ the allowed list in `scripts/validate_data.py` (or `Regional`)
- `lat` ∈ [−60, 35], `lng` ∈ [−120, −25]
- `description` 30–600 chars · `url` is `""` or an `https://…` link
- `id` is a unique lowercase hyphen slug
