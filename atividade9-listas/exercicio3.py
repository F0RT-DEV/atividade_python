listaA = []
listaB = []

for i in range(9):
    valor = int(input(f"Digite o número da posição {i} da listaA: "))
    listaA.append(valor)

for i in range(9):
    valor = int(input(f"Digite o número da posição {i} da listaB: "))
    listaB.append(valor)

listaC = []
for i in range(9):
    diferenca = listaA[i] - listaB[i]
    if diferenca < 0:
        diferenca = listaB[i] - listaA[i]
    listaC.append(diferenca)

print("A lista resultante é:", listaC)