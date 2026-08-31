horasTrabalhadas = int(input("Digite o número de horas trabalhadas: "))
valorPorHora = float(input("Digite o valor da hora trabalhada: "))
percentualDesconto = float(input("Digite o percentual de desconto: "))
numeroDescendentes = int(input("Digite o número de descendentes: "))
salarioBruto = horasTrabalhadas * valorPorHora
valorDesconto = salarioBruto * (percentualDesconto / 100)
salarioLiquido = (salarioBruto - valorDesconto) + (100 * numeroDescendentes)
print("Este funcionário receberá o salário líquido de", salarioLiquido)