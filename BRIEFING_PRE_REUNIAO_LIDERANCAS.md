# 🎯 Briefing Pré-Reunião com Lideranças

> **Objetivo:** sair da reunião com 2-3 desafios reais por trilha (Teleconsulta Eletiva e Teleinterconsulta), validados, com métricas e output esperado claros.

---

## 📌 Contexto rápido

- **Hackathon em D-40** (40 dias)
- **40 pessoas, 4 horas, presencial**
- **2 trilhas:** Teleconsulta Eletiva e Teleinterconsulta
- **Stack:** Gemma 4 + MedGemma rodando local + app Streamlit pronto
- **Risco atual:** os desafios atuais são hipóteses, não problemas reais da área

Sem esta reunião, o hackathon vai trabalhar em problemas inventados. Esta conversa **destrava 80% do valor pedagógico**.

---

## 🧭 Como conduzir a reunião (45 min)

### Roteiro minuto-a-minuto

| Tempo | Bloco | O que fazer |
|---|---|---|
| **00:00 – 00:05** | Contexto | Explicar o hackathon em 1 minuto + por que essa conversa importa |
| **00:05 – 00:15** | Pergunta 1 | Deixar fluir — não interromper, anotar |
| **00:15 – 00:25** | Perguntas 2 e 3 | Aterrissar em métrica e tarefa concreta |
| **00:25 – 00:35** | Pergunta 4 (Canvas) | Preencher o canvas junto, em voz alta |
| **00:35 – 00:40** | Pergunta 5 | Filtros de segurança / regulatório / LGPD |
| **00:40 – 00:45** | Fechamento | Resumir os desafios extraídos + combinar próximos passos |

### Como abrir a conversa (script de 1 minuto)

> "Estamos organizando um hackathon de 4 horas com 40 pessoas usando IA generativa local. A ideia é dois objetivos juntos: **o time aprende a usar IA com método** e **a gente sai com soluções para problemas reais da sua área**. Vim aqui para garantir o segundo: quero que as 4h sejam usadas em problemas que importam pra você, não em exemplos genéricos. Pode ser bem específico — quanto mais real, mais útil."

---

## 🎤 As 5 Perguntas Estratégicas

### Pergunta 1 — Prioridade real

> *"Se eu pudesse colocar 10 pessoas inteligentes da sua área trabalhando 4 horas em UMA questão, com apoio de IA generativa, em que problema você jogaria essas pessoas? Não precisa ser o problema 'certo' — pode ser o que está te tirando o sono."*

**O que extrair:**
- O problema **top of mind** (não da lista oficial de OKRs, mas o que dói de verdade)
- Tom da resposta — se é urgência ou cansaço crônico
- Se a pessoa hesita ou já vem com problema pronto

**O que evitar:**
- "Melhorar tudo" → puxar para específico: *"se tivesse que escolher UM?"*
- "Não sei" → reformular: *"qual foi a última reclamação ou crise que você teve?"*

---

### Pergunta 2 — Mensurabilidade

> *"Esse problema tem alguma métrica que você acompanha hoje? Qual é o valor atual e qual seria 'bom'?"*

**O que extrair:**
- Métrica oficial da área (no-show %, tempo de resposta, taxa de resolução, NPS, etc.)
- Valor atual aproximado
- Meta ou benchmark

**Por que importa:**
- Sem métrica, equipes não conseguem propor solução verificável
- Vira o critério da rubrica de avaliação

**O que evitar:**
- "A gente sente que..." → forçar quantificação, mesmo aproximada

---

### Pergunta 3 — Tarefa concreta passível de IA

> *"Quem na sua área hoje gasta mais tempo do que deveria com uma tarefa repetitiva, de comunicação, análise ou síntese — algo que talvez IA pudesse acelerar?"*

**O que extrair:**
- Tarefa específica de uma função (ex: enfermeiro triagista, médico interconsultor, agendador)
- Estimativa de tempo gasto / volume
- Onde o gargalo realmente está

**Por que importa:**
- IA generativa brilha em **comunicação, síntese, classificação, geração de texto**
- Não brilha em otimização operacional, previsão estatística ou integração de sistemas

---

### Pergunta 4 — Output útil (Canvas do Desafio)

> *"Imagine que ao final das 4h cada equipe te entrega um conjunto de prompts + uma análise + uma proposta de ação. O que precisaria estar nesse pacote para você dizer 'isso me ajuda na segunda-feira'?"*

**Preencher o Canvas abaixo durante a resposta.**

#### Canvas do Desafio (preencher ao vivo)

```
┌─────────────────────────────────────────────────────────────┐
│ NOME DO DESAFIO:                                            │
│ [Frase curta, ex: "Reduzir no-show em primeira consulta"]   │
├─────────────────────────────────────────────────────────────┤
│ TRILHA: [ ] Teleconsulta Eletiva  [ ] Teleinterconsulta     │
├─────────────────────────────────────────────────────────────┤
│ PROBLEMA EM 1 FRASE:                                        │
│ [Ex: 18% dos pacientes não comparecem na primeira consulta] │
├─────────────────────────────────────────────────────────────┤
│ POR QUE IMPORTA AGORA:                                      │
│ [Urgência: meta do tri, crise, oportunidade, etc.]          │
├─────────────────────────────────────────────────────────────┤
│ MÉTRICA AFETADA:                                            │
│ Nome:        ___________________________________________    │
│ Valor atual: ___________________________________________    │
│ Meta:        ___________________________________________    │
├─────────────────────────────────────────────────────────────┤
│ "DONO" NA ÁREA (quem cuida disso no dia-a-dia):             │
│ [Cargo / pessoa que vai julgar se a solução é boa]          │
├─────────────────────────────────────────────────────────────┤
│ OUTPUT ESPERADO DAS EQUIPES (escolher 1-2):                 │
│ [ ] Prompt + análise textual                                │
│ [ ] Prompt + classificação/triagem de casos                 │
│ [ ] Prompt + comunicação ao paciente/médico (template)      │
│ [ ] Prompt + síntese / resumo de informação                 │
│ [ ] Prompt + roteiro / checklist operacional                │
├─────────────────────────────────────────────────────────────┤
│ DADOS / CONTEXTO QUE EU POSSO FORNECER:                     │
│ [Ex: 5 transcrições anonimizadas, dashboard com KPIs]       │
└─────────────────────────────────────────────────────────────┘
```

---

### Pergunta 5 — Filtros de segurança

> *"Existe algum tema sensível — regulatório, jurídico, dado de paciente, decisão clínica direta — que precisamos evitar nesse desafio?"*

**O que extrair:**
- Restrições de LGPD (não usar prontuário real)
- Decisões clínicas que IA não deve sugerir diretamente (prescrição, diagnóstico)
- Áreas politicamente sensíveis (substituir função, mudar processo aprovado)

**Por que importa:**
- Hackathon educacional não deve flertar com responsabilidade clínica
- Output das equipes não pode causar passivo regulatório
- Bons desafios usam dados **sintéticos** ou **anonimizados**, não reais

---

## ✅ Critérios de Validação — "Esse desafio é hackathonável?"

Use este checklist **durante ou logo após** a reunião. Se um desafio falha em 2+ critérios, repensar:

| # | Critério | OK? |
|---|---|---|
| 1 | Cabe em 4h de trabalho com prompts (não exige código de produção) | ☐ |
| 2 | IA generativa **de fato** ajuda (não é problema de BI, dashboard ou infra) | ☐ |
| 3 | Output esperado é texto, análise, classificação ou síntese (não app funcional) | ☐ |
| 4 | Não envolve dado pessoal real de paciente (LGPD) | ☐ |
| 5 | Líder consegue julgar "isso é bom" ou "isso é genérico" em <2 min | ☐ |
| 6 | Tem métrica concreta associada | ☐ |
| 7 | A solução teria utilidade real **na semana seguinte** ao hackathon | ☐ |

---

## 🚫 Anti-padrões — Desafios a recusar

Se a liderança propor algo nessas categorias, **redirecionar gentilmente**:

| Anti-padrão | Por que não funciona | Como redirecionar |
|---|---|---|
| **"Melhorar a experiência do paciente"** | Muito amplo, não tem foco | *"Que parte específica da experiência? Em que momento da jornada?"* |
| **"Reduzir custo da operação"** | Vago, IA generativa não ataca diretamente | *"Qual atividade hoje consome tempo/dinheiro que IA poderia acelerar?"* |
| **"Substituir [função X]"** | Político + irrealista em 4h | *"Em quais tarefas específicas dessa função IA poderia ser copilota?"* |
| **"Automatizar o processo Y inteiro"** | É infra/RPA, não generative AI | *"Em que etapa específica do processo IA agrega valor de texto/análise?"* |
| **"Analisar a base de dados Z"** | É BI/SQL, não generative AI | *"Tem alguma comunicação ou síntese que sai dessa base que IA poderia melhorar?"* |
| **"Diagnosticar paciente automaticamente"** | Risco regulatório + clínico | *"E se IA apoiasse o profissional na coleta de informação ou organização de hipóteses?"* |

---

## 🎯 Exemplos de Bons Desafios (Calibração)

Para você se calibrar antes da reunião, exemplos do que **um bom desafio se parece**:

### Trilha Teleconsulta Eletiva — exemplos

> **Desafio bom:** *"Criar um prompt que gera 3 versões de mensagem de lembrete de consulta (24h, 6h, 1h antes), personalizadas por perfil de paciente (jovem digital, idoso, primeira consulta vs. recorrente), com objetivo de reduzir no-show. Cada equipe testa, ajusta, e entrega o conjunto + análise de qual estratégia provavelmente funciona melhor."*

> **Desafio bom:** *"Criar um prompt que recebe a queixa em texto livre escrita pelo paciente no agendamento e gera: (1) classificação de urgência (baixa/média/alta), (2) sugestão de especialidade, (3) perguntas de pré-consulta que o paciente deveria responder antes do médico atender."*

### Trilha Teleinterconsulta — exemplos

> **Desafio bom:** *"Criar um prompt que recebe a solicitação de interconsulta escrita pelo médico solicitante e gera: (1) resumo estruturado (queixa, achados, dúvida), (2) lista de informações faltantes que o especialista provavelmente vai pedir, (3) hipóteses iniciais para o especialista revisar."*

> **Desafio bom:** *"Criar um prompt que, dado o parecer do especialista, gera uma resposta em linguagem clara para o médico solicitante + um plano de cuidado estruturado para o paciente em linguagem leiga."*

**Observe o padrão:**
- Tarefa específica de comunicação/síntese
- Output em texto avaliável
- Persona e contexto claros
- Métrica implícita (qualidade, completude, tempo economizado)

---

## 📋 Pós-Reunião — Próximos Passos

Logo depois da reunião (no mesmo dia ou D+1):

1. **Preencher os canvases** em arquivo (`desafios_validados_RASCUNHO.md`)
2. **Validar consigo:** os 4-6 desafios passam no checklist de validação?
3. **Compartilhar de volta** com a liderança em 48h para confirmação
4. **Reescrever** o `desafios_por_trilha.md` oficial com os desafios validados
5. **Marcar** na agenda: checkpoint D-20 com lideranças para confirmação final

---

## 🧠 Dicas finais para a conversa

- **Anotar nas palavras da pessoa** — não traduzir para "languagem PM" enquanto escreve. Quanto mais o desafio soar como a liderança falou, mais a equipe vai entender o problema real.
- **Não defender o hackathon** — se a liderança questionar, ouvir. Pode revelar restrições importantes.
- **Não prometer entregar a solução** — o hackathon entrega **ideias e prompts**, não código produtivo. Calibrar expectativa.
- **Aceitar "não sei" como resposta válida** — se uma pergunta não tem resposta clara, é sinal de que o problema ainda não está maduro. Talvez não vire desafio.
- **Capturar quem pode ajudar** — se a liderança mencionar pessoas-chave da área que conhecem o problema fundo, anotar. Podem virar mentores no dia do hackathon.

---

## ✅ Checklist final — Saiu da reunião com:

- [ ] 2-3 desafios candidatos para **Teleconsulta Eletiva**
- [ ] 2-3 desafios candidatos para **Teleinterconsulta**
- [ ] Cada desafio com canvas preenchido (problema, métrica, output, dono)
- [ ] Filtros de segurança / LGPD documentados
- [ ] Lista de dados/contexto que a liderança pode fornecer
- [ ] Combinação para checkpoint D-20 confirmar versão final
- [ ] Possíveis mentores convidáveis para o dia do hackathon
