#16) Programa "Total da compra": peça ao usuário o preço de um produto (float) e a quantidade comprada
#(int). Calcule o valor total da compra (preço × quantidade) e exiba o resultado usando f-string, no formato:

preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade
print(f"O valor total da compra é R$ {total:.2f}")