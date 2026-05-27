"""
HACKATHON IA + SAUDE DIGITAL
App Streamlit para explorar prompts com Gemma via Ollama
Trilhas: Teleconsulta Eletiva | Teleinterconsulta
"""

import sys
import json
import time
import requests
import streamlit as st
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# -------------------------------------------------------------------
# Configuracao da pagina
# -------------------------------------------------------------------
st.set_page_config(
    page_title="Hackathon IA + Saude Digital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------------------------
# Carregar prompts
# -------------------------------------------------------------------
@st.cache_data
def carregar_prompts():
    path = Path(__file__).parent / "exemplos_prompts.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

dados = carregar_prompts()

# -------------------------------------------------------------------
# Funcoes utilitarias
# -------------------------------------------------------------------
def chamar_ollama(prompt: str, modelo: str, url_base: str) -> str:
    """Chama o Ollama via API REST e retorna a resposta."""
    try:
        resp = requests.post(
            f"{url_base}/api/generate",
            json={"model": modelo, "prompt": prompt, "stream": False},
            timeout=120,
        )
        if resp.status_code == 200:
            return resp.json().get("response", "Sem resposta.")
        return f"Erro HTTP {resp.status_code}: {resp.text}"
    except requests.exceptions.ConnectionError:
        return "❌ Nao foi possivel conectar ao Ollama. Verifique se ele esta rodando (execute: ollama serve)"
    except requests.exceptions.Timeout:
        return "⏱️ Timeout: o modelo demorou mais de 2 minutos. Tente um prompt mais curto."
    except Exception as e:
        return f"❌ Erro inesperado: {str(e)}"

def salvar_resultado(trilha: str, desafio: str, prompt: str, resposta: str):
    """Salva resultado em arquivo txt na pasta output."""
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome = f"{ts}_{trilha}_{desafio[:20].replace(' ', '_')}.txt"
    path = output_dir / nome
    conteudo = f"""HACKATHON IA + SAUDE DIGITAL
Trilha: {trilha}
Desafio: {desafio}
Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M')}
{'='*60}

PROMPT:
{prompt}

{'='*60}

RESPOSTA DO MODELO:
{resposta}
"""
    path.write_text(conteudo, encoding="utf-8")
    return str(path)

# -------------------------------------------------------------------
# Sidebar
# -------------------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/hospital.png", width=60)
    st.title("⚙️ Configuracoes")
    st.divider()

    url_ollama = st.text_input(
        "URL do Ollama",
        value="http://localhost:11434",
        help="Padrao: http://localhost:11434",
    )
    modelo = st.selectbox(
        "Modelo",
        [
            "medgemma:4b",      # Especializado em saude
            "gemma4:e2b",       # Gemma 4 mais recente
        ],
        index=0,
        help="MedGemma: melhor para prompts clinicos. Gemma 4 E2B: melhor para produto/negocio.",
    )

    # Dica de qual modelo usar
    st.markdown("**💡 Qual modelo usar?**")
    st.markdown("""
    - 🏥 **MedGemma 4B** — Triagem, interconsulta, sintese clinica
    - 🎯 **Gemma 4 E2B** — No-show, UX, jornada paciente
    """)

    # Testar conexao
    if st.button("🔌 Testar Conexao", use_container_width=True):
        try:
            r = requests.get(f"{url_ollama}/api/tags", timeout=5)
            if r.status_code == 200:
                modelos_disponiveis = [m["name"] for m in r.json().get("models", [])]
                st.success(f"✅ Ollama conectado!")
                if modelos_disponiveis:
                    st.info("Modelos: " + ", ".join(modelos_disponiveis))
            else:
                st.error("Ollama respondeu com erro.")
        except Exception:
            st.error("❌ Ollama nao encontrado. Execute: ollama serve")

    st.divider()
    st.markdown("**⏱️ Agenda do Hackathon**")
    st.markdown("""
    | Horario | Atividade |
    |---------|-----------|
    | 0h00 | Abertura + Setup |
    | 0h30 | Exploracao livre |
    | 1h00 | Sprint solucao |
    | 2h30 | Construir pitch |
    | 3h30 | Apresentacoes |
    """)
    st.divider()
    st.caption("Hackathon IA + Saude Digital")
    st.caption("Powered by Gemma via Ollama")

# -------------------------------------------------------------------
# Header
# -------------------------------------------------------------------
st.title("🏥 Hackathon IA + Saude Digital")
st.markdown("**Explore como a Inteligencia Artificial pode transformar a saude digital**")
st.divider()

# -------------------------------------------------------------------
# Tabs principais
# -------------------------------------------------------------------
aba_eletiva, aba_interconsulta, aba_livre, aba_resultados = st.tabs([
    "🩺 Equipe TeleEletiva",
    "🔄 Equipe TeleInterconsulta",
    "✏️ Prompt Livre",
    "📁 Resultados Salvos",
])

# ===================================================================
# ABA: TELEELETIVA
# ===================================================================
with aba_eletiva:
    trilha = dados["trilhas"]["teleeletiva"]

    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("🩺 Teleconsulta Eletiva")
        st.markdown(f"*{trilha['descricao']}*")
    with col2:
        st.metric("Desafios disponíveis", len(trilha["desafios"]))

    st.divider()

    # Seletor de desafio
    opcoes_desafio = {d["titulo"]: d for d in trilha["desafios"]}
    desafio_nome = st.selectbox(
        "Escolha o desafio:",
        list(opcoes_desafio.keys()),
        key="sel_eletiva",
    )
    desafio = opcoes_desafio[desafio_nome]

    # Card do desafio
    with st.expander(f"📋 {desafio['id']} — Contexto do Desafio", expanded=True):
        st.markdown(f"**Problema:** {desafio['problema']}")
        st.markdown("**Metricas de sucesso:**")
        for m in desafio["metricas_alvo"]:
            st.markdown(f"  - {m}")
        st.markdown("**Perguntas-guia para reflexao:**")
        for p in desafio["perguntas_guia"]:
            st.markdown(f"  - _{p}_")

    st.subheader("💬 Testar com o Modelo")

    # Botoes de prompts prontos
    st.markdown("**Prompts prontos para comecar:**")
    cols = st.columns(len(desafio["prompts_exemplo"]))
    prompt_selecionado = st.session_state.get("prompt_eletiva", "")

    for i, exemplo in enumerate(desafio["prompts_exemplo"]):
        with cols[i]:
            if st.button(f"📝 {exemplo['nome']}", key=f"btn_eletiva_{i}", use_container_width=True):
                st.session_state["prompt_eletiva"] = exemplo["prompt"]
                st.rerun()

    # Area de prompt
    prompt_texto = st.text_area(
        "Prompt (edite livremente):",
        value=st.session_state.get("prompt_eletiva", ""),
        height=200,
        key="ta_eletiva",
        placeholder="Digite seu prompt aqui ou clique em um dos botoes acima para carregar um exemplo...",
    )

    col_btn1, col_btn2, col_espaco = st.columns([1, 1, 3])
    with col_btn1:
        executar = st.button("▶️ Executar", type="primary", key="exec_eletiva", use_container_width=True)
    with col_btn2:
        limpar = st.button("🗑️ Limpar", key="clear_eletiva", use_container_width=True)

    if limpar:
        st.session_state["prompt_eletiva"] = ""
        st.rerun()

    if executar and prompt_texto.strip():
        with st.spinner("🤖 Processando... (pode levar 15-30 segundos)"):
            inicio = time.time()
            resposta = chamar_ollama(prompt_texto, modelo, url_ollama)
            duracao = time.time() - inicio

        st.success(f"✅ Resposta gerada em {duracao:.1f}s")
        st.markdown("**Resposta do modelo:**")
        st.markdown(resposta)

        # Botao salvar
        if st.button("💾 Salvar resultado", key="save_eletiva"):
            path_salvo = salvar_resultado(
                "TeleEletiva", desafio_nome, prompt_texto, resposta
            )
            st.success(f"Salvo em: `{path_salvo}`")
    elif executar:
        st.warning("Digite ou selecione um prompt antes de executar.")

# ===================================================================
# ABA: TELEINTERCONSULTA
# ===================================================================
with aba_interconsulta:
    trilha_ti = dados["trilhas"]["teleinterconsulta"]

    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("🔄 Teleinterconsulta")
        st.markdown(f"*{trilha_ti['descricao']}*")
    with col2:
        st.metric("Desafios disponíveis", len(trilha_ti["desafios"]))

    st.divider()

    opcoes_ti = {d["titulo"]: d for d in trilha_ti["desafios"]}
    desafio_ti_nome = st.selectbox(
        "Escolha o desafio:",
        list(opcoes_ti.keys()),
        key="sel_interconsulta",
    )
    desafio_ti = opcoes_ti[desafio_ti_nome]

    with st.expander(f"📋 {desafio_ti['id']} — Contexto do Desafio", expanded=True):
        st.markdown(f"**Problema:** {desafio_ti['problema']}")
        st.markdown("**Metricas de sucesso:**")
        for m in desafio_ti["metricas_alvo"]:
            st.markdown(f"  - {m}")
        st.markdown("**Perguntas-guia para reflexao:**")
        for p in desafio_ti["perguntas_guia"]:
            st.markdown(f"  - _{p}_")

    st.subheader("💬 Testar com o Modelo")

    st.markdown("**Prompts prontos para comecar:**")
    cols_ti = st.columns(len(desafio_ti["prompts_exemplo"]))

    for i, exemplo in enumerate(desafio_ti["prompts_exemplo"]):
        with cols_ti[i]:
            if st.button(f"📝 {exemplo['nome']}", key=f"btn_ti_{i}", use_container_width=True):
                st.session_state["prompt_ti"] = exemplo["prompt"]
                st.rerun()

    prompt_ti = st.text_area(
        "Prompt (edite livremente):",
        value=st.session_state.get("prompt_ti", ""),
        height=200,
        key="ta_ti",
        placeholder="Digite seu prompt aqui ou clique em um dos botoes acima...",
    )

    col_btn_ti1, col_btn_ti2, _ = st.columns([1, 1, 3])
    with col_btn_ti1:
        executar_ti = st.button("▶️ Executar", type="primary", key="exec_ti", use_container_width=True)
    with col_btn_ti2:
        limpar_ti = st.button("🗑️ Limpar", key="clear_ti", use_container_width=True)

    if limpar_ti:
        st.session_state["prompt_ti"] = ""
        st.rerun()

    if executar_ti and prompt_ti.strip():
        with st.spinner("🤖 Processando... (pode levar 15-30 segundos)"):
            inicio_ti = time.time()
            resposta_ti = chamar_ollama(prompt_ti, modelo, url_ollama)
            duracao_ti = time.time() - inicio_ti

        st.success(f"✅ Resposta gerada em {duracao_ti:.1f}s")
        st.markdown("**Resposta do modelo:**")
        st.markdown(resposta_ti)

        if st.button("💾 Salvar resultado", key="save_ti"):
            path_salvo_ti = salvar_resultado(
                "TeleInterconsulta", desafio_ti_nome, prompt_ti, resposta_ti
            )
            st.success(f"Salvo em: `{path_salvo_ti}`")
    elif executar_ti:
        st.warning("Digite ou selecione um prompt antes de executar.")

# ===================================================================
# ABA: PROMPT LIVRE
# ===================================================================
with aba_livre:
    st.header("✏️ Prompt Livre")
    st.markdown("Explore qualquer ideia sem restricao de template.")

    prompt_livre = st.text_area(
        "Seu prompt:",
        height=250,
        key="ta_livre",
        placeholder="Exemplo: 'Quais sao as 5 principais causas de atraso em teleconsultas eletivas e como a IA pode resolver cada uma?'",
    )

    col_livre1, col_livre2, _ = st.columns([1, 1, 3])
    with col_livre1:
        exec_livre = st.button("▶️ Executar", type="primary", key="exec_livre", use_container_width=True)
    with col_livre2:
        limpar_livre = st.button("🗑️ Limpar", key="clear_livre", use_container_width=True)

    if limpar_livre:
        st.session_state["ta_livre"] = ""
        st.rerun()

    if exec_livre and prompt_livre.strip():
        with st.spinner("🤖 Processando..."):
            inicio_l = time.time()
            resp_livre = chamar_ollama(prompt_livre, modelo, url_ollama)
            dur_livre = time.time() - inicio_l
        st.success(f"✅ Resposta em {dur_livre:.1f}s")
        st.markdown(resp_livre)

        if st.button("💾 Salvar", key="save_livre"):
            p = salvar_resultado("Livre", "prompt-livre", prompt_livre, resp_livre)
            st.success(f"Salvo em: `{p}`")
    elif exec_livre:
        st.warning("Digite um prompt antes de executar.")

# ===================================================================
# ABA: RESULTADOS SALVOS
# ===================================================================
with aba_resultados:
    st.header("📁 Resultados Salvos")
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)

    arquivos = sorted(output_dir.glob("*.txt"), reverse=True)

    if not arquivos:
        st.info("Nenhum resultado salvo ainda. Execute um prompt e clique em 'Salvar resultado'.")
    else:
        st.metric("Total de resultados", len(arquivos))
        for arq in arquivos:
            with st.expander(f"📄 {arq.name}"):
                st.text(arq.read_text(encoding="utf-8"))
                st.download_button(
                    "⬇️ Baixar",
                    data=arq.read_bytes(),
                    file_name=arq.name,
                    key=f"dl_{arq.name}",
                )
