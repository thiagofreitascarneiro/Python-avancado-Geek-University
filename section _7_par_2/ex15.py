print('CORREÇÃO DE PROVA')
print(30 * '=')
matriz = []
cont = 0
aluno = 1
for i in range(2):
    lista = []
    for resposta in range(10):
        resposta_aluno = str(input(f'Digite sua resposta aluno {aluno}º:[A, B, C, D] ')).upper()[0]
        lista.append(resposta_aluno)
    aluno = aluno + 1
    matriz.append(lista)

gabarito = ['A', 'B', 'C', 'C', 'D', 'D', 'B', 'A', 'A', 'B']
resultado_aluno = []
ponto = 1
cont = 0
for i in matriz:
    resultado = []
    for resposta in i:
        if resposta == gabarito[cont]:
            resultado.append(ponto)
        cont = cont + 1
        if cont == 10:
            cont = 0
            resultado_aluno.append(resultado)
print(30 * '=')
aluno = 1
for i in resultado_aluno:
    print(f'O aluno {aluno}º tirou {sum(i)}')
    aluno = aluno + 1




