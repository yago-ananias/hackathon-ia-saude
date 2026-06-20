# 🧠 Guia Rápido de Engenharia de Prompt — Saúde Digital

> **Para quem:** participantes do hackathon (qualquer área — não precisa ser técnico)
> **Tempo de leitura:** 10 minutos
> **Objetivo:** sair daqui sabendo escrever prompts que geram respostas úteis de verdade

---

## A ideia em 1 frase

> **Um bom prompt é uma boa delegação:** você explica para a IA *quem ela é*, *o que precisa*, *com quais informações* e *em que formato* — exatamente como faria com um colega novo no time.

Modelos locais como MedGemma e Gemma 4 são **menores** que o ChatGPT. Isso significa que eles **dependem mais de um bom prompt**. A boa notícia: as técnicas abaixo fazem uma diferença enorme.

---

## 🧩 A anatomia de um bom prompt (PCFE)

Um prompt forte costuma ter 4 partes. Decore a sigla **PCFE**:

| Parte | Pergunta que responde | Exemplo |
|---|---|---|
| **P — Persona** | Quem a IA deve ser? | "Você é um médico especialista em triagem de telessaúde." |
| **C — Contexto** | Quais dados/situação? | "Paciente, 58 anos, dor torácica há 2 dias, HAS e diabetes." |
| **F — Formato** | Como quer a resposta? | "Liste em 3 tópicos: hipótese, conduta, urgência." |
| **E — Exemplo** (opcional) | Modelo a seguir? | "Siga este formato: [exemplo preenchido]" |

> No app do hackathon, a **Persona** já pode ser escolhida na barra lateral. Use isso a seu favor: deixe a persona certa ligada e foque o texto no Contexto + Formato.

---

## ❌ Antes e ✅ Depois (exemplos reais de saúde)

### Exemplo 1 — Triagem

❌ **Prompt fraco:**
```
dor nas costas, o que faço?
```
Resposta provável: genérica, longa, sem foco no nosso problema.

✅ **Prompt forte (PCFE):**
```
Você é um assistente de triagem clínica em telessaúde. (Persona)

Paciente relata: dor lombar há 3 semanas, piora ao abaixar,
sem febre, sem perda de peso, já tomou dipirona sem melhora. (Contexto)

Responda em 4 itens: (Formato)
1. Especialidade recomendada
2. Nível de urgência (eletivo / prioritário / urgente)
3. 2 perguntas adicionais que refinariam a triagem
4. 1 sinal de alarme que exigiria atendimento presencial
```

### Exemplo 2 — Negócio / produto

❌ **Fraco:** `como reduzir no-show?`

✅ **Forte:**
```
Você é gestor de produto de uma operadora de saúde. (Persona)

Contexto: teleconsulta eletiva com 30% de no-show. Canal principal
com o paciente é WhatsApp. Time pequeno, sem orçamento para ligações. (Contexto)

Proponha 3 ações priorizadas. Para cada uma: (Formato)
- O que é (1 linha)
- Esforço de implementação (baixo/médio/alto)
- Métrica que provaria que funcionou
```

---

## 🎚️ Temperatura: o botão criatividade × precisão

No app, a **temperatura** (barra lateral) muda o comportamento:

| Temperatura | Comportamento | Use para |
|---|---|---|
| **0.0 – 0.3** | Preciso, factual, repetível | Triagem, classificação, extração de dados, resumo clínico |
| **0.4 – 0.7** | Equilibrado | Maioria dos casos |
| **0.8 – 1.0** | Criativo, variado | Brainstorm de ideias, variações de mensagem, naming |

> **Regra prática:** decisão clínica → temperatura **baixa**. Brainstorm de growth → temperatura **alta**.

---

## 🔁 A técnica mais importante: ITERAR

O segredo de quem usa IA bem **não é acertar o prompt de primeira** — é **refinar**. Use a aba **💬 Chat / Refino** do app.

Fluxo típico:
1. Peça a primeira versão
2. **Critique:** "está muito técnico, simplifique para o paciente"
3. **Ajuste o ângulo:** "e se o paciente for idoso e sozinho?"
4. **Mude o formato:** "transforme isso num checklist para WhatsApp"
5. **Estresse:** "quais riscos dessa abordagem?"

> Cada rodada te aproxima. Iterar 4 vezes num prompt médio bate começar 4 prompts novos.

---

## 🛠️ 7 técnicas que funcionam (com mini-exemplos)

1. **Dê um papel (role):** "Você é um especialista em..."
2. **Peça passo a passo:** "Pense passo a passo antes de responder."
3. **Limite o tamanho:** "Responda em no máximo 5 linhas."
4. **Peça o formato exato:** "Devolva como tabela com colunas X, Y, Z."
5. **Dê um exemplo (few-shot):** "Siga este modelo: [exemplo]."
6. **Peça alternativas:** "Dê 3 opções com prós e contras."
7. **Peça autocrítica:** "Aponte 1 risco ou limitação da sua resposta."

---

## 🩺 Cuidados específicos de saúde (importante!)

A IA **erra** e inventa com confiança. Em saúde, isso é sério:

- ⚠️ **Nunca trate a saída como diagnóstico definitivo.** É apoio à decisão, não decisão.
- ⚠️ **Desconfie de números, doses e estatísticas** que a IA "lembrou". Ela pode inventar (alucinação).
- ⚠️ **Peça que a IA diga o que NÃO sabe:** "Se faltar informação, liste o que falta em vez de assumir."
- ⚠️ **Dados de paciente real não entram aqui.** Use sempre casos fictícios (este app é educacional). Tudo roda local, mas o hábito de não expor dado sensível é regra.
- ✅ **Sempre um humano no circuito.** A IA estrutura, prioriza e rascunha; o profissional decide.

---

## ✅ Checklist antes de apertar "Executar"

- [ ] Defini **quem** a IA deve ser? (persona)
- [ ] Dei o **contexto** necessário? (dados do caso)
- [ ] Pedi um **formato** claro de resposta?
- [ ] A **temperatura** combina com a tarefa? (precisa = baixa)
- [ ] Tenho um plano de **refino** se a 1ª resposta não vier ideal?

---

## 🎯 Desafio-relâmpago (5 min)

Pegue qualquer desafio da sua trilha e escreva **a pior versão** do prompt (1 linha vaga). Rode. Depois reescreva usando **PCFE** e rode de novo. Compare as duas respostas com o time. **Essa diferença é o valor da engenharia de prompt.**

---

*Guia rápido — Hackathon IA + Saúde Digital. Imprima e deixe na mesa de cada equipe.*
