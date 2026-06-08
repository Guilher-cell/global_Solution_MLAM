# Análise Estatística de Dados de Lançamentos Espaciais
Integrantes
André Fujinaga - RM569158
Guilherme Belo - RM570079

## Descrição

Este projeto tem como objetivo aplicar conceitos de Estatística Descritiva em uma base de dados real relacionada ao setor espacial.

A análise foi desenvolvida utilizando Python e contempla a construção de tabelas de frequência, gráficos estatísticos e medidas descritivas, permitindo compreender melhor o comportamento dos dados presentes na base analisada.

---

## Objetivos

* Classificar as variáveis presentes na base de dados.
* Construir tabelas de distribuição de frequência.
* Desenvolver gráficos estatísticos para representação dos dados.
* Calcular medidas de tendência central.
* Calcular medidas de dispersão.
* Calcular medidas separatrizes.
* Interpretar estatisticamente os resultados obtidos.

---

## Base de Dados

A base utilizada contém informações sobre lançamentos espaciais, incluindo características das cargas transportadas, países clientes e tipos de órbitas utilizadas nas missões.

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Pandas
* NumPy
* Matplotlib

---

## Variáveis Analisadas

### Variável Quantitativa Discreta

**Quantidade de lançamentos por país cliente**

* Variável obtida a partir da contagem de ocorrências da coluna `Customer Country`.

### Variável Quantitativa Contínua

**Payload Mass (kg)**

* Representa a massa da carga útil transportada em cada lançamento espacial.

---

## Tabelas de Frequência

Foram construídas tabelas contendo:

* Frequência Absoluta
* Frequência Relativa (%)
* Frequência Acumulada

### Tabela 1

Distribuição da quantidade de lançamentos por país cliente.

### Tabela 2

Distribuição da massa das cargas úteis transportadas.

---

## 📈 Gráficos Estatísticos

### Histograma

Representa a distribuição da variável:

* Payload Mass (kg)

O gráfico permite visualizar a concentração e dispersão das massas transportadas.

### Gráfico de Barras

Representa:

* Quantidade de lançamentos por órbita

O gráfico permite identificar quais tipos de órbita aparecem com maior frequência na base de dados.

---

## Estatística Descritiva

As seguintes medidas foram calculadas para a variável **Payload Mass (kg)**.

### Medidas de Tendência Central

* Média
* Mediana
* Moda

### Medidas de Dispersão

* Valor Máximo
* Valor Mínimo
* Amplitude
* Variância
* Desvio Padrão

### Medidas Separatrizes

* Primeiro Quartil (Q1)
* Segundo Quartil (Q2)
* Terceiro Quartil (Q3)

---

## Interpretação dos Resultados

A análise estatística permite compreender o comportamento das massas transportadas nos lançamentos espaciais.

A média e a mediana auxiliam na identificação do valor típico das cargas úteis, enquanto a variância e o desvio padrão mostram o grau de dispersão dos dados.

Os quartis permitem observar como os valores estão distribuídos ao longo da amostra, facilitando a identificação de concentrações e possíveis diferenças entre os lançamentos.

Além disso, a análise da frequência das órbitas utilizadas possibilita compreender quais tipos de missão são mais recorrentes na base estudada.

---

## Conclusão

A utilização de técnicas de Estatística Descritiva possibilitou a análise e interpretação de uma base de dados real do setor espacial.

As tabelas de frequência, os gráficos e as medidas estatísticas forneceram informações relevantes sobre a distribuição dos dados, contribuindo para uma melhor compreensão das características dos lançamentos espaciais analisados.
