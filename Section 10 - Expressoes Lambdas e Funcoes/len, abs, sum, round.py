'''
Len, Abs, Sum, Round

# Len

len() - Retorna o tamanho ( ou seja, o numero de itens) de um iterável.

# Só pra Revisar:

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

# Por debaixo dos panos quando utilizamos a função len() o Python faz o seguinte:

# Duder len
print('Geek University'.__len__())

# ABS

abs() - Retorna  o valor absoluto  de um número  interio ou real, De forma básica, seria o seu valor real sem o sinal.

# exemplos Abs
print(abs(5))
print(abs(-5))

# Sum
# Exemplo

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

# Round

round() - Retorna um numero arredondado para n digito de precisão.
'''

# Exemplo

print(round(10.2))
print(round(10.5))
print(round(1.21213434, 2))


