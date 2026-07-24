---
tags: [data-generation, csv, reproducibility, healthcare-safety]
modules: [dados/]
applies_to: [scripts]
confidence: inferred
---
# Pattern: Geração de Dados Sintéticos com Gabarito Oculto

<!-- vibeflow:auto:start -->
## What
Dados fictícios (nunca reais) são gerados por regras probabilísticas explícitas, com seed fixa
para reprodutibilidade entre participantes, e sempre incluem uma coluna "gabarito" (resposta
correta) que fica oculta da lógica de exibição principal — usada só para o participante
comparar depois com o que a IA respondeu.

## Where
`dados/gerar_dados_sinteticos.py` (geração), `dados/analise_noshow.py` (análise exploratória
standalone do mesmo dado), consumidos por `app_hackathon.py` na aba "📊 Dados".

## The Pattern

**Seed fixa no topo do módulo — todo mundo gera o mesmo dataset:**
```python
random.seed(42)  # reprodutivel: todos geram o mesmo conjunto
```

**Regra de risco explícita e comentada, com o alvo (`compareceu`) sendo o gabarito:**
```python
risco = 0.10
risco += hist_noshow * 0.13                      # historico pesa muito
risco += 0.12 if tipo == "primeira_vez" else 0   # 1a vez falta mais
risco += 0.10 if antecedencia >= 15 else 0       # marcou muito longe -> esquece
risco += 0.12 if confirmou == "nao" else -0.08   # confirmacao reduz
risco = min(max(risco, 0.02), 0.95)

compareceu = "nao" if random.random() < risco else "sim"
linhas.append({..., "compareceu": compareceu})  # alvo a prever
```

**Casos-modelo por categoria (não puramente aleatório) para a trilha de priorização, com
`urgencia_real` como gabarito:**
```python
CASOS = {
    "urgente": [("Cardiologia", "Dor toracica em aperto ha 1h, irradia para braco esquerdo..."), ...],
    "prioritario": [...],
    "eletivo": [...],
}
...
linhas.append({..., "urgencia_real": nivel})  # gabarito para comparar com a IA
random.shuffle(linhas)  # embaralha para nao entregar ordenado por urgencia
```

**Análise exploratória do mesmo dado roda como script standalone independente do app:**
```python
def main():
    df = pd.read_csv(BASE / "agendamentos.csv")
    base = (df["compareceu"] == "nao").mean() * 100
    ...
if __name__ == "__main__":
    main()
```

## Rules
- Toda geração de dado fictício fixa `random.seed()` — nunca gerar dado não-reprodutível para
  material de hackathon.
- Toda coluna-alvo (o que a IA deve prever/classificar) é chamada de forma explícita
  como o "gabarito" e mantida na mesma tabela, nunca em arquivo separado — simplifica o
  storytelling didático do exercício.
- Ao embaralhar dados ordenados por categoria (ex: fila por urgência), sempre `random.shuffle`
  no final para não vazar a resposta pela ordem das linhas.
- Nenhum dado real de paciente é usado ou permitido em lugar nenhum do pipeline — reforçado
  também no app (`st.error` na aba Imagem, avisos na aba Transcrição).

## Examples from this codebase
File: dados/gerar_dados_sinteticos.py:52-63 (regra de risco de no-show)
File: dados/gerar_dados_sinteticos.py:115-144 (`gerar_fila`, casos-modelo por urgência)
<!-- vibeflow:auto:end -->

## Anti-patterns (if found)
Nenhum encontrado.
