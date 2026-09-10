#2. Escreva um algoritmo para determinar o consumo médio de um automóvel sendo que será
#fornecida via teclado a distância total percorrida pelo automóvel e o total de combustível gasto

distancia = float(input("Digite a distância total percorrida (km): "))
combustivel = float(input("Digite o total de combustível gasto (litros): "))

consumo_medio = distancia / combustivel
print(f"O consumo médio é {consumo_medio:.2f} km/l")