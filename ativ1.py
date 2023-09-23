#Bibliotecas utilizadas: pandas, matplot e numpy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#extraindo os dados para cada dataframe
df2018 = pd.read_csv("Dados_PRF_2018.csv", encoding="latin-1", sep=";")
df2019 = pd.read_csv("Dados_PRF_2019.csv", encoding="latin-1", sep=";")
df2020 = pd.read_csv("Dados_PRF_2020.csv", encoding="latin-1", sep=";")
df2021 = pd.read_csv("Dados_PRF_2021.csv", encoding="latin-1", sep=";")
df2022 = pd.read_csv("Dados_PRF_2022.csv", encoding="latin-1", sep=";")

#criando novos dataframes separando os periodos dia e noite, em seguida contando o numero de acidentes para cada um - 2018 
df_noite2018 = df2018[df2018["fase_dia"] == "Plena Noite"]
df_dia2018 = df2018[df2018["fase_dia"] == "Pleno dia"]
cont2018dia = df_dia2018["fase_dia"].count()
cont2018noite = df_noite2018["fase_dia"].count()

#criando novos dataframes separando os periodos dia e noite, em seguida contando o numero de acidentes para cada um - 2019
df_noite2019 = df2019[df2019["fase_dia"] == "Plena Noite"]
df_dia2019 = df2019[df2019["fase_dia"] == "Pleno dia"]
cont2019dia = df_dia2019["fase_dia"].count()
cont2019noite = df_noite2019["fase_dia"].count()

#criando novos dataframes separando os periodos dia e noite, em seguida contando o numero de acidentes para cada um - 2020
df_noite2020 = df2020[df2020["fase_dia"] == "Plena Noite"]
df_dia2020 = df2020[df2020["fase_dia"] == "Pleno dia"]
cont2020dia = df_dia2020["fase_dia"].count()
cont2020noite = df_noite2020["fase_dia"].count()

#criando novos dataframes separando os periodos dia e noite, em seguida contando o numero de acidentes para cada um - 2021
df_noite2021 = df2021[df2021["fase_dia"] == "Plena Noite"]
df_dia2021 = df2021[df2021["fase_dia"] == "Pleno dia"]
cont2021dia = df_dia2021["fase_dia"].count()
cont2021noite = df_noite2021["fase_dia"].count()

#criando novos dataframes separando os periodos dia e noite, em seguida contando o numero de acidentes para cada um - 2022
df_noite2022 = df2022[df2022["fase_dia"] == "Plena Noite"]
df_dia2022 = df2022[df2022["fase_dia"] == "Pleno dia"]
cont2022dia = df_dia2022["fase_dia"].count()
cont2022noite = df_noite2022["fase_dia"].count()

#criando uma lista com os numeros de acidentes dia e noite de cada ano para em seguida por no gráfico
periodo_dia = [cont2018dia, cont2019dia, cont2020dia, cont2021dia, cont2022dia]
periodo_noite = [cont2018noite, cont2019noite, cont2020noite, cont2021noite, cont2022noite]
anos = [2018, 2019, 2020, 2021, 2022]

#Configurando o gráfico, que será de linha
plt.plot(anos, periodo_dia, marker='o', linestyle='-', color='blue', label='Dia')
plt.plot(anos, periodo_noite, marker='o', linestyle='-', color='red', label='Noite')

#informações exibidas nos eixos do grafico
plt.xlabel('Ano')
plt.ylabel('Quantidade de Acidentes')
plt.title('Quantidade de Acidentes por Ano (Dia vs. Noite)')
plt.legend()

#Nesse trecho está sendo determinado que em cada ponto do gráfico, no caso cada elemento da lista periodo_dia, será exibido o seu valor
for x, y in zip(anos, periodo_dia):
   plt.text(x, y, str(y), ha='center', va='bottom', fontsize=10, color='blue')

#Nesse trecho está sendo determinado que em cada ponto do gráfico, no caso cada elemento da lista periodo_noite, será exibido o seu valor
for x, y in zip(anos, periodo_noite):
   plt.text(x, y, str(y), ha='center', va='top', fontsize=10, color='red')

#essa parte determina que no eixo x do gráfico, em cada ponto, será mostrado o ano em questão
plt.xticks(np.arange(min(anos), max(anos) + 1, 1))

plt.show()