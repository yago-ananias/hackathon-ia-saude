"""
Gera o arquivo desafios_por_trilha.md a partir de exemplos_prompts.json (fonte unica).

Isso elimina a duplicacao: os desafios vivem so no JSON (consumido pelo app) e o
documento em markdown e DERIVADO automaticamente. Nao edite o .md a mao.

Rode apos qualquer alteracao no JSON:
    python gerar_desafios_md.py
"""

import sys
import json
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
BASE = Path(__file__).parent


def bloco_desafio(d: dict) -> str:
    linhas = [f"### {d['id']} — {d['titulo']}", ""]
    linhas.append(f"**Problema real:**  ")
    linhas.append(d["problema"])
    linhas.append("")
    linhas.append("**Perguntas-guia:**")
    for p in d["perguntas_guia"]:
        linhas.append(f"- {p}")
    linhas.append("")

    if d.get("metricas_detalhe"):
        linhas.append("**Metricas de sucesso:**")
        linhas.append("")
        linhas.append("| Metrica | Hoje | Meta |")
        linhas.append("|---------|------|------|")
        for m in d["metricas_detalhe"]:
            linhas.append(f"| {m['metrica']} | {m['hoje']} | {m['meta']} |")
        linhas.append("")
    else:
        linhas.append("**Metricas-alvo:** " + ", ".join(d["metricas_alvo"]))
        linhas.append("")

    if d.get("dados_relacionados"):
        linhas.append(f"**Dados sinteticos para este desafio:** `{d['dados_relacionados']}` "
                      "(aba 📊 Dados no app)")
        linhas.append("")

    linhas.append(f"**Prompts prontos no app:** " +
                  ", ".join(f'"{p["nome"]}"' for p in d["prompts_exemplo"]))
    linhas.append("")
    linhas.append("**Entregavel:** 1) Proposta com IA · 2) Prompt testado no app · "
                  "3) Metrica principal · 4) Risco assistencial a gerenciar")
    linhas.append("")
    linhas.append("---")
    linhas.append("")
    return "\n".join(linhas)


def main():
    with open(BASE / "exemplos_prompts.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    out = []
    out.append("# Desafios do Hackathon IA + Saude Digital")
    out.append("")
    out.append("> ⚠️ **Arquivo gerado automaticamente** a partir de `exemplos_prompts.json`.")
    out.append("> Nao edite a mao - rode `python gerar_desafios_md.py` apos mudar o JSON.")
    out.append("")
    out.append("> **Formato:** 4 horas | 2 equipes (~20 pessoas cada) | "
               "Entregavel: pitch de 15 min com solucao baseada em IA")
    out.append("")
    out.append("---")
    out.append("")

    emojis = {"teleeletiva": "🩺", "teleinterconsulta": "🔄"}
    for chave, trilha in dados["trilhas"].items():
        emoji = emojis.get(chave, "•")
        out.append(f"## {emoji} Trilha — Equipe {trilha['nome']}")
        out.append("")
        out.append(f"_{trilha['descricao']}_")
        out.append("")
        for d in trilha["desafios"]:
            out.append(bloco_desafio(d))

    # Criterios de avaliacao
    out.append("## 🏆 Criterios de Avaliacao")
    out.append("")
    out.append("| Criterio | Peso | O que avaliar |")
    out.append("|----------|------|---------------|")
    for c in dados["config"]["avaliacao"]:
        out.append(f"| **{c['criterio']}** | {c['peso']} | {c['o_que_avaliar']} |")
    out.append("")

    # Estrutura do pitch
    out.append("## 📋 Estrutura do Pitch (15 minutos)")
    out.append("")
    for i, p in enumerate(dados["config"]["estrutura_pitch"], 1):
        out.append(f"{i}. {p}")
    out.append("")
    out.append("---")
    out.append("")
    out.append("*Hackathon IA + Saude Digital — desafios derivados de exemplos_prompts.json*")
    out.append("")

    destino = BASE / "desafios_por_trilha.md"
    destino.write_text("\n".join(out), encoding="utf-8")
    n_desafios = sum(len(t["desafios"]) for t in dados["trilhas"].values())
    print(f"OK: desafios_por_trilha.md gerado com {n_desafios} desafios "
          f"em {len(dados['trilhas'])} trilhas.")


if __name__ == "__main__":
    main()
