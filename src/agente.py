import os
import json
import pandas as pd
from google import genai
from config import GEMINI_API_KEY, SYSTEM_PROMPT

client = genai.Client(api_key=GEMINI_API_KEY)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def carregar_dados():
    with open(os.path.join(BASE, "perfil_investidor.json"), "r", encoding="utf-8") as f:
        perfil = json.load(f)
    with open(os.path.join(BASE, "orcamento.json"), "r", encoding="utf-8") as f:
        orcamento = json.load(f)
    with open(os.path.join(BASE, "produtos_financeiros.json"), "r", encoding="utf-8") as f:
        produtos = json.load(f)
    transacoes = pd.read_csv(os.path.join(BASE, "transacoes.csv"))
    historico = pd.read_csv(os.path.join(BASE, "historico_atendimento.csv"))
    return perfil, orcamento, produtos, transacoes, historico

def montar_contexto():
    perfil, orcamento, produtos, transacoes, historico = carregar_dados()
    gastos_categoria = transacoes[transacoes["tipo"] == "saida"].groupby("categoria")["valor"].sum().to_dict()
    alertas = []
    for categoria, limite in orcamento["limites"].items():
        gasto = gastos_categoria.get(categoria, 0)
        percentual = (gasto / limite) * 100
        if percentual >= 100:
            alertas.append(f"CRÍTICO: {categoria} estourou o limite! R$ {gasto:.2f} / R$ {limite:.2f}")
        elif percentual >= 80:
            alertas.append(f"ATENÇÃO: {categoria} em {percentual:.0f}% do limite. R$ {gasto:.2f} / R$ {limite:.2f}")
    contexto = f"""
Dados do Cliente:
- Nome: {perfil['nome']}
- Perfil: {perfil['perfil_investidor']}
- Renda mensal: R$ {perfil['renda_mensal']:.2f}
- Aceita risco: {perfil['aceita_risco']}

Orçamento por categoria:
{json.dumps(orcamento['limites'], ensure_ascii=False, indent=2)}

Gastos atuais:
{json.dumps(gastos_categoria, ensure_ascii=False, indent=2)}

Alertas ativos:
{chr(10).join(alertas) if alertas else 'Nenhum alerta no momento'}
"""
    return contexto

historico_chat = []

def conversar(mensagem):
    contexto = montar_contexto()
    prompt_completo = SYSTEM_PROMPT + "\n\nCONTEXTO DO USUÁRIO:\n" + contexto
    historico_chat.append({"role": "user", "parts": [{"text": mensagem}]})
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=historico_chat,
        config={"system_instruction": prompt_completo}
    )
    resposta = response.text
    historico_chat.append({"role": "model", "parts": [{"text": resposta}]})
    return resposta