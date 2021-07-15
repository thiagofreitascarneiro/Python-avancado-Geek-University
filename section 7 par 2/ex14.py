from random import randint
matriz = []
cartela = []
cont = contador = 0
cont_cartela = 0
cont_cartela2 = 5
while contador < 5:
    num = randint(0, 100)
    if num not in cartela:
        cartela.append(num)
        cont = cont + 1
    if cont == 5:
        if contador == 1:
            cont_cartela = 5
        if contador > 1:
            cont_cartela = cont_cartela + cont_cartela
        cont_cartela2 = cont_cartela2 + cont_cartela2
        matriz.append(cartela[cont_cartela:cont_cartela2])
        cont = 0
        contador = contador + 1

print(cartela)
print(matriz)
