try:
    with open('arq4', 'w') as arquivo:
        frase = input('Digite uma frase: ')
        caracter = input('Digite um caractere: ')
        arquivo.write(frase)
except:
    print('Erro! Verificar.')

try:
    with open('arq4', 'r') as arquivo:
        cont = 0
        for valor in arquivo.read():
            if caracter == valor:
                cont = cont + 1
        print(f'O caracter mencionado apareceu {cont} vezes')
except:
    print('Erro! Verificar.')