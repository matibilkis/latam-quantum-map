# LATAM Quantum Map

🌐 **English** | [Español](README.es.md) | [Português](README.pt.md)

Interactive map of the quantum technology ecosystem in Latin America — labs, startups, corporate programs, governments, training, infrastructure, and networks.

**→ Live map:** [qutsur.com/LATAM-quantum-map](https://qutsur.com/LATAM-quantum-map/)

[![LATAM Quantum Map preview](assets/preview.png)](https://qutsur.com/LATAM-quantum-map/)

**86 entities** across 12 countries — plus regional networks and events. Maintained by [QutSur](https://qutsur.com).

> **Read it with cariño.** Work in progress, parts compiled with AI assistance. Verify before citing.

---

## Data files

| File | Contents |
|------|----------|
| `data/entities.json` | 86 mapped entities (labs, startups, programs…) |
| `data/networks.json` | Regional networks and consortia |
| `data/events.json` | Upcoming and past ecosystem events |

Schema documented in [`agent_instructions.md`](agent_instructions.md). Sources in [`sources.md`](sources.md).

```bash
python3 -m http.server 8000   # run locally from repo root
```

## Contribute

Additions and corrections are very welcome — the ecosystem moves fast and local knowledge beats any crawler.

**Open an issue** (easiest): [Add an entity](../../issues/new?template=add-entity.yml) or [Fix / remove](../../issues/new?template=fix-entity.yml). A verifiable primary source is required.

**Open a pull request**: edit only `data/*.json`, follow [`agent_instructions.md`](agent_instructions.md), include sources in the PR description, run `python3 scripts/validate_data.py` before pushing.

AI-assisted contributions are explicitly welcome — point your agent at `agent_instructions.md`. Same review pipeline as human contributions.

### Governance

- **Data/code separation** — PRs may only touch `data/*.json`; CI fails anything else.
- **Mechanical validation** — `scripts/validate_data.py` enforces schema on every PR. No LLM in the enforcement path.
- **Readable review** — CI posts a per-PR diff summary with full text and sources for new entries.
- **Final authority** — branch protection on `main` requires maintainer review; nothing auto-merges. [@matibilkis](https://github.com/matibilkis) has the last word.

## Related maps

| Project | Scope |
|---------|-------|
| [Mapa Cuántico Argentino](https://gbosyk.github.io/mapa_cuantico_argentina/) | 31 quantum research groups in Argentina |
| [Quantum Navigator](https://entangledfuture.com/countries/) | 1,150+ orgs globally, sparse LATAM coverage |
| [QURECA Quantum Initiatives](https://www.qureca.com/quantum-initiatives-worldwide/) | National programs; Brazil is the only LATAM entry |
| [Quantiki groups](https://www.quantiki.org/groups) | Self-registered academic QI/QC groups worldwide |
| [Impact Quantum Global Report](https://impactquantum.com/GlobalReport/) | Country-level data for 108 ecosystems |

This map fills the gap: entity-level, region-wide coverage of LATAM. See [`sources.md`](sources.md) for the full cross-reference list.

## License

Code: [MIT](LICENSE) · Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reuse freely with attribution to *QutSur — LATAM Quantum Map*.
