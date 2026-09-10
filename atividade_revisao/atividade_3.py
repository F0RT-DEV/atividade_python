#3. Faça um programa para ler 2 números inteiros, e apresente o quociente e o resto da divisão entre
#eles

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

quociente = num1 // num2
resto = num1 % num2

print(f"Quociente: {quociente}")
print(f"Resto: {resto}")