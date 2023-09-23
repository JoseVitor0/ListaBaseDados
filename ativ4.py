import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
#

df2018 = pd.read_csv("Dados_PRF_2018.csv", encoding="latin-1", sep=";")

df2019 = pd.read_csv("Dados_PRF_2019.csv", encoding="latin-1", sep=";")

df2020 = pd.read_csv("Dados_PRF_2020.csv", encoding="latin-1", sep=";")

df2021 = pd.read_csv("Dados_PRF_2021.csv", encoding="latin-1", sep=";")

df2022 = pd.read_csv("Dados_PRF_2022.csv", encoding="latin-1", sep=";")

print(set(df2018["condicao_metereologica"]))

df_sol2018 = df2018[(df2018["condicao_metereologica"] == "Céu Claro") | (df2018["condicao_metereologica"] == "Sol")] 
df_chuva2018 = df2018[(df2018["condicao_metereologica"] == "Garoa/Chuvisco") | (df2018["condicao_metereologica"] == "Chuva")] 
df_neblina2018 = df2018[df2018["condicao_metereologica"] == "Nevoeiro/Neblina"]

df_sol2019 = df2019[(df2019["condicao_metereologica"] == "Céu Claro") | (df2019["condicao_metereologica"] == "Sol")] 
df_chuva2019 = df2019[(df2019["condicao_metereologica"] == "Garoa/Chuvisco") | (df2019["condicao_metereologica"] == "Chuva")] 
df_neblina2019 = df2019[df2019["condicao_metereologica"] == "Nevoeiro/Neblina"]

df_sol2020 = df2020[(df2020["condicao_metereologica"] == "Céu Claro") | (df2020["condicao_metereologica"] == "Sol")] 
df_chuva2020 = df2020[(df2020["condicao_metereologica"] == "Garoa/Chuvisco") | (df2020["condicao_metereologica"] == "Chuva")] 
df_neblina2020 = df2020[df2020["condicao_metereologica"] == "Nevoeiro/Neblina"]

df_sol2021 = df2021[(df2021["condicao_metereologica"] == "Céu Claro") | (df2021["condicao_metereologica"] == "Sol")] 
df_chuva2021 = df2021[(df2021["condicao_metereologica"] == "Garoa/Chuvisco") | (df2021["condicao_metereologica"] == "Chuva")] 
df_neblina2021 = df2021[df2021["condicao_metereologica"] == "Nevoeiro/Neblina"]

df_sol2022 = df2022[(df2022["condicao_metereologica"] == "Céu Claro") | (df2022["condicao_metereologica"] == "Sol")] 
df_chuva2022 = df2022[(df2022["condicao_metereologica"] == "Garoa/Chuvisco") | (df2022["condicao_metereologica"] == "Chuva")] 
df_neblina2022 = df2022[df2022["condicao_metereologica"] == "Nevoeiro/Neblina"]


mortes_neblina2018 = df_neblina2018["mortos"].sum()
mortes_sol2018 = df_sol2018["mortos"].sum()
mortes_chuva2018 = df_chuva2018["mortos"].sum()

mortes_neblina2019 = df_neblina2019["mortos"].sum()
mortes_sol2019 = df_sol2019["mortos"].sum()
mortes_chuva2019 = df_chuva2019["mortos"].sum()

mortes_neblina2020 = df_neblina2020["mortos"].sum()
mortes_sol2020 = df_sol2020["mortos"].sum()
mortes_chuva2020 = df_chuva2020["mortos"].sum()

mortes_neblina2021 = df_neblina2021["mortos"].sum()
mortes_sol2021 = df_sol2021["mortos"].sum()
mortes_chuva2021 = df_chuva2021["mortos"].sum()

mortes_neblina2022 = df_neblina2022["mortos"].sum()
mortes_sol2022 = df_sol2022["mortos"].sum()
mortes_chuva2022 = df_chuva2022["mortos"].sum()

mortes_chuva = [mortes_chuva2018, mortes_chuva2019, mortes_chuva2020, mortes_chuva2021, mortes_chuva2022]
mortes_sol = [mortes_sol2018, mortes_sol2019, mortes_sol2020, mortes_sol2021, mortes_sol2022]
mortes_neblina = [mortes_neblina2018, mortes_neblina2019, mortes_neblina2020, mortes_neblina2021, mortes_neblina2022]

anos = [2018, 2019, 2020, 2021, 2022]

plt.plot(anos, mortes_chuva, marker='o', linestyle='-', color='blue', label='Chuva')

plt.plot(anos, mortes_sol, marker='o', linestyle='-', color='red', label='Sol')

plt.plot(anos, mortes_neblina, marker='o', linestyle='-', color='green', label='Neblina')


# Personalize o gráfico

plt.xlabel('Ano')

plt.ylabel('Quantidade de Acidentes com Vitimas')

plt.title('Quantidade de Acidentes por situação climática')

plt.legend()


# Adicione rótulos de texto aos pontos
for x, y in zip(anos, mortes_chuva):

   plt.text(x, y, str(y), ha='center', va='bottom', fontsize=10, color='blue')

for x, y in zip(anos, mortes_sol):

   plt.text(x, y, str(y), ha='center', va='top', fontsize=10, color='red')

for x, y in zip(anos, mortes_neblina):

   plt.text(x, y, str(y), ha='center', va='top', fontsize=10, color='green')

# Defina os valores do eixo x igualmente espaçados

plt.xticks(np.arange(min(anos), max(anos) + 1, 1))

# Mostre o gráfico

plt.show()


