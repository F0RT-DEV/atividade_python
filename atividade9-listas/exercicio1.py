numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

soma = sum(numeros)
print("A soma total é:", soma)