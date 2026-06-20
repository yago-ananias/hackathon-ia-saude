# Desafios do Hackathon IA + Saude Digital

> ⚠️ **Arquivo gerado automaticamente** a partir de `exemplos_prompts.json`.
> Nao edite a mao - rode `python gerar_desafios_md.py` apos mudar o JSON.

> **Formato:** 4 horas | 2 equipes (~20 pessoas cada) | Entregavel: pitch de 15 min com solucao baseada em IA

---

## 🩺 Trilha — Equipe Teleconsulta Eletiva

_Consultas medicas agendadas realizadas por video ou chat, sem necessidade de presenca fisica._

### TE-01 — Reduzir No-Show com IA

**Problema real:**  
30% dos pacientes agendados nao comparecem a teleconsulta eletiva, gerando ociosidade medica e perda de acesso para outros pacientes.

**Perguntas-guia:**
- Quais fatores mais influenciam o nao comparecimento?
- Como a IA pode prever quem nao vai comparecer?
- Que tipo de mensagem reduz o no-show sem irritar o paciente?

**Metricas de sucesso:**

| Metrica | Hoje | Meta |
|---------|------|------|
| Taxa de no-show | 30% | < 15% |
| Taxa de reagendamento | 10% | > 25% |
| Tempo ocioso medico/dia | 1,5h | < 30min |

**Dados sinteticos para este desafio:** `dados/agendamentos.csv` (aba 📊 Dados no app)

**Prompts prontos no app:** "Classificar risco de no-show", "Gerar mensagem de lembrete personalizada", "Proposta de solucao completa"

**Entregavel:** 1) Proposta com IA · 2) Prompt testado no app · 3) Metrica principal · 4) Risco assistencial a gerenciar

---

### TE-02 — Triagem Inteligente de Sintomas

**Problema real:**  
Pacientes sao direcionados ao especialista errado em 25% dos casos, gerando reencaminhamento, atraso no cuidado e desperdicio de consulta.

**Perguntas-guia:**
- Como a IA pode entender a queixa principal e sugerir o especialista correto?
- Que perguntas de triagem aumentam a precisao da classificacao?
- Como equilibrar agilidade e seguranca clinica na triagem automatizada?

**Metricas de sucesso:**

| Metrica | Hoje | Meta |
|---------|------|------|
| Taxa de encaminhamento incorreto | 25% | < 8% |
| Tempo ate consulta correta | 12 dias | < 5 dias |
| Taxa de resolucao na 1a consulta | 60% | > 80% |

**Prompts prontos no app:** "Triagem de queixa clinica", "Fluxo de perguntas de triagem"

**Entregavel:** 1) Proposta com IA · 2) Prompt testado no app · 3) Metrica principal · 4) Risco assistencial a gerenciar

---

### TE-03 — Plano de Cuidado Pos-Consulta com IA

**Problema real:**  
40% dos pacientes nao seguem as orientacoes pos-teleconsulta por falta de clareza ou esquecimento, gerando reconsulta desnecessaria em curto prazo.

**Perguntas-guia:**
- Como transformar o resumo medico em linguagem acessivel ao paciente?
- Que tipo de lembrete aumenta adesao sem ser invasivo?
- Como personalizar o plano de cuidado por perfil de paciente?

**Metricas-alvo:** taxa de adesao ao cuidado, taxa de reconsulta em 30 dias, satisfacao do paciente

**Prompts prontos no app:** "Simplificar orientacao medica", "Criar plano de cuidado semanal"

**Entregavel:** 1) Proposta com IA · 2) Prompt testado no app · 3) Metrica principal · 4) Risco assistencial a gerenciar

---

## 🔄 Trilha — Equipe Teleinterconsulta

_Consulta entre medicos (generalista + especialista) por plataforma digital para apoio a decisao clinica, sem necessidade do paciente estar presente._

### TI-01 — Estruturar Pedido de Interconsulta com IA

**Problema real:**  
70% dos pedidos de interconsulta chegam ao especialista com informacoes incompletas, gerando resposta inadequada ou necessidade de contato adicional para esclarecimentos.

**Perguntas-guia:**
- Quais informacoes sao essenciais para cada especialidade?
- Como a IA pode ajudar o generalista a estruturar melhor o pedido?
- Como reduzir o tempo entre pedido e resposta qualificada?

**Metricas de sucesso:**

| Metrica | Hoje | Meta |
|---------|------|------|
| Completude do pedido | 30% | > 85% |
| Tempo de resposta do especialista | 48h | < 12h |
| Taxa de retrabalho por info incompleta | 40% | < 10% |

**Prompts prontos no app:** "Avaliar qualidade do pedido de interconsulta", "Gerar template de pedido completo", "Proposta de assistente de pedido"

**Entregavel:** 1) Proposta com IA · 2) Prompt testado no app · 3) Metrica principal · 4) Risco assistencial a gerenciar

---

### TI-02 — Priorizar Casos por Urgencia com IA

**Problema real:**  
Especialistas recebem filas de 20-50 pedidos diarios sem criterio claro de priorizacao, respondendo por ordem de chegada mesmo quando ha casos criticos aguardando.

**Perguntas-guia:**
- Como a IA pode classificar urgencia clinica sem ver o paciente?
- Quais sinais no pedido indicam necessidade de resposta rapida?
- Como equilibrar priorizacao automatica com responsabilidade clinica?

**Metricas de sucesso:**

| Metrica | Hoje | Meta |
|---------|------|------|
| Tempo de resposta casos criticos | 48h | < 2h |
| Taxa de priorizacao correta | 45% | > 90% |
| Satisfacao do medico generalista | NPS 20 | NPS 50+ |

**Dados sinteticos para este desafio:** `dados/fila_interconsulta.csv` (aba 📊 Dados no app)

**Prompts prontos no app:** "Classificar urgencia de fila de interconsultas", "Definir criterios de priorizacao por especialidade"

**Entregavel:** 1) Proposta com IA · 2) Prompt testado no app · 3) Metrica principal · 4) Risco assistencial a gerenciar

---

### TI-03 — Sintese Clinica para Resposta Mais Rapida

**Problema real:**  
Especialistas levam em media 20 minutos para ler, interpretar e responder uma interconsulta por falta de resumo estruturado, reduzindo capacidade de resposta diaria.

**Perguntas-guia:**
- Como a IA pode pre-processar o pedido para o especialista?
- Que formato de resumo reduz mais o tempo de leitura sem perder informacao?
- Como a IA pode sugerir resposta sem substituir o julgamento clinico?

**Metricas-alvo:** tempo medio de resposta, volume de interconsultas respondidas/dia, qualidade percebida da resposta

**Prompts prontos no app:** "Resumir caso para especialista", "Rascunho de resposta ao generalista"

**Entregavel:** 1) Proposta com IA · 2) Prompt testado no app · 3) Metrica principal · 4) Risco assistencial a gerenciar

---

## 🏆 Criterios de Avaliacao

| Criterio | Peso | O que avaliar |
|----------|------|---------------|
| **Clareza do problema** | 25% | O problema esta bem definido? A dor e real? |
| **Uso da IA** | 30% | A IA realmente ajuda? O prompt foi testado no app? |
| **Viabilidade** | 20% | E possivel implementar em 6 meses? |
| **Impacto** | 15% | Qual metrica melhora? Em quanto? |
| **Risco assistencial** | 10% | O risco foi identificado e mitigado? |

## 📋 Estrutura do Pitch (15 minutos)

1. Problema (2 min) - Qual dor voce resolveu? Qual a magnitude?
2. Solucao com IA (4 min) - Como funciona? Mostre um exemplo real do app
3. Dados e metricas (3 min) - O que muda? Como vamos medir?
4. Riscos e mitigacoes (2 min) - O que pode dar errado e como prevenir?
5. Proximos passos (2 min) - Se tivesse 30 dias, o que faria primeiro?
6. Perguntas (2 min)

---

*Hackathon IA + Saude Digital — desafios derivados de exemplos_prompts.json*
