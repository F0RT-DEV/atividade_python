#14)Programa "Cartão de visita": peça ao usuário o nome, a idade e a cidade onde mora. Em seguida, exiba
#uma única frase de apresentação juntando essas informações, usando f-string. Exemplo de saída esperada

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite a cidade onde mora: ")

print(f"Olá! Meu nome é {nome}, tenho {idade} anos e moro em {cidade}.")