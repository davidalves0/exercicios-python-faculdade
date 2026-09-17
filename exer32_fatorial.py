numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
i = 1

while i <= numero:
    fatorial = fatorial * i
    i = i + 1

print(fatorial)