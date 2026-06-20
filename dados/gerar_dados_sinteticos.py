"""
Gerador de DADOS SINTETICOS (ficticios) para o Hackathon IA + Saude Digital.

Gera 2 arquivos CSV para as equipes terem materia-prima realista:
  - agendamentos.csv        -> trilha TeleEletiva (no-show)
  - fila_interconsulta.csv  -> trilha TeleInterconsulta (priorizacao)

Tudo e FICTICIO e gerado por regras probabilisticas. Nenhum dado real de paciente.
Usa apenas biblioteca padrao do Python (csv, random). Rode com:
    python gerar_dados_sinteticos.py
"""

import sys
import csv
import random
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

random.seed(42)  # reprodutivel: todos geram o mesmo conjunto
BASE = Path(__file__).parent

# -------------------------------------------------------------------
# 1) AGENDAMENTOS (no-show) - trilha TeleEletiva
# -------------------------------------------------------------------
ESPECIALIDADES = [
    "Cardiologia", "Dermatologia", "Clinica Medica", "Endocrinologia",
    "Ginecologia", "Ortopedia", "Pediatria", "Psiquiatria", "Nutricao",
]
CANAIS = ["WhatsApp", "SMS", "E-mail", "Ligacao"]
PERIODOS = ["manha", "tarde", "noite"]
DIAS = ["seg", "ter", "qua", "qui", "sex", "sab"]


def gerar_agendamentos(n=200):
    linhas = []
    for i in range(1, n + 1):
        idade = random.randint(8, 88)
        sexo = random.choice(["F", "M"])
        esp = random.choice(ESPECIALIDADES)
        tipo = random.choices(["primeira_vez", "retorno"], weights=[40, 60])[0]
        antecedencia = random.choices(
            [1, 2, 3, 5, 7, 10, 15, 21, 30], weights=[6, 8, 10, 12, 14, 12, 12, 10, 16]
        )[0]
        canal = random.choices(CANAIS, weights=[55, 20, 15, 10])[0]
        hist_noshow = random.choices([0, 1, 2, 3], weights=[55, 25, 13, 7])[0]
        regiao = random.choices(["capital", "interior"], weights=[60, 40])[0]
        periodo = random.choice(PERIODOS)
        dia = random.choice(DIAS)
        confirmou = random.choices(["sim", "nao"], weights=[65, 35])[0]

        # ---- Regra de risco (oculta - o time deve "descobrir" no hackathon) ----
        risco = 0.10
        risco += hist_noshow * 0.13                      # historico pesa muito
        risco += 0.12 if tipo == "primeira_vez" else 0   # 1a vez falta mais
        risco += 0.10 if antecedencia >= 15 else 0       # marcou muito longe -> esquece
        risco += 0.12 if confirmou == "nao" else -0.08   # confirmacao reduz
        risco += 0.05 if periodo == "noite" else 0
        risco += 0.04 if regiao == "interior" else 0
        risco += 0.05 if idade < 25 else 0
        risco = min(max(risco, 0.02), 0.95)

        compareceu = "nao" if random.random() < risco else "sim"
        linhas.append({
            "id_paciente": f"P{i:04d}",
            "idade": idade,
            "sexo": sexo,
            "especialidade": esp,
            "tipo_consulta": tipo,
            "dias_antecedencia": antecedencia,
            "canal_preferido": canal,
            "historico_noshow_6m": hist_noshow,
            "regiao": regiao,
            "periodo": periodo,
            "dia_semana": dia,
            "confirmou_presenca": confirmou,
            "compareceu": compareceu,  # alvo a prever
        })
    return linhas


# -------------------------------------------------------------------
# 2) FILA DE INTERCONSULTA (priorizacao) - trilha TeleInterconsulta
# -------------------------------------------------------------------
# Casos-modelo por nivel de urgencia. O 'gabarito' (urgencia_real) permite
# ao time comparar a classificacao da IA com a resposta esperada.
CASOS = {
    "urgente": [
        ("Cardiologia", "Dor toracica em aperto ha 1h, irradia para braco esquerdo, sudorese, PA 90x60."),
        ("Neurologia", "Cefaleia subita de forte intensidade, pior da vida, rigidez de nuca, vomito."),
        ("Endocrinologia", "Glicemia 480, confusao mental, desidratacao, respiracao rapida."),
        ("Pneumologia", "Dispneia importante, satO2 86%, cianose de extremidades, febre."),
        ("Psiquiatria", "Ideacao suicida ativa com plano, paciente agitado, sem rede de apoio."),
        ("Cirurgia", "Dor abdominal intensa em FID, defesa, febre, vomitos ha 12h."),
    ],
    "prioritario": [
        ("Cardiologia", "Dor toracica aos esforcos ha 2 semanas, melhora com repouso, HAS e DM2."),
        ("Endocrinologia", "Glicemia de jejum entre 200-300 nas ultimas semanas, polidipsia."),
        ("Neurologia", "Cefaleia recorrente ha 1 mes, piora matinal, sem deficit focal."),
        ("Nefrologia", "Creatinina subindo em 3 exames, edema de membros, HAS de dificil controle."),
        ("Dermatologia", "Lesao pigmentada que cresceu e mudou de cor em 2 meses."),
        ("Gastroenterologia", "Emagrecimento de 8kg em 2 meses, disfagia progressiva."),
    ],
    "eletivo": [
        ("Endocrinologia", "Hipotireoidismo em acompanhamento, TSH levemente alterado em rotina."),
        ("Cardiologia", "DM2 controlado, deseja segunda opiniao sobre ajuste de medicacao."),
        ("Dermatologia", "Acne leve a moderada, sem sinais de alarme, ha 6 meses."),
        ("Nutricao", "Orientacao nutricional para perda de peso, sem comorbidade aguda."),
        ("Ortopedia", "Dor no joelho ao correr ha meses, melhora com repouso, sem trauma."),
        ("Ginecologia", "Revisao de rotina, exames normais, sem queixas agudas."),
    ],
}


def gerar_fila(n=70):
    linhas = []
    pesos = {"urgente": 20, "prioritario": 35, "eletivo": 45}
    niveis = list(pesos.keys())
    for i in range(1, n + 1):
        nivel = random.choices(niveis, weights=list(pesos.values()))[0]
        esp, resumo = random.choice(CASOS[nivel])
        idade = random.randint(18, 90)
        alarme = "sim" if nivel == "urgente" and random.random() < 0.85 else \
                 ("sim" if random.random() < 0.10 else "nao")
        # pedidos urgentes as vezes esperam demais (o problema a resolver!)
        if nivel == "urgente":
            espera = random.choices([1, 3, 8, 24, 48], weights=[20, 25, 25, 20, 10])[0]
        elif nivel == "prioritario":
            espera = random.choices([6, 12, 24, 48, 72], weights=[15, 25, 30, 20, 10])[0]
        else:
            espera = random.choices([24, 48, 72, 96, 120], weights=[20, 25, 25, 20, 10])[0]
        completude = random.randint(25, 100)
        linhas.append({
            "id_pedido": f"IC{i:04d}",
            "especialidade": esp,
            "idade_paciente": idade,
            "resumo_clinico": resumo,
            "sinais_alarme": alarme,
            "tempo_espera_horas": espera,
            "completude_pedido_pct": completude,
            "urgencia_real": nivel,  # gabarito para comparar com a IA
        })
    random.shuffle(linhas)  # embaralha para nao entregar ordenado por urgencia
    return linhas


def escrever_csv(caminho: Path, linhas: list):
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(linhas[0].keys()))
        writer.writeheader()
        writer.writerows(linhas)


def main():
    ag = gerar_agendamentos(200)
    fila = gerar_fila(70)
    escrever_csv(BASE / "agendamentos.csv", ag)
    escrever_csv(BASE / "fila_interconsulta.csv", fila)

    # Resumo no console
    faltas = sum(1 for x in ag if x["compareceu"] == "nao")
    print("Dados sinteticos gerados com sucesso:")
    print(f"  - agendamentos.csv ......... {len(ag)} linhas "
          f"(no-show: {faltas} = {faltas/len(ag)*100:.0f}%)")
    dist = {}
    for x in fila:
        dist[x["urgencia_real"]] = dist.get(x["urgencia_real"], 0) + 1
    print(f"  - fila_interconsulta.csv ... {len(fila)} linhas "
          f"(urgente: {dist.get('urgente',0)}, "
          f"prioritario: {dist.get('prioritario',0)}, "
          f"eletivo: {dist.get('eletivo',0)})")


if __name__ == "__main__":
    main()
