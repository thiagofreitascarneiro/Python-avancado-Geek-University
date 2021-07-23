'''
Faça um programa no qual o usuário informa o nome do arquivo e uma palavra, e retorne
o número de vezes que aquela palavra aparece no arquivo.
'''

arquivo = input('Digite o nome do arquivo: ')
palavra = input('Digite qual palavra deseja procurar no arquivo: ')
contador = 0


with open(f'{arquivo}', 'r') as arq:
    texto = arq.read().lower()
    for letra in texto:
        if letra == palavra:
            contador = contador + 1
    print(f' a palavra "{palavra}" apareceu {contador} vezes.')





