listaA = []

while len(listaA) < 5:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        listaA.append(numero)

listaB = []
for n in listaA:
    listaB.append(n ** 3)

print("A lista com os cubos é:", listaB)