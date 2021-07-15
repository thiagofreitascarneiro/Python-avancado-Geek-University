valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = [[num*valor for valor in valores] for num in range(1, 20) if num % 2 == 0]

print(lista)
print(dir(lista))
