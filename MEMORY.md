# Vibeflow Index
> Project: hackathon-ia-saude | Stack: Python + Streamlit + Ollama (MedGemma/Gemma 4) | Analyzed: 2026-07-18

## .vibeflow/ docs available
- index.md — visão geral do projeto e estrutura
- conventions.md — convenções de código (idioma, encoding, session_state, fonte única)
- patterns/streamlit-app-composition.md — abas, painel reutilizável, session_state, callbacks
- patterns/ollama-streaming-integration.md — chamada ao Ollama com streaming e métricas
- patterns/synthetic-data-generation.md — geração de CSV fictício com seed fixa e gabarito
- patterns/docs-generated-from-source-json.md — JSON como fonte única, markdown derivado
- decisions.md — log de decisões arquiteturais (vazio, cresce com o uso)

## Quick Reference
- Todo script novo deve abrir com `sys.stdout.reconfigure(encoding="utf-8")` logo após os imports.
- Nunca mutar `st.session_state[chave]` de um widget já renderizado no meio do script — usar
  `on_click=` + função de callback.
- Toda chamada ao modelo local passa por `gerar_stream`/`chat_stream` → `_consumir_stream`,
  nunca `requests.post` direto numa aba.
- Mudança de conteúdo de desafio/trilha/prompt só em `exemplos_prompts.json`, seguida de
  `python gerar_desafios_md.py` — nunca editar `desafios_por_trilha.md` à mão.
- Nenhum dado real de paciente em nenhum fluxo (imagem, áudio, texto) — só fictício/didático.

## Instructions
Before generating ANY spec, prompt pack, or audit:
1. Read .vibeflow/index.md for project context
2. Read .vibeflow/conventions.md for coding standards
3. Read the relevant pattern docs from .vibeflow/patterns/
4. Embed applicable patterns in your output

When you learn something new about this project, update:
- .vibeflow/decisions.md for architectural decisions
- .vibeflow/conventions.md if new conventions are discovered
- .vibeflow/patterns/*.md if patterns evolve
- This MEMORY.md index if new docs are added
