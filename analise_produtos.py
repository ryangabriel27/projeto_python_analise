import pandas as pd
import matplotlib.pyplot as plt
import yaml

# Carregue os dados do arquivo YAML
with open("empresa.yaml", "r") as file:
    data = yaml.safe_load(file)

# Converta os dados em um DataFrame de vendas
df_vendas = pd.DataFrame(data["vendas"])
df_produtos = pd.DataFrame(data["desempenho_do_produto"])

# Identifique os produtos mais vendidos
produtos_mais_vendidos = df_vendas["produto"].head()

# Calcular a quantidade vendida e a receita total por produto
df_vendas["receita"] = df_vendas["quantidade"] * df_vendas["preco_unitario"]
vendas_por_produto = (
    df_vendas.groupby("produto")
    .agg(quantidade_vendida=("quantidade", "sum"), receita_total=("receita", "sum"))
    .reset_index()
)

# Atualizar o DataFrame df_produtos com os valores calculados
for index, row in df_produtos.iterrows():
    produto = row["produto"]
    vendas_produto = vendas_por_produto[vendas_por_produto["produto"] == produto]
    if not vendas_produto.empty:
        df_produtos.loc[index, "vendas_totais"] = vendas_produto[
            "quantidade_vendida"
        ].values[0]
        df_produtos.loc[index, "receita_total"] = vendas_produto[
            "receita_total"
        ].values[0]
    else:
        # Se o produto não tiver vendas, atribuir 0
        df_produtos.loc[index, "vendas_totais"] = 0
        df_produtos.loc[index, "receita_total"] = 0


# -- GRÁFICO DE BARRA MOSTRANDO A QUANTIDADE DE PRODUTOS VENDIDA
plt.figure(figsize=(10, 6))
plt.bar(df_produtos["produto"], df_produtos["vendas_totais"], color="darkblue")
plt.title("Quantidade Vendida de Cada Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade Vendida")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y")
plt.show()

# -- GRÁFICO DE PIZZA ENTRE AS RECEITAS DOS PRODUTOS
plt.figure(figsize=(8, 8))
plt.pie(
    df_produtos["receita_total"],
    labels=df_produtos["produto"],
    autopct="%1.1f%%",
    startangle=140,
)
plt.title("Receita Gerada por Produto")
plt.axis("equal")  # Assegura que o gráfico de pizza seja desenhado como um círculo
plt.show()


# Com esses gráficos concluimos que o Ofurô foi o produto mais vendido com mais de 40 unidades vendidas, e o produto que gerou uma maior receita foi o SPA correspondendo a 47.7%
