# 🏥 Hackathon IA + Saúde Digital

> **Teleconsulta Eletiva × Teleinterconsulta**
> 4 horas | 2 equipes | ~40 pessoas | IA local com Ollama + MedGemma + Gemma 4

---

## 👋 Como navegar neste repositório

### 🎯 Você é PARTICIPANTE do hackathon?
👉 Comece por **[PARTICIPANTES_LEIA_ME.md](PARTICIPANTES_LEIA_ME.md)**
Guia de 30 minutos para preparar seu notebook antes do dia.

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
├── 🎯 PLANO_FACILITADOR.md         ← Plano completo do organizador
├── 📨 MENSAGENS_TEMPLATE.md        ← Mensagens prontas (D-7 até pós)
├── 🛟 BACKUP_SERVIDOR.md           ← Como subir servidor central como backup
├── 📋 desafios_por_trilha.md       ← Os 6 desafios (3 por trilha)
│
├── ⚙️ setup_hackathon.ps1          ← Script de instalação automática
├── 🐍 app_hackathon.py             ← Interface Streamlit
├── 📦 exemplos_prompts.json        ← 14 prompts prontos
│
└── 📁 output/                       ← Resultados salvos (gitignore)
```

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
| 🎯 **Gemma 4 E2B** | 7.2 GB | Produto, UX, jornada do paciente |

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
