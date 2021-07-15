'''
O bloco with

Passos para se trabalhar com arquivos

# 1 - Abrir o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with

'''

# O bloco with - Forma Pythônica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readline())
    print(arquivo.closed)


# print(arquivo.read())

print(arquivo.closed)