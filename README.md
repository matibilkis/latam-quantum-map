# LATAM Quantum Map

An interactive, open map of the quantum technology ecosystem in Latin America — research groups, startups, corporate programs, government strategies, training initiatives, infrastructure, and networks.

**Live map:** [qutsur.com/LATAM-quantum-map](https://qutsur.com/LATAM-quantum-map/) · **Preview of this repo:** [matiasbilkis.com/latam-quantum-map](https://matiasbilkis.com/latam-quantum-map/) (GitHub Pages)

[![LATAM Quantum Map preview](assets/preview.png)](https://qutsur.com/LATAM-quantum-map/)

Maintained by [QutSur](https://qutsur.com). Currently tracking **86 entities** across 12 countries, plus regional networks and upcoming events.

> **Read it with cariño.** This map is a work in progress and parts of the dataset were compiled with AI assistance. Information may be incomplete or outdated — always double-check claims against the primary sources before citing.

## Structure

The map is a single self-contained page (`index.html`, Leaflet) that loads its data from three JSON files:

| File | Contents |
|------|----------|
| `data/entities.json` | The 86 mapped entities (labs, startups, programs…) |
| `data/networks.json` | Regional networks/consortia linking entities |
| `data/events.json` | Upcoming and recent ecosystem events |

The schema for each file is documented in [`agent_instructions.md`](agent_instructions.md) (also written as a briefing for research agents that enrich the dataset). Source notes live in [`sources.md`](sources.md).

To run locally:

```bash
python3 -m http.server 8000   # from the repo root
# open http://localhost:8000
```

## How to contribute

Additions, corrections and removals are very welcome — the ecosystem moves fast and local knowledge beats any crawler.

**Easiest path — open an issue:** use the [Add an entity](../../issues/new?template=add-entity.yml) or [Fix or remove an entity](../../issues/new?template=fix-entity.yml) form. A verifiable primary source (institutional page, official announcement, paper) is required; entries without sources are not added.

**Direct path — open a pull request** editing only the `data/*.json` files:

1. Follow the field rules in [`agent_instructions.md`](agent_instructions.md) (allowed types, focus tags, coordinate conventions, description style).
2. Include your sources in the PR description.
3. Run `python3 scripts/validate_data.py` before pushing — CI runs the same check.

AI/agent-assisted contributions are explicitly welcome — point your agent at `agent_instructions.md`. They go through exactly the same review pipeline as human ones.

### How contributions are reviewed (governance)

The pipeline is designed so that data flows in easily but nothing lands without human sign-off:

- **Data/code separation** — community PRs may only touch `data/*.json`. CI fails any PR that modifies code, workflows, or anything else; those changes are authored by the maintainer only.
- **Mechanical validation** — `scripts/validate_data.py` enforces the schema (unique slug ids, allowed types/countries/focus tags, coordinate ranges, description and URL sanity) on every PR and push. The check is deterministic stdlib Python: there is no LLM in the enforcement path, so it cannot be prompt-injected.
- **Readable review surface** — CI posts a per-PR summary of added/removed/modified entities, with full text and sources for new entries, so review focuses on factual accuracy.
- **Final authority** — every file is covered by [CODEOWNERS](.github/CODEOWNERS); branch protection on `main` requires the maintainer's review and passing checks before merge. Nothing is auto-merged. [@matibilkis](https://github.com/matibilkis) has the last word on every change.

## Similar initiatives

Related maps and directories we know of (and cross-check against — see [`sources.md`](sources.md) for the full list):

- [**Mapa Cuántico Argentino**](https://gbosyk.github.io/mapa_cuantico_argentina/) ([repo](https://github.com/gbosyk/mapa_cuantico_argentina)) — interactive map of 31 quantum research groups in Argentina, companion to [CONICET's IYQ 2025 survey](https://imit.conicet.gov.ar/launch-of-iyq-2025-and-presentation-of-the-map-of-quantum-in-argentina/). The closest project in spirit; Argentina-only scope.
- [**Quantum Navigator** (Entangled Future)](https://entangledfuture.com/countries/) — global directory of 1,150+ quantum organizations across 52 countries; sparse LATAM coverage.
- [**QURECA — Quantum Initiatives Worldwide**](https://www.qureca.com/quantum-initiatives-worldwide/) — annual map of national quantum programs; Brazil is the only LATAM country with a detailed entry.
- [**Quantiki research groups directory**](https://www.quantiki.org/groups) — self-registered academic QI/QC groups worldwide.
- [**Impact Quantum Global Report**](https://impactquantum.com/GlobalReport/) — country-level data for 108 quantum ecosystems.

This map exists because LATAM is structurally underrepresented in all of the global ones — entity-level, region-wide coverage is the gap we fill.

## License

Code: [MIT](LICENSE). Data (`data/*.json`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reuse freely with attribution to *QutSur — LATAM Quantum Map*.
