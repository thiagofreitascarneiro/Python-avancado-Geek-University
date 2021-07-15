matriz = []
for i in range(10):
    lista = []
    for n in range(3):
        prova = int(input(f'Digite as notas do {i + 1}º aluno: '))
        lista.append(prova)
    matriz.append(lista)

print(matriz)
menor_nota = 0
cont_notas = cont_alunos = 0
lista_notas = []
for alunos in matriz:
    cont_notas = 0
    for notas in alunos:
        if cont_notas == 0:
            menor_nota = alunos[0]
        else:
            if menor_nota > notas:
                menor_nota = notas
        cont_notas = cont_notas + 1
    lista_notas.append(menor_nota)

for aluno, nota in enumerate(lista_notas):
    print(f'A menor nota do {aluno + 1}º aluno {nota}')
    print(30 * '-')










