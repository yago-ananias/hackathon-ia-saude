"""
HACKATHON IA + SAUDE DIGITAL
App Streamlit para explorar prompts com modelos locais (Ollama).
Trilhas: Teleconsulta Eletiva | Teleinterconsulta

Recursos:
- Persona (system prompt) e temperatura ajustaveis na barra lateral
- Lista de modelos detectada automaticamente do Ollama
- Metricas de velocidade (tokens/s) a cada resposta
- Comparacao lado a lado de 2 modelos no mesmo prompt
- Chat multi-turn para ensinar refino iterativo de prompt
- Resultados salvos de forma persistente (corrige bug do salvar)
"""

import sys
import json
import time
import tempfile
import requests
import pandas as pd
import streamlit as st
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).parent
OUTPUT_DIR = BASE / "output"
DADOS_DIR = BASE / "dados"

# Transcricao de audio (opcional) - so ativa se faster-whisper estiver instalado
try:
    from faster_whisper import WhisperModel
    WHISPER_OK = True
except Exception:
    WHISPER_OK = False

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
# Personas (system prompts) - melhoram MUITO modelos pequenos
# -------------------------------------------------------------------
PERSONAS = {
    "Nenhuma (prompt cru)": "",
    "Especialista clinico (saude)": (
        "Voce e um medico especialista senior em telessaude no Brasil. "
        "Responda com rigor clinico, linguagem tecnica precisa e seguranca do paciente em primeiro lugar. "
        "Quando faltar informacao, diga o que falta em vez de assumir. "
        "Nunca invente diagnostico definitivo sem dados suficientes. Responda sempre em portugues do Brasil."
    ),
    "Gestor de produto (growth/negocio)": (
        "Voce e um gestor de produto senior em saude digital em uma operadora de saude no Brasil. "
        "Conecte cada analise a uma decisao de negocio. Diferencie metrica operacional de desfecho clinico. "
        "Seja objetivo, pratico e executivo. Considere experiencia do paciente, eficiencia operacional e "
        "sustentabilidade economica. Responda sempre em portugues do Brasil."
    ),
    "Facilitador didatico (explica simples)": (
        "Voce e um facilitador que explica IA de forma simples para um time multidisciplinar de saude. "
        "Use linguagem clara, exemplos do dia a dia e evite jargao desnecessario. Responda em portugues do Brasil."
    ),
}

FALLBACK_MODELOS = ["medgemma:4b", "gemma4:e4b-it-qat"]

# -------------------------------------------------------------------
# Dados (prompts e desafios)
# -------------------------------------------------------------------
@st.cache_data
def carregar_prompts():
    with open(BASE / "exemplos_prompts.json", "r", encoding="utf-8") as f:
        return json.load(f)

dados = carregar_prompts()


@st.cache_data
def carregar_csv(nome: str):
    """Carrega um CSV da pasta dados/. Retorna None se nao existir."""
    caminho = DADOS_DIR / nome
    if caminho.exists():
        return pd.read_csv(caminho)
    return None


def taxa_noshow_por(df, coluna):
    """Serie com a taxa de no-show (%) por categoria de uma coluna."""
    return (df.groupby(coluna)["compareceu"]
              .apply(lambda s: round((s == "nao").mean() * 100, 1))
              .sort_values(ascending=False))


@st.cache_resource
def carregar_whisper(tamanho: str = "base"):
    """Carrega o modelo Whisper (cacheado). int8 para rodar leve em CPU."""
    return WhisperModel(tamanho, device="cpu", compute_type="int8")

# -------------------------------------------------------------------
# Integracao com Ollama
# -------------------------------------------------------------------
# recomendados aparecem primeiro; e2b mantidos p/ quem instalou com o guia antigo
PREFERENCIA = ["medgemma:4b", "gemma4:e4b-it-qat", "gemma4:e2b-it-qat", "gemma4:e2b"]


def listar_modelos(url_base: str):
    """Detecta modelos instalados no Ollama (recomendados primeiro). Fallback se offline."""
    try:
        r = requests.get(f"{url_base}/api/tags", timeout=5)
        if r.status_code == 200:
            nomes = [m["name"] for m in r.json().get("models", [])]
            if nomes:
                return sorted(
                    nomes,
                    key=lambda n: (PREFERENCIA.index(n) if n in PREFERENCIA else len(PREFERENCIA), n),
                )
    except Exception:
        pass
    return FALLBACK_MODELOS


def _metricas(chunk_final: dict, segundos: float) -> str:
    """Monta string de metricas a partir do chunk final do Ollama."""
    eval_count = chunk_final.get("eval_count")
    eval_dur = chunk_final.get("eval_duration")  # nanosegundos
    if eval_count and eval_dur:
        tok_s = eval_count / (eval_dur / 1e9)
        return f"{eval_count} tokens · {tok_s:.0f} tok/s · {segundos:.1f}s"
    return f"{segundos:.1f}s"


def gerar_stream(prompt: str, modelo: str, url_base: str, system: str = "",
                 temperatura: float = 0.7, placeholder=None):
    """Gera resposta via /api/generate com streaming. Retorna (texto, metricas)."""
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": True,
        "options": {"temperature": temperatura},
    }
    if system:
        payload["system"] = system
    return _consumir_stream(f"{url_base}/api/generate", payload, placeholder, "response")


def chat_stream(mensagens: list, modelo: str, url_base: str,
                temperatura: float = 0.7, placeholder=None):
    """Gera resposta multi-turn via /api/chat com streaming. Retorna (texto, metricas)."""
    payload = {
        "model": modelo,
        "messages": mensagens,
        "stream": True,
        "options": {"temperature": temperatura},
    }
    return _consumir_stream(f"{url_base}/api/chat", payload, placeholder, "chat")


def _consumir_stream(endpoint: str, payload: dict, placeholder, modo: str):
    """Consome o stream do Ollama e devolve (texto, metricas). modo: 'response' ou 'chat'."""
    inicio = time.time()
    try:
        with requests.post(endpoint, json=payload, timeout=(10, 600), stream=True) as resp:
            if resp.status_code != 200:
                return f"❌ Erro HTTP {resp.status_code}: {resp.text}", ""
            texto = ""
            chunk_final = {}
            for linha in resp.iter_lines():
                if not linha:
                    continue
                try:
                    chunk = json.loads(linha.decode("utf-8"))
                except json.JSONDecodeError:
                    continue
                if modo == "chat":
                    parte = chunk.get("message", {}).get("content", "")
                else:
                    parte = chunk.get("response", "")
                texto += parte
                if placeholder is not None:
                    placeholder.markdown(texto + " ▌")
                if chunk.get("done"):
                    chunk_final = chunk
                    break
            if placeholder is not None:
                placeholder.empty()
            metr = _metricas(chunk_final, time.time() - inicio)
            return (texto if texto else "Sem resposta."), metr
    except requests.exceptions.ConnectionError:
        return "❌ Nao foi possivel conectar ao Ollama. Verifique se ele esta rodando (ollama serve).", ""
    except requests.exceptions.Timeout:
        return "⏱️ Timeout: modelo demorou demais. Tente um prompt mais curto ou o MedGemma 4B (mais rapido).", ""
    except Exception as e:
        return f"❌ Erro inesperado: {str(e)}", ""


def salvar_resultado(trilha: str, desafio: str, prompt: str, resposta: str,
                     modelo: str = "", system: str = "", metricas: str = "") -> str:
    """Salva resultado em arquivo txt na pasta output."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome = f"{ts}_{trilha}_{desafio[:20].replace(' ', '_')}.txt"
    path = OUTPUT_DIR / nome
    conteudo = f"""HACKATHON IA + SAUDE DIGITAL
Trilha: {trilha}
Desafio: {desafio}
Modelo: {modelo}
Persona: {system[:80] + '...' if system else 'nenhuma'}
Metricas: {metricas}
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


def prompt_autoavaliacao(prompt_original: str, resposta: str) -> str:
    """Monta um prompt que pede ao modelo para avaliar a resposta pela rubrica do hackathon."""
    criterios = dados["config"].get("avaliacao", [])
    linhas_crit = "\n".join(
        f"- {c['criterio']} (peso {c['peso']}): {c['o_que_avaliar']}" for c in criterios
    )
    return (
        "Voce e um jurado de hackathon de saude digital. Avalie a RESPOSTA abaixo segundo a rubrica.\n"
        "Para cada criterio, de uma nota de 0 a 10 e uma justificativa de 1 linha. "
        "No final, calcule a nota ponderada (0 a 10) e aponte a MELHORIA mais importante.\n\n"
        f"RUBRICA:\n{linhas_crit}\n\n"
        f"PROMPT QUE GEROU A RESPOSTA:\n{prompt_original}\n\n"
        f"RESPOSTA A AVALIAR:\n{resposta}\n\n"
        "Formato: tabela com Criterio | Nota | Justificativa, depois 'Nota final: X/10' e 'Melhoria prioritaria: ...'."
    )


def prompt_pitch(blocos: list, trilha: str, desafio: str) -> str:
    """Monta um prompt para gerar o esqueleto do pitch a partir de respostas salvas."""
    material = "\n\n---\n\n".join(blocos)
    return (
        "Voce e um mentor de pitch. Com base no material de trabalho abaixo (respostas que a equipe "
        f"gerou para o desafio '{desafio}' da trilha '{trilha}'), monte o ESQUELETO de um pitch de 15 min.\n\n"
        "Estruture exatamente nestas secoes, objetivo e pronto para apresentar:\n"
        "1. Problema (a dor e a magnitude)\n"
        "2. Solucao com IA (como funciona)\n"
        "3. Dados e metricas (o que muda e como medir)\n"
        "4. Riscos e mitigacoes (1 risco assistencial)\n"
        "5. Proximos passos (o que fazer em 30 dias)\n"
        "Use bullets curtos. Seja concreto e executivo.\n\n"
        f"MATERIAL DE TRABALHO DA EQUIPE:\n{material}"
    )


# -------------------------------------------------------------------
# Callbacks (forma correta de mexer em session_state sem erro)
# -------------------------------------------------------------------
def carregar_exemplo(chave_widget: str, texto: str):
    st.session_state[chave_widget] = texto


def limpar_campo(chave_widget: str):
    st.session_state[chave_widget] = ""


# -------------------------------------------------------------------
# Sidebar
# -------------------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/hospital.png", width=60)
    st.title("⚙️ Configuracoes")
    st.divider()

    url_ollama = st.text_input("URL do Ollama", value="http://localhost:11434")

    modelos_instalados = listar_modelos(url_ollama)
    modelo = st.selectbox(
        "Modelo",
        modelos_instalados,
        index=0,
        help="Lista detectada automaticamente do seu Ollama.",
    )

    if "1.5" in modelo:
        st.caption("⚠️ A MedGemma 1.5 expoe o raciocinio (em ingles) antes da resposta final. "
                   "Boa para ver como a IA 'pensa'; para respostas limpas, use a medgemma:4b.")

    persona_nome = st.selectbox(
        "Persona (system prompt)",
        list(PERSONAS.keys()),
        index=1,
        help="A persona orienta o tom e o foco. Modelos pequenos respondem MUITO melhor com persona.",
    )
    system_prompt = PERSONAS[persona_nome]

    temperatura = st.slider(
        "Temperatura", 0.0, 1.0, 0.7, 0.1,
        help="Baixa (0.0-0.3) = preciso e factual. Alta (0.7-1.0) = criativo e variado.",
    )

    if st.button("🔌 Testar Conexao", use_container_width=True):
        try:
            r = requests.get(f"{url_ollama}/api/tags", timeout=5)
            if r.status_code == 200:
                nomes = [m["name"] for m in r.json().get("models", [])]
                st.success("✅ Ollama conectado!")
                st.info("Modelos: " + (", ".join(nomes) if nomes else "nenhum baixado"))
            else:
                st.error("Ollama respondeu com erro.")
        except Exception:
            st.error("❌ Ollama nao encontrado. Execute: ollama serve")

    st.divider()
    st.markdown("**💡 Qual modelo usar?**")
    st.markdown("- 🏥 **MedGemma** - triagem, interconsulta, clinica\n- 🎯 **Gemma 4** - no-show, UX, negocio")
    st.divider()
    st.caption("Hackathon IA + Saude Digital · Gemma/MedGemma via Ollama")

# -------------------------------------------------------------------
# Header
# -------------------------------------------------------------------
st.title("🏥 Hackathon IA + Saude Digital")
st.markdown("**Explore como a Inteligencia Artificial pode transformar a saude digital**")
st.caption(f"Modelo ativo: `{modelo}`  ·  Persona: _{persona_nome}_  ·  Temperatura: {temperatura}")
st.divider()

# -------------------------------------------------------------------
# Bloco reutilizavel: exibe resposta persistida + botao salvar
# (corrige o bug do salvar - resposta vive no session_state)
# -------------------------------------------------------------------
def render_resposta(chave: str, trilha_label: str, desafio_label: str):
    """Renderiza a ultima resposta guardada para 'chave' e oferece salvar."""
    res = st.session_state.get(f"resp_{chave}")
    if not res:
        return
    st.markdown("**Resposta do modelo:**")
    st.markdown(res["resposta"])
    if res.get("metricas"):
        st.caption(f"⚡ {res['metricas']}  ·  modelo: `{res['modelo']}`")

    cbs1, cbs2, _ = st.columns([1.2, 1.6, 2])
    with cbs1:
        salvar = st.button("💾 Salvar", key=f"save_{chave}", use_container_width=True)
    with cbs2:
        avaliar = st.button("🧮 Autoavaliar pela rubrica", key=f"aval_{chave}", use_container_width=True)

    if salvar:
        p = salvar_resultado(
            trilha_label, desafio_label, res["prompt"], res["resposta"],
            res.get("modelo", ""), res.get("system", ""), res.get("metricas", ""),
        )
        st.success(f"Salvo em: `{p}`")

    if avaliar:
        st.markdown("**🧮 Autoavaliacao pela rubrica do hackathon:**")
        ph = st.empty()
        ph.info("Avaliando...")
        pa = prompt_autoavaliacao(res["prompt"], res["resposta"])
        texto_av, _ = gerar_stream(pa, modelo, url_ollama, system_prompt, 0.2, ph)
        ph.markdown(texto_av)


def executar_e_guardar(chave: str, prompt: str, modelo: str, system: str,
                       temperatura: float, url: str):
    """Executa com streaming e guarda no session_state (persiste entre reruns)."""
    st.markdown("**Resposta do modelo:**")
    placeholder = st.empty()
    placeholder.info("🤖 Gerando resposta...")
    texto, metr = gerar_stream(prompt, modelo, url, system, temperatura, placeholder)
    st.session_state[f"resp_{chave}"] = {
        "prompt": prompt, "resposta": texto, "modelo": modelo,
        "system": system, "metricas": metr,
    }


# -------------------------------------------------------------------
# Painel reutilizavel de trilha (mata a duplicacao de codigo)
# -------------------------------------------------------------------
def painel_trilha(chave_trilha: str, trilha_label: str):
    trilha = dados["trilhas"][chave_trilha]

    col1, col2 = st.columns([3, 1])
    with col1:
        st.header(trilha["nome"])
        st.markdown(f"*{trilha['descricao']}*")
    with col2:
        st.metric("Desafios", len(trilha["desafios"]))

    st.divider()

    opcoes = {f"{d['id']} — {d['titulo']}": d for d in trilha["desafios"]}
    desafio_nome = st.selectbox("Escolha o desafio:", list(opcoes.keys()), key=f"sel_{chave_trilha}")
    desafio = opcoes[desafio_nome]

    with st.expander(f"📋 {desafio['id']} — Contexto do Desafio", expanded=True):
        st.markdown(f"**Problema:** {desafio['problema']}")
        st.markdown("**Metricas-alvo:** " + ", ".join(desafio["metricas_alvo"]))
        st.markdown("**Perguntas-guia:**")
        for p in desafio["perguntas_guia"]:
            st.markdown(f"  - _{p}_")

    st.subheader("💬 Testar com o Modelo")
    st.markdown("**Prompts prontos (clique para carregar):**")
    chave_widget = f"ta_{chave_trilha}"
    cols = st.columns(len(desafio["prompts_exemplo"]))
    for i, exemplo in enumerate(desafio["prompts_exemplo"]):
        with cols[i]:
            st.button(
                f"📝 {exemplo['nome']}",
                key=f"btn_{chave_trilha}_{i}",
                use_container_width=True,
                on_click=carregar_exemplo,
                args=(chave_widget, exemplo["prompt"]),
            )

    prompt_texto = st.text_area(
        "Prompt (edite livremente):",
        height=200,
        key=chave_widget,
        placeholder="Digite seu prompt ou clique em um exemplo acima...",
    )

    c1, c2, c3, _ = st.columns([1.2, 1.6, 1, 2])
    with c1:
        executar = st.button("▶️ Executar", type="primary", key=f"exec_{chave_trilha}", use_container_width=True)
    with c2:
        comparar = st.button("⚖️ Comparar 2 modelos", key=f"cmp_{chave_trilha}", use_container_width=True)
    with c3:
        st.button("🗑️ Limpar", key=f"clr_{chave_trilha}", use_container_width=True,
                  on_click=limpar_campo, args=(chave_widget,))

    if comparar and prompt_texto.strip():
        comparar_modelos(prompt_texto, modelos_instalados, system_prompt, temperatura, url_ollama)
    elif executar and prompt_texto.strip():
        executar_e_guardar(chave_trilha, prompt_texto, modelo, system_prompt, temperatura, url_ollama)
    elif (executar or comparar):
        st.warning("Digite ou selecione um prompt antes de executar.")

    render_resposta(chave_trilha, trilha_label, desafio_nome)


# -------------------------------------------------------------------
# Comparacao lado a lado de 2 modelos
# -------------------------------------------------------------------
def comparar_modelos(prompt: str, modelos: list, system: str, temperatura: float, url: str):
    st.markdown("### ⚖️ Comparacao lado a lado")
    if len(modelos) < 2:
        st.warning("Voce precisa de pelo menos 2 modelos instalados para comparar.")
        return
    m_a, m_b = modelos[0], modelos[1]
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"#### 🅰️ `{m_a}`")
        ph_a = st.empty()
        ph_a.info("Gerando...")
        txt_a, met_a = gerar_stream(prompt, m_a, url, system, temperatura, ph_a)
        ph_a.markdown(txt_a)
        st.caption(f"⚡ {met_a}")
    with col_b:
        st.markdown(f"#### 🅱️ `{m_b}`")
        ph_b = st.empty()
        ph_b.info("Gerando...")
        txt_b, met_b = gerar_stream(prompt, m_b, url, system, temperatura, ph_b)
        ph_b.markdown(txt_b)
        st.caption(f"⚡ {met_b}")
    st.info("💡 Compare: qual respondeu melhor para ESTE tipo de tarefa? Clinico tende a ir melhor no MedGemma; negocio/UX no Gemma 4.")


# ===================================================================
# Tabs principais
# ===================================================================
aba_eletiva, aba_ti, aba_dados, aba_voz, aba_chat, aba_livre, aba_result = st.tabs([
    "🩺 TeleEletiva",
    "🔄 TeleInterconsulta",
    "📊 Dados",
    "🎙️ Transcricao",
    "💬 Chat / Refino",
    "✏️ Prompt Livre",
    "📁 Resultados",
])

with aba_eletiva:
    painel_trilha("teleeletiva", "TeleEletiva")

with aba_ti:
    painel_trilha("teleinterconsulta", "TeleInterconsulta")

# ----------------------------- DADOS SINTETICOS -----------------------------
with aba_dados:
    st.header("📊 Dados Sinteticos (ficticios)")
    st.markdown(
        "Dados **ficticios** para vocês testarem ideias com matéria-prima realista. "
        "Selecione um registro, gere o prompt automatico e veja o que o modelo faz com **dado**, não só texto solto."
    )
    st.caption("Nenhum dado real de paciente. Gerados por regras em `dados/gerar_dados_sinteticos.py`.")

    sub_ag, sub_fila, sub_an = st.tabs([
        "🩺 Agendamentos (no-show)",
        "🔄 Fila de Interconsulta (priorizacao)",
        "📈 Analytics no-show",
    ])

    # ---- Agendamentos / no-show ----
    with sub_ag:
        df_ag = carregar_csv("agendamentos.csv")
        if df_ag is None:
            st.warning("Arquivo `dados/agendamentos.csv` nao encontrado. "
                       "Rode: `python dados/gerar_dados_sinteticos.py`")
        else:
            taxa = (df_ag["compareceu"] == "nao").mean() * 100
            c1, c2 = st.columns(2)
            c1.metric("Total de agendamentos", len(df_ag))
            c2.metric("Taxa de no-show", f"{taxa:.0f}%")
            st.dataframe(df_ag, use_container_width=True, height=240)

            pid = st.selectbox("Selecione um paciente:", df_ag["id_paciente"].tolist(), key="sel_ag")
            reg = df_ag[df_ag["id_paciente"] == pid].iloc[0]
            prompt_ag = (
                "Voce e especialista em experiencia do paciente em telessaude. "
                "Analise o agendamento abaixo e classifique o RISCO de no-show (alto/medio/baixo) "
                "com justificativa, e sugira 2 acoes preventivas personalizadas.\n\n"
                f"- Idade: {reg['idade']} | Sexo: {reg['sexo']}\n"
                f"- Especialidade: {reg['especialidade']} | Tipo: {reg['tipo_consulta']}\n"
                f"- Antecedencia do agendamento: {reg['dias_antecedencia']} dias\n"
                f"- Canal preferido: {reg['canal_preferido']}\n"
                f"- No-shows nos ultimos 6 meses: {reg['historico_noshow_6m']}\n"
                f"- Regiao: {reg['regiao']} | Periodo: {reg['periodo']} | Confirmou: {reg['confirmou_presenca']}"
            )
            st.code(prompt_ag, language="text")
            if st.button("▶️ Analisar este paciente", type="primary", key="run_ag"):
                executar_e_guardar("dados_ag", prompt_ag, modelo, system_prompt, temperatura, url_ollama)
            render_resposta("dados_ag", "Dados-NoShow", f"paciente-{pid}")
            st.info(f"💡 Dica: o gabarito real deste paciente e **compareceu = {reg['compareceu']}**. "
                    "A previsao do modelo bateu com a realidade?")

    # ---- Fila de interconsulta / priorizacao ----
    with sub_fila:
        df_f = carregar_csv("fila_interconsulta.csv")
        if df_f is None:
            st.warning("Arquivo `dados/fila_interconsulta.csv` nao encontrado. "
                       "Rode: `python dados/gerar_dados_sinteticos.py`")
        else:
            urg = (df_f["urgencia_real"] == "urgente").sum()
            c1, c2 = st.columns(2)
            c1.metric("Pedidos na fila", len(df_f))
            c2.metric("Casos urgentes", int(urg))
            st.dataframe(df_f, use_container_width=True, height=240)

            n = st.slider("Quantos pedidos enviar para priorizacao:", 3, 10, 5, key="sl_fila")
            amostra = df_f.head(n)
            blocos = []
            for _, r in amostra.iterrows():
                blocos.append(
                    f"[{r['id_pedido']}] {r['especialidade']} - idade {r['idade_paciente']} - "
                    f"espera {r['tempo_espera_horas']}h - alarme: {r['sinais_alarme']}\n"
                    f"Resumo: {r['resumo_clinico']}"
                )
            prompt_fila = (
                "Voce e um sistema de triagem de teleinterconsultas. Ordene os pedidos abaixo por "
                "PRIORIDADE CLINICA (1 = mais urgente), justificando cada decisao em 1 linha.\n\n"
                + "\n\n".join(blocos)
            )
            st.code(prompt_fila, language="text")
            if st.button("▶️ Priorizar esta fila", type="primary", key="run_fila"):
                executar_e_guardar("dados_fila", prompt_fila, modelo, system_prompt, temperatura, url_ollama)
            render_resposta("dados_fila", "Dados-Fila", f"fila-{n}-pedidos")
            with st.expander("👁️ Ver gabarito (urgencia_real) para comparar"):
                st.dataframe(amostra[["id_pedido", "especialidade", "urgencia_real"]],
                             use_container_width=True)

    # ---- Analytics de no-show ----
    with sub_an:
        df_a = carregar_csv("agendamentos.csv")
        if df_a is None:
            st.warning("Arquivo `dados/agendamentos.csv` nao encontrado. "
                       "Rode: `python dados/gerar_dados_sinteticos.py`")
        else:
            df_a = df_a.copy()
            df_a["faixa_antecedencia"] = pd.cut(
                df_a["dias_antecedencia"], bins=[0, 3, 10, 100],
                labels=["1-3 dias", "4-10 dias", "11+ dias"],
            )
            geral = (df_a["compareceu"] == "nao").mean() * 100
            st.metric("Taxa de no-show geral", f"{geral:.1f}%")
            st.markdown("**Qual fator mais prediz o no-show?** Compare a taxa por categoria:")

            fatores = {
                "confirmou_presenca": "Confirmou presenca?",
                "historico_noshow_6m": "Historico de no-show (6m)",
                "tipo_consulta": "Tipo de consulta",
                "regiao": "Regiao",
            }
            col_e, col_d = st.columns(2)
            for i, (col, titulo) in enumerate(fatores.items()):
                serie = taxa_noshow_por(df_a, col)
                alvo = col_e if i % 2 == 0 else col_d
                with alvo:
                    st.markdown(f"**{titulo}**")
                    st.bar_chart(serie, height=200, color="#005DA0")

            st.info("💡 Para o time TeleEletiva: estes sao os fatores que a IA poderia usar "
                    "para priorizar quem recebe lembrete/confirmacao ativa. O maior preditor costuma "
                    "ser o historico de no-show e a falta de confirmacao.")

# ----------------------------- TRANSCRICAO (VOZ) -----------------------------
with aba_voz:
    st.header("🎙️ Transcricao de Teleconsulta")
    st.markdown(
        "Suba o **audio** de uma consulta (ficticia!) e a IA transcreve e gera uma **nota clinica**. "
        "Fluxo: audio → Whisper (transcricao) → MedGemma (resumo estruturado)."
    )
    st.caption("Tudo roda local. Use apenas audios ficticios/de teste - nunca audio real de paciente.")

    if not WHISPER_OK:
        st.warning(
            "Capacidade de transcricao **nao instalada**. Para ativar, rode no terminal:\n\n"
            "```\npip install faster-whisper\n```\n\n"
            "Depois reinicie o app. O modelo Whisper (~150 MB) baixa sozinho no primeiro uso."
        )
    else:
        col_u, col_t = st.columns([3, 1])
        with col_u:
            audio = st.file_uploader("Audio da consulta", type=["wav", "mp3", "m4a", "ogg", "flac"])
        with col_t:
            tam = st.selectbox("Modelo Whisper", ["base", "small"], index=0,
                               help="base = rapido. small = mais preciso, mais lento.")

        if audio is not None:
            st.audio(audio)
            if st.button("📝 Transcrever", type="primary", key="run_voz"):
                with tempfile.NamedTemporaryFile(delete=False, suffix=Path(audio.name).suffix) as tmp:
                    tmp.write(audio.getvalue())
                    caminho_tmp = tmp.name
                with st.spinner(f"Transcrevendo com Whisper {tam} (pode levar 1-3 min em CPU)..."):
                    modelo_w = carregar_whisper(tam)
                    segmentos, info = modelo_w.transcribe(caminho_tmp, language="pt")
                    texto_trans = " ".join(s.text.strip() for s in segmentos).strip()
                st.session_state["transcricao"] = texto_trans
                st.success(f"Transcricao concluida (idioma detectado: {info.language}).")

        if st.session_state.get("transcricao"):
            st.markdown("**Transcricao:**")
            st.text_area("Texto transcrito (edite se quiser):", key="transcricao", height=160)
            if st.button("🩺 Gerar nota clinica (MedGemma)", key="resumo_voz"):
                pr = (
                    "Voce e um assistente clinico. A partir da transcricao de uma teleconsulta abaixo, "
                    "gere uma NOTA CLINICA estruturada em: 1) Queixa principal, 2) Historia da doenca atual, "
                    "3) Hipoteses, 4) Conduta sugerida, 5) Retorno. Use linguagem tecnica e concisa. "
                    "Se faltar informacao, registre 'nao informado'.\n\n"
                    f"TRANSCRICAO:\n{st.session_state['transcricao']}"
                )
                st.markdown("**Nota clinica:**")
                ph_v = st.empty()
                ph_v.info("Gerando nota...")
                txt_v, _ = gerar_stream(pr, modelo, url_ollama, system_prompt, 0.3, ph_v)
                ph_v.markdown(txt_v)

# ----------------------------- CHAT / MULTI-TURN -----------------------------
with aba_chat:
    st.header("💬 Chat / Refino Iterativo")
    st.markdown(
        "Aqui a IA **lembra do que ja foi dito**. Use para refinar: peca uma resposta, "
        "depois diga *'deixe mais curto'*, *'e se o paciente for idoso?'*, *'transforme em checklist'*. "
        "Iterar e a habilidade central de usar IA."
    )

    if "chat_msgs" not in st.session_state:
        st.session_state["chat_msgs"] = []

    col_lim, _ = st.columns([1, 4])
    with col_lim:
        if st.button("🗑️ Nova conversa", use_container_width=True):
            st.session_state["chat_msgs"] = []
            st.rerun()

    # Render historico
    for msg in st.session_state["chat_msgs"]:
        with st.chat_message("user" if msg["role"] == "user" else "assistant"):
            st.markdown(msg["content"])

    entrada = st.chat_input("Escreva sua mensagem para a IA...")
    if entrada:
        st.session_state["chat_msgs"].append({"role": "user", "content": entrada})
        with st.chat_message("user"):
            st.markdown(entrada)
        # monta mensagens com system na frente
        mensagens = []
        if system_prompt:
            mensagens.append({"role": "system", "content": system_prompt})
        mensagens.extend(st.session_state["chat_msgs"])
        with st.chat_message("assistant"):
            ph = st.empty()
            ph.info("🤖 Pensando...")
            texto, metr = chat_stream(mensagens, modelo, url_ollama, temperatura, ph)
            ph.markdown(texto)
            if metr:
                st.caption(f"⚡ {metr}  ·  modelo: `{modelo}`")
        st.session_state["chat_msgs"].append({"role": "assistant", "content": texto})

# ----------------------------- PROMPT LIVRE -----------------------------
with aba_livre:
    st.header("✏️ Prompt Livre")
    st.markdown("Explore qualquer ideia sem template. Persona e temperatura da barra lateral se aplicam.")

    st.text_area(
        "Seu prompt:",
        height=220,
        key="ta_livre",
        placeholder="Ex: 'Liste 5 causas de atraso em teleconsultas e como a IA resolve cada uma.'",
    )

    cL1, cL2, cL3, _ = st.columns([1.2, 1.6, 1, 2])
    with cL1:
        exec_livre = st.button("▶️ Executar", type="primary", key="exec_livre", use_container_width=True)
    with cL2:
        cmp_livre = st.button("⚖️ Comparar 2 modelos", key="cmp_livre", use_container_width=True)
    with cL3:
        st.button("🗑️ Limpar", key="clr_livre", use_container_width=True,
                  on_click=limpar_campo, args=("ta_livre",))

    prompt_livre = st.session_state.get("ta_livre", "")
    if cmp_livre and prompt_livre.strip():
        comparar_modelos(prompt_livre, modelos_instalados, system_prompt, temperatura, url_ollama)
    elif exec_livre and prompt_livre.strip():
        executar_e_guardar("livre", prompt_livre, modelo, system_prompt, temperatura, url_ollama)
    elif (exec_livre or cmp_livre):
        st.warning("Digite um prompt antes de executar.")

    render_resposta("livre", "Livre", "prompt-livre")

# ----------------------------- RESULTADOS -----------------------------
with aba_result:
    st.header("📁 Resultados Salvos")
    OUTPUT_DIR.mkdir(exist_ok=True)
    arquivos = sorted(OUTPUT_DIR.glob("*.txt"), reverse=True)
    if not arquivos:
        st.info("Nenhum resultado salvo ainda. Execute um prompt e clique em 'Salvar resultado'.")
    else:
        st.metric("Total de resultados", len(arquivos))

        # ---- Gerador de pitch ----
        with st.expander("🎤 Gerar esqueleto de PITCH a partir dos resultados", expanded=True):
            st.markdown("Selecione 1+ resultados que a equipe quer transformar em apresentacao.")
            escolha = st.multiselect("Resultados:", [a.name for a in arquivos],
                                     default=[arquivos[0].name], key="ms_pitch")
            cpa, cpb = st.columns(2)
            trilha_p = cpa.text_input("Trilha", value="TeleEletiva", key="pitch_trilha")
            desafio_p = cpb.text_input("Desafio", value="", key="pitch_desafio",
                                       placeholder="ex: Reduzir No-Show")
            if st.button("🎤 Gerar pitch", type="primary", key="run_pitch"):
                if not escolha:
                    st.warning("Selecione pelo menos um resultado.")
                else:
                    blocos = [(OUTPUT_DIR / nome).read_text(encoding="utf-8") for nome in escolha]
                    pp = prompt_pitch(blocos, trilha_p, desafio_p or "(desafio)")
                    st.markdown("**Esqueleto do pitch:**")
                    ph_pitch = st.empty()
                    ph_pitch.info("Montando pitch...")
                    texto_p, _ = gerar_stream(pp, modelo, url_ollama, system_prompt, 0.5, ph_pitch)
                    ph_pitch.markdown(texto_p)
                    st.download_button("⬇️ Baixar pitch (.md)", data=texto_p,
                                       file_name="pitch_esqueleto.md", key="dl_pitch")

        st.divider()
        for arq in arquivos:
            with st.expander(f"📄 {arq.name}"):
                st.text(arq.read_text(encoding="utf-8"))
                st.download_button("⬇️ Baixar", data=arq.read_bytes(),
                                   file_name=arq.name, key=f"dl_{arq.name}")
