limite = int(input("Digite o valor de N para a série: "))
soma_serie = 1
i = 1

while i <= limite:
    fatorial = 1
    j = 1
    
    while j <= i:
        fatorial = fatorial * j
        j = j + 1
        
    soma_serie = soma_serie + (1 / fatorial)
    i = i + 1

print(soma_serie)
