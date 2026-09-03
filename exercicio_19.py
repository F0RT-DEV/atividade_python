#19) Programa "Desconto na compra": peça ao usuário o valor de um produto (float) e a porcentagem de
#desconto (float, ex.: digitar 10 para 10%). Calcule o valor do desconto e o valor final a pagar, e exiba os dois
#valores

valor = float(input("Digite o valor do produto: "))
desconto_pct = float(input("Digite a porcentagem de desconto: "))

desconto = valor * (desconto_pct / 100)
valor_final = valor - desconto

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")