listas = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for lista in range(0, 5):
    for i in range(0, 5):
        valor = int(input('Digite um valor :'))
        listas[lista][i] = valor
cont = 0
x = int(input('digite o valor a ser procurado: '))
for linha, lista in enumerate(listas):
    for coluna, num in enumerate(lista):
        if x == num:
            print(f'O valor {x} se encontra na linha {linha} e na coluna {coluna}')
    cont = cont + 1
    if x not in lista and cont == len(lista):
        print(f'O valor {x} não se encontra na lista.')



