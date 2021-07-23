'''
Faça um programa que permita que o usuário entre com diversos nomes e telefone
para cadastro, e crie um arquivo com essas informações, uma por linha, o suario finaliza
a entrada com '0' para o telefone.
'''

with open('arq13', 'w') as arquivo:
    while True:
        nome = input('Digite seu nome [0] pra sair: ')
        telefone = input('Dgite seu telefone [0] pra sair: ')
        if telefone == '0' or nome == '0':
            break
        arquivo.write(f'{nome} - ')
        arquivo.write(f'{telefone}\n')



