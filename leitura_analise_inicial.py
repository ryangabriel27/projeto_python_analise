
import pandas as pd 
import matplotlib.pyplot as plt
import yaml

#leitura do conjunto de dados em um DataFrame Pandas
with open('empresa.yaml', 'r') as file:
    data = yaml.safe_load(file)

df_vendas = pd.DataFrame(data['vendas'])
df_clientes = pd.DataFrame(data['comportamento_do_cliente'])
df_produtos = pd.DataFrame(data['desempenho_do_produto'])

#Visualize as primeiras linhas do DAtaFRame para entender a estrurura dos dados
print("Primeiras linhas do DataFrame:")
print(df_clientes.head())
print(df_vendas.head())
print(df_produtos.head())

# Convertendo a coluna 'data' para o formato de data
df_vendas['data'] = pd.to_datetime(df_vendas['data'])

# Extraindo o mês de cada venda
df_vendas['mês'] = df_vendas['data'].dt.month

# Plote um gráfico de barras mostrando a contagem de vendas por mês
plt.figure(figsize=(10, 6))
df_vendas['mês'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Contagem de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Contagem de Vendas')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()