#. Muitos países estão passando a usar o sistema métrico. Preparar um algoritmo para executar a
#conversão de Celsius para Fahrenheit.
#A fórmula de conversão é: F= (9*C+160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura
#em Celsius

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (9 * celsius + 160) / 5
print(f"{celsius}°C equivalem a {fahrenheit}°F")