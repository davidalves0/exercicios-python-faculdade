num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

maior = num1
menor = num2

if num2 > num1:
    maior = num2
    menor = num1

numero_atual = menor

while numero_atual <= maior:
    divisores = 0
    i = 1
    
    while i <= numero_atual:
        if numero_atual % i == 0:
            divisores = divisores + 1
        i = i + 1
        
    if divisores == 2:
        print(numero_atual)
        
    numero_atual = numero_atual + 1
