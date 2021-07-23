'''
Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas
e o numero de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre
no arquivo (ignorando letras com acento). Obs: palavras são separadas por um ou mais
carateres espaço, tabulação ou nova linha.
'''
from collections import Counter
cont_letras = 0
cont_linhas = 0
cont_palavras = 0

with open('arq12', 'r+') as arquivo:
    with open('arq12.mod', 'w+') as arq:
        texto = arquivo.read().replace(' ', '')
        for letra in texto:
            cont_letras = cont_letras + 1
        arquivo.seek(0)
        palavras = arquivo.read()
        palavra = palavras.split()
        counter = Counter(palavras)
        cont_linhas = len(texto.split('\n'))
        cont_linhas = cont_linhas - 1
        for p in palavra:
            cont_palavras = cont_palavras + 1
        arq.write(f'\n Total de palavras que ocorre no arquivo: {cont_palavras}')
        arq.write(f'\n Total de letra no arquivo: {counter}')
        arq.write(f'\n Total de linha no arquivo: {cont_linhas}')
        arq.write(f'\n Total de cada letras: {cont_letras - cont_linhas}')










