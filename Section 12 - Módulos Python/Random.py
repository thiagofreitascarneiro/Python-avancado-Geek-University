'''
Módulo Random e o que são modulos?

- Em Python, módulos nada mais são que outros arquivos Python.

Módulo Random - Possui várias funções para geração de números pseudo-aleatório.

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - importando todo o módulo (Não recomendado).

import random

# Ao realizar o import todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponiveis(em memória)
# A maneira correta é importar apenas a função que for usar.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome
# do pacote ew o nome da função, separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função
# random() é apenas uma função dentro do módulo random.

# Forma 2 - Importando uma função específica do módulo (Forma Recomendada)

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())

# uniform() - Gerar um número pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))# 7 não é incluído.

# randint() - Gera valores pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=' ') # de 1 a 60

# choice() - Mostra um valor aleatório entre um iterável.
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

from random import shuffle

# shuffle() - Tem a função de embaralhar dados

cartas = ['k', 'Q', 'J', 'A', '2', '7']

print(cartas)

shuffle(cartas)

print(cartas.pop())
'''




