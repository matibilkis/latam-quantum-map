# Mapa Quântico LATAM

🌐 [English](README.md) | [Español](README.es.md) | **Português**

Mapa interativo do ecossistema de tecnologia quântica na América Latina — laboratórios, startups, programas corporativos, governos, formação, infraestrutura e redes.

**→ Mapa ao vivo:** [qutsur.com/LATAM-quantum-map](https://qutsur.com/LATAM-quantum-map/)

[![Prévia do Mapa Quântico LATAM](assets/preview.png)](https://qutsur.com/LATAM-quantum-map/)

**86 entidades** em 12 países — mais redes regionais e eventos. Mantido por [QutSur](https://qutsur.com).

> **Leia com carinho.** Trabalho em andamento, partes compiladas com auxílio de IA. Verifique antes de citar.

---

## Arquivos de dados

| Arquivo | Conteúdo |
|---------|----------|
| `data/entities.json` | 86 entidades mapeadas (laboratórios, startups, programas…) |
| `data/networks.json` | Redes e consórcios regionais |
| `data/events.json` | Eventos do ecossistema, futuros e passados |

Esquema documentado em [`agent_instructions.md`](agent_instructions.md). Fontes em [`sources.md`](sources.md).

```bash
python3 -m http.server 8000   # rodar localmente a partir da raiz do repo
```

## Contribuir

Adições e correções são muito bem-vindas — o ecossistema evolui rápido e o conhecimento local supera qualquer crawler.

**Abrir uma issue** (mais fácil): [Adicionar uma entidade](../../issues/new?template=add-entity.yml) ou [Corrigir / remover](../../issues/new?template=fix-entity.yml). Uma fonte primária verificável é obrigatória.

**Abrir um pull request**: editar apenas `data/*.json`, seguir [`agent_instructions.md`](agent_instructions.md), incluir fontes na descrição do PR, rodar `python3 scripts/validate_data.py` antes do push.

Contribuições com auxílio de IA são explicitamente bem-vindas — aponte seu agente para `agent_instructions.md`. Mesmo pipeline de revisão das contribuições humanas.

### Governança

- **Separação dados/código** — PRs só podem tocar `data/*.json`; o CI rejeita qualquer outra modificação.
- **Validação automática** — `scripts/validate_data.py` verifica o esquema em cada PR. Sem LLM no caminho de enforcement.
- **Revisão legível** — o CI posta um resumo por PR com texto completo e fontes para novas entidades.
- **Autoridade final** — branch protection em `main` requer revisão do mantenedor; nada é mergeado automaticamente. [@matibilkis](https://github.com/matibilkis) tem a palavra final.

## Mapas similares

| Projeto | Escopo |
|---------|--------|
| [Mapa Cuántico Argentino](https://gbosyk.github.io/mapa_cuantico_argentina/) | 31 grupos de pesquisa quântica na Argentina |
| [Quantum Navigator](https://entangledfuture.com/countries/) | 1.150+ organizações globais, cobertura LATAM escassa |
| [QURECA Quantum Initiatives](https://www.qureca.com/quantum-initiatives-worldwide/) | Programas nacionais; Brasil é o único país LATAM |
| [Quantiki groups](https://www.quantiki.org/groups) | Grupos acadêmicos de QI/QC registrados globalmente |
| [Impact Quantum Global Report](https://impactquantum.com/GlobalReport/) | Dados por país para 108 ecossistemas |

Este mapa preenche a lacuna: cobertura em nível de entidade, para toda a região LATAM. Ver [`sources.md`](sources.md) para a lista completa de referências cruzadas.

## Licença

Código: [MIT](LICENSE) · Dados: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reutilização livre com atribuição a *QutSur — Mapa Quântico LATAM*.
