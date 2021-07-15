'''
Debugando com PDB

PDB - Python Debugger

Vida de Inseto - Life's Bug

Bug - Inseto

# OBS: A utilização do print para debugar código é uma pratica ruim.
def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debuggger
# Em python, podemos fazer isso em diferentes IDES, como o Pycharm ou tulizando
# o PDB - Python Debugger

# Exemplo com PyCharm

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 0))

# Exemplo com o PDB - Python Debugger - Exemplo 2

# Para utilizaro Pythom Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comando básicos do PDB
# l (listar onde estamos no código
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Para utilizaro Pythom Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comando básicos do PDB
# l (listar onde estamos no código
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)



nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Custamos realizar todos os imports de bibliotecas
# no ínicio do arquivo. Por isso, ao invés de colocarmos o import do pdb no inicio do arquivo,
# nós colocamos somente onde vamos debugar.

# Exemplo com o PDB - Python Debugger - Exemplo 3

# Para utilizaro Pythom Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# A partir do Python 3.7, não pe mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como funçãi built-in (integrada) chamada breakpoint()

# Comando básicos do PDB
# l (listar onde estamos no código
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)



nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 2, 3, 8))

# Como os nomes das variaveis são os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel

# Não coloque nomes não representativos em variáveis. Sempre optar por nomes significativos.
'''



