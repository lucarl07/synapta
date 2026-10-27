<!--
MODELO DE README - DESAFIO SYNAPTA - OPÇÃO 1: ANÁLISE DE PREÇOS DE ALUGUEL EM SÃO PAULO
Substitua tudo que estiver entre [colchetes] e apague os comentários (<!-- -->) antes de entregar.
Não deixe nenhum [colchete] restante no arquivo final.
-->

# Análise de Preços de Aluguel em São Paulo

Análise de preços de aluguel de imóveis da cidade de São Paulo, feita com base no dataset [**Sao Paulo housing prices**](https://www.kaggle.com/datasets/renatosn/sao-paulo-housing-prices), cujos dados foram extraídos em maio de 2023.

Este repositório foi criado como entrega do desafio inicial proposto na Etapa 2 do processo seletivo da SYNAPTA, pelo candidato **Luiz Carlos**, do 4° período do curso de Ciência da Computação.

## 1. Identificação do candidato

| Campo | Informação |
|---|---|
| Nome completo | Luiz Carlos dos Santos Júnior |
| Matrícula | 01805589 |
| Período atual | 4° período |
| Projeto escolhido | Opção 1 - Análise de preços de aluguel em São Paulo |
| GitHub | [Link do repositório](https://github.com/lucarl07/synapta) |

## 2. Objetivo e pergunta orientadora

**Contexto:** [2 ou 3 linhas sobre o tema: imóveis disponíveis para aluguel na cidade de São Paulo e a relação entre localização, área, quantidade de cômodos e valor anunciado.]

**Pergunta orientadora:** Quais características parecem acompanhar os maiores e os menores preços de aluguel, e o que os dados não permitem concluir?

**Tarefas desenvolvidas** (cada uma é respondida na seção indicada):

| # | Tarefa | Onde está |
|---|---|---|
| 1 | Descrever as colunas utilizadas com palavras próprias | Seção 4 |
| 2 | Linhas, colunas, valores ausentes, repetidos e inconsistentes | Seção 3 e Seção 8 |
| 3 | Decisões tomadas na preparação dos dados | Seção 8 |
| 4 | Preço médio e mediano, e por que diferem | Seção 9.1 |
| 5 | Localidades com maiores e menores preços médios | Seção 9.2 |
| 6 | Aluguel x pelo menos duas características | Seções 9.3 e 9.4 |
| 7 | Pelo menos três gráficos legíveis | Seção 9 |
| 8 | Pelo menos cinco conclusões objetivas | Seção 10 |
| 9 | Limitações da análise | Seção 11 |

## 3. Dataset

- **Nome:** Sao Paulo Housing Prices
- **Fonte:** [Link do dataset no Kaggle](https://www.kaggle.com/datasets/renatosn/sao-paulo-housing-prices/data)
- **Licença / condições de uso:** [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed.pt-br)
- **Arquivo principal utilizado:** `data/Sao_Paulo_housing_prices_20230501.csv`
- **Outros arquivos do dataset (se houver):** Nenhum.
- **Dimensões originais:** 11658 linhas x 8 colunas
- **Filtro aplicado (se necessário):** [Ex.: o arquivo mistura anúncios de venda e aluguel; foram mantidos apenas os de aluguel, resultando em N linhas.]

## 4. Descrição das colunas utilizadas

<!-- Descreva com SUAS PRÓPRIAS PALAVRAS o que cada coluna representa. Liste apenas as colunas usadas na análise. -->

| Coluna | Tipo | O que representa |
|---|---|---|
| `[coluna_preco]` | numérica | [Valor do aluguel anunciado, em reais, por mês?] |
| `[coluna_localidade]` | categórica | [Bairro / distrito / região do imóvel] |
| `[coluna_area]` | numérica | [Área do imóvel, em m²] |
| `[coluna_quartos]` | numérica | [Quantidade de quartos] |
| `[coluna_banheiros]` | numérica | [Quantidade de banheiros] |
| `[coluna_vagas]` | numérica | [Vagas de garagem] |

## 5. Ferramentas e tecnologias

- **Linguagem / ferramenta principal:** [Python / Google Colab / Planilha / Power BI]
- **Bibliotecas:** [pandas, numpy, matplotlib, seaborn, ...]
- **Ambiente:** [Google Colab / Jupyter Notebook / VS Code / ...]
- **Versão do Python (se aplicável):** [3.x]

## 6. Estrutura do repositório

```
.
├── README.md             # Este arquivo
├── [notebook.ipynb]      # Arquivo principal da análise
├── requirements.txt      # Dependências (quando houver código Python)
├── images/               # Gráficos usados no README
└── data/
    └── LEIA-ME.md        # Onde baixar o dataset e onde posicioná-lo
```
<!-- Ajuste conforme a ferramenta escolhida (planilha, Power BI, etc.). -->

## 7. Como executar

### 7.1 Baixar os dados
1. Acesse o dataset no Kaggle: [link do dataset]
2. Baixe o arquivo `[nome_do_arquivo.csv]` (é necessário estar logado no Kaggle).
3. Coloque o arquivo na pasta `data/` com o nome `[nome_do_arquivo.csv]`.

### 7.2 Instalar dependências
```bash
git clone [link do repositório]
cd [nome-do-repositorio]
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 7.3 Executar ou visualizar
- **Jupyter:** `jupyter notebook [notebook.ipynb]` e execute as células em ordem.
- **Google Colab:** [link do notebook] (envie o dataset ao ambiente quando solicitado).
- **Planilha / Power BI:** abra `[nome_do_arquivo]` e [instrução de uso, ex.: atualize o caminho da fonte de dados].

## 8. Limpeza e preparação dos dados

**Verificações realizadas:**

| Verificação | Resultado encontrado | Decisão tomada e justificativa |
|---|---|---|
| Valores ausentes | [Ex.: N ausentes na coluna X / nenhum] | [Ex.: linhas removidas porque... / mantidos porque...] |
| Registros repetidos | [Ex.: N duplicatas / nenhuma] | [Ex.: removidas porque... / não houve necessidade] |
| Valores inconsistentes | [Ex.: área igual a zero, preços fora de uma faixa plausível, quartos = 0 em casas] | [Ex.: excluídos / mantidos e por quê] |
| Tipos de dados | [Ex.: preço lido como texto] | [Ex.: convertido para numérico] |
| Filtros ou novas variáveis | [Ex.: apenas aluguel; criação de `preco_por_m2`] | [Por quê] |

<!-- Se nenhuma alteração foi necessária em alguma verificação, registre isso explicitamente: "Nenhuma alteração foi necessária porque ...". -->

**Resultado final:** o conjunto passou de [N linhas x M colunas] para [N' linhas x M' colunas].

## 9. Resultados

<!-- Em cada subseção: o que foi pedido, o resultado (valor, tabela ou gráfico) e uma leitura curta.
Todo gráfico precisa de título, eixos identificados e uma explicação breve do que mostra.
No total, tenha pelo menos 3 gráficos simples e legíveis. -->

### 9.1 Preço médio e mediano do aluguel

| Medida | Valor (R$) |
|---|---|
| Média | [valor] |
| Mediana | [valor] |

**Por que os valores diferem:** [Explicação simples: a média é influenciada por valores muito altos ou muito baixos; a mediana é o valor central e é menos sensível a eles. Relacione com o que você observou nos dados.]

### 9.2 Localidades com maiores e menores preços médios

**Critério de agrupamento:** foram consideradas apenas localidades com no mínimo **[N] registros**, porque [justificativa: médias de grupos muito pequenos não são confiáveis].

| Posição | Localidade | Preço médio (R$) | Nº de registros |
|---|---|---|---|
| Maiores 1 | [local] | [valor] | [n] |
| Maiores 2 | [local] | [valor] | [n] |
| Maiores 3 | [local] | [valor] | [n] |
| Menores 1 | [local] | [valor] | [n] |
| Menores 2 | [local] | [valor] | [n] |
| Menores 3 | [local] | [valor] | [n] |

![Preço médio por localidade](images/grafico_localidades.png)

**O que o gráfico mostra:** [1 ou 2 frases.]

### 9.3 Aluguel x [característica 1 - ex.: área]

![Aluguel x área](images/grafico_area.png)

**O que o gráfico mostra:** [1 ou 2 frases.]

**Observação:** [Relação aparente (positiva, fraca, sem padrão)? Se calculou correlação, informe o valor e lembre que ela não prova causa.]

### 9.4 Aluguel x [característica 2 - ex.: quantidade de quartos]

![Aluguel x quartos](images/grafico_quartos.png)

**O que o gráfico mostra:** [1 ou 2 frases.]

**Observação:** [...]

### 9.5 Comparações adicionais (opcional)
<!-- Banheiros, vagas, preço por m², etc. Apague esta subseção se não usar. -->

## 10. Conclusões

<!-- Mínimo de 5 conclusões objetivas, cada uma apoiada em um resultado da seção 9. -->

1. [Conclusão 1 - ex.: "A mediana do aluguel (R$ X) é menor que a média (R$ Y), indicando valores muito altos que puxam a média para cima."]
2. [Conclusão 2 - sobre as localidades mais caras e mais baratas.]
3. [Conclusão 3 - sobre a relação entre aluguel e a característica 1.]
4. [Conclusão 4 - sobre a relação entre aluguel e a característica 2.]
5. [Conclusão 5]

### Resposta à pergunta orientadora

**Quais características parecem acompanhar os maiores e os menores preços?** [Resposta direta, baseada nas conclusões acima.]

**O que os dados não permitem concluir?** [Ex.: não permitem afirmar que a área *causa* o aluguel maior; não mostram o preço efetivamente pago; não representam todos os imóveis da cidade.]

## 11. Limitações da análise

- **Ausência de informações:** [Ex.: faltam dados sobre idade do imóvel, padrão de acabamento, condomínio, proximidade de transporte.]
- **Concentração dos anúncios:** [Ex.: parte dos bairros tem muitos anúncios e outros muito poucos; a faixa de preço predominante pode distorcer as médias.]
- **Preço anunciado x preço negociado:** os valores são os anunciados e podem diferir do valor efetivamente fechado.
- [Outras limitações encontradas, ex.: outliers, período dos dados, qualidade do preenchimento.]

**Possíveis trabalhos futuros:** [O que poderia ser feito com mais tempo ou dados.]

## 12. Declaração sobre o uso de inteligência artificial generativa

<!-- Escolha UMA das opções e apague a outra. Seja honesto e específico. -->

**Opção A - Houve uso:**
Utilizei [nome da ferramenta] para [finalidade: ex.: tirar dúvidas de sintaxe do pandas, revisar a redação do README, estruturar este modelo de documento]. As respostas foram verificadas da seguinte forma: [ex.: executei e testei todo o código, conferi os números calculados diretamente nos dados, comparei com a documentação oficial das bibliotecas]. As decisões de limpeza, a interpretação dos resultados e as conclusões são de minha autoria.

**Opção B - Não houve uso:**
Declaro que não utilizei inteligência artificial generativa na elaboração deste projeto.

## 13. Referências

- [Sao Paulo Housing Prices - Kaggle](https://www.kaggle.com/datasets/...)
- [Documentação das bibliotecas utilizadas]
- [Outros materiais consultados]

---
Desenvolvido por **[Seu nome completo]** - [Sua matrícula] - [Ano]

<!--
CHECKLIST ANTES DE ENVIAR (apague esta seção depois)

Tarefas do edital:
[ ] Colunas descritas com minhas próprias palavras
[ ] Nº de linhas e colunas informado
[ ] Ausentes, repetidos e inconsistentes verificados (ou registrado que não houve alteração)
[ ] Decisões de preparação explicadas
[ ] Média e mediana calculadas + explicação da diferença
[ ] Maiores e menores preços médios por localidade, com mínimo de registros justificado
[ ] Aluguel comparado com pelo menos 2 características
[ ] Pelo menos 3 gráficos, com título, eixos e explicação
[ ] Pelo menos 5 conclusões objetivas
[ ] Limitações registradas
[ ] Pergunta orientadora respondida (incluindo o que os dados não permitem concluir)

Repositório:
[ ] Arquivo principal da análise (notebook, .py, planilha ou .pbix)
[ ] README.md sem nenhum [colchete] restante
[ ] requirements.txt (se usou Python)
[ ] Pasta images/ com os gráficos referenciados
[ ] Dataset NÃO republicado se a licença não permitir (link + instruções)
[ ] Declaração de IA preenchida (uma opção só)
[ ] Repositório público e link testado

E-mail:
[ ] Assunto: Desafio SYNAPTA - [nome completo]
[ ] Corpo: nome completo, matrícula, período atual, projeto escolhido e link do GitHub
-->
