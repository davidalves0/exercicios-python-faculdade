import math

a = float(input("Digite o valor do coeficiente a:"))
b = float(input("Digite o valor do coeficiente b:"))
c = float(input("Digite o valor do coeficiente c:"))
delta = (b ** 2) - (4 * a * c)
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print("Essas são as raízes da equação: x1 =", x1, "e x2 =", x2)
