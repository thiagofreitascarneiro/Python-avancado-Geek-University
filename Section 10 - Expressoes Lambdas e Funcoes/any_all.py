'''
Any e All

all() - Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros ? False
print(all([1, 2, 3, 4, 5])) # Todos os números são verdadeiros ? True
print(all([])) # True iteravel vazio

print(all('Geek')) # Todos os números são verdadeiros ? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C'for nome in nomes]))

print(all([letra for letra in 'aeiof' if letra in 'aeiou']))

print(all([num for num in [4, 2, 3, 10, 8] if num % 2 == 1]))

any() - Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

print(any([0, 1, 2, 3, 4, 5])) # True

print(any([0, False, {}, []]))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))
'''







