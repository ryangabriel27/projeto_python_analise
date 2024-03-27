import pandas as pd 
import matplotlib.pyplot as plt
import yaml

# Carregar os dados do arquivo YAML
with open('empresa.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Converter os dados em um DataFrame de vendas
df_vendas = pd.DataFrame(data['vendas'])

# Analisar a distribuição de preços dos produtos
precos = df_vendas['preco_unitario']

# Plotar um gráfico de caixa mostrando a distribuição dos preços dos produtos
plt.figure(figsize=(8, 6))
plt.boxplot(precos)
plt.title('Distribuição de Preços dos Produtos')
plt.ylabel('Preço Unitário')
plt.show()

# Calcular o preço médio dos produtos
preco_medio = precos.mean()
print("Preço médio dos produtos:", preco_medio)
