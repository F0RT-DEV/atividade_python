#17) Programa "Cálculo do IMC": peça ao usuário o peso (em kg) e a altura (em metros). Calcule o Índice de
#Massa Corporal usando a fórmula IMC = peso / (altura ** 2) e exiba o resultado.

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")