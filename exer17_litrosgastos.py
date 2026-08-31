tempoPercurso = int(input("Digite o tempo de percurso em horas: "))
velocidadeMedia = int(input("Digite a velocidade média em km/h: "))
kmPercorridos = tempoPercurso * velocidadeMedia
litrosGastos = kmPercorridos / 12
print("Nesta viagem, foram consumidos", litrosGastos, "litros de combustível.")
