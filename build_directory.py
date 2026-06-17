#!/usr/bin/env python3
"""Generate a static, crawlable directory page from entities.json.

Single source of truth = data/entities.json. Re-run after data changes:
    cd webpage/LATAM-quantum-map && python3 build_directory.py
Outputs directorio/index.html — a server-free, SEO-indexable list of every
entity (names/descriptions live in the HTML, unlike the JS map which fetches
them client-side and is invisible to crawlers).
"""
import html
import json
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
ENTITIES = json.loads((HERE / "data" / "entities.json").read_text(encoding="utf-8"))

# ES labels — mirror T.es in index.html
TYPE_ES = {
    "research": "Investigación", "startup": "Startup", "corporate": "Corporativo",
    "government": "Gobierno", "training": "Formación", "infrastructure": "Infraestructura",
    "network": "Red",
}
FOCUS_ES = {
    "computing": "Comp. Cuántica", "sensing": "Sensado", "communication": "Com. Cuántica",
    "cryptography": "PQC/QKD", "optimization": "Optimización", "education": "Educación",
    "other": "Otro",
}
TYPE_COLOR = {
    "research": "#34598e", "startup": "#2e7d5b", "corporate": "#c8920a",
    "government": "#c0392b", "training": "#6d5aa8", "infrastructure": "#b05c2c",
    "network": "#2e8b9a",
}
COUNTRY_ES = {
    "Brazil": "Brasil", "Mexico": "México", "Peru": "Perú", "Panama": "Panamá",
    "Trinidad and Tobago": "Trinidad y Tobago", "Regional": "Regional / Multinacional",
}


def es_country(c):
    return COUNTRY_ES.get(c, c)


def esc(s):
    return html.escape(str(s), quote=True)


# group by country, ordered by count desc, Regional last
by_country = {}
for e in ENTITIES:
    by_country.setdefault(e["country"], []).append(e)
for v in by_country.values():
    v.sort(key=lambda e: e["name"].lower())

order = sorted(
    by_country,
    key=lambda c: (c == "Regional", -len(by_country[c]), es_country(c)),
)
n_entities = len(ENTITIES)
n_countries = len([c for c in by_country if c != "Regional"])
today = date.today().isoformat()

# ---- JSON-LD ItemList ----
item_list = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Ecosistema cuántico de América Latina",
    "description": f"Directorio de {n_entities} entidades de tecnología cuántica en {n_countries} países de América Latina.",
    "numberOfItems": n_entities,
    "itemListElement": [],
}
pos = 0
for c in order:
    for e in by_country[c]:
        pos += 1
        org = {
            "@type": "Organization",
            "name": e["name"],
            "description": e["description"],
            "address": {"@type": "PostalAddress", "addressLocality": e["city"], "addressCountry": e["country"]},
        }
        if e.get("url"):
            org["url"] = e["url"]
        item_list["itemListElement"].append({"@type": "ListItem", "position": pos, "item": org})

# ---- country nav ----
nav = " · ".join(
    f'<a href="#{esc(c.lower().replace(" ", "-"))}">{esc(es_country(c))} <span>{len(by_country[c])}</span></a>'
    for c in order
)

# ---- sections ----
sections = []
for c in order:
    ents = by_country[c]
    cid = esc(c.lower().replace(" ", "-"))
    cards = []
    for e in ents:
        tcolor = TYPE_COLOR.get(e["type"], "#7d8494")
        tlabel = TYPE_ES.get(e["type"], e["type"])
        foci = " · ".join(FOCUS_ES.get(f, f) for f in e.get("focus", []))
        inactive = (
            '<span class="badge-inact">⚠ Posiblemente inactivo</span>' if e.get("inactive") else ""
        )
        meta = f'<span class="city">{esc(e["city"])}</span>'
        if foci:
            meta += f' <span class="sep">·</span> <span class="foci">{esc(foci)}</span>'
        link = (
            f'<a class="ent-link" href="{esc(e["url"])}" target="_blank" rel="noopener">Sitio oficial ↗</a>'
            if e.get("url")
            else ""
        )
        cards.append(
            f'''      <article class="ent" style="--tc:{tcolor}">
        <div class="ent-head"><h3>{esc(e["name"])}</h3><span class="badge-type">{esc(tlabel)}</span>{inactive}</div>
        <div class="ent-meta">{meta}</div>
        <p class="ent-desc">{esc(e["description"])}</p>
        {link}
      </article>'''
        )
    sections.append(
        f'''    <section class="country" id="{cid}">
      <h2>{esc(es_country(c))} <span class="cnt">{len(ents)} {"entidad" if len(ents)==1 else "entidades"}</span></h2>
{chr(10).join(cards)}
    </section>'''
    )

jsonld = json.dumps(item_list, ensure_ascii=False, separators=(",", ":"))

HTML = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Directorio del ecosistema cuántico de América Latina — {n_entities} entidades | QutSur</title>
  <meta name="description" content="Directorio completo del ecosistema de tecnología cuántica en América Latina: {n_entities} universidades, startups, empresas, redes e infraestructura de computación, sensado, comunicación y criptografía cuántica en {n_countries} países.">
  <link rel="canonical" href="https://qutsur.com/LATAM-quantum-map/directorio/">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Directorio del ecosistema cuántico de América Latina — QutSur">
  <meta property="og:description" content="{n_entities} entidades de tecnología cuántica en {n_countries} países de América Latina. Datos abiertos CC BY 4.0.">
  <meta property="og:url" content="https://qutsur.com/LATAM-quantum-map/directorio/">
  <meta property="og:image" content="https://qutsur.com/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Directorio del ecosistema cuántico de América Latina — QutSur">
  <meta name="twitter:description" content="{n_entities} entidades de tecnología cuántica en {n_countries} países de América Latina.">
  <meta name="twitter:image" content="https://qutsur.com/og-image.png">
  <link rel="icon" type="image/svg+xml" href="../../branding/Mesa de trabajo 1_3.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">{jsonld}</script>
  <style>
    :root {{
      --bg:#fafaf8; --navy:#1a2035; --ink:#171327; --red:#c0392b; --ochre:#c8920a;
      --muted:#7d8494; --dim:#b0b7c3; --border:#e4e4e0; --font:'Inter',-apple-system,sans-serif;
    }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:var(--bg); color:var(--navy); font-family:var(--font); line-height:1.55; -webkit-font-smoothing:antialiased; }}
    a {{ color:inherit; }}
    .wrap {{ max-width:980px; margin:0 auto; padding:0 22px; }}
    header.top {{ padding:54px 0 28px; border-bottom:1px solid var(--border); }}
    .dots {{ display:flex; gap:7px; margin-bottom:20px; }}
    .dots i {{ width:11px; height:11px; border-radius:47% 53% 51% 49%; display:block; }}
    .dots i:nth-child(1){{ background:var(--ink); }} .dots i:nth-child(2){{ background:var(--ochre); }} .dots i:nth-child(3){{ background:var(--red); }}
    h1 {{ font-family:'Cormorant Garamond',Georgia,serif; font-style:italic; font-weight:500; font-size:clamp(30px,5vw,46px); line-height:1.08; margin:0 0 10px; letter-spacing:-0.01em; }}
    .sub {{ font-size:16px; color:var(--muted); max-width:620px; margin:0 0 22px; }}
    .stats {{ display:flex; gap:26px; flex-wrap:wrap; margin:18px 0 4px; }}
    .stats b {{ font-size:26px; font-weight:700; display:block; color:var(--ink); }}
    .stats span {{ font-size:12px; text-transform:uppercase; letter-spacing:0.08em; color:var(--muted); }}
    .actions {{ margin-top:22px; display:flex; gap:14px; flex-wrap:wrap; }}
    .btn {{ display:inline-block; padding:9px 16px; border-radius:8px; font-size:14px; font-weight:600; text-decoration:none; }}
    .btn-pri {{ background:var(--ink); color:#fafaf8; }}
    .btn-sec {{ border:1px solid var(--border); color:var(--navy); }}
    nav.idx {{ font-size:13.5px; line-height:2.1; padding:22px 0; border-bottom:1px solid var(--border); color:var(--muted); }}
    nav.idx a {{ text-decoration:none; white-space:nowrap; }}
    nav.idx a:hover {{ color:var(--ink); }}
    nav.idx a span {{ color:var(--dim); font-size:11px; }}
    section.country {{ padding:34px 0 8px; }}
    section.country h2 {{ font-size:22px; font-weight:700; margin:0 0 18px; color:var(--ink); display:flex; align-items:baseline; gap:12px; scroll-margin-top:14px; }}
    section.country h2 .cnt {{ font-size:12px; font-weight:500; color:var(--muted); text-transform:uppercase; letter-spacing:0.06em; }}
    .ent {{ border-left:3px solid var(--tc); padding:2px 0 14px 16px; margin:0 0 16px; }}
    .ent-head {{ display:flex; align-items:baseline; gap:10px; flex-wrap:wrap; }}
    .ent-head h3 {{ font-size:16.5px; font-weight:600; margin:0; color:var(--navy); }}
    .badge-type {{ font-size:11px; font-weight:600; color:var(--tc); border:1px solid color-mix(in srgb,var(--tc) 35%,transparent); padding:1px 7px; border-radius:20px; white-space:nowrap; }}
    .badge-inact {{ font-size:11px; font-weight:600; color:#9c6f08; background:#c8920a1f; padding:1px 7px; border-radius:20px; white-space:nowrap; }}
    .ent-meta {{ font-size:13px; color:var(--muted); margin:4px 0 6px; }}
    .ent-meta .sep {{ color:var(--dim); }}
    .ent-desc {{ font-size:14.5px; margin:0 0 7px; max-width:760px; }}
    .ent-link {{ font-size:13px; font-weight:600; color:var(--tc); text-decoration:none; }}
    .ent-link:hover {{ text-decoration:underline; }}
    footer.bot {{ margin-top:30px; padding:34px 0 60px; border-top:1px solid var(--border); font-size:13px; color:var(--muted); }}
    footer.bot a {{ color:var(--navy); font-weight:500; }}
  </style>
</head>
<body>
  <div class="wrap">
    <header class="top">
      <div class="dots" aria-hidden="true"><i></i><i></i><i></i></div>
      <h1>Ecosistema cuántico de América Latina</h1>
      <p class="sub">Directorio abierto de universidades, startups, empresas, programas de gobierno, redes e infraestructura que trabajan en tecnología cuántica en la región. Mantenido por QutSur.</p>
      <div class="stats">
        <div><b>{n_entities}</b><span>Entidades</span></div>
        <div><b>{n_countries}</b><span>Países</span></div>
      </div>
      <div class="actions">
        <a class="btn btn-pri" href="../">Ver el mapa interactivo →</a>
        <a class="btn btn-sec" href="https://qutsur.com/">QutSur</a>
      </div>
    </header>
    <nav class="idx" aria-label="Índice por país">{nav}</nav>
    <main>
{chr(10).join(sections)}
    </main>
    <footer class="bot">
      <p>Datos abiertos bajo <a href="https://creativecommons.org/licenses/by/4.0/" rel="license">CC BY 4.0</a>. Última actualización: {today}. ¿Falta alguien o hay un dato a corregir? Escribinos.</p>
      <p><a href="../">Mapa interactivo</a> · <a href="https://qutsur.com/">qutsur.com</a> · <a href="https://github.com/matibilkis/latam-quantum-map">Repositorio de datos</a></p>
    </footer>
  </div>
</body>
</html>
'''

out = HERE / "directorio" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(HTML, encoding="utf-8")
print(f"OK — wrote {out} ({n_entities} entities, {n_countries} countries, {len(order)} sections)")
