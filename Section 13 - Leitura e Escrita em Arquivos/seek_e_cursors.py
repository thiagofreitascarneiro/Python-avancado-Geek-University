'''
Seek e Cursors

seek() - É utilizada para mvimentar o cursor pelo arquivo.

arquivo = open('texto.txt')

print(arquivo.read())

print(arquivo.read())

# seek() - A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um
# parâmetro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)

print(arquivo.read())

# posso usar para qualquer ponto do cursor
arquivo.seek(20)

#readline() - Função que Lê arquivo linha a linha

ret = arquivo.readline()

print(ret)

print(ret.split(' '))

# readlines()

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open(0 é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finaliazar
os trabalhos com o arquivo devemos fechar conexão. Para isso utilizamos a funcao close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivol

3 - Fechar o arquivo;

# 1 abrir o arquivo;
arquivo = open('texto.txt')

#2 - Trabalhar o arquivo
print(arquivo.read())

print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo
arquivo.close()

print(arquivo.closed) # True

# OBS - Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError

'''


arquivo = open('texto.txt')

# Com a função reaad(0 podemos limitar a quantidade de caracteres a serem lidos.
print(arquivo.read(50))

