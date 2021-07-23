matriz = []
for valor in range(3):
    lista = []
    for num in range(3):
        numero = int(input('Digite um número: '))
        lista.append(numero)
    matriz.append(lista)

lista = []
cont = soma = 0
while cont <= 2:
    if soma > 0:
        lista.append(soma)
        soma = 0
        cont = cont + 1
    for i, coluna in enumerate(matriz):
        for indice, num in enumerate(coluna):
            if indice == cont:
                soma = soma + num
print(matriz)
print(lista)







