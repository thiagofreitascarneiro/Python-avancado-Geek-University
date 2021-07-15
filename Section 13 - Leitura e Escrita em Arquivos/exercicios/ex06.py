'Quantas letras do Alfabeto'

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open('arq6', 'w') as arquivo:
    frase = input('Digite uma frase: ')
    arquivo.write(frase)

with open('arq6', 'r') as arquivo:
    for valor in alfabeto:
        cont = 0
        for letra in arquivo.read():
            if valor == letra:
                cont = cont + 1
            arquivo.seek(0)
        if cont == 0:
            pass
        else:
            print(f'A letra "{valor}" do alfabeto apareceu {cont} vezes')




