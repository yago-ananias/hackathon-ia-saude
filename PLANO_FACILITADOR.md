# 🎯 Plano do Facilitador — Hackathon IA + Saúde Digital

> **Para:** Yago Ananias (organizador)
> **Formato:** 4 horas, 2 equipes (~20 pessoas cada), presencial
> **Objetivo:** time aprender IA + propor solução para problema real de saúde digital
> **Versão 2.0** — roteiro atualizado para explorar as 8 abas do app (dados, voz, imagem, chat, autoavaliação e gerador de pitch)

---

## 🧩 O app em 1 minuto (cola do facilitador)

| Aba | O que faz | Quando usar no evento |
|---|---|---|
| 🩺 TeleEletiva / 🔄 TeleInterconsulta | Desafios com prompts prontos | Exploração + Sprint |
| 📊 Dados | CSVs fictícios (no-show, fila) + **Analytics** com gráficos | Sprint (dá números ao pitch) |
| 🎙️ Transcricao | Áudio → Whisper → nota clínica | Demo de abertura (opcional) |
| 🖼️ Imagem | MedGemma **enxerga**: derma/raio-x didáticos | **Demo "uau" de abertura** |
| 💬 Chat / Refino | Conversa com memória — ensina iteração | Exploração |
| ✏️ Prompt Livre | Qualquer prompt + comparar 2 modelos | Exploração |
| 📁 Resultados | Respostas salvas + **🎤 Gerador de pitch** | Construção do pitch |

Recursos transversais: **persona** e **temperatura** na sidebar, **🧮 Autoavaliar pela rubrica** em toda resposta, métricas de tokens/s.

---

## 🗓️ Preparação Pré-Hackathon

### D-7 até D-1 (1 semana antes)

- [ ] **D-7:** Enviar mensagem inicial + link do repositório
- [ ] **D-7:** Criar grupo de suporte no WhatsApp/Slack
- [ ] **D-5:** Verificar quem já instalou (pedir reação ✅ no grupo)
- [ ] **D-3:** Cobrar quem não respondeu
- [ ] **D-2:** Call de troubleshooting (30 min)
- [ ] **D-1:** Checagem final + envio de logística (local, horário)
- [ ] **D-1:** Subir servidor backup com Cloudflare Tunnel (ver `BACKUP_SERVIDOR.md`)
- [ ] **D-1:** Testar servidor backup com 1 colega remoto

### Preparação das demos (novo na v2.0)

- [ ] Separar **2–3 imagens didáticas públicas** (ilustração de lesão de pele, raio-x educacional) numa pasta local — **nunca imagem real de paciente**
- [ ] Gravar **1 áudio fictício de teleconsulta** (~1 min, você mesmo simulando médico e paciente) para a demo de voz
- [ ] Instalar `pip install faster-whisper` na sua máquina e rodar 1 transcrição de teste
- [ ] Testar a aba 🖼️ Imagem com as imagens escolhidas (1ª análise demora ~1 min em CPU — já deixe "aquecida" no dia)
- [ ] Ensaiar a demo de abertura pelo menos 1 vez, com cronômetro

### Manhã do hackathon

- [ ] Chegar **1h antes** no local
- [ ] Conferir Wi-Fi, energia, projetor
- [ ] Subir o servidor backup (manter ligado durante as 4h)
- [ ] **Abrir o app e rodar 1 prompt em cada modelo** (aquece os modelos — evita esperar a carga na demo)
- [ ] Imprimir/projetar os desafios das duas trilhas
- [ ] Identificar 2 facilitadores auxiliares (1 por trilha)
- [ ] Preparar slides de abertura (10 min — contexto + regras)

---

## ⏱️ Cronograma do Dia (4 horas)

### 🟢 0h00 – 0h30 — Abertura e Setup (30 min)

**Você faz:**
- Boas-vindas (4 min)
- Contexto: por que IA + saúde? Por que essas 2 trilhas? (8 min)
- **Demo "uau" (3 min):** na aba 🖼️ Imagem, suba uma imagem didática e deixe a MedGemma descrever ao vivo. Frase-âncora: *"isso está rodando NESTE notebook, sem internet, sem mandar dado para nuvem"*. Emende o disclaimer: *"descreve, não diagnostica — a decisão é sempre do profissional"*
  - *Plano B se travar:* prompt pronto TE-01 na aba TeleEletiva (resposta em ~20s)
- Explicar regras e critérios de avaliação (5 min)
- Dividir as equipes nas trilhas (5 min)
- Setup final / verificação de ambiente (5 min): todos clicam **🔌 Testar Conexão** na sidebar

**Sinais de problema:**
- 🔴 Mais de 3 pessoas sem app rodando → ative imediatamente o servidor backup
- 🟡 1-2 pessoas com problema → coloque junto com colegas que estão OK

**Mensagem na tela:**
```
Bem-vindos!
Trilha TeleEletiva → [SALA A]
Trilha TeleInterconsulta → [SALA B]

Backup: [URL CLOUDFLARE]
Materiais: github.com/yago-ananias/hackathon-ia-saude
```

---

### 🟡 0h30 – 1h00 — Exploração Guiada (30 min)

**Objetivo:** todos experimentam a IA sem pressão — mas com um percurso, para ninguém ficar perdido.

**Percurso sugerido (projete na tela):**
```
1. (10 min) Aba da SUA trilha → clique num prompt pronto → Executar
   Depois: mude a PERSONA na sidebar e rode de novo. O que mudou?
2. (10 min) ✏️ Prompt Livre → escreva um prompt seu
   Teste o ⚖️ Comparar 2 modelos: clínico vs produto — qual foi melhor?
3. (10 min) Escolha livre: 💬 Chat (peça e refine: "agora mais curto",
   "e se for idoso?") ou 📊 Dados (gere um prompt a partir de um registro)
```

**Você faz:**
- Circula entre as duas salas
- Demonstra 1 truque por sala: temperatura baixa p/ tarefa clínica, alta p/ brainstorm (está no `GUIA_PROMPT.md`)
- Estimula: "tenta perguntar X, vê o que ele responde"

**Marcos:**
- ⏰ Aos 15 min: cada equipe deve ter escolhido **1 desafio**
- ⏰ Aos 25 min: aviso de transição

---

### 🔵 1h00 – 2h30 — Sprint de Solução (1h30)

**Objetivo:** equipes constroem uma proposta concreta usando IA — **com dado, não só opinião**.

**Regra de ouro da v2.0 (anuncie no início do sprint):**
> "Pitch sem número não convence. A aba **📊 Dados** tem os CSVs e a sub-aba **📈 Analytics** mostra o que prediz o no-show. Usem."

**Você faz:**
- Atribui papéis dentro de cada equipe (sugestão):
  - 2-3 pessoas: experimentam prompts
  - 2-3 pessoas: exploram a aba 📊 Dados / Analytics e anotam números
  - 2-3 pessoas: pensam em métricas e riscos
  - 2-3 pessoas: começam slides do pitch
  - 1 pessoa: facilitador interno (você indica)
- Lembra as equipes de **💾 Salvar** as melhores respostas (viram matéria-prima do pitch na aba 📁 Resultados)
- Faz **check-in aos 45 min** (metade do tempo): "Onde estão? O que falta? Algum bloqueio?"
- **Checkpoint de qualidade aos 60 min:** cada equipe roda **🧮 Autoavaliar pela rubrica** na melhor resposta que tem. Nota baixa em algum critério = é ali que o pitch está fraco
- Disponível para tirar dúvidas, mas **não resolve por eles**

**Sinais de problema:**
- 🔴 Equipe travada → pergunta socrática: "Qual a métrica que importa?"
- 🔴 Equipe dispersa → "Em 5 frases, qual a solução de vocês?"
- 🔴 Equipe só no 'achismo' → "Que número da aba Dados sustenta isso?"
- 🔴 Discordância interna → "Qual é a 1 dor mais clara que vocês resolveriam?"

**Marcos:**
- ⏰ 1h15 (45 min de sprint): check-in geral
- ⏰ 2h00 (1h30 de sprint): checkpoint de autoavaliação + aviso "30 min para fechar"
- ⏰ 2h25: aviso "fechem a solução, agora é pitch"

---

### 🟣 2h30 – 3h30 — Construção do Pitch (1h)

**Objetivo:** equipes preparam apresentação de 15 min.

**Arranque rápido (anuncie):**
> "Na aba **📁 Resultados**, o botão **🎤 Gerar esqueleto de pitch** monta o rascunho da apresentação a partir do que vocês salvaram. Comecem por ele — não do zero."

**Estrutura do pitch (a mesma da rubrica, projete na sala):**
1. **Problema** (2 min) — Qual dor você resolveu? Qual a magnitude?
2. **Solução com IA** (4 min) — Como funciona? Demo de prompt AO VIVO no app
3. **Dados e métricas** (3 min) — O que muda? Como vamos medir?
4. **Riscos e mitigações** (2 min) — O que pode dar errado e como prevenir?
5. **Próximos passos** (2 min) — Se tivesse 30 dias, o que faria primeiro?
6. **Perguntas** (2 min)

**Você faz:**
- Encoraja demo ao vivo no pitch (prompt rodando > print de slide)
- Encoraja prática: "ensaiem pelo menos 1 vez antes"
- Avisa 30 min, 15 min, 5 min antes

**Sinais de problema:**
- 🔴 Equipe sem slides aos 3h00 → mande usar o 🎤 Gerador de pitch agora
- 🟡 Equipe com 30 slides → ajude a cortar para 8-10

---

### 🔴 3h30 – 4h00 — Apresentações Finais (30 min)

**Objetivo:** cada equipe pitcha 15 min (incluindo perguntas).

**Você faz:**
- Modera tempo (rigoroso: 12 min pitch + 3 min perguntas)
- Faz perguntas críticas mas construtivas
- Convida outras pessoas a perguntarem
- **NÃO eleja vencedor na hora** — diga que vai avaliar e voltar com decisão

**Perguntas-modelo para fazer:**
- "Qual o maior risco da solução de vocês?"
- "Em 6 meses, como saberíamos que funcionou?"
- "O que vocês descartaram e por quê?"
- "Quem na empresa precisa comprar essa ideia para acontecer?"

**Encerramento (5 min):**
- Agradecer todos
- Próximos passos: quando você volta com decisão (sugestão: 1 semana)
- Feedback rápido (NPS na hora): "de 0 a 10, recomendaria?"

---

## 🎯 Critérios de Avaliação (uso interno)

Anote durante as apresentações:

| Critério | Peso | Equipe TE | Equipe TI |
|---|---|---|---|
| Clareza do problema | 25% | ___ | ___ |
| Uso real da IA (prompt mostrado) | 30% | ___ | ___ |
| Viabilidade em 6 meses | 20% | ___ | ___ |
| Impacto mensurável | 15% | ___ | ___ |
| Risco assistencial identificado | 10% | ___ | ___ |
| **TOTAL** | 100% | ___ | ___ |

> Dica: os critérios são os mesmos da **🧮 Autoavaliação** do app — se a equipe usou o recurso no sprint, o pitch tende a vir mais redondo.

---

## 🚨 Plano de Contingência

### Cenário 1: Ollama trava em várias máquinas
- **Ação:** Comunicar URL do servidor backup imediatamente
- **Quem cuida:** Você ou facilitador auxiliar
- **Tempo de reação:** < 5 min

### Cenário 2: Wi-Fi do local cai
- **Ação:** Equipes seguem rodando local (não dependem de internet após setup)
- **Backup:** Hotspot do seu celular para o servidor backup

### Cenário 3: Equipe não consegue convergir num desafio
- **Ação:** Você entra na conversa e força uma escolha em 5 min
- **Mensagem:** "Não precisa ser perfeito, precisa ser claro. Escolham 1 agora."

### Cenário 4: Modelo demora muito a responder (>30s)
- **Ação:** Recomende trocar para MedGemma 4B (mais leve); máquinas de 8 GB devem usar `gemma4:e2b-it-qat` como modelo de produto
- **Backup:** Usar servidor central

### Cenário 5: Discussão técnica trava o foco
- **Ação:** Você redireciona: "Vamos focar no problema do paciente, não na arquitetura"

### Cenário 6: Aba Imagem / Transcrição lenta demais na máquina de alguém
- **Ação:** São recursos **bônus**, não obrigatórios — a equipe segue com texto e dados; a demo multimodal pode rodar só na sua máquina/projetor
- **Lembrete:** 1ª análise de imagem demora ~1 min (carga do modelo); as seguintes são mais rápidas

---

## 📝 Checklist do Material no Dia

- [ ] Notebook seu carregado + carregador
- [ ] Notebook backup (caso o principal trave) com Ollama instalado
- [ ] **2–3 imagens didáticas** salvas localmente (para a demo e para as equipes)
- [ ] **1 áudio fictício** de teleconsulta (para a demo de voz)
- [ ] Cabo HDMI para projetor
- [ ] Apresentação de abertura (slides)
- [ ] Cronômetro / app de timer
- [ ] Flip chart ou quadro branco
- [ ] Canetinhas / post-its
- [ ] Folha impressa com critérios de avaliação (1 por equipe)
- [ ] Folha impressa com cronograma + percurso da exploração (1 por equipe)
- [ ] Lista de presença
- [ ] Crachás com nome (opcional)

---

## 📊 Após o Hackathon

### Mesmo dia (até 24h)
- [ ] Recolher os arquivos da pasta `output/` de cada equipe (respostas salvas + esqueletos de pitch)
- [ ] Fotografar/printar os slides das apresentações
- [ ] Anotações de critérios de avaliação consolidadas
- [ ] Mensagem de agradecimento no grupo

### Próximos 7 dias
- [ ] Consolidar 2 propostas em **1 documento executivo** (1 página por proposta)
- [ ] Apresentar para [LIDERANÇA] e tomar decisão de continuidade
- [ ] Voltar para o time com:
  - Quais ideias vão evoluir
  - Quais não vão (e o porquê)
  - Próximos passos

### Próximos 30 dias
- [ ] Eleger 1-2 pessoas para desenvolver POC da proposta vencedora
- [ ] Definir métrica baseline para comparação
- [ ] Setar revisão em 90 dias

---

## 💭 Lembretes para Você

- **Você é o facilitador, não o protagonista.** Deixe o time pensar.
- **Tempo é o seu inimigo.** Não deixe debate técnico atrasar.
- **Erros são parte.** Se o modelo der resposta ruim, é insight: "como melhoraríamos o prompt?"
- **Saída perfeita > saída completa.** Melhor 1 ideia bem testada que 5 ideias meia-boca.
- **Dado > opinião.** Puxe as equipes para a aba 📊 Dados sempre que o papo virar achismo.
- **Comemore as conexões.** Hackathon é também sobre criar relacionamento.

---

*Bom hackathon! 🚀*
