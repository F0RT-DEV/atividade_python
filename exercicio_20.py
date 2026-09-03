#20) Programa "Média com f-string": peça ao usuário três notas (float) de um aluno. Calcule a média
#aritmética das três notas e exiba uma frase completa com o nome do aluno (peça o nome também) e sua
#média, usando f-string.


nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3
print(f"{nome} teve média {media:.2f}")