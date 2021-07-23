lst1 = []
lst2 = []
cont = cont2 = cont3 = cont4 = 0
while cont < 5:
    lst1.append(int(input('Digite um numero na lista 1 (não pode repetir o mesmo numero ): ')))
    lst2.append(int(input('Digite um numero na lista 2 (não pode repetir o mesmo numero): ')))
    cont = cont + 1

for i in lst1:
    soma = i + lst2[cont2]
    print(f'A soma de {i} + {lst2[cont2]} é igual a {soma}')
    cont2 = cont2 + 1
    print(20 * '=')
for i in lst1:
    mult = i * lst2[cont3]
    print(f'A multiplicação de {i} x {lst2[cont3]} é igual a {mult}')
    cont2 = cont3 + 1
    print(20 * '=')
for i in lst1:
    if i not in lst2:
        print(f'Os elementos da lista 1 que não existem na lista 2 são: {i}')
for i in lst1:
    if i in lst2:
        print(f'Os elementos da lista 1 que aparecem na lista 2 são {i}')

print(lst1)
print(lst2)
for i in lst2:
    if i not in lst1:
        lst1.append(i)
print(f'Valores das duas lista sem repetir {lst1}')

