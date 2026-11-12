letras = []

for i in range(80):
    letra = input(f"Digite a letra da posição {i}: ").upper()
    letras.append(letra)

contagem_a = letras.count('A')
print("Parte A:")
if contagem_a > 0:
    print("A letra 'A' apareceu", contagem_a, "vezes.")
else:
    print("A letra 'A' não foi encontrada.")

# Parte B
pares = []
for i in range(len(letras) - 1):
    if letras[i] == letras[i + 1]:
        par = letras[i] + letras[i + 1]
        pares.append(par)

print("Parte B:")
print("Total de pares sequenciais:", len(pares))
print("Pares encontrados:", pares)