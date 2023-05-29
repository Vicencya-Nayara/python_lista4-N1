#Escreva uma função que receba uma lista de dicionários, onde cada dicionário representa um aluno com as chaves 
#"nome" e "nota". A função deve retornar o nome do aluno com a maior nota.

def aluno_com_maior_nota(alunos):
    maior_nota = 0
    nome_aluno = ""

    for aluno in alunos:
        nota = aluno["nota"]
        
        if nota > maior_nota:
            maior_nota = nota
            nome_aluno = aluno["nome"]

    return nome_aluno

# Obtendo os dados dos alunos
alunos = []
num_alunos = int(input("Digite o número de alunos: "))

for i in range(num_alunos):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    aluno = {"nome": nome, "nota": nota}
    alunos.append(aluno)

# Chamando a função e exibindo o resultado
aluno_maior_nota = aluno_com_maior_nota(alunos)
print("Aluno com maior nota:", aluno_maior_nota)

