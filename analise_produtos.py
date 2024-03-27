import pandas as pd
import matplotlib.pyplot as plt
import yaml

# Carregue os dados do arquivo YAML
with open("empresa.yaml", "r") as file:
    data = yaml.safe_load(file)

# Converta os dados em um DataFrame de vendas
df_vendas = pd.DataFrame(data["vendas"])
df_produtos = pd.DataFrame(data["desempenho_produtos"])

# Identifique os produtos mais vendidos
produtos_mais_vendidos = df_vendas["produto"].head()
# Agrupar as vendas por produto e calcular a soma da quantidade vendida de cada produto
vendas_por_produto = (
    df_vendas.groupby("produto")["quantidade"]
    .sum()
    .reset_index(name="quantidade_vendida_por_produto")
)

# Calcular a receita total gerada por cada produto
df_vendas["receita"] = df_vendas["quantidade"] * df_vendas["preco_unitario"]
receita_por_produto = (
    df_vendas.groupby("produto")["receita"]
    .sum()
    .reset_index(name="receita_total_por_produto")
)    

# -- GRÁFICO DE BARRA MOSTRANDO A QUANTIDADE DE PRODUTOS VENDIDA
plt.figure(figsize=(10, 6))
plt.bar(
    vendas_por_produto["produto"],
    vendas_por_produto["quantidade_vendida_por_produto"],
    color="darkblue",
)
plt.title("Quantidade Vendida de Cada Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y")
plt.show()

# -- GRÁFICO DE PIZZA ENTRE AS RECEITAS DOS PRODUTOS
plt.figure(figsize=(8, 8))
plt.pie(
    receita_por_produto["receita_total_por_produto"],
    labels=receita_por_produto["produto"],
    autopct="%1.1f%%",
    startangle=140,
)
plt.title("Receita dos Produtos")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
