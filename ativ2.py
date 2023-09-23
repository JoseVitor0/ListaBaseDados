#Bibliotecas utilizadas: pandas, matplot e numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#extraindo os dados para cada dataframe
df2018 = pd.read_csv("Dados_PRF_2018.csv", encoding="latin-1", sep=";")
df2019 = pd.read_csv("Dados_PRF_2019.csv", encoding="latin-1", sep=";")
df2020 = pd.read_csv("Dados_PRF_2020.csv", encoding="latin-1", sep=";")
df2021 = pd.read_csv("Dados_PRF_2021.csv", encoding="latin-1", sep=";")
df2022 = pd.read_csv("Dados_PRF_2022.csv", encoding="latin-1", sep=";")

# Aqui está sendo filtrado nos dados, apenas os acidentes que tiveram relação com ingestão de alcool
def filtrar_ingestao_alcool(df):
    return df[(df["causa_acidente"] == "Ingestão de álcool pelo condutor") | (df["causa_acidente"] == "Ingestão de Álcool")]

# Aplicando o filtro para cada DataFrame
df_alcool2018 = filtrar_ingestao_alcool(df2018)
df_alcool2019 = filtrar_ingestao_alcool(df2019)
df_alcool2020 = filtrar_ingestao_alcool(df2020)
df_alcool2021 = filtrar_ingestao_alcool(df2021)
df_alcool2022 = filtrar_ingestao_alcool(df2022)

# Contando o número total de acidentes relacionados à ingestão de álcool para cada ano
contagens = [
    len(df_alcool2018),
    len(df_alcool2019),
    len(df_alcool2020),
    len(df_alcool2021),
    len(df_alcool2022)
]

anos = [2018, 2019, 2020, 2021, 2022]

#Aqui está sendo criado o gráfico, nesse caso será um grafico de barra
plt.bar(anos, contagens, color='blue')

#informações exibidas nos eixos do grafico
plt.xlabel('Ano')
plt.ylabel('Quantidade de Acidentes')
plt.title('Quantidade Total de Acidentes por Ano - Ingestão de Álcool')

#Configurando para exibir em cada barra o valor de acidentes
for x, y in zip(anos, contagens):
   plt.text(x, y, str(y), ha='center', va='bottom', fontsize=10, color='blue')

#Definindo para no eixo x exibir cada ano embaixo das barras
plt.xticks(anos)

#Exibindo o grafico
plt.show()
