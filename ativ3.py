
import pandas as pd
import matplotlib.pyplot as plt


df2018 = pd.read_csv("Dados_PRF_2018.csv", encoding="latin-1", sep=";")
df2019 = pd.read_csv("Dados_PRF_2019.csv", encoding="latin-1", sep=";")
df2020 = pd.read_csv("Dados_PRF_2020.csv", encoding="latin-1", sep=";")
df2021 = pd.read_csv("Dados_PRF_2021.csv", encoding="latin-1", sep=";")
df2022 = pd.read_csv("Dados_PRF_2022.csv", encoding="latin-1", sep=";")


dfs = {
    '2018': df2018,
    '2019': df2019,
    '2020': df2020,
    '2021': df2021,
    '2022': df2022
}


quantidades_acidentes = []
anos = [2018, 2019, 2020, 2021, 2022]
nomes_estados = []

for ano, df in dfs.items():
    estado_max_acidentes = df['uf'].value_counts().idxmax()
    quantidade_acidentes = df[df['uf'] == estado_max_acidentes].shape[0]
    quantidades_acidentes.append(quantidade_acidentes)
    nomes_estados.append(estado_max_acidentes)

plt.figure(figsize=(10, 6))
plt.plot(anos, quantidades_acidentes, marker='o', linestyle='-', color='skyblue')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Acidentes')
plt.title('Quantidade de Acidentes por Ano com Nome do Estado e Quantidade (Gráfico de Linha)')
plt.grid(True)
plt.tight_layout()

for ano, quantidade, nome_estado in zip(anos, quantidades_acidentes, nomes_estados):
    plt.text(ano, quantidade, str(nome_estado), ha='center', va='bottom', fontsize=10, color='black')


plt.xticks(anos, [str(int(ano)) for ano in anos])


plt.show()
