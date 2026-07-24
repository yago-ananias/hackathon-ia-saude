---
tags: [single-source-of-truth, code-generation, docs]
modules: [exemplos_prompts.json, gerar_desafios_md.py]
applies_to: [scripts, configs]
confidence: inferred
---
# Pattern: JSON como Fonte Única, Markdown Derivado

<!-- vibeflow:auto:start -->
## What
`exemplos_prompts.json` é a única fonte de verdade para trilhas, desafios, perguntas-guia e
prompts de exemplo. O app lê o JSON diretamente; o documento humano-legível
(`desafios_por_trilha.md`) é sempre **gerado** a partir dele por script, nunca editado à mão.

## Where
`exemplos_prompts.json` (dado), `gerar_desafios_md.py` (gerador), `app_hackathon.py` função
`carregar_prompts` (consumidor via `@st.cache_data`).

## The Pattern

**Consumo direto do JSON pelo app, com cache:**
```python
@st.cache_data
def carregar_prompts():
    with open(BASE / "exemplos_prompts.json", "r", encoding="utf-8") as f:
        return json.load(f)

dados = carregar_prompts()
```

**Geração do artefato derivado, com aviso explícito de "não editar":**
```python
out.append("> ⚠️ **Arquivo gerado automaticamente** a partir de `exemplos_prompts.json`.")
out.append("> Nao edite a mao - rode `python gerar_desafios_md.py` apos mudar o JSON.")
```

**Estrutura do JSON usada por ambos os consumidores (`config` + `trilhas.<chave>.desafios[]`):**
```python
for chave, trilha in dados["trilhas"].items():
    for d in trilha["desafios"]:
        bloco_desafio(d)  # cada desafio tem: id, titulo, problema, metricas_alvo,
                           # metricas_detalhe, perguntas_guia, dados_relacionados, prompts_exemplo
```

## Rules
- Qualquer mudança de conteúdo de desafio/trilha/prompt acontece SOMENTE em
  `exemplos_prompts.json`.
- Depois de editar o JSON, rodar `python gerar_desafios_md.py` para regenerar
  `desafios_por_trilha.md` — nunca editar o `.md` gerado diretamente.
- O `.md` gerado sempre carrega o aviso de "gerado automaticamente" no topo, para qualquer
  pessoa que abra o arquivo isoladamente saber que não deve editá-lo.

## Examples from this codebase
File: gerar_desafios_md.py:57-107 (`main`, monta o `.md` linha a linha a partir do JSON)
File: app_hackathon.py:77-82 (`carregar_prompts`, consumidor cacheado)
<!-- vibeflow:auto:end -->

## Anti-patterns (if found)
Nenhum encontrado.
