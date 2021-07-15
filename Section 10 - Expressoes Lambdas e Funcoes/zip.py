'''
Zip

zip() - Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados
como entrada em pares.

#Exemplos

lista1 = [1, 2, 5]
lista2 = [4, 5, 8]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla ou dicionario

print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver
# Trabalhando com iteráveis de tamanhos diferentes, irá para quando os elementos do menor
# iterável acabar.

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista3, lista2, lista1)
print(list(zip1))

# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*dados)))

'''

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [90, 32, 97]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# usando map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))

