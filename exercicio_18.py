#18) Programa "Conversor de tempo": peça ao usuário uma quantidade de minutos (int). Calcule quantas
#horas e quantos segundos essa quantidade de minutos representa, e exiba os dois resultados.

minutos = int(input("Digite a quantidade de minutos: "))

horas = minutos / 60
segundos = minutos * 60

print(f"{minutos} minutos equivalem a {horas:.2f} horas")
print(f"{minutos} minutos equivalem a {segundos} segundos")