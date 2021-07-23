num_pasc = int(input('Valor para o triangulo de pascal: '))
lista = []
cont = 1
for i in range(num_pasc):
    lista.append(cont)
    print(lista)
    if len(lista) == 2:
        lista.append(lista[0] + lista[1])
        lista.append(lista[1] + lista[2])
        lista.pop(1)
        lista.pop(2)
    elif len(lista) > 2:
        lista.append(lista[0] + lista[1])
        lista.append(lista[1] + lista[2])
        lista.pop(len(lista) - 1)
        lista.pop(len(lista) - 2)










