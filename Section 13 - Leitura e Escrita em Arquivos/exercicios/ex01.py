"Programa que lê arquivo"
with open('arq.txt', 'w') as arquivo:
    while True:
        palavra = str(input('Digite qualquer letra: '))
        if palavra != '0':
            arquivo.write(palavra)
            arquivo.write('\n')
        else:
            break


with open('arq.txt', 'r') as arquivo:
    print(arquivo.read())
