nomes = ['Arroz', 'Feijão', 'Macarrão','Açúcar','Sal']
quantidades = [10, 20, 5,15, 8]
precos = [25.00, 8.00, 4.50, 3.00, 2.50]

faturamento_total = 0.0

for i in range(len(nomes)):
    nome = nomes[i]
    quantidade = quantidades[i]
    preco = precos[i]
    
    faturamento_item = quantidade * preco
    faturamento_total += faturamento_item
    
    print(f"Faturamento do {nome}: R$ {faturamento_item:.2f}")

print(f"Faturamento TOTAL da loja: R$ {faturamento_total:.2f}")





"""
outro jeito de fazer

nomes = ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
quantidades = [10, 20, 5, 15, 8]
precos = [25.00, 8.00, 4.50, 3.00, 2.50]

faturamentos = []

for i in range(len(nomes)):
    faturamento = quantidades[i] * precos[i]
    faturamentos.append(faturamento)
    print(f"Faturamento do {nomes[i]}: R$ {faturamento:.2f}")

faturamento_total = sum(faturamentos)

print(f"Faturamento TOTAL da loja: R$ {faturamento_total:.2f}")"""