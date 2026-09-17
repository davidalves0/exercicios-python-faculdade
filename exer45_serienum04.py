numerador = 1
soma = 0

while numerador <= 15:
    denominador = numerador * numerador
    
    if numerador % 2 == 0:
        soma = soma - (numerador / denominador)
    else:
        soma = soma + (numerador / denominador)
        
    numerador = numerador + 1

print(soma)
