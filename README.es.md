# Mapa Cuántico LATAM

🌐 [English](README.md) | **Español** | [Português](README.pt.md)

Un mapa abierto e interactivo de quién hace tecnología cuántica en América Latina — laboratorios, startups, empresas, programas de gobierno, formación, infraestructura y redes.

**→ Mirá el mapa en vivo: [qutsur.com/LATAM-quantum-map](https://qutsur.com/LATAM-quantum-map/)**

[![Vista previa del Mapa Cuántico LATAM](assets/preview.png)](https://qutsur.com/LATAM-quantum-map/)

**85+ lugares en 12 países.** Mantenido por [QutSur](https://qutsur.com). Leelo con cariño — es un trabajo en progreso.

---

## ✏️ Agregar o corregir un lugar — 2 minutos, sin programar

¿Conocés un laboratorio, startup o programa cuántico que falta o está mal? Avisanos. No necesitás tocar nada de código.

### ➕ [Hacé clic acá para **agregar un lugar**](../../issues/new?template=add-entity.yml)

Completá el formulario corto: **nombre · tipo · ciudad · una o dos frases de lo que hacen · un link** (su sitio o un artículo). Enviá.

### 🔧 [Hacé clic acá para **corregir o eliminar un lugar**](../../issues/new?template=fix-entity.yml)

Contá qué está mal y pegá un link. Enviá.

**Listo.** Un bot lee tu formulario, lo ubica en el mapa y abre una propuesta automáticamente — normalmente en menos de un minuto. Un mantenedor le da una mirada rápida y la aprueba.

> ⚠️ **Siempre hace falta un link como fuente.** Sin link, no entra. (Su sitio oficial, un artículo o un paper.)

---

<details>
<summary>🛠️ Para desarrolladores</summary>

El mapa es HTML simple + [Leaflet](https://leafletjs.com); todo el contenido vive en tres archivos JSON:

| Archivo | Contenido |
|---------|-----------|
| `data/entities.json` | los lugares |
| `data/networks.json` | redes regionales |
| `data/events.json` | eventos |

Editá **solo** `data/*.json`, corré `python3 scripts/validate_data.py` y abrí un PR (el CI rechaza cualquier cosa que toque otros archivos). Esquema y guía de campos: [`agent_instructions.md`](agent_instructions.md). Fuentes: [`sources.md`](sources.md).

```bash
python3 -m http.server 8000   # correr localmente desde la raíz del repo
```

Las contribuciones asistidas por IA son bienvenidas — apuntá tu agente a `agent_instructions.md`.

</details>

## Licencia

Código: [MIT](LICENSE) · Datos: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reutilizá libremente con atribución a *QutSur — Mapa Cuántico LATAM*.
