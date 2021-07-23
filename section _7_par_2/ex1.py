lista = [[0, 2, 0, 5, 10], [0, 2, 0, 5, 11], [0, 2, 0, 5, 12], [0, 2, 0, 15, 10], [0, 12, 0, 5, 10]]
cont = 0
for matriz in lista:
    for valor in matriz:
        if valor > 10:
            print(f'{valor}')
            cont = cont + 1

print(f'A quantidade de números 10 na lista são: {cont}')


