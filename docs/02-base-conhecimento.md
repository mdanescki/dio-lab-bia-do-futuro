# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo                     | Formato | Utilização no Agente                                        |
|-----------------------------|---------|-------------------------------------------------------------|
| historico_atendimento.csv   | CSV     | Contextualizar interações anteriores e temas já discutidos  |
| perfil_cliente.json         | JSON    | Personalizar respostas com base no perfil, renda e metas    |
| produtos_financeiros.json   | JSON    | Sugerir produtos adequados ao perfil e aversão a risco      |
| transacoes.csv              | CSV     | Analisar padrão de gastos e emitir alertas por categoria    |
| orcamento.json              | JSON    | Definir limites por categoria e disparar alertas em 80%     |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Sim. Foi adicionado o arquivo orcamento.json na pasta data, contendo
os limites mensais de gasto por categoria (alimentação, moradia,
transporte, saúde e lazer) e um gatilho de alerta configurado em 80%
do limite. Esse arquivo é essencial para o funcionamento do agente,
pois sem ele o Orça não teria parâmetros para comparar os gastos
registrados em transacoes.csv e emitir alertas proativos.

Os demais arquivos (historico_atendimento.csv, perfil_cliente.json,
produtos_financeiros.json e transacoes.csv) foram mantidos como
fornecidos originalmente. 

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON e CSV são carregados no início de cada sessão 
via Python (pandas para CSV, json.load para JSON) e convertidos 
em texto estruturado para compor o contexto do agente.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são incluídos no system prompt em duas camadas:

- Contexto fixo: perfil_cliente.json e orcamento.json são carregados
  uma vez e inseridos no system prompt, definindo quem é o usuário
  e quais são seus limites de gasto.

- Contexto dinâmico: transacoes.csv e historico_atendimento.csv são
  consultados a cada interação para calcular o total gasto por categoria
  e verificar se algum limite foi atingido ou está próximo dos 80%.

- Consulta sob demanda: produtos_financeiros.json é acessado apenas
  quando o usuário pergunta sobre investimentos ou quando o agente
  identifica uma oportunidade de sugerir um produto adequado ao perfil.
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Idade: 32 anos | Profissão: Analista de Sistemas
- Perfil investidor: Moderado | Aceita risco: Não
- Renda mensal: R$ 5.000,00
- Patrimônio total: R$ 15.000,00

Metas:
- Completar reserva de emergência: R$ 10.000 / R$ 15.000 (jun/2026)
- Entrada do apartamento: R$ 0 / R$ 50.000 (dez/2027)

Orçamento mensal por categoria:
- Alimentação:  gasto R$ 570,00 / limite R$ 600,00 (95% — ALERTA)
- Moradia:      gasto R$ 1.380,00 / limite R$ 1.400,00 (98% — ALERTA)
- Transporte:   gasto R$ 295,00 / limite R$ 300,00 (98% — ALERTA)
- Saúde:        gasto R$ 188,00 / limite R$ 200,00 (94% — ALERTA)
- Lazer:        gasto R$ 55,90 / limite R$ 150,00 (37% — OK)

Últimas transações:
- 01/10: Salário — R$ 5.000,00 (entrada)
- 02/10: Aluguel — R$ 1.200,00 (moradia)
- 03/10: Supermercado — R$ 450,00 (alimentação)
- 05/10: Netflix — R$ 55,90 (lazer)
- 07/10: Farmácia — R$ 89,00 (saúde)
- 10/10: Restaurante — R$ 120,00 (alimentação)
- 12/10: Uber — R$ 45,00 (transporte)
- 15/10: Conta de Luz — R$ 180,00 (moradia)
- 20/10: Academia — R$ 99,00 (saúde)
- 25/10: Combustível — R$ 250,00 (transporte)

Histórico de atendimento:
- 15/09: CDB — pergunta sobre rentabilidade e prazos (resolvido)
- 01/10: Tesouro Selic — explicação sobre Tesouro Direto (resolvido)
- 12/10: Metas financeiras — acompanhamento da reserva (resolvido)5
...
```
