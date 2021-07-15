lista = []
cont = 0
while cont < 10:
    valor = int(input('Digite um número: '))
    if valor not in lista:
        lista.append(valor)
    else:
        while valor in lista:
            valor = int(input('O VALOR já foi digitado. Digite outro número: '))
            if valor not in lista:
                lista.append(valor)
                break
    cont = cont + 1

print(lista)


