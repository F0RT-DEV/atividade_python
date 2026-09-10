#8. Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas
#efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre
#suas vendas efetuadas, informar ao final do programa o seu nome, o salário fixo e salário no final
#do mês.

nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas efetuadas no mês: "))

comissao = total_vendas * 0.15
salario_final = salario_fixo + comissao

print(f"Vendedor: {nome}")
print(f"Salário fixo: R$ {salario_fixo:.2f}")
print(f"Salário no final do mês: R$ {salario_final:.2f}")