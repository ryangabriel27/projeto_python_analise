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

# Quantidade média de itens vendidos
quantidade_media_vendas = df_vendas['quantidade'].mean()
print(quantidade_media_vendas) # 1.833

quantidade_media_vendas = df_vendas['quantidade'].mean()
print(quantidade_media_vendas) # 1.833
