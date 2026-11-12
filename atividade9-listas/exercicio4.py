numeros = []

for i in range(5):
    numero = int(input(f"Digite o número da posição {i}: "))
    numeros.append(numero)

maior = max(numeros)
posicao = numeros.index(maior)

print(f"O maior número é {maior} e está na posição {posicao}.")