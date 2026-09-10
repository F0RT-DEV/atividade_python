#6. Faça um programa para calcular e apresentar o volume de uma lata de óleo, utilizando a fórmula
#volume = 3.14159 ∗ raio ∗ raio ∗ altura. Identifique na fórmula os valores de entrada de dados e leia-
#os via teclado.

raio = float(input("Digite o raio da lata (cm): "))     
altura = float(input("Digite a altura da lata (cm): ")) 

volume = 3.14159 * raio * raio * altura                  
print(f"O volume da lata é {volume} cm³")