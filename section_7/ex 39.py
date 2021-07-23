vet = []
maior = 0
menor = 0
num = 0
for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))
    if i == 0:
        maior = num
        menor = num
        vet.append(num)
    if num > maior:
        maior = num
        vet.append(maior)
    if num < menor:
        menor = num
        vet.insert(0, menor)
print(vet)