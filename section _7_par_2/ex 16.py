print('Sistema de Correção de Prova')
print(30 * '=')
matriz = []
lista_matricula = []
for i in range(3):
    lista = []
    matricula = int(input('Digite seu R.A: '))
    lista_matricula.append(matricula)
    for r in range(10):
        resposta = str(input(f'Digite sua resoposta para a {r + 1}º questão:[A, B, C, D, E] ')).upper()[0]
        lista.append(resposta)
    matriz.append(lista)

print('CORREÇÃO DO ALUNO')
print(30 * '=')
cont = 0
gabarito = ['A', 'B', 'D', 'C', 'C', 'B', 'C', 'E', 'E', 'A']
cont_gabarito = 0
lista_pontos = []
for aluno in matriz:
    total_ponto = []
    for nota in aluno:
        if nota == gabarito[cont]:
            total_ponto.append(1)
        cont = cont + 1
        if cont == 10:
            cont = 0
            lista_pontos.append(total_ponto)

cont_matricula = 0
for valor in lista_pontos:
    print(f'O aluno da matricula: {lista_matricula[cont_matricula]} ')
    pontos = sum(valor)
    print(f'Obteve um total de {pontos} pontos.')
    if pontos >= 7:
        print(f'O aluno está APROVADO')
        print(30 * '=')
    else:
        print(f'O aluno está REPROVADO')
        print(30 * '=')
    cont_matricula = cont_matricula + 1




