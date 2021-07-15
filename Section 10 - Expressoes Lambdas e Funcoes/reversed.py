'''
Reversed

OBS: Não confunda com a função reserve() que estudamos nas listas.

Afunção reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator
'''

# Exemplos

lista = [1, 2, 4, 5, 6]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBs: Em conjuntos, não definimos a ordem dos elementos
# Conjunto (Set)
print(set(reversed(lista)))

# Podemso iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais fdacil com o slice
print('Geek University'[::-1])
