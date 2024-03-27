import pandas as pd 
import matplotlib.pyplot as plt
import yaml

# Carregue os dados do arquivo YAML
with open('empresa.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Converta os dados em um DataFrame de vendas
df_vendas = pd.DataFrame(data['vendas'])

# Identifique os produtos mais vendidos
produtos_mais_vendidos = df_vendas['produto'].value_counts().head(5)  # Aqui pegamos os top 5 produtos mais vendidos

# Plote um gráfico de barras mostrando os produtos mais vendidos
plt.figure(figsize=(10, 6))
produtos_mais_vendidos.plot(kind='bar', color='skyblue')
plt.title('Produtos Mais Vendidos')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Calcular a receita total gerada por cada produto
receita_por_produto = df_vendas.groupby('produto').apply(lambda x: (x['preco_unitario'] * x['quantidade']).sum())

# Plotar um gráfico de pizza mostrando a distribuição da receita entre os produtos
plt.figure(figsize=(8, 8))
plt.pie(receita_por_produto, labels=receita_por_produto.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição da Receita por Produto')
plt.axis('equal')  # Garante que o gráfico de pizza seja desenhado como um círculo
plt.show()
