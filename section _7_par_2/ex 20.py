matriz = [[valor * num for num in range(6)] for valor in range(1, 7)]
print(matriz)
soma = soma2 = 0
for indice, lista in enumerate(matriz):
    if indice % 2 == 1:
        print(f'A soma das colunas {indice} ímpares são:  {sum(lista)}')
    if indice == 2 or indice == 4:
        print(f'A média das colunas {indice} são {sum(lista)/(len(lista))}')
    if indice == 0:
        soma = sum(lista)
    if indice == 1:
        soma2 = sum(lista)
    if indice == 5:
        lista.clear()
        lista.append(soma)
        lista.append(soma2)

print(matriz)