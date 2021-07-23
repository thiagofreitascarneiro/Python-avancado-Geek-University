listas = [[9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9], [9, 9, 9, 9, 9]]
valor = 1
cont = 0
for lista in range(0, 5):
    for coluna in range(0, 5):
        if lista == cont:
            if coluna == cont:
                listas[lista][coluna] = 1
            else:
                if coluna != cont:
                    listas[lista][coluna] = 0
    cont = cont + 1
print(listas)
