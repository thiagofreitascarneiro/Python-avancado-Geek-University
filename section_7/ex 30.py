list1 = []
list2 = []
list3 = []
cont = 0
while cont < 10:
    valor = int(input('Digite um numero na lista 1: '))
    list1.append(valor)
    valor2 = int(input('Digite um numero na lista 2: '))
    list2.append(valor2)
    cont = cont + 1
    if cont == 10:
        for i in list1:
            if i in list2:
                if i not in list3:
                    list3.append(i)

print(list1)
print(list2)
print(f'Os númeoros que contem em ambos os vetores são: {list3}')
