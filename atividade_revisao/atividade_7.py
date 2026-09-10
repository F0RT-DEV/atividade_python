#7. Você irá fazer uma viagem internacional e precisa levar seu dinheiro em dólares. Elabore um
#algoritmo para calcular e apresentar o valor da conversão de real (R$) para dólar (US$). O algoritmo
#deverá solicitar o valor da cotação do dólar e quantos Reais(R$) você tem para converter em dólar.
#Ao final mostre a quantidade de dólares que você irá levar para a viagem

cotacao_dolar = float(input("Digite o valor da cotação do dólar: "))
reais = float(input("Digite quantos Reais você tem: "))

dolares = reais / cotacao_dolar
print(f"Você levará US$ {dolares:.2f} para a viagem")