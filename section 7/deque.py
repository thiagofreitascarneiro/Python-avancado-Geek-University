'''
Módulo Collection - Deque

Podemos dizer que o deque é uma lista de alta performance.

'''

from collections import deque

# Criando deques

deq = deque('geek')

# adicionando elementos no deque
deq.append('y')
print(deq)

deq.appendleft('k')

print(deq)

print(deq.pop()) # remove o ultimo elemento

print(deq.popleft()) # Remove e retorna o primeiro elemento
