'''
Vogais substituidas por *
'''

arquivo = input('Insira o arquivo a ser aberto: ')
with open(f'{arquivo}', 'r') as arq:
    with open(f'{arquivo}.modificado.txt', 'w') as arq2:
        letras = arq.read()
        for vogal in letras:
            if vogal in 'aeiou':
                vogal = '*'
                arq2.write(vogal)
            else:
                arq2.write(vogal)






























