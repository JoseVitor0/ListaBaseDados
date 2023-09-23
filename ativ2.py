import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leitura dos DataFrames
df2018 = pd.read_csv("Dados_PRF_2018.csv", encoding="latin-1", sep=";")
df2019 = pd.read_csv("Dados_PRF_2019.csv", encoding="latin-1", sep=";")
df2020 = pd.read_csv("Dados_PRF_2020.csv", encoding="latin-1", sep=";")
df2021 = pd.read_csv("Dados_PRF_2021.csv", encoding="latin-1", sep=";")
df2022 = pd.read_csv("Dados_PRF_2022.csv", encoding="latin-1", sep=";")

# Filtrar acidentes relacionados à ingestão de álcool
def filtrar_ingestao_alcool(df):
    return df[(df["causa_acidente"] == "Ingestão de álcool pelo condutor") | (df["causa_acidente"] == "Ingestão de Álcool")]

# Aplicar o filtro para cada DataFrame
df_alcool2018 = filtrar_ingestao_alcool(df2018)
df_alcool2019 = filtrar_ingestao_alcool(df2019)
df_alcool2020 = filtrar_ingestao_alcool(df2020)
df_alcool2021 = filtrar_ingestao_alcool(df2021)
df_alcool2022 = filtrar_ingestao_alcool(df2022)

# Contar o número total de acidentes relacionados à ingestão de álcool para cada ano
contagens = [
    len(df_alcool2018),
    len(df_alcool2019),
    len(df_alcool2020),
    len(df_alcool2021),
    len(df_alcool2022)
]

anos = [2018, 2019, 2020, 2021, 2022]

# Crie um gráfico de barras
plt.bar(anos, contagens, color='blue')

# Personalize o gráfico
plt.xlabel('Ano')
plt.ylabel('Quantidade de Acidentes')
plt.title('Quantidade Total de Acidentes por Ano - Ingestão de Álcool')

# Adicione rótulos de texto acima das barras
for x, y in zip(anos, contagens):
   plt.text(x, y, str(y), ha='center', va='bottom', fontsize=10, color='blue')

# Defina os valores do eixo x igualmente espaçados
plt.xticks(anos)

# Mostre o gráfico
plt.show()
