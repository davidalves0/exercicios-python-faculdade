tipo_investimento = int(input("Digite o tipo de investimento (1 para poupança, 2 para renda fixa): "))
valor_investimento = float(input("Digite o valor a ser investido: "))

if tipo_investimento == 1:
    valor_corrigido = valor_investimento + (valor_investimento * 0.03)
    print(valor_corrigido)
elif tipo_investimento == 2:
    valor_corrigido = valor_investimento + (valor_investimento * 0.05)
    print(valor_corrigido)