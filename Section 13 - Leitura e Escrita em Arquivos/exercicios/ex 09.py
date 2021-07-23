'''
Juntando dois arquivos e criando um terceiro
'''

with open('arq9A', 'r') as arq:
    with open('arq9B', 'r') as arq2:
        with open('arq9', 'w') as arquivo:
            soma_arquivo = arq.read() + arq2.read()
            arquivo.write(soma_arquivo)

