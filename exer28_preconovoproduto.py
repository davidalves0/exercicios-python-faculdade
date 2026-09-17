preco_atual = float(input("Digite o preço atual do produto: "))
venda_mensal = int(input("Digite a quantidade de vendas mensais: "))
preco_novo = preco_atual

if venda_mensal < 500 and preco_atual < 30.00:
    preco_novo = preco_atual + (preco_atual * 0.10)
elif venda_mensal >= 500 and venda_mensal < 1000 and preco_atual >= 30.00 and preco_atual < 80.00:
    preco_novo = preco_atual + (preco_atual * 0.15)
elif venda_mensal >= 1000 and preco_atual >= 80.00:
    preco_novo = preco_atual - (preco_atual * 0.05)

print(preco_novo)