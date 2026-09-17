limite = int(input("Digite o número de termos da série de Fibonacci: "))
termo1 = 0
termo2 = 1
i = 1

while i <= limite:
    print(termo1)
    proximo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo
    i = i + 1
