# LATAM Quantum Map

🌐 **English** | [Español](README.es.md) | [Português](README.pt.md)

An open, interactive map of who's doing quantum technology in Latin America — labs, startups, companies, government programs, training, infrastructure and networks.

**→ See the live map: [qutsur.com/LATAM-quantum-map](https://qutsur.com/LATAM-quantum-map/)**

[![LATAM Quantum Map preview](assets/preview.png)](https://qutsur.com/LATAM-quantum-map/)

**86 places across 12 countries.** Maintained by [QutSur](https://qutsur.com). Read it with cariño — it's a work in progress.

---

## ✏️ Add or fix a place — 2 minutes, no coding

Know a quantum lab, startup, or program that's missing or wrong? Tell us. You don't need to touch any code.

### ➕ [Click here to **add a place**](../../issues/new?template=add-entity.yml)

Fill the short form: **name · type · city · one or two sentences on what they do · a link** (their website or an article). Submit.

### 🔧 [Click here to **fix or remove a place**](../../issues/new?template=fix-entity.yml)

Say what's wrong and paste a link. Submit.

**That's it.** A bot reads your form, places it on the map, and opens a proposal automatically — usually within a minute. A maintainer takes a quick look and approves it.

> ⚠️ **A source link is always required.** No link, no entry. (Their official site, an article, or a paper.)

---

<details>
<summary>🛠️ For developers</summary>

The map is plain HTML + [Leaflet](https://leafletjs.com); all the content lives in three JSON files:

| File | Contents |
|------|----------|
| `data/entities.json` | the places |
| `data/networks.json` | regional networks |
| `data/events.json` | events |

Edit **only** `data/*.json`, run `python3 scripts/validate_data.py`, and open a PR (CI rejects anything that touches other files). Schema and field guidance: [`agent_instructions.md`](agent_instructions.md). Sources: [`sources.md`](sources.md).

```bash
python3 -m http.server 8000   # run locally from the repo root
```

AI-assisted contributions are welcome — point your agent at `agent_instructions.md`.

</details>

## License

Code: [MIT](LICENSE) · Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reuse freely with attribution to *QutSur — LATAM Quantum Map*.
