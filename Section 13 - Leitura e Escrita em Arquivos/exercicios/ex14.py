'''
Dado um arquivo contendo um conjunto de nome e data de nascimento (DD MM AAAA, isto é,
3 inteiros em sequência), faça um programa que leia o nome do arquivo e a data de hoje e
construa outro arquivo contendo o nome e a idade de cada pessoa do primeiro arquivo.


'''
arquivo = input('Informe o nome do arquivo que deseja abrir: ')

data = input('Informe a Data de Hoje (DD MM AAA): ')
ano = data.split()
ano_hoje = int(ano[-1])


with open(f'{arquivo}', 'r') as arq:
    with open(f'{arquivo}.modi', 'w') as arq2:
        list_arq = list(arq)
        for x in range(len(list_arq)):
            n = list_arq[x].split()
            if len(n) == 0:
                pass
            else:
                idade = ano_hoje - int(n[4])
                print(idade)
                arq2.write(f'O/A {n[0]} tem {idade} anos')
                arq2.write('\n')