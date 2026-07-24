# Coding Conventions
> hackathon-ia-saude · gerado por `/vibeflow:analyze` em 2026-07-18

<!-- vibeflow:auto:start -->
## Idioma e nomenclatura
- Todo o código (variáveis, funções, strings de UI, comentários, docstrings) é em
  **português do Brasil**.
- **Sem acentos** em identificadores E na maior parte do texto solto de console/docstring
  (`nao`, `sao`, `Configuracoes`, `FICTICIO`, `ficticio`) — provável mitigação a problemas de
  encoding UTF-8 no console do Windows. Textos renderizados na UI do Streamlit (`st.markdown`,
  `st.title`) já usam acentuação normal (`"Saúde"`, `"não"`), pois passam pelo navegador, não
  pelo console.
- Nomes de função em `snake_case` em português: `carregar_prompts`, `gerar_stream`,
  `executar_e_guardar`, `salvar_resultado`.

## Encoding
- Todo script com `print()` ou `main()` que roda via CLI declara
  `sys.stdout.reconfigure(encoding="utf-8")` logo após os imports, antes de qualquer lógica.
  Presente em `app_hackathon.py:26`, `gerar_desafios_md.py:15`,
  `dados/analise_noshow.py:12`, `dados/gerar_dados_sinteticos.py:18`.

## Docstrings e cabeçalhos de arquivo
- Todo arquivo `.py` abre com uma docstring de módulo explicando o propósito, quando aplicável
  o comando para rodar (`python arquivo.py`) e, se for gerado/derivado, um aviso para não editar
  à mão.

## Reprodutibilidade de dados sintéticos
- Geração de dados fictícios sempre fixa a seed (`random.seed(42)`) para que qualquer pessoa
  rodando o script gere exatamente o mesmo dataset.

## Streamlit: estado e reatividade
- Qualquer valor que precise sobreviver a um rerun do Streamlit vai para `st.session_state`,
  nunca em variável local solta (ver `patterns/streamlit-app-composition.md`).
- Mutação de widgets (limpar campo, carregar exemplo) é feita via `on_click` + função de
  callback dedicada — nunca escrevendo direto em `st.session_state` no meio do corpo do script
  após o widget já ter sido instanciado (isso quebra no Streamlit).

## Fonte única de verdade
- `exemplos_prompts.json` é a única fonte de dados de trilhas/desafios/prompts. Documentos
  derivados (`desafios_por_trilha.md`) são gerados por script e carregam aviso explícito de
  "não editar à mão".

## Don'ts
- **Não** reintroduzir acentuação em identificadores de código ou em `print()`/docstrings de
  script — quebra encoding no console do Windows (mesmo cuidado documentado no `CLAUDE.md`
  global do usuário sobre `PYTHONIOENCODING`).
- **Não** editar `desafios_por_trilha.md` diretamente — é gerado; qualquer mudança deve ir em
  `exemplos_prompts.json` seguida de `python gerar_desafios_md.py`.
- **Não** enviar ou usar imagem/áudio real de paciente em nenhuma aba (Transcrição, Imagem) —
  regra de segurança explícita no app (`st.error` bloqueando a aba de Imagem lembrando que é
  "EXERCICIO DIDATICO - NAO E DIAGNOSTICO").
- **Não** tratar a saída da MedGemma/Gemma como diagnóstico ou laudo — todos os prompts clínicos
  no app são rotulados como exercício didático.
- **Não** mutar `st.session_state[chave]` diretamente no corpo do script para um widget que já
  foi renderizado no mesmo rerun — usar sempre callback (`on_click=..., args=(...)`), conforme
  o comentário no código: "corrige bug do salvar".
<!-- vibeflow:auto:end -->
