import math

catetoB = float(input("Digite o valor do cateto B: "))
catetoC = float(input("Digite o valor do cateto C: "))
hipotenusaAoQ = float((catetoB ** 2) + (catetoC ** 2))
print("O valor desta hipotenusa é de", math.sqrt(hipotenusaAoQ))