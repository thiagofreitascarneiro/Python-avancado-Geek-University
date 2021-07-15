matriz = [[valor + 2 * lista for lista in range(1, 3)] for valor in range(1, 3)]
print(matriz)
opc = 5
while True:
    opc = int(input('''Digite a opção desejada: [1] somar duas matrizes, [2] - subtrair a primeira matriz da segunda 
    [3] - adicionar uma constante em duas matrizes - [4] - imprimir as matrizes e sair do programa
    '''))
    if opc == 1:
        total = sum(matriz[0]) + sum(matriz[1])
        print(f'A soma dos valores das duas matrizes são: {total} ')
        print(30 * '-')
    if opc == 2:
        matriz[0].clear()
        print(matriz)
        print(30 * '-')
    if opc == 3:
        valor = int(input('Digite um valor inteiro para adicionar na matriz: '))
        matriz[0].append(valor)
        matriz[1].append(valor)
        print(30 * '-')
    if opc == 4:
        print('saindo...')
        print(matriz)
        print(30 * '-')
        break