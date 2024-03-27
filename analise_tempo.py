import pandas as pd
import yaml
import matplotlib.pyplot as plt

# Carregar dados do arquivo YAML
with open("empresa.yaml", "r") as file:
    dados = yaml.safe_load(file)

# Criar DataFrame com os dados de vendas
df_vendas = pd.DataFrame(dados["vendas"])

# Converter a coluna 'data' para o tipo datetime
df_vendas["data"] = pd.to_datetime(df_vendas["data"])

# Agrupar as vendas por data e somar a quantidade de vendas em cada data
vendas_por_data = df_vendas.groupby('data')['quantidade'].sum().cumsum().reset_index(name='soma_quantidade_vendas')

# Criar um gráfico de linha mostrando a soma da quantidade de vendas ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(
    vendas_por_data["data"],
    vendas_por_data["soma_quantidade_vendas"],
    marker="o",
    color="darkgreen",
)
plt.title("Vendas em relação ao tempo")
plt.xlabel("Data (Ano/Mês)")
plt.ylabel("Qntde. de Vendas")
plt.grid(True)
plt.show()
