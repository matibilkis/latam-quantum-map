# Mapa Cuántico LATAM

🌐 [English](README.md) | **Español** | [Português](README.pt.md)

Mapa interactivo del ecosistema de tecnología cuántica en América Latina — laboratorios, startups, programas corporativos, gobiernos, formación, infraestructura y redes.

**→ Mapa en vivo:** [qutsur.com/LATAM-quantum-map](https://qutsur.com/LATAM-quantum-map/)

[![Vista previa del Mapa Cuántico LATAM](assets/preview.png)](https://qutsur.com/LATAM-quantum-map/)

**86 entidades** en 12 países — más redes regionales y eventos. Mantenido por [QutSur](https://qutsur.com).

> **Léelo con cariño.** Trabajo en progreso, partes compiladas con asistencia de IA. Verifica antes de citar.

---

## Archivos de datos

| Archivo | Contenido |
|---------|-----------|
| `data/entities.json` | 86 entidades mapeadas (laboratorios, startups, programas…) |
| `data/networks.json` | Redes y consorcios regionales |
| `data/events.json` | Eventos del ecosistema, próximos y pasados |

Esquema documentado en [`agent_instructions.md`](agent_instructions.md). Fuentes en [`sources.md`](sources.md).

```bash
python3 -m http.server 8000   # ejecutar localmente desde la raíz del repo
```

## Contribuir

Las adiciones y correcciones son muy bienvenidas — el ecosistema se mueve rápido y el conocimiento local supera a cualquier crawler.

**Abrir un issue** (lo más fácil): [Agregar una entidad](../../issues/new?template=add-entity.yml) o [Corregir / eliminar](../../issues/new?template=fix-entity.yml). Se requiere una fuente primaria verificable.

**Abrir un pull request**: editar solo `data/*.json`, seguir [`agent_instructions.md`](agent_instructions.md), incluir fuentes en la descripción del PR, correr `python3 scripts/validate_data.py` antes de hacer push.

Las contribuciones asistidas por IA son explícitamente bienvenidas — apunta tu agente a `agent_instructions.md`. Mismo pipeline de revisión que las contribuciones humanas.

### Gobernanza

- **Separación datos/código** — los PRs solo pueden tocar `data/*.json`; el CI rechaza cualquier otra modificación.
- **Validación automática** — `scripts/validate_data.py` verifica el esquema en cada PR. Sin LLM en la cadena de enforcement.
- **Revisión legible** — el CI publica un resumen por PR con texto completo y fuentes para las entidades nuevas.
- **Autoridad final** — branch protection en `main` requiere revisión del mantenedor; nada se mergea automáticamente. [@matibilkis](https://github.com/matibilkis) tiene la última palabra.

## Mapas similares

| Proyecto | Alcance |
|----------|---------|
| [Mapa Cuántico Argentino](https://gbosyk.github.io/mapa_cuantico_argentina/) | 31 grupos de investigación cuántica en Argentina |
| [Quantum Navigator](https://entangledfuture.com/countries/) | 1.150+ organizaciones globales, cobertura LATAM escasa |
| [QURECA Quantum Initiatives](https://www.qureca.com/quantum-initiatives-worldwide/) | Programas nacionales; Brasil es el único país LATAM |
| [Quantiki groups](https://www.quantiki.org/groups) | Grupos académicos de QI/QC registrados globalmente |
| [Impact Quantum Global Report](https://impactquantum.com/GlobalReport/) | Datos a nivel país para 108 ecosistemas |

Este mapa cubre el vacío: cobertura a nivel de entidad, para toda la región LATAM. Ver [`sources.md`](sources.md) para la lista completa de referencias cruzadas.

## Licencia

Código: [MIT](LICENSE) · Datos: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reutilización libre con atribución a *QutSur — Mapa Cuántico LATAM*.
