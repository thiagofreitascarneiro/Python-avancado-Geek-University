'''
Utilizadno Lambdas

Conhecidas por Expressões Lambdas, ou simplismente Lambdas, são funções sem nome, ou seja,
funções anônimas.

# Função em Python

def soma(a, b):
    return a + b

def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# Expressão Lambda
lambda x: 3 * x + 1

# como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo(' FELICITY       ', ' jones '))

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também

amar = lambda: 'como não amar python'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Outro exemplo

autores = ['Thiago Freitas', 'Liev Tolstoi', 'Walter Block', 'Ludwig Von Mises', 'Frederic Hayek', 'Thomas Sowell']

print(autores)

# Obs: o Key do sort significa que eu estou escolhendo por qual chave eu quero fazer a ordenação.
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
'''




