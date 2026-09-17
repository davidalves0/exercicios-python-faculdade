limite = int(input("Digite o valor de N para a série: "))
soma = 0
i = 1

while i <= limite:
    soma = soma + (1 / i)
    i = i + 1

print(soma)