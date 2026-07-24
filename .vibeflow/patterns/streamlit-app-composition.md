---
tags: [streamlit, ui, tabs, session-state, callbacks]
modules: [app_hackathon.py]
applies_to: [components, handlers]
confidence: inferred
---
# Pattern: Composição do App Streamlit

<!-- vibeflow:auto:start -->
## What
O app é uma única página Streamlit organizada em abas (`st.tabs`), com um painel de trilha
reutilizável para evitar duplicação entre as duas trilhas do hackathon (TeleEletiva /
TeleInterconsulta), e persistência de resposta via `st.session_state` para sobreviver a reruns.

## Where
`app_hackathon.py` — sidebar (linhas 282-330), definição das 8 abas (linhas 485-494), painel de
trilha reutilizável (`painel_trilha`, linhas 392-452) usado pelas duas primeiras abas.

## The Pattern

**1. Configuração de página única, no topo, antes de qualquer widget:**
```python
st.set_page_config(
    page_title="Hackathon IA + Saude Digital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)
```

**2. Painel parametrizado para eliminar duplicação entre trilhas:**
```python
def painel_trilha(chave_trilha: str, trilha_label: str):
    trilha = dados["trilhas"][chave_trilha]
    ...
    if comparar and prompt_texto.strip():
        comparar_modelos(prompt_texto, modelos_instalados, system_prompt, temperatura, url_ollama)
    elif executar and prompt_texto.strip():
        executar_e_guardar(chave_trilha, prompt_texto, modelo, system_prompt, temperatura, url_ollama)
    render_resposta(chave_trilha, trilha_label, desafio_nome)

with aba_eletiva:
    painel_trilha("teleeletiva", "TeleEletiva")
with aba_ti:
    painel_trilha("teleinterconsulta", "TeleInterconsulta")
```

**3. Persistência de resultado em `session_state`, desacoplada do render:**
```python
def executar_e_guardar(chave: str, prompt: str, modelo: str, system: str,
                       temperatura: float, url: str):
    texto, metr = gerar_stream(prompt, modelo, url, system, temperatura, placeholder)
    st.session_state[f"resp_{chave}"] = {
        "prompt": prompt, "resposta": texto, "modelo": modelo,
        "system": system, "metricas": metr,
    }

def render_resposta(chave: str, trilha_label: str, desafio_label: str):
    res = st.session_state.get(f"resp_{chave}")
    if not res:
        return
    st.markdown(res["resposta"])
```

**4. Mutação de widget SEMPRE via callback, nunca inline:**
```python
def carregar_exemplo(chave_widget: str, texto: str):
    st.session_state[chave_widget] = texto

st.button(
    f"📝 {exemplo['nome']}",
    on_click=carregar_exemplo,
    args=(chave_widget, exemplo["prompt"]),
)
```

## Rules
- Toda chave de `session_state` que guarda resposta de modelo segue o prefixo `resp_<chave>`.
- Toda função que dispara uma chamada ao modelo (`executar_e_guardar`, `comparar_modelos`)
  NÃO renderiza a resposta diretamente — grava em `session_state` e delega o render a
  `render_resposta`, que é chamada de novo a cada rerun. Isso é o que corrige o "bug do salvar"
  mencionado no docstring do módulo.
- Botões que alteram um `text_area`/`session_state` já renderizado usam `on_click=` + `args=`,
  nunca atribuição direta no corpo do script após a criação do widget.

## Examples from this codebase
File: app_hackathon.py:271-277
```python
def carregar_exemplo(chave_widget: str, texto: str):
    st.session_state[chave_widget] = texto

def limpar_campo(chave_widget: str):
    st.session_state[chave_widget] = ""
```

File: app_hackathon.py:344-373 (`render_resposta`, usado por todas as 8 abas)
<!-- vibeflow:auto:end -->

## Anti-patterns (if found)
Nenhum encontrado — o código já documenta explicitamente que a abordagem atual (callback +
session_state) corrige um bug anterior ("corrige bug do salvar"), então é a versão validada.
