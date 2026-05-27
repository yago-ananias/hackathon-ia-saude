# 🎯 Plano do Facilitador — Hackathon IA + Saúde Digital

> **Para:** Yago Ananias (organizador)
> **Formato:** 4 horas, 2 equipes (~20 pessoas cada), presencial
> **Objetivo:** time aprender IA + propor solução para problema real de saúde digital

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

### Manhã do hackathon

- [ ] Chegar **1h antes** no local
- [ ] Conferir Wi-Fi, energia, projetor
- [ ] Subir o servidor backup (manter ligado durante as 4h)
- [ ] Imprimir/projetar os desafios das duas trilhas
- [ ] Identificar 2 facilitadores auxiliares (1 por trilha)
- [ ] Preparar slides de abertura (10 min — contexto + regras)

---

## ⏱️ Cronograma do Dia (4 horas)

### 🟢 0h00 – 0h30 — Abertura e Setup (30 min)

**Você faz:**
- Boas-vindas (5 min)
- Contexto: por que IA + saúde? Por que essas 2 trilhas? (10 min)
- Explicar regras e critérios de avaliação (5 min)
- Dividir as equipes nas trilhas (5 min)
- Disparar setup final / verificação de ambiente (5 min)

**Sinais de problema:**
- 🔴 Se mais de 3 pessoas não conseguem rodar o app → ative imediatamente o servidor backup
- 🟡 Se 1-2 pessoas têm problema → coloque junto com colegas que estão OK

**Mensagem na tela:**
```
Bem-vindos!
Trilha TeleEletiva → [SALA A]
Trilha TeleInterconsulta → [SALA B]

Backup: [URL CLOUDFLARE]
Materiais: github.com/yago-ananias/hackathon-ia-saude
```

---

### 🟡 0h30 – 1h00 — Exploração Livre (30 min)

**Objetivo:** todos brincam com a IA, sem pressão. Aprendem como o modelo responde.

**Você faz:**
- Circula entre as duas salas
- Demonstra prompts em 1 ou 2 momentos
- Estimula perguntas tipo: "tenta perguntar X, vê o que ele responde"

**O time faz:**
- Testa os prompts prontos do app
- Faz prompts livres na aba "Prompt Livre"
- Conversa entre si: "isso é útil?", "como melhoraria?"

**Marcos:**
- ⏰ Aos 15 min: cada equipe deve ter escolhido **1 desafio**
- ⏰ Aos 25 min: aviso de transição

---

### 🔵 1h00 – 2h30 — Sprint de Solução (1h30)

**Objetivo:** equipes constroem uma proposta concreta usando IA.

**Você faz:**
- Atribui papéis dentro de cada equipe (sugestão):
  - 2-3 pessoas: experimentam prompts
  - 2-3 pessoas: documentam o que funciona
  - 2-3 pessoas: pensam em métricas e riscos
  - 2-3 pessoas: começam slides do pitch
  - 1 pessoa: facilitador interno (você indica)
- Faz **check-in aos 45 min** (metade do tempo):
  - "Onde estão?"
  - "O que falta?"
  - "Algum bloqueio?"
- Disponível para tirar dúvidas, mas **não resolve por eles**

**Sinais de problema:**
- 🔴 Equipe travada → faça uma pergunta socrática: "Qual a métrica que importa?"
- 🔴 Equipe dispersa → traga foco com: "Em 5 frases, qual a solução de vocês?"
- 🔴 Discordância interna → pergunta: "Qual é a 1 dor mais clara que vocês resolveriam?"

**Marcos:**
- ⏰ 1h15 (45 min de sprint): check-in geral
- ⏰ 2h00 (1h30 de sprint): aviso "30 min para começar a fechar"
- ⏰ 2h25: aviso "fechem a solução, agora é pitch"

---

### 🟣 2h30 – 3h30 — Construção do Pitch (1h)

**Objetivo:** equipes preparam apresentação de 15 min.

**Estrutura do pitch (recomendar para todos):**
1. **Problema** (2 min) — Qual a dor? Quanto custa hoje?
2. **Solução com IA** (4 min) — Como funciona? Demo de prompt funcionando
3. **Métricas** (3 min) — O que muda? Como mediríamos?
4. **Risco assistencial** (2 min) — O que pode dar errado e como prevenir
5. **Próximos passos** (2 min) — Se tivesse 30 dias, faria o quê primeiro?
6. **Perguntas** (2 min)

**Você faz:**
- Lembra a estrutura com pôster/slide na sala
- Encoraja prática: "ensaiem pelo menos 1 vez antes"
- Avisa 30 min, 15 min, 5 min antes

**Sinais de problema:**
- 🔴 Equipe sem slides aos 3h00 → entre e ajude a estruturar
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
- **Ação:** Recomende trocar para MedGemma 4B (mais leve)
- **Backup:** Usar servidor central

### Cenário 5: Discussão técnica trava o foco
- **Ação:** Você redireciona: "Vamos focar no problema do paciente, não na arquitetura"

---

## 📝 Checklist do Material no Dia

- [ ] Notebook seu carregado + carregador
- [ ] Notebook backup (caso o principal trave) com Ollama instalado
- [ ] Cabo HDMI para projetor
- [ ] Apresentação de abertura (slides)
- [ ] Cronômetro / app de timer
- [ ] Flip chart ou quadro branco
- [ ] Canetinhas / post-its
- [ ] Folha impressa com critérios de avaliação (1 por equipe)
- [ ] Folha impressa com cronograma (1 por equipe)
- [ ] Lista de presença
- [ ] Crachás com nome (opcional)

---

## 📊 Após o Hackathon

### Mesmo dia (até 24h)
- [ ] Salvar todos os outputs das equipes (pasta `output/`)
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
- **Comemore as conexões.** Hackathon é também sobre criar relacionamento.

---

*Bom hackathon! 🚀*
