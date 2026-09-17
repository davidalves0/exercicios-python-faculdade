num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

maior = num1
menor = num2

if num2 > num1:
    maior = num2
    menor = num1

soma_impares = 0
i = menor

while i <= maior:
    if i % 2 != 0:
        soma_impares = soma_impares + i
    i = i + 1

print(soma_impares)
