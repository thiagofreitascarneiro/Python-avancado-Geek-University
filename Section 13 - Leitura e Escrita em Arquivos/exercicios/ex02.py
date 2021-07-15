'Quantas linhas o arquivo possui'

with open('arq2', 'w') as arquivo:
    cont = 0
    while True:
        frase = input('Escreva uma frase ou sair: ')
        if frase != 'sair':
            arquivo.write(frase)
            arquivo.write('\n')
            cont = cont + 1
        else:
            print(f'O arquivo Possui {cont} linhas.')
            break

