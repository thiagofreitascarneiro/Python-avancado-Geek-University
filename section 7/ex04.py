lista = []
cont = 0
x = int(input('Digite uma posição de 0 a 8:'))
y = int(input('Digite uma posição de 0 a 8:'))
while cont < 8:
    cont = cont + 1
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if cont == 8:
        print(f'A soma dos valores das posições {x} e {y} são: {sum(lista[x:y])} ')


