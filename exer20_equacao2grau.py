from math import sqrt

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = (b * b) - (4 * a * c)

if delta < 0:
    print("Sem raízes reais para esta equação.")
else:
    x1 = (-b + (sqrt(delta)) / (2 * a))
    x2 = (-b - (sqrt(delta)) / (2 * a))
    print("As raízes da equação são: x1 =", x1, "e x2 =", x2)