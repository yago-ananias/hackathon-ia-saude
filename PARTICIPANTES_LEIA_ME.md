# 🏥 Hackathon IA + Saúde Digital — Guia do Participante

> **Bem-vindo!** Este guia te prepara para o hackathon em **30 minutos**.
> Faça isso **com pelo menos 3 dias de antecedência**.

---

## ⏱️ O que você vai instalar

| Ferramenta | Para que serve | Tempo |
|---|---|---|
| **Python 3.10+** | Roda a interface do app | 5 min |
| **Ollama** | Motor que roda a IA localmente | 5 min |
| **2 modelos de IA** | MedGemma + Gemma 4 (10 GB) | 15 min |

**Total:** ~30 min (depende da sua internet)

---

## 📋 Pré-requisitos

Antes de começar, garanta que você tem:

- ☐ **Windows 10/11**, macOS, ou Linux
- ☐ **15 GB livres** em disco
- ☐ **8 GB de RAM** mínimo (16 GB recomendado)
- ☐ **Permissão de administrador** para instalar programas
- ☐ **Conexão estável** para baixar ~10 GB

---

## 🚀 Passo a Passo

### 1️⃣ Instalar Python (5 min)

**Windows:** Baixe em https://www.python.org/downloads/ → instale com a opção **"Add Python to PATH"** marcada.

**macOS:** Já vem instalado. Verifique com `python3 --version`.

**Linux:** `sudo apt install python3 python3-pip`

**Como saber que deu certo:**
Abra o terminal (PowerShell no Windows) e rode:
```
python --version
```
Deve mostrar algo como `Python 3.10.x` ou superior.

---

### 2️⃣ Instalar Ollama (5 min)

Acesse: **https://ollama.com/download** e baixe para seu sistema.

Execute o instalador (próximo → próximo).

**Como saber que deu certo:**
Abra o terminal e rode:
```
ollama --version
```
Deve mostrar a versão (ex: `ollama version 0.24.0`).

> ⚠️ **Importante:** Se aparecer "comando não encontrado", **feche e reabra o terminal**.

---

### 3️⃣ Clonar o repositório (1 min)

No terminal, navegue até onde quer guardar (ex: Desktop) e rode:

```
git clone https://github.com/yago-ananias/hackathon-ia-saude.git
cd hackathon-ia-saude
```

> Se você não tem git instalado, baixe o ZIP em **github.com/yago-ananias/hackathon-ia-saude** → botão verde "Code" → "Download ZIP" → descompacte.

---

### 4️⃣ Instalar dependências e modelos (15 min)

**Windows (PowerShell):**
```
powershell -ExecutionPolicy Bypass -File setup_hackathon.ps1
```

**macOS / Linux:**
```
pip install streamlit requests
ollama pull medgemma:4b
ollama pull gemma4:e4b-it-qat
```

> 💻 Seu notebook tem 8 GB de RAM? Troque a última linha por `ollama pull gemma4:e2b-it-qat` (4.3 GB, mais leve).

> ☕ Boa hora pra um café. Vai baixar ~9,5 GB.

---

### 5️⃣ Testar (2 min)

Rode o app:
```
streamlit run app_hackathon.py
```

Vai abrir automaticamente em **http://localhost:8501**.

Na sidebar, clique em **"🔌 Testar Conexão"**. Deve aparecer:
- ✅ Ollama conectado
- Lista com `medgemma:4b` e `gemma4:e4b-it-qat` (ou `gemma4:e2b-it-qat`, se escolheu a versão leve)

Agora teste um prompt:
1. Vá em **"🩺 Equipe TeleEletiva"**
2. Clique em qualquer botão de prompt pronto
3. Clique em **"▶️ Executar"**
4. Aguarde 10-20 segundos pela resposta

**Se a resposta aparecer em português, tudo certo!** Você está pronto. 🎉

---

## 🆘 Problemas Comuns

### "ollama: comando não encontrado"
**Solução:** Feche e reabra o terminal após instalar o Ollama.

### "Streamlit: comando não encontrado"
**Solução:** Rode `pip install streamlit requests` antes.

### "Não conecta ao Ollama"
**Solução:** Abra outro terminal e rode `ollama serve`. Deixe rodando enquanto usa o app.

### Modelo muito lento (>1 minuto por resposta)
**Solução:** Sua máquina pode estar com pouca RAM. Tente fechar outros programas. Se persistir, use o servidor backup que será disponibilizado no dia.

### "Permissão negada" no Windows
**Solução:** Abra o PowerShell como **Administrador** (botão direito → "Executar como administrador").

---

## 💡 Dicas Antes do Hackathon

1. **Teste 1 dia antes** — não deixe para a hora
2. **Salve o repositório** num lugar fácil de achar
3. **Tire prints dos passos que funcionaram** (caso precise refazer)
4. **Anote dúvidas** para perguntar no grupo de suporte

---

## 📞 Suporte

**Canal de dúvidas:** [link do WhatsApp/Slack a ser preenchido pelo organizador]
**Quem ajuda:** Yago Ananias e equipe

**No dia do hackathon**, se nada funcionar:
- Um **servidor backup** estará no ar (URL será compartilhada no início)
- Você só precisa abrir o link no navegador

---

## 🎯 No Dia do Hackathon

**O que trazer:**
- Notebook com tudo instalado e testado
- Carregador
- Disposição para resolver problema real de saúde digital com IA

**O que esperar:**
- 4 horas intensas
- 2 trilhas: Teleconsulta Eletiva e Teleinterconsulta
- Equipes de ~20 pessoas cada
- Apresentações de 15 min no final

**Boa preparação!** 🚀

---

*Hackathon IA + Saúde Digital | Yago Ananias*
