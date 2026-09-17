valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
if valor1 > valor2:
    menorValor = valor2
    maiorValor = valor1
else: 
    menorValor = valor1
    maiorValor = valor2
for contador in range(menorValor, maiorValor + 1):
    print(contador)