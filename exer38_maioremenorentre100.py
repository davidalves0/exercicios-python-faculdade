maior = 0
menor = 0
i = 1

while i <= 100:
    numero = float(input("Digite um número positivo: "))
    
    if i == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
            
    i = i + 1

print(maior)
print(menor)
