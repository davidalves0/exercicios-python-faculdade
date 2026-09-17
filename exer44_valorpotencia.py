base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
resultado = 1
i = 1

while i <= expoente:
    resultado = resultado * base
    i = i + 1

print(resultado)
