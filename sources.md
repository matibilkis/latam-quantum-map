# LATAM Quantum Map — Sources

_Last updated: June 2026_

---

## Similar GitHub Projects

### mapa_cuantico_argentina
- **Repo:** https://github.com/gbosyk/mapa_cuantico_argentina
- **Live:** https://gbosyk.github.io/mapa_cuantico_argentina/
- **What:** Interactive map of 31 quantum research groups in Argentina. Static HTML. Built by a CONICET researcher.
- **Scrape value:** Pull the 31 group entries (names, institutions, cities). Cross-check against our Argentina entries.
- **Note:** Argentina-only scope. No schema visible in the repo — the data is likely hardcoded in the HTML.

---

## Global Directories With LATAM Entries

### Quantum Navigator (Entangled Future)
- **URL:** https://entangledfuture.com/countries/
- **LATAM pages:** Brazil (6), Colombia (2), Chile (2), Mexico (1), Argentina (1), Paraguay (1), Uruguay (1)
- **Brazil page:** https://entangledfuture.com/brazil-quantum/
- **New startups page:** https://entangledfuture.com/new-startups/
- **What:** 1156+ organizations across 52 countries. Tracks hardware, software, research, VCs, enterprise adopters.
- **Data fields:** Name, logo, location, founding year, Commercial/Research classification, description, technology tags.
- **Scrape value:** Medium. Pages are scrapeable HTML. Contains several LATAM companies not in our DB (Dobslit, Qnity, Qnow). Check all 7 LATAM country pages.
- **Note:** Coverage is sparse for LATAM. Paraguay has 1 entry (ITTI / SignQuantum distributor).

### Qureca – Quantum Initiatives Worldwide
- **URL:** https://www.qureca.com/quantum-initiatives-worldwide/
- **What:** Annual interactive map of national quantum programs. 40+ countries. Brazil is the only LATAM country with a detailed entry. Chile, Argentina, Colombia absent.
- **Data fields:** Government funding, program names, timelines, key orgs, tech focus.
- **Scrape value:** Low for LATAM — too Brazil-centric. But good for government/policy entries.
- **Note:** Manually updated once a year. No API or download.

### Quantiki – Research Groups Directory
- **URL:** https://www.quantiki.org/groups
- **Brazil filter:** https://www.quantiki.org/groups?order=country&sort=asc&field_country_value=BR
- **What:** World's leading QI/QC portal. Maintains a paginated directory of academic research groups (35+ pages). Sortable by country.
- **Data fields:** Group name, institution, country, research type (Theory / Experiment / Both), focus areas.
- **Scrape value:** High for academia. URL parameters allow country filtering. LATAM coverage is sparse but authoritative when present — confirmed: UFF Brazil, IFT-UNESP São Paulo.
- **Note:** Groups must self-register. Gaps are common in LATAM. Good for finding groups not otherwise indexed.

### The Quantum Insider – Company / Country Database
- **URL:** https://thequantuminsider.com
- **LATAM article:** https://thequantuminsider.com/2025/02/23/guest-post-latin-america-is-delivering-quantum-technology-its-time-to-recognize-it/
- **Country ranking:** https://thequantuminsider.com/2026/03/26/leading-quantum-computing-countries/
- **What:** Major quantum media site. Has a premium company directory (not freely scrapeable) and extensive editorial coverage of LATAM.
- **Scrape value:** High for editorial content — scrape articles tagged Brazil/Argentina/Chile/Colombia/Mexico for entity discovery. Premium directory requires subscription.
- **Note:** Their editorial coverage is the best free source for discovering new LATAM companies and initiatives.

### Quantum Computing Report – Private Companies
- **URL:** https://quantumcomputingreport.com/privatestartup/
- **What:** Global list of quantum startups and private companies. Lightly covers LATAM — only Dobslit (Brazil, São Carlos) found in scan.
- **Scrape value:** Low for LATAM specifically. Worth a periodic check for new Brazilian/Argentine spinoffs.

### Impact Quantum – Global Report (Interactive Map)
- **URL:** https://impactquantum.com/GlobalReport/
- **What:** Interactive map of 108 quantum ecosystems. Country-level data as of March 2026.
- **Data fields:** Readiness Index (1–5), Funding USD, Strategy Year, Ecosystem Type, Policy Status, Academic Hubs, Private Sector, Infrastructure, International Ties, 2025+ Outlook.
- **Scrape value:** High. **CSV export is available.** Download the CSV and cross-reference all LATAM country rows. Good for government/policy layer.
- **Note:** Country-level only — not entity-level. But the CSV is a fast way to get policy and funding data for underrepresented countries.

---

## LATAM-Specific Platforms

### RIPAISC — Red Iberoamericana para el avance de la Ingeniería de Software Cuántico
- **URL:** https://www.ripaisc.net/
- **What:** Iberian-American quantum software engineering network. Members in Argentina, Colombia, Chile, Spain. Organizes TLISC (Taller Latinoamericano en Ingeniería y Software Cuántico) workshops and publishes news on member institutions.
- **Scrape value:** Medium. Blog contains announcements about quantum activities at member universities — useful for finding new research groups and programs in Colombia and Chile.
- **Note:** Academia-focused. Hosted QSE PhD school 2025.

### mapa_cuantico_argentina (CONICET / IYQ 2025)
- **URL:** https://imit.conicet.gov.ar/launch-of-iyq-2025-and-presentation-of-the-map-of-quantum-in-argentina/
- **What:** CONICET's first systematic survey of quantum research groups in Argentina. Launched for IYQ 2025. Companion to the gbosyk GitHub map above.
- **Scrape value:** High for Argentina. This is the authoritative Argentine academic registry. 31 groups.

### Quantum Latino Conference
- **URL:** https://quantum-latino.com/
- **What:** Pan-LATAM annual quantum conference. Speaker and attendee network spans the whole region. Program pages list institutions and researchers from every LATAM country.
- **Scrape value:** High. Program pages for 2021/2022/2023/2026 list hundreds of researchers with institutional affiliations. Good for finding groups in underrepresented countries.
- **2026 edition:** Medellín, Oct 21–23.

### QBrasil (QWorld Node)
- **URL:** https://qworld.net/qbrasil/
- **What:** Brazilian node of the global QWorld quantum education network. Organizes workshops, courses, hackathons.
- **Scrape value:** Low-medium. Events page lists participating Brazilian universities not in our DB.

### QMexico (QWorld Node)
- **URL:** https://qmexico.org/
- **What:** Mexican/LATAM quantum education community. QCousins affiliate of QWorld. Organizes workshops in Spanish/English.
- **Scrape value:** Low. Small team. Useful for discovering emerging Mexico community groups.

### Instituto Principia
- **URL:** https://www.institutoprincipia.org/en/quantum-technologies
- **What:** São Paulo-based research institute. Since Aug 2020 building a quantum technology initiative anchored in USP/UFSCar/Unicamp, expanding to other Brazilian states and LATAM.
- **Scrape value:** Medium. Contact point for discovering quantum groups outside the main hubs (São Paulo, Salvador, Rio).

### Latin American Committee for Quantum Optics
- **URL:** http://www.quantum-optics.df.uba.ar/latin_committee/index.html
- **What:** Promotes quantum optics in Latin America. Organizes the RIAO/OPTILAS conference (biennial, rotating LATAM countries). Member list covers academic groups across the continent.
- **Scrape value:** High for academic quantum optics groups (sensing, communication). Lists institutions and researchers by country.
- **Note:** TLS cert issue on direct fetch — use cached/Google versions.

### Brazil Quantum (Medium)
- **URL:** https://brazilquantum.medium.com
- **What:** Community blog aggregating Brazilian quantum news and initiative announcements.
- **Scrape value:** Low-medium. Useful for discovering startups and programs before they appear in larger directories.

---

## Scrapeable Institutional Databases

### CNPq – Lattes Platform (Brazil)
- **URL:** http://lattes.cnpq.br/ | Search: http://buscatextual.cnpq.br/buscatextual/busca.do
- **What:** Brazil's national researcher CV database. 3.5M+ CVs indexed. Searchable by research area, institution, keyword ("computação quântica", "informação quântica").
- **Scrape value:** Very high. Gold standard for finding Brazilian quantum research groups and their institutional affiliation. Each researcher links to their group.
- **Note:** Requires scraping or API access. CNPq has a data export program for research use.

### CONICET – Researcher Search (Argentina)
- **URL:** https://www.conicet.gov.ar/new_scp/buscar.php
- **What:** Argentina's national science council researcher search. Similar to Lattes — search by discipline ("computación cuántica") returns researchers with institutional affiliations.
- **Scrape value:** High for Argentina. Complements the mapa_cuantico_argentina GitHub project.

---

## Academic and Survey Sources

### Springer — Overview of Quantum Software Engineering in Latin America
- **URL:** https://link.springer.com/article/10.1007/s11128-024-04586-5
- **What:** Peer-reviewed survey (2024) of quantum software engineering across LATAM. Lists institutions, groups, countries with active QSE research.
- **Scrape value:** High. Read the full paper — tables and appendices likely list every known institution. Free access uncertain; check via Sci-Hub or institutional access.

### arXiv:2410.18307 — Quantum Computing Education in Latin America
- **URL:** https://arxiv.org/abs/2410.18307
- **What:** Survey of QC education initiatives, experiences, and strategies across LATAM (updated Aug 2025). Lists programs, institutions, community efforts.
- **Scrape value:** High for training/education entities. Free access.

### arXiv:2409.00059 — Quantum Ecosystem Research in Colombia
- **URL:** https://arxiv.org/html/2409.00059v1
- **What:** Colombia-specific deep dive (UNAL + Ministry of Digital). Lists every known quantum group and institution in Colombia with assessment.
- **Scrape value:** High for Colombia. Free access.

### OECD-EPO — Mapping the Global Quantum Ecosystem (Dec 2025)
- **URL:** https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/mapping-the-global-quantum-ecosystem_47891dd2/20251217-0001.pdf
- **What:** 163-page joint report. Patent data, startup counts, investment flows, workforce trends by country. LATAM coverage exists but limited compared to US/Europe/Asia.
- **Scrape value:** Medium. PDF — extract tables. Useful for government/policy layer and validating funding figures.

### ResearchGate — Quantum Research from Latin American Countries
- **URL:** https://www.researchgate.net/figure/Quantum-research-from-Latin-American-countries-and-institutions_fig5_386043985
- **What:** Visualization from a bibliometric study showing paper output by LATAM country and institution. Good for identifying active institutions not widely covered.
- **Scrape value:** Low directly. But the underlying paper likely contains the full institution list.

### Springer — CNRS-USP IRC Transitions Quantum Pillar
- **URL:** https://link.springer.com/article/10.1007/s13538-025-02005-3
- **What:** Details the French-Brazilian quantum collaboration (15 USP + 15 CNRS researchers). Lists specific sub-projects and research groups.
- **Scrape value:** Medium. Adds detail to existing USP entry.

---

## Market and Policy Data

### Grand View Research — LATAM Quantum Computing Market
- **URL:** https://www.grandviewresearch.com/horizon/outlook/quantum-computing-market/latin-america
- **What:** Market size projections for LATAM. Not entity-level data.
- **Note:** Paid report. Use for funding/market size stats in descriptions.

### OECD — National Quantum Strategies Overview
- **URL:** https://www.oecd.org/en/publications/an-overview-of-national-strategies-and-policies-for-quantum-technologies_5e55e7ab-en.html
- **What:** Overview of national strategies and policies. Useful for validating/dating government entries.

---

## Scraping Priority Order

For the next enrichment run, scrape in this order:

1. `impactquantum.com/GlobalReport/` — download the CSV export first (108 countries, policy + funding data)
2. `entangledfuture.com` — scrape all 7 LATAM country pages (find new companies: Dobslit, Qnity)
3. `github.com/gbosyk/mapa_cuantico_argentina` — extract the 31 Argentine groups
4. `quantum-latino.com` — scrape program pages for 2021/2022/2023/2026 (researchers + institutions)
5. `quantiki.org/groups` — paginate through all 35+ pages, extract LATAM groups
6. `arxiv.org:2410.18307` + `arxiv.org:2409.00059` — read full text, extract all mentioned institutions
7. `lattes.cnpq.br` — keyword search "computação quântica" for Brazilian groups
8. `ripaisc.net` — scrape blog for new LATAM institution mentions
