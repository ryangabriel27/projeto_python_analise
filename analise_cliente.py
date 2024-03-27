import pandas as pd
import yaml
import matplotlib.pyplot as plt

# Carregar dados do arquivo YAML
with open("empresa.yaml", "r") as file:
    dados = yaml.safe_load(file)

# Criar DataFrame com os dados
df_clientes = pd.DataFrame(dados["comportamento_do_cliente"])
df_vendas = pd.DataFrame(dados["vendas"])

# Adicionando uma coluna 'valor_total_gasto' ao DataFrame de clientes
df_clientes["valor_gasto_total"] = 0.0

# Adicionando uma coluna 'numero_de_compras' ao DataFrame de clientes
df_clientes["numero_de_compras"] = 0

# Verificando cada cliente
for cliente_id in df_clientes["id"]:
    # Filtrar as vendas desse cliente
    vendas_cliente = df_vendas[df_vendas["cliente_id"] == cliente_id]
    # Calcular o total gasto pelo cliente
    total_gasto = vendas_cliente["quantidade"] * vendas_cliente["preco_unitario"]
    total_gasto = total_gasto.sum()
    # Atualizar o DataFrame de clientes com o total gasto pelo cliente
    df_clientes.loc[df_clientes["id"] == cliente_id, "valor_gasto_total"] = total_gasto
    # Contar o número de compras do cliente
    num_compras = len(vendas_cliente)
    # Atualizar o DataFrame de clientes com o número de compras do cliente
    df_clientes.loc[df_clientes["id"] == cliente_id, "numero_de_compras"] = num_compras

# Para encontrar o cliente mais fiel basta verificar qual cliente teve o maior valor gasto total
cliente_mais_fiel = df_clientes[
    df_clientes["valor_gasto_total"] == df_clientes["valor_gasto_total"].max()
]

# ---- HISTOGRAMA DO COMPORTAMENTO DE CLIENTES
plt.figure(figsize=(10, 10))
plt.hist(df_clientes["valor_gasto_total"], bins=50, color="purple", edgecolor="black")
plt.title("Histograma do comportamento de clientes")
plt.xlabel("Valor Total Gasto(R$)")
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x para facilitar a leitura
plt.ylabel("Número de Clientes")
plt.grid(True)
plt.show()


# ---- GRÁFICO FREQUENCIA VS VALOR TOTAL GASTO
plt.figure(figsize=(10, 6))
plt.scatter(
    df_clientes["numero_de_compras"],
    df_clientes["valor_gasto_total"],
    color="black",
    edgecolor="black",
)
plt.title("Valor Total Gasto vs. Frequência de Compras")
plt.xlabel("Frequência de Compras")
plt.ylabel("Valor Total Gasto")
plt.grid(True)

# Destacar o cliente mais fiel no gráfico
plt.scatter(
    cliente_mais_fiel["numero_de_compras"],
    cliente_mais_fiel["valor_gasto_total"],
    color="red",
    label="Cliente Mais Fiel",
)
plt.legend()
plt.show()
