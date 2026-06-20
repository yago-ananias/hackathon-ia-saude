"""
Analise dos dados sinteticos de no-show (agendamentos.csv).
Calcula a taxa de no-show por fator para revelar o que mais prediz o nao comparecimento.
Roda com biblioteca padrao + pandas:
    python analise_noshow.py
"""

import sys
import pandas as pd
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
BASE = Path(__file__).parent


def taxa_por(df, coluna):
    """Taxa de no-show (%) agrupada por uma coluna."""
    g = df.groupby(coluna)["compareceu"].apply(lambda s: (s == "nao").mean() * 100)
    return g.round(1).sort_values(ascending=False)


def faixa_antecedencia(d):
    if d <= 3:
        return "1-3 dias"
    if d <= 10:
        return "4-10 dias"
    return "11+ dias"


def faixa_idade(i):
    if i < 25:
        return "< 25"
    if i < 45:
        return "25-44"
    if i < 65:
        return "45-64"
    return "65+"


def main():
    df = pd.read_csv(BASE / "agendamentos.csv")
    base = (df["compareceu"] == "nao").mean() * 100
    df["faixa_antecedencia"] = df["dias_antecedencia"].apply(faixa_antecedencia)
    df["faixa_idade"] = df["idade"].apply(faixa_idade)

    print(f"Taxa de no-show GERAL: {base:.1f}% ({len(df)} agendamentos)\n")
    for col, titulo in [
        ("confirmou_presenca", "Confirmou presenca?"),
        ("historico_noshow_6m", "No-shows nos ultimos 6 meses"),
        ("tipo_consulta", "Tipo de consulta"),
        ("faixa_antecedencia", "Antecedencia do agendamento"),
        ("faixa_idade", "Faixa etaria"),
        ("periodo", "Periodo do dia"),
        ("regiao", "Regiao"),
    ]:
        print(f"== {titulo} ==")
        print(taxa_por(df, col).to_string())
        print()


if __name__ == "__main__":
    main()
