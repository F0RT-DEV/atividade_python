#22) Crie o seu próprio programa! Use sua criatividade para pensar em uma situação do dia a dia. Seu
#programa deve pedir pelo menos duas informações com input(), realizar algum cálculo simples e mostrar o
#resultado com print() ou f-string. Descreva em uma frase, antes do código, qual é o objetivo do seu
#programa

valor_conta = float(input("Digite o valor total da conta: "))
pessoas = int(input("Digite quantas pessoas vão dividir a conta: "))
gorjeta_pct = float(input("Digite a porcentagem de gorjeta: "))

gorjeta = valor_conta * (gorjeta_pct / 100)
total = valor_conta + gorjeta
valor_por_pessoa = total / pessoas

print(f"Cada pessoa deve pagar R$ {valor_por_pessoa:.2f}")