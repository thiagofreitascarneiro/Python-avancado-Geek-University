'Letras vogais'

try:
    with open('arq3', 'r') as arquivo:
        cont = 0
        # sempre que abrir um arquivo não se esqueça de utilizar a função read()
        for letra in arquivo.read():
            if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
                print(letra)
                cont = cont + 1
except:
    print('arquivo já existe')

print(f'{cont} total de letras vogais.')