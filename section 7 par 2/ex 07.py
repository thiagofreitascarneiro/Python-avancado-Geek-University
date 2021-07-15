matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for linha in range(10):
    for coluna in range(10):
        if linha < coluna:
            matriz[linha][coluna] = (2 * linha) + (7 * coluna) - 2
        if linha == coluna:
            matriz[linha][coluna] = (3**2 * linha) - 1
        if linha > coluna:
            matriz[linha][coluna] = ((4 * linha) ** 3) - ((5 * coluna) ** 2) + 1
        print(f"[{matriz[linha][coluna]:^5}]", end='')
    print()


