import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
database = pd.read_csv("csv/database.csv")
amostra = database
print(amostra.head())


# Qualitativas:
# amostra["Customer Country"].value_conts()
# amostra["Vehicle Type"].value_conts()
# amostra["Payload Orbit"].value_conts()

# Quantitativa Discreta:
# mostra["Customer Country"].value_counts()

# Quantitativa Contínua:
# amostra["Payload Mass (kg)"].value_conts()


# QUESTÃO 2 - TABELAS DE FREQUÊNCIA
# a) Variável Quantitativa Discreta

freq_pais = amostra["Customer Country"].value_counts()

freq_rel_pais = (freq_pais / freq_pais.sum()) * 100

freq_acum_pais = freq_pais.cumsum()

tabela_discreta = pd.DataFrame({
    "Frequência": freq_pais,
    "Frequência Relativa (%)": freq_rel_pais.round(2),
    "Frequência Acumulada": freq_acum_pais
})

print("TABELA DE FREQUÊNCIA - QUANTITATIVA DISCRETA")
print(tabela_discreta)


# b) Variável Quantitativa Contínua
# Payload Mass (kg)

massa = amostra["Payload Mass (kg)"]

freq_massa = massa.value_counts().sort_index()

freq_rel_massa = (freq_massa / freq_massa.sum()) * 100

freq_acum_massa = freq_massa.cumsum()

tabela_continua = pd.DataFrame({
    "Frequência": freq_massa,
    "Frequência Relativa (%)": freq_rel_massa.round(2),
    "Frequência Acumulada": freq_acum_massa
})

print("\nTABELA DE FREQUÊNCIA - QUANTITATIVA CONTÍNUA")
print(tabela_continua)


# QUESTÃO 3 - GRÁFICOS

# Gráfico 1 - Histograma

plt.figure(figsize=(10,6))

plt.hist(
    amostra["Payload Mass (kg)"],
    bins=10,
    color="skyblue",
    edgecolor="black"
)

plt.title(
    "Distribuição da Massa das Cargas Úteis",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel(
    "Massa da Carga (kg)",
    fontsize=12
)

plt.ylabel(
    "Frequência",
    fontsize=12
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()
plt.show()



# Gráfico 2 - Barras por Órbita

orbita = amostra["Payload Orbit"].value_counts()

plt.figure(figsize=(10,6))

orbita.plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title(
    "Quantidade de Lançamentos por Órbita",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel(
    "Tipo de Órbita",
    fontsize=12
)

plt.ylabel(
    "Quantidade de Lançamentos",
    fontsize=12
)

plt.xticks(rotation=45)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()
plt.show()


# QUESTÃO 4 - ESTATÍSTICA DESCRITIVA
massa = amostra["Payload Mass (kg)"]
media = massa.mean()
mediana = massa.median()
moda = massa.mode()
maxi = massa.max()
mini = massa.min()
ampli = massa.max() - massa.min()
variancia = massa.var()
desvio = massa.std()
print("\nESTATÍSTICA DESCRITIVA")
print("Média: ", media)
print("Mediana: ",mediana)
print("Moda:", moda)
print("Máximo:",maxi)
print("Mínimo:", mini)
print("Amplitude:", ampli)
print("Variância: ",variancia)
print("Desvio Padrão: ",desvio)
print("Quartis")
print("Q1:", massa.quantile(0.25))
print("Q2:", massa.quantile(0.50))
print("Q3:", massa.quantile(0.75))


# Insights
# 1. A média representa a massa média transportada nos lançamentos da amostra.

# 2. A mediana indica o valor central das massas, dividindo os dados em duas partes iguais.

# 3. A amplitude mostra a diferença entre a maior e a menor massa transportada.

# 4. O desvio padrão e a variância indicam o quanto as massas variam em relação à média.

# 5. Os quartis permitem observar como os valores estão distribuídos ao longo da amostra.

# 6. O gráfico de massa mostra a distribuição das cargas transportadas.

# 7. O gráfico de órbitas permite identificar quais tipos de órbita aparecem com maior frequência.