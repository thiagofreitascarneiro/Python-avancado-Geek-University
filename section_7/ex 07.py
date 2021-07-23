lista = []
cont = 0
while cont < 10:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    cont = cont + 1
    if cont == 10:
        for p, v in enumerate(lista):
            if v == max(lista):
                print(f'O maior valor foi {v} na posição {p}')
