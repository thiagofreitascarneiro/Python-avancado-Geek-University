listas = [[0, 0, 5, 0, 10], [0, 0, 0, 10, 0], [120, 100, 0, 10, 0], [0, 15, 10, 150, 170]]
maior = cont = 0
for coluna in range(0, 4):
    for num in range(0, 4):
        valor = int(input('Digite um valor: '))
        listas[coluna][num] = valor
print(listas)
for c, lista in enumerate(listas):
    for i, valor in enumerate(lista):
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1
        if cont == len(lista) * 4:
            print(f'na Linha {c} na coluna {i} o maior valor foi {maior}')




