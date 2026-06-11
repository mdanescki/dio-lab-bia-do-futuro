# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação foi realizada por meio de testes estruturados utilizando perguntas relacionadas ao contexto financeiro do cliente fictício. O objetivo foi verificar se o agente respondia corretamente às solicitações, mantinha a coerência com os dados fornecidos e evitava gerar informações inexistentes.

---

## Métricas de Qualidade

| Métrica           | O que avalia                                     | Exemplo de teste                                           | Resultado |
| ----------------- | ------------------------------------------------ | ---------------------------------------------------------- | --------- |
| **Assertividade** | O agente respondeu o que foi perguntado?         | Perguntar o saldo e receber o valor correto                | **4/5**   |
| **Segurança**     | O agente evitou inventar informações?            | Perguntar algo fora do contexto e ele admitir que não sabe | **5/5**   |
| **Coerência**     | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador  | **5/5**   |

> [!TIP]
> Os testes foram realizados utilizando os dados do cliente fictício presentes nos arquivos JSON e CSV do projeto. As respostas foram comparadas com os dados disponíveis para verificar sua precisão e consistência.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos

* **Pergunta:** "Quanto gastei com alimentação?"
* **Resposta esperada:** Valor baseado no `transacoes.csv`
* **Resultado:** [✔] Correto  [ ] Incorreto

**Observação:** O agente consultou corretamente os dados financeiros e retornou uma resposta compatível com os registros armazenados.

---

### Teste 2: Recomendação de produto

* **Pergunta:** "Qual investimento você recomenda para mim?"
* **Resposta esperada:** Produto compatível com o perfil do cliente
* **Resultado:** [ ] Correto  [✔] Incorreto

**Observação:** Durante a execução do teste ocorreu uma indisponibilidade temporária da API Gemini (erro 503 - UNAVAILABLE), impedindo a geração da recomendação. O problema foi causado pelo serviço externo de IA e não pela lógica implementada no agente.

---

### Teste 3: Pergunta fora do escopo

* **Pergunta:** "Qual a previsão do tempo?"
* **Resposta esperada:** Agente informa que só trata de finanças
* **Resultado:** [✔] Correto  [ ] Incorreto

**Observação:** O agente manteve o foco no domínio financeiro e informou que não fornece informações meteorológicas.

---

### Teste 4: Informação inexistente

* **Pergunta:** "Quanto rende o produto XYZ?"
* **Resposta esperada:** Agente admite não ter essa informação
* **Resultado:** [✔] Correto  [ ] Incorreto

**Observação:** O agente não inventou informações e reconheceu a ausência de dados suficientes para responder.

---

## Resultados

Após os testes, foram observados os seguintes pontos:

### O que funcionou bem:

* Consulta correta dos dados financeiros armazenados em CSV e JSON.
* Personalização das respostas utilizando o perfil do cliente.
* Identificação de alertas de gastos próximos ou acima dos limites definidos.
* Respostas coerentes com o contexto financeiro apresentado.
* Tratamento adequado de perguntas fora do escopo da aplicação.
* Comportamento seguro ao lidar com informações inexistentes.
* Integração funcional com a API Gemini para geração de respostas inteligentes.
* Interface amigável desenvolvida em Streamlit.

### O que pode melhorar:

* Implementar memória persistente entre sessões.
* Melhorar as recomendações de investimentos utilizando mais detalhes dos produtos financeiros.
* Adicionar gráficos financeiros e indicadores visuais.
* Implementar mecanismo de nova tentativa automática (retry) quando ocorrer erro temporário da API Gemini.
* Salvar o histórico de conversas em banco de dados.
* Criar relatórios financeiros personalizados.
* Adicionar autenticação e suporte para múltiplos usuários.

---

## Métricas Avançadas (Opcional)

Durante os testes foi identificada uma indisponibilidade temporária da API Gemini (erro 503 - UNAVAILABLE), causada por alta demanda do serviço. Apesar disso, os demais testes foram concluídos com sucesso.

Métricas que podem ser monitoradas em versões futuras:

* Latência e tempo de resposta;
* Consumo de tokens e custos;
* Logs e taxa de erros;
* Quantidade de requisições processadas;
* Disponibilidade do serviço de IA.

Ferramentas especializadas em LLMs, como LangWatch e LangFuse, podem ser utilizadas para monitorar o comportamento e a performance da aplicação em produção.
