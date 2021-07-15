matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for lista in range(4):
    for valor in range(4):
        num = int(input('Digite um número: '))
        matriz[lista][valor] = num

print(matriz)
maiores = []
for lista in matriz:
    valor = max(lista)
    maiores.append(valor)

print(maiores)