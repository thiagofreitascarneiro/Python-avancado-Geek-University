matriz = [[1, 30, 4, 20], [2, 5, 78, 90], [12, 13, 9, 10], [11, 44, 7, 6]]

def calc_matriz(matriz):
    cont = 0
    lista = []
    for coluna in matriz:
        for valor in coluna:
            if valor > 10:
                cont = cont + 1
                lista.append(valor)
    return f'Total de valores maiores que 10: {cont} e os valores são {lista}'


print(calc_matriz(matriz))
