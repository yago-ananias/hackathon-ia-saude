# Desafios do Hackathon IA + Saúde Digital

> **Formato:** 4 horas | 2 equipes | ~20 pessoas cada
> **Entregável final:** Pitch de 15 minutos com proposta de solução baseada em IA

---

## 🩺 Trilha 1 — Equipe TeleEletiva

### Contexto
Teleconsulta eletiva é uma consulta médica agendada por vídeo ou chat. O paciente agenda com antecedência, passa pela triagem e é atendido por um médico de forma remota.

---

### Desafio TE-01 — Reduzir No-Show com IA

**Problema real:**
30% dos pacientes agendados não comparecem à teleconsulta eletiva, gerando ociosidade médica, perda de acesso para outros pacientes e custo operacional sem retorno.

**O que vocês precisam responder:**
- Como a IA pode identificar quem tem maior risco de não comparecer?
- Que ação preventiva (mensagem, ligação, reagendamento) é mais eficaz para cada perfil?
- Como fazer isso de forma escalável sem aumentar custo operacional?

**Métricas de sucesso:**
| Métrica | Hoje (hipotético) | Meta |
|---------|-------------------|------|
| Taxa de no-show | 30% | < 15% |
| Taxa de reagendamento | 10% | > 25% |
| Tempo ocioso médico/dia | 1,5h | < 30min |

**Entregável esperado:**
1. Proposta de solução com IA (como funciona, quais dados usa)
2. Exemplo de prompt que vocês testaram e funcionou
3. Métrica principal para medir sucesso
4. Um risco assistencial que precisaria ser gerenciado

---

### Desafio TE-02 — Triagem Inteligente de Sintomas

**Problema real:**
25% dos pacientes são direcionados ao especialista errado na primeira consulta, gerando reencaminhamento, atraso no cuidado e consulta desperdiçada.

**O que vocês precisam responder:**
- Como a IA pode entender a queixa principal e sugerir o especialista correto?
- Que perguntas de triagem aumentam a precisão sem aumentar abandono do fluxo?
- Como garantir segurança clínica em triagem automatizada?

**Métricas de sucesso:**
| Métrica | Hoje | Meta |
|---------|------|------|
| Taxa de encaminhamento incorreto | 25% | < 8% |
| Tempo até consulta correta | 12 dias | < 5 dias |
| Taxa de resolução na 1ª consulta | 60% | > 80% |

---

### Desafio TE-03 — Adesão ao Cuidado Pós-Consulta

**Problema real:**
40% dos pacientes não seguem as orientações pós-teleconsulta por falta de clareza ou esquecimento, gerando reconsulta desnecessária em menos de 30 dias.

**O que vocês precisam responder:**
- Como a IA pode transformar o resumo médico em linguagem acessível ao paciente?
- Que tipo de lembrete aumenta adesão sem ser invasivo?
- Como personalizar por perfil (idade, escolaridade, cronicidade)?

---

## 🔄 Trilha 2 — Equipe TeleInterconsulta

### Contexto
Teleinterconsulta é uma consulta entre médicos (generalista + especialista) via plataforma digital. O médico generalista pede apoio ao especialista para um caso específico, sem necessidade do paciente estar presente.

---

### Desafio TI-01 — Estruturar Pedido de Interconsulta com IA

**Problema real:**
70% dos pedidos de teleinterconsulta chegam ao especialista com informações incompletas (sem exames, sem histórico, sem pergunta objetiva), gerando resposta inadequada ou necessidade de contato adicional.

**O que vocês precisam responder:**
- Que informações são essenciais para cada especialidade?
- Como a IA pode guiar o generalista a estruturar melhor o pedido?
- Como reduzir o tempo entre pedido e resposta qualificada?

**Métricas de sucesso:**
| Métrica | Hoje | Meta |
|---------|------|------|
| Completude do pedido | 30% | > 85% |
| Tempo de resposta do especialista | 48h | < 12h |
| Taxa de retrabalho por info incompleta | 40% | < 10% |

**Entregável esperado:**
1. Proposta de assistente de IA para estruturar pedidos
2. Template de pedido testado com o modelo
3. Métrica principal para medir sucesso
4. Um risco que precisaria ser gerenciado

---

### Desafio TI-02 — Priorizar Casos por Urgência com IA

**Problema real:**
Especialistas recebem 20-50 pedidos diários sem critério claro de priorização. Respondem por ordem de chegada mesmo quando há casos clínicos críticos aguardando há horas.

**O que vocês precisam responder:**
- Como a IA pode classificar urgência clínica a partir do texto do pedido?
- Quais sinais linguísticos/clínicos indicam necessidade de resposta imediata?
- Como equilibrar priorização automática com responsabilidade médica?

**Métricas de sucesso:**
| Métrica | Hoje | Meta |
|---------|------|------|
| Tempo de resposta casos críticos | 48h | < 2h |
| Taxa de priorização correta | 45% | > 90% |
| Satisfação do médico generalista | NPS 20 | NPS 50+ |

---

### Desafio TI-03 — Síntese Clínica para Resposta Mais Rápida

**Problema real:**
Especialistas levam em média 20 minutos para ler, interpretar e responder uma interconsulta por falta de resumo estruturado, limitando a capacidade de atender mais casos por dia.

**O que vocês precisam responder:**
- Como a IA pode pré-processar o pedido e gerar um resumo útil para o especialista?
- Que formato de resumo reduz tempo de leitura sem perder informação clínica relevante?
- Como a IA pode sugerir rascunho de resposta sem substituir o julgamento clínico?

---

## 🏆 Critérios de Avaliação

| Critério | Peso | O que avaliar |
|----------|------|---------------|
| **Clareza do problema** | 25% | O problema está bem definido? A dor é real? |
| **Uso da IA** | 30% | A IA realmente ajuda? O prompt foi testado? |
| **Viabilidade** | 20% | É possível implementar em 6 meses? |
| **Impacto** | 15% | Qual métrica melhora? Em quanto? |
| **Risco assistencial** | 10% | O risco foi identificado e mitigado? |

---

## 📋 Estrutura do Pitch (15 minutos)

1. **Problema** (2 min) — Qual dor você resolveu? Qual a magnitude?
2. **Solução com IA** (4 min) — Como funciona? Mostre um exemplo real do app
3. **Dados e métricas** (3 min) — O que muda? Como vamos medir?
4. **Riscos e mitigações** (2 min) — O que pode dar errado e como prevenir?
5. **Próximos passos** (2 min) — Se tivesse 30 dias, o que faria primeiro?
6. **Perguntas** (2 min)

---

*Hackathon IA + Saúde Digital | Versão 1.0*
