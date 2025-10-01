# String com os dados do pedido
dados_pedido = "COD:01234|PRODUTO:Coleira Personalizada|QUANTIDADE:2|PRECO_UNITARIO:25.50|STATUS:EM PROCESSAMENTO"



#Extrair o Código do Pedido
inicio_cod = dados_pedido.find("COD:") + 4
fim_cod = dados_pedido.find("|", inicio_cod)
codigo = dados_pedido[inicio_cod:fim_cod]
print(f"Código do pedido: {codigo}")

#Extrair o Nome do Produto
inicio_produto = dados_pedido.find("PRODUTO:") + 8
fim_produto = dados_pedido.find("|QUANTIDADE:")
produto = dados_pedido[inicio_produto:fim_produto]
print(f"Produto: {produto}")



#Calcular o Preço Total
# Extrair quantidade
inicio_quantidade = dados_pedido.find("QUANTIDADE:") + 11
fim_quantidade = dados_pedido.find("|", inicio_quantidade)
quantidade = int(dados_pedido[inicio_quantidade:fim_quantidade])

# Extrair preço unitário
inicio_preco = dados_pedido.find("PRECO_UNITARIO:") + 15
fim_preco = dados_pedido.find("|", inicio_preco)
preco_unitario = float(dados_pedido[inicio_preco:fim_preco])

# Calcular preço total
preco_total = quantidade * preco_unitario
print(f"Preço total: {preco_total}")

#Padronizar o Status
inicio_status = dados_pedido.find("STATUS:") + 7
status = dados_pedido[inicio_status:]
status_minusculo = status.lower()
print(f"status: {status_minusculo}")
