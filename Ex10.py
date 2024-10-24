def gerarNotas():
    alunos = []
    for i in range(6):
        lista = []
        for j in range(4):
            nota = float(input(f'Digite a nota do aluno {i+1} na prova {j+1}: '))
            lista.append(nota)
        alunos.append(lista)

    return alunos

def mediaAluno(alunos):
    medias = []
    for i in alunos:
        soma = 0
        for j in i:
            soma += j
        medias.append(soma/4)
    return medias

print(mediaAluno(gerarNotas()))

