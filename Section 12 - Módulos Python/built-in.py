'''
Trabalhando com módulos Builtin ( Módulos integrados, que já vem instalados no Python)

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *
#import random

print(random())

# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))

# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

https://docs.python.org/3/py-modindex.html
'''
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import random, randint, shuffle, choice

print(random())

print(randint(1, 10))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))
