# 🏥 Hackathon IA + Saúde Digital

> **Teleconsulta Eletiva × Teleinterconsulta**
> 4 horas | 2 equipes | ~40 pessoas | IA local com Ollama + MedGemma + Gemma 4

---

## 👋 Como navegar neste repositório

### 🎯 Você é PARTICIPANTE do hackathon?
👉 Comece por **[PARTICIPANTES_LEIA_ME.md](PARTICIPANTES_LEIA_ME.md)**
Guia de 30 minutos para preparar seu notebook antes do dia.
Depois leia o **[GUIA_PROMPT.md](GUIA_PROMPT.md)** (10 min) para escrever bons prompts.

### 🎯 Você é o ORGANIZADOR / FACILITADOR?
👉 Comece por **[PLANO_FACILITADOR.md](PLANO_FACILITADOR.md)**
Cronograma minuto-a-minuto, plano de contingência e pós-hackathon.

### 🎯 Você é PATROCINADOR / LIDERANÇA?
👉 Leia **[desafios_por_trilha.md](desafios_por_trilha.md)**
Desafios reais que serão trabalhados e critérios de avaliação.

---

## 📂 Estrutura do Repositório

```
hackathon-ia-saude/
│
├── 📘 README.md                    ← Você está aqui (índice)
├── 👥 PARTICIPANTES_LEIA_ME.md     ← Guia de setup para participantes
├── 🧠 GUIA_PROMPT.md               ← Guia de engenharia de prompt (10 min)
├── 🎯 PLANO_FACILITADOR.md         ← Plano completo do organizador
├── 📨 MENSAGENS_TEMPLATE.md        ← Mensagens prontas (D-7 até pós)
├── 🛟 BACKUP_SERVIDOR.md           ← Como subir servidor central como backup
├── 📋 desafios_por_trilha.md       ← Os 6 desafios (GERADO do JSON)
│
├── ⚙️ setup_hackathon.ps1          ← Script de instalação automática
├── 🐍 app_hackathon.py             ← Interface Streamlit
├── 📦 exemplos_prompts.json        ← FONTE ÚNICA: desafios + prompts
├── 🔧 gerar_desafios_md.py         ← Gera o .md a partir do JSON
│
├── 📊 dados/
│   ├── gerar_dados_sinteticos.py   ← Gera os CSVs fictícios
│   ├── analise_noshow.py           ← Análise estatística do no-show
│   ├── agendamentos.csv            ← 200 agendamentos (no-show)
│   └── fila_interconsulta.csv      ← 70 pedidos (priorização)
│
└── 📁 output/                       ← Resultados salvos (gitignore)
```

## 🧩 Recursos do app

| Recurso | O que faz |
|---|---|
| **Persona (system prompt)** | Escolha o "papel" da IA na barra lateral — melhora muito modelos pequenos |
| **Temperatura** | Ajuste criatividade × precisão (baixa p/ clínica, alta p/ brainstorm) |
| **Detecção de modelos** | Lista automaticamente os modelos instalados no Ollama |
| **⚖️ Comparar 2 modelos** | Roda o mesmo prompt no MedGemma e no Gemma 4 lado a lado |
| **💬 Chat / Refino** | Conversa multi-turn — a IA lembra do contexto (ensina iteração) |
| **📊 Dados** | Usa os CSVs fictícios: classifica risco de no-show, prioriza fila |
| **📈 Analytics** | Gráficos de quais fatores predizem o no-show (sub-aba em Dados) |
| **🎙️ Transcrição** | Áudio de consulta → Whisper transcreve → MedGemma vira nota clínica (opcional: `pip install faster-whisper`) |
| **🖼️ Imagem** | A MedGemma **enxerga**: envie uma imagem (didática, nunca de paciente real) e ela descreve — teledermatologia e raio-x como exercício, **nunca diagnóstico** |
| **🧮 Autoavaliação** | A IA pontua a própria resposta pela rubrica do hackathon |
| **🎤 Gerador de pitch** | Monta o esqueleto da apresentação a partir dos resultados salvos |
| **Métricas** | Mostra tokens/s e tempo a cada resposta |
| **Salvar resultados** | Persiste a resposta e exporta `.txt` |

---

## ⚡ Quick Start (se já leu o guia)

```bash
# 1. Clonar
git clone https://github.com/yago-ananias/hackathon-ia-saude.git
cd hackathon-ia-saude

# 2. Setup (Windows)
powershell -ExecutionPolicy Bypass -File setup_hackathon.ps1

# 3. Rodar
streamlit run app_hackathon.py
# Abre em http://localhost:8501
```

**Pré-requisitos:** Python 3.10+, Ollama, ~12 GB de disco livre.

---

## 🧠 Modelos Utilizados

| Modelo | Tamanho | Especialidade |
|---|---|---|
| 🏥 **MedGemma 4B** | 3.3 GB | Triagem, interconsulta, síntese clínica |
| 🎯 **Gemma 4 E4B QAT** | 6.1 GB | Produto, UX, jornada do paciente |

> 💻 Notebook com 8 GB de RAM? Troque o segundo por `gemma4:e2b-it-qat` (4.3 GB) — mesma família, mais leve.

Ambos rodam **100% local** via Ollama. Zero envio de dados para nuvem.

---

## 🩺 Trilhas e Desafios

### Equipe TeleEletiva
- **TE-01** — Reduzir No-Show com IA
- **TE-02** — Triagem Inteligente de Sintomas
- **TE-03** — Adesão ao Cuidado Pós-Consulta

### Equipe TeleInterconsulta
- **TI-01** — Estruturar Pedido de Interconsulta com IA
- **TI-02** — Priorizar Casos por Urgência com IA
- **TI-03** — Síntese Clínica para Resposta Mais Rápida

Detalhes em [desafios_por_trilha.md](desafios_por_trilha.md).

---

## 📅 Cronograma de 4 Horas

| Tempo | Atividade |
|---|---|
| 0h00 – 0h30 | Abertura + verificação de setup |
| 0h30 – 1h00 | Exploração livre da IA |
| 1h00 – 2h30 | Sprint de solução |
| 2h30 – 3h30 | Construção do pitch |
| 3h30 – 4h00 | Apresentações finais (15min × 2) |

---

## 🛟 Suporte

**Antes do hackathon:** abra uma [issue](https://github.com/yago-ananias/hackathon-ia-saude/issues) ou pergunte no grupo do WhatsApp.

**Durante o hackathon:** servidor backup disponível em URL compartilhada no início.

---

## 📜 Licença

Material educacional aberto. Use, adapte e replique para outros hackathons.
Atribuição: Yago Ananias.

---

*Construído com Claude + Ollama + muito café ☕*
