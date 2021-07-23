'''
Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos
(separados por linha), e calcule o total da compra.
'''

with open('arq18', 'w') as arquivo:
    lista_total = []
    while True:
        produto = input('Digite o produto: 0 pra sair ')
        valor = input('Digite o valor do produto: 0 pra sair ')
        lista_total.append(float(valor))
        if produto == '0' or valor == '0':
            total = sum(f'{lista_total}')
            arquivo.write('\n')
            arquivo.write(f'O valor total da sua compra foi de {str(total)}')
            break
        arquivo.write(f'{produto}')
        arquivo.write(f': {valor}')
        arquivo.write('\n')







