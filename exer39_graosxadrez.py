casa = 1
graos_na_casa = 1
total_graos = 0

while casa <= 64:
    total_graos = total_graos + graos_na_casa
    graos_na_casa = graos_na_casa * 2
    casa = casa + 1

print(total_graos)
