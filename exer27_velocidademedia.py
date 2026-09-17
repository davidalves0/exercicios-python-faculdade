voltas = int(input("Digite o número de voltas: "))
extensao_metros = float(input("Digite a extensão do circuito em metros: "))
tempo_minutos = float(input("Digite o tempo em minutos: "))

distancia_km = (voltas * extensao_metros) / 1000
tempo_horas = tempo_minutos / 60
velocidade_media = distancia_km / tempo_horas

print(velocidade_media)