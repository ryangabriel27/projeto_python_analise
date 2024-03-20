import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml

# Carregar dados do arquivo YAML
with open("empresa.yaml", "r") as file:
    dados = yaml.safe_load(file)

# Criar DataFrame com os dados
df_clientes = pd.DataFrame(dados['comportamento_do_cliente'])
df_vendas = pd.DataFrame(dados['vendas'])

# Adicionando uma coluna 'valor_total_gasto' ao DataFrame de clientes
df_clientes['valor_gasto_total'] = 0.0

# Iterar sobre cada cliente
for cliente_id in df_clientes['id']:
    # Filtrar as vendas desse cliente
    compras_cliente = df_vendas[df_vendas['cliente_id'] == cliente_id]
    # Calcular o total gasto pelo cliente
    total_gasto = compras_cliente['quantidade'] * compras_cliente['preco_unitario']
    total_gasto = total_gasto.sum()
    # Atualizar o DataFrame de clientes com o total gasto pelo cliente
    df_clientes.loc[df_clientes['id'] == cliente_id, 'valor_gasto_total'] = total_gasto

# Exibir o DataFrame atualizado com o valor total gasto por cliente
print(df_clientes)
    




