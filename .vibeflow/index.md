# Project: hackathon-ia-saude
> Analyzed: 2026-07-18
> Stack: Python 3.10+ · Streamlit (UI) · Ollama (LLM local: MedGemma 4B + Gemma 4) · pandas · faster-whisper (opcional)
> Type: App único (Streamlit) + scripts utilitários de dados — ferramenta educacional para hackathon, não um produto multi-módulo
> Suggested budget: ≤ 4 files per task

## Structure

Projeto pequeno e plano: um app Streamlit de arquivo único (`app_hackathon.py`) que consome
dados de duas fontes estáticas — `exemplos_prompts.json` (desafios/prompts, fonte única) e
`dados/*.csv` (dados sintéticos). Dois scripts geram artefatos derivados (markdown de desafios
e os próprios CSVs). Sem framework de rotas, sem banco de dados, sem testes automatizados.

## Structural Units

- **`app_hackathon.py`** — app Streamlit único, 8 abas (TeleEletiva, TeleInterconsulta, Dados,
  Transcrição, Imagem, Chat, Prompt Livre, Resultados). Toda a UI e lógica de integração com
  Ollama vivem aqui.
- **`dados/`** — geração e análise de dados sintéticos (CSV). Sem dependência do app;
  roda standalone via CLI.
- **`exemplos_prompts.json`** — fonte única de verdade dos desafios/trilhas/prompts. Consumida
  pelo app E pelo gerador de markdown.
- **`gerar_desafios_md.py`** — script standalone que deriva `desafios_por_trilha.md` do JSON.
- **`output/`** — resultados salvos pelo app em runtime (gitignored).
- **Docs de operação** (`README.md`, `PLANO_FACILITADOR.md`, `PARTICIPANTES_LEIA_ME.md`,
  `GUIA_PROMPT.md`, `MENSAGENS_TEMPLATE.md`, `BACKUP_SERVIDOR.md`) — não são código, mas
  documentam o evento (hackathon de 4h). Fora do escopo de padrões de código.

## Pattern Registry

<!-- vibeflow:patterns:start -->
patterns:
  - file: patterns/streamlit-app-composition.md
    tags: [streamlit, ui, tabs, session-state, callbacks]
    modules: [app_hackathon.py]
  - file: patterns/ollama-streaming-integration.md
    tags: [ollama, llm, streaming, api-integration]
    modules: [app_hackathon.py]
  - file: patterns/synthetic-data-generation.md
    tags: [data-generation, csv, reproducibility, healthcare-safety]
    modules: [dados/]
  - file: patterns/docs-generated-from-source-json.md
    tags: [single-source-of-truth, code-generation, docs]
    modules: [exemplos_prompts.json, gerar_desafios_md.py]
<!-- vibeflow:patterns:end -->

## Pattern Docs Available
- [streamlit-app-composition.md](patterns/streamlit-app-composition.md) — abas, painel reutilizável por trilha, persistência via `session_state`, callbacks em vez de mutação direta
- [ollama-streaming-integration.md](patterns/ollama-streaming-integration.md) — chamada ao Ollama (`/api/generate` e `/api/chat`) com streaming e métricas de tokens/s
- [synthetic-data-generation.md](patterns/synthetic-data-generation.md) — geração de CSV fictício por regras probabilísticas com seed fixa e "gabarito" oculto
- [docs-generated-from-source-json.md](patterns/docs-generated-from-source-json.md) — `exemplos_prompts.json` como fonte única; markdown é derivado, nunca editado à mão

## Key Files
- `app_hackathon.py` — app Streamlit inteiro (846 linhas): sidebar, 8 abas, integração Ollama, persistência de resultado
- `exemplos_prompts.json` — fonte única de trilhas/desafios/prompts consumida pelo app
- `dados/gerar_dados_sinteticos.py` — gera `agendamentos.csv` (no-show) e `fila_interconsulta.csv` (priorização), com seed fixa (`random.seed(42)`)
- `dados/analise_noshow.py` — análise exploratória standalone da taxa de no-show por fator
- `gerar_desafios_md.py` — deriva `desafios_por_trilha.md` a partir do JSON
- `setup_hackathon.ps1` — instala Python deps + Ollama + baixa os modelos

## Dependencies (critical only)
- `streamlit` — toda a UI do app
- `requests` — chamadas HTTP ao Ollama local (`http://localhost:11434`)
- `pandas` — leitura/agrupamento dos CSVs sintéticos
- `faster-whisper` (opcional) — transcrição de áudio; app degrada graciosamente se ausente (`WHISPER_OK` flag)

## Known Issues / Tech Debt
- Sem testes automatizados (nenhum arquivo `test_*` ou `*_test` encontrado) — esperado para um
  projeto educacional de hackathon de 4h, mas vale registrar.
- `app_hackathon.py` concentra toda a lógica em um único arquivo de ~850 linhas; funcional para
  o escopo atual, mas qualquer extensão significativa de features se beneficiaria de separar
  a camada de integração Ollama (`gerar_stream`/`chat_stream`/`_consumir_stream`) em um módulo
  próprio (ex: `ollama_client.py`).
- Sem `.cursorrules`, `CLAUDE.md` ou `.github/` neste repositório — nenhuma fonte de regras
  declarada localmente (diferente do workspace `.claude` do usuário, que é externo a este repo).
