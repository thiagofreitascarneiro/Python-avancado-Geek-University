cont = 0
lista = []
menor = maior = 0
while cont <= 10:
    cont = cont + 1
    valor = int(input('Digite um numero: '))
    if cont == 1:
        lista.append(valor)
        maior = valor
        menor = valor
    if cont > 1:
        if valor >= maior:
            maior = valor
            lista.append(maior)
        elif valor <= menor:
            menor = valor
            lista.insert(0, menor)

print(lista)




