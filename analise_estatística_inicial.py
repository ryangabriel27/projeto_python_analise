import pandas as pd 
import matplotlib.pyplot as plt
import yaml

# Carregue os dados do arquivo YAML
with open('empresa.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Converta os dados em DataFrames
df_vendas = pd.DataFrame(data['vendas'])
df_clientes = pd.DataFrame(data['comportamento_do_cliente'])
df_produtos = pd.DataFrame(data['desempenho_do_produto'])


# --- Análise Inicial dos Dados ---
# xxxx Vendas xxxx
# Média da quantidade de itens vendidos
quantidade_media_vendas = df_vendas['quantidade'].mean()
# print(quantidade_media_vendas) = 1.833

# Mediana da quantidade de itens vendidos
quantidade_mediana_vendas = df_vendas['quantidade'].median()
# print(quantidade_mediana_vendas) = 2

# Moda da quantidade de itens vendidos
quantidade_moda_vendas = df_vendas['quantidade'].mode()
# print(quantidade_moda_vendas) = 1

# Média do valor das vendas
media_valor_vendas = df_vendas['preco_unitario'].mean()
# print(media_valor_vendas) = 3500

# Mediana do valor das vendas
mediana_valor_vendas = df_vendas['preco_unitario'].median()
# print(mediana_valor_vendas) = 3000

# Moda do valor das vendas
moda_valor_vendas = df_vendas['preco_unitario'].mode()
# print(moda_valor_vendas) = 3500

# xxxx Clientes xxxx
# Média da idade dos clientes
media_idade_clientes = df_clientes['idade'].mean()
# print(media_idade_clientes) = 46.3

# Mediana da idade dos clientes
mediana_idade_clientes = df_clientes['idade'].median()
# print(mediana_idade_clientes) = 46

# moda da idade dos clientes
moda_idade_clientes = df_clientes['idade'].mode()
# print(moda_idade_clientes)

# No momento há diversas colunas vazias nas 3 tabelas, para preenche-la será feita uma análise de dados.
