'''
Sorted

OBS: Não confunda, apesar do nome com a função sort() que já estufdamos em Listas. O( sort()
só funciona em listas.

podemos utilizar o sorted() com qualquer interável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: O sorted, SEMPRE retorna uma lista com os elementos iterável ordenados

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))
print(numeros)

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))
# Adcionando parâmetros ao sorted()

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
            {'username': 'samuel', 'tweets': ["Eu adoro bolos", 'Eu adoro pizzas']},
            {'username': 'carla', 'tweets': ["Eu amo meu gato"]},
            {'username': 'Bob', 'tweets': []},
            {'username': 'Bill', 'tweets': [], 'cor': 'amarelo'},
            {'username': 'Doggo', 'tweets': ["Eu gosto de cães", "Vou sair hoje"]}]

print(usuarios)

# Ordenando por username -Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

# Ultimo exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead skin mask", "tocou": 2},
    {"titulo": "Too old to rock", "tocou": 32},
    {"titulo": "Back in Black", "tocou": 4}
]
# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
'''



