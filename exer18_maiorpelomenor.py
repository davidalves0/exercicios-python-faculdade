valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
maiorvalor = int
menorvalor = int
if valor1 > valor2:
    maiorvalor = valor1
    menorvalor = valor2
else:
    maiorvalor = valor2
    menorvalor = valor1
print("A diferença entre o maior e o menor valor é de", (maiorvalor - menorvalor))