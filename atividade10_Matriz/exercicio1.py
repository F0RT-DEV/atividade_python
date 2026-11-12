matriz_notas = [
    [6.0, 7.0, 7.5, 8.0, 10.0],   
    [9.0, 8.0, 7.0, 8.0, 8.0],    
    [5.0, 7.5, 8.0, 8.0, 7.0],    
    [5.0, 6.0, 8.0, 8.0, 7.0],    
    [6.0, 10.0, 10.0, 9.5, 7.0],  
]

num_alunos = len(matriz_notas)
num_provas = len(matriz_notas[0])


print("-----Média por aluno-----")
for i in range(num_alunos):
    soma = 0
    for j in range(num_provas):
        soma = soma + matriz_notas[i][j]
    media_aluno = soma / num_provas
    print(f"Aluno {i}: {media_aluno:.2f}")

print()


print("-----Maior nota por prova-----")
for j in range(num_provas):
    maior_nota = matriz_notas[0][j]
    for i in range(num_alunos):
        if matriz_notas[i][j] > maior_nota:
            maior_nota = matriz_notas[i][j]
    print(f"Prova {j}: {maior_nota:.2f}")

print()


print("-----Média geral da turma-----")
soma_geral = 0
total_de_notas = 0
for i in range(num_alunos):
    for j in range(num_provas):
        soma_geral = soma_geral + matriz_notas[i][j]
        total_de_notas = total_de_notas + 1

media_geral = soma_geral / total_de_notas
print(f"Média geral: {media_geral:.2f}")