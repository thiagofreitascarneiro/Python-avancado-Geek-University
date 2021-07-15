'''
Min e Max

max() - Retorna o maior valor em um iterável ou o maior de dois ou mais elemento.

# Exemplos

lista = (1, 8, 4, 99, 34, 129)
print(max(lista))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 8}
print(max(dicionario.values()))

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

min() - Retorna o menor valor em um iterável ou menor de dois ou mais elementos

# Exemplos

lista = (1, 8, 4, 99, 34, 129)
print(min(lista))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 8}
print(min(dicionario.values()))

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))

print(min('a', 'b', 'c', 'd'))

# Outros exemplos

nomes = ['Arya', 'Jhon', 'Boby', 'Jonny', ' Walther', 'Ollinvander']

print(max(nomes))

print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
'''

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead skin mask", "tocou": 2},
    {"titulo": "Too old to rock", "tocou": 32},
    {"titulo": "Back in Black", "tocou": 4}]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Titulo da musica mais tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# musica mais tocada sem usar max(), min() e lambda?

max = mni = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
    if musica['tocou'] < min:
        min = musica['tocou']

print(max)
print(min)


