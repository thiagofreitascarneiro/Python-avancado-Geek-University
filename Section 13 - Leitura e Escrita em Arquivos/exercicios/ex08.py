'''
convertendo letra maiuscula em minuscula

'''

arquivo = input('Insira o nome do arquivo: ')

try:
    with open(f'{arquivo}', 'r') as arq:
        with open(f'{arquivo}.maiuscula', 'w') as arq2:
            valor = arq.read()
            for letra in valor:
                maisc = letra.upper()
                arq2.write(maisc)
except FileNotFoundError:
    print('problema com arquivo ou diretório.')
