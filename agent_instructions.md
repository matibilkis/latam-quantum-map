# Agent Instructions: LATAM Quantum Map — Database Enrichment

## Role

You are a research agent tasked with expanding and enriching the LATAM quantum ecosystem database used in the interactive map at `webpage/LATAM-quantum-map/index.html`. Your job is to:

1. **Find new entities** not currently in the database
2. **Enrich existing entries** with missing URLs, updated descriptions, corrected coordinates
3. **Flag stale entries** where activity has stopped or information may be outdated

You have web search and web fetch tools available. Use them aggressively.

---

## The Database

Entities live in the `ENTITIES` array inside `index.html`. Each entry is a JS object:

```javascript
{ id:'slug-lowercase', name:'Display Name', type:'<TYPE>', country:'<COUNTRY>',
  city:'City Name', lat:<decimal>, lng:<decimal>, focus:['<FOCUS>',...],
  description:'2–4 sentences. Concrete facts only. No fluff.', url:'https://...' }
```

**Field rules:**
- `id`: lowercase slug, hyphens only, unique across all entries
- `type`: must be one of the 7 types below
- `country`: exact string from the country list (or `'Regional'` for pan-LATAM)
- `lat`/`lng`: decimal degrees. Verify against actual city location. For same-city entities offset by ±0.02–0.05 degrees to avoid marker overlap.
- `focus`: array of 1–4 focus tags from the allowed list below
- `description`: 2–4 sentences. Cite concrete facts (funding amounts, partner names, years, publications). No marketing language.
- `url`: official homepage, lab page, or institutional page. Empty string `''` if none found.

### Allowed types

| type | What it covers |
|------|---------------|
| `research` | University labs, research groups, national labs, institutes |
| `startup` | Companies born from quantum (spinoffs, founded to commercialize quantum) |
| `corporate` | Large incumbent companies with quantum programs or pilots |
| `government` | National strategies, funding programs, government mandates, policy |
| `training` | Courses, bootcamps, communities, education pipelines, diplomas |
| `infrastructure` | Physical hardware (QPUs, simulators, QKD networks, cryo labs), cloud access nodes |
| `network` | Conferences, alliances, consortia, ecosystem organizations, multilateral programs |

### Allowed focus tags

`computing`, `sensing`, `communication`, `cryptography`, `optimization`, `education`, `other`

---

## Current Coverage Summary

Use this to understand what's already in the database and what's thin:

| Country | Count | Strong areas | Gaps |
|---------|-------|-------------|------|
| Brazil | 19 | Research centers, hardware, startups, corporate | UNESP, QWorld Brazil, IBM Quantum Network BR chapter, defense (ITA), more industry adoption |
| Argentina | 9 | Buenos Aires groups, QUBIT.AR, /q99 | UNC/Córdoba separately, ASQC event, QPL conference |
| Chile | 6 | SeQure, Quantü, MIRO, strategy | Classiq+UCChile pilot, USM quantum group, Lihuen's parent lab (U. de Chile) |
| Colombia | 4 | MinCiencias, UNAL, Los Andes | U. del Valle hardware project, Orchids Program, EAFIT |
| Mexico | 7 | UNAM, CINVESTAV, Tec MTY | SpinQ LATAM regional office, QWorld Mexico, BUAP quantum optics, IBM Quantum Network MX |
| Uruguay | 2 | Quantum-South | Universidad de Montevideo (origin of QS), PEDECIBA |
| Peru | 2 | QuantumHub, QuantumQuipu | Quantum AI Summit Peru |
| Costa Rica | 1 | UNA SpinQ | — |
| Panama | 1 | TR Consultores | — |
| Regional | 2 | Quantum Latino, NTT+Kipu | IBM Quantum Network LATAM, QWorld LATAM, SpinQ LATAM, Santander+IBM challenge |
| **Missing entirely** | — | — | Bolivia, Ecuador, Cuba, Venezuela, Dominican Republic, Paraguay, Guatemala |

---

## Search Strategy

### Phase 1 — Systematic web searches

Run the following queries (adapt language as needed; Spanish/Portuguese sources are valid):

**By country (repeat for each underrepresented country):**
```
"quantum computing" Bolivia university research 2024 OR 2025 OR 2026
"computación cuántica" Ecuador universidad laboratorio
"quantum technology" Venezuela research group
"quantum" Cuba InSTEC OR "Universidad Central"
"computación cuántica" Paraguay
"quantum computing" Guatemala OR Honduras OR Nicaragua site:edu OR site:gob
```

**By entity type:**
```
"quantum startup" "Latin America" OR "América Latina" 2024 OR 2025 OR 2026
"quantum computing" Brazil UNESP OR ITA OR "Universidade Federal" 2025
"quantum" Argentina "Universidad Nacional de Córdoba" OR UNSAM OR UTN
"quantum sensing" "Latin America" mining OR agriculture 2025
"QKD" OR "quantum key distribution" "Latin America" 2025 OR 2026
"post-quantum cryptography" "América Latina" gobierno OR ministerio
"quantum hub" OR "quantum center" Brazil OR Chile OR Colombia 2025 2026
site:arxiv.org "quantum" "Latin America" OR "Brazil" OR "Colombia" 2025
```

**By organization type:**
```
"IBM Quantum Network" "Latin America" members 2025
"QWorld" LATAM OR "Latin America" chapter OR node
SpinQ "Latin America" distributors OR partners 2025
"quantum bootcamp" OR "quantum course" "América Latina" 2025 2026
"Microsoft Quantum" "Latin America" partner
"Google Quantum" Brazil OR Chile OR Colombia research
```

**Specific missing entries to verify:**
```
Classiq "UC Chile" quantum biomedical 2026
"Universidad del Valle" Colombia quantum computer 2025
UNESP "quantum computing" Brazil 2025
"Instituto Tecnológico de Aeronáutica" ITA quantum
SpinQ Mexico "oficina regional" OR "regional office"
"Orchids" OR "Orquídeas" Colombia quantum women postdoc
"Quantum AI Summit" Peru 2025
ASQC "symposium on quantum computing" Argentina 2025
"Universidade de Montevideo" Quantum-South origin
```

### Phase 2 — Direct source scraping

Fetch and scan these pages for LATAM entities not in the current database:

- `https://thequantuminsider.com` — search for "Latin America", "Brazil", "Chile", "Colombia", "Argentina", "Mexico"
- `https://quantumcomputingreport.com` — same searches
- `https://www.qureca.com/quantum-initiatives-worldwide/` — filter LATAM entries
- `https://qworld.net/qedu/` — find LATAM QWorld nodes
- `https://arxiv.org/search/?searchtype=all&query=quantum+latin+america&start=0` — scan 2024–2026 papers for new institutions
- Each country's science ministry website (look for "cuántica" or "quantum" programs):
  - Brazil: `mcti.gov.br`
  - Argentina: `argentina.gob.ar/ciencia`
  - Chile: `anid.cl`
  - Colombia: `minciencias.gov.co`
  - Mexico: `conahcyt.mx`
  - Peru: `concytec.gob.pe`
  - Bolivia: `minedu.gob.bo`

### Phase 3 — Enrich existing entries

For each existing entry with `url: ''`, try to find the official URL:
- Search `"<entity name>" quantum site:edu OR site:org OR site:com`
- Check if the institution has a dedicated quantum lab/group page

For entries with thin descriptions (under 2 sentences), look for:
- Funding amounts
- Key researchers/directors
- Partner organizations
- Recent publications (arXiv ID)
- Active projects

---

## Validation Rubric

Before adding any entity, verify ALL of the following:

| Criterion | Pass condition |
|-----------|---------------|
| **Quantum relevance** | Activity is substantively quantum — not "quantum-inspired" marketing, not classical HPC labeled quantum, not only quantum mechanics in curriculum |
| **LATAM presence** | Entity operates in, is headquartered in, or was founded in a LATAM country. HQ outside LATAM is OK only if the entity is LATAM-origin (e.g., /q99 founded by Argentine researchers) |
| **Evidence of existence** | Website, arXiv paper, news article, or institutional page confirms the entity and its quantum activity |
| **Activity recency** | Evidence of activity within the last 3 years (2023–2026). Purely historical groups with no recent output → flag as `status:'inactive'`, do not add as new |
| **Description accuracy** | Every claim in the description has a verifiable source. If uncertain, omit the claim rather than guess |

**Automatic rejects:**
- "Quantum-inspired" classical algorithms marketed as quantum
- Companies that only resell IBM/AWS quantum cloud access with no IP of their own
- University courses that cover quantum mechanics in physics curriculum but have no quantum computing/QI research
- Press releases with no follow-through (announced center that never opened)

---

## Output Format

### For new entries

Output a ready-to-paste JS block:

```javascript
// NEW ENTRIES — <date> — found via <search method>
// Sources: <URL1>, <URL2>

{ id:'slug-here', name:'Display Name', type:'research', country:'Brazil', city:'City',
  lat:-00.00, lng:-00.00, focus:['computing'],
  description:'Factual description. Key researcher/director. Funding if known. Partners.',
  url:'https://...' },
```

Group by country. Include a comment above each block with the source URL(s) where you found the information.

### For updates to existing entries

```javascript
// UPDATE: <existing-id>
// Field: url → 'https://...'
// Field: description → 'Updated text...'
// Reason: <why the change>
// Source: <URL>
```

### For stale/incorrect entries

```javascript
// FLAG: <existing-id>
// Issue: <description of the problem>
// Evidence: <URL or reasoning>
// Suggested action: update | remove | mark inactive
```

### Summary at the end

After all entries/updates, output a short table:

```
## Summary
New entries: N
Updates to existing: N
Flags: N

New countries added: X, Y, Z
Largest type gap filled: <type>
```

---

## Coordinate Lookup

For any city not obvious, use this reference or look up on OpenStreetMap:

| City | lat | lng |
|------|-----|-----|
| São Paulo | -23.55 | -46.63 |
| Rio de Janeiro | -22.91 | -43.17 |
| Campinas | -22.82 | -47.07 |
| Brasília | -15.77 | -47.92 |
| Salvador | -12.97 | -38.50 |
| Recife | -8.05 | -34.88 |
| Belo Horizonte | -19.92 | -43.94 |
| Buenos Aires | -34.60 | -58.38 |
| Bariloche | -41.15 | -71.31 |
| Córdoba (AR) | -31.42 | -64.18 |
| Santiago | -33.45 | -70.67 |
| Concepción (CL) | -36.82 | -73.04 |
| Bogotá | 4.71 | -74.07 |
| Medellín | 6.25 | -75.56 |
| Cali | 3.45 | -76.52 |
| Mexico City | 19.43 | -99.13 |
| Monterrey | 25.65 | -100.29 |
| Guadalajara | 20.66 | -103.35 |
| Montevideo | -34.90 | -56.19 |
| Lima | -12.05 | -77.04 |
| Heredia | 10.00 | -84.12 |
| Panama City | 8.99 | -79.52 |
| La Paz | -16.50 | -68.15 |
| Quito | -0.22 | -78.51 |
| Guayaquil | -2.19 | -79.89 |
| Havana | 23.13 | -82.38 |
| Caracas | 10.48 | -66.88 |
| Asunción | -25.29 | -57.65 |
| Santo Domingo | 18.48 | -69.93 |
| Guatemala City | 14.64 | -90.51 |

If two entries share the same city, offset one by ±0.03–0.05 degrees on lat or lng to prevent marker overlap.

---

## Priority Targets

These are specific entities that likely exist and should be verified first:

1. **Classiq + UC Chile** (biomedical quantum pilot, June 2026) — add as `corporate` or `research`
2. **Universidad del Valle** (Colombia, planned quantum computer) — add as `infrastructure`
3. **UNESP** (São Paulo, mentioned in ITU Quantum World Tour) — add as `research`
4. **QWorld LATAM nodes** — check `qworld.net` for registered nodes in LATAM countries
5. **SpinQ LATAM regional office** (Mexico City) — add as `network`
6. **IBM Quantum Network LATAM** — add as `network` (regional node)
7. **Orchids / Orquídeas Program** (Colombia, women in quantum) — add as `training` or `government`
8. **ASQC** (Argentinean Symposium on Quantum Computing, annual) — add as `network`
9. **Universidad de Montevideo** (origin of Quantum-South) — add as `research`
10. **QutSur** itself — add as `network`, country: `Regional`, city: `Buenos Aires`
11. **Santander X + IBM Quantum AI Leap Challenge** — add as `network`
12. **UNSAM quantum groups** (Argentina, QUBIT.AR partner) — check if merits own entry
13. **BUAP** (Benemérito Universidad Autónoma de Puebla) — quantum optics group
14. **InSTEC** (Cuba) — if active quantum research exists
15. **Any Bolivian or Ecuadoran university** with quantum physics groups
16. **NTT DATA LATAM directly** — check if they merit a separate corporate entry beyond the Kipu alliance

---

## Quality Bar

**Prefer depth over breadth.** A well-described entry with a verified URL and concrete facts is worth more than three thin entries with placeholder descriptions.

**Descriptions should answer:** What do they do specifically? Who leads it? What has been built/published/deployed? Any notable partnerships or funding?

**Do not** fabricate or extrapolate. If you can't verify a fact from a primary source, leave it out. Use phrases like "research directions include" rather than stating unverified claims as fact.
