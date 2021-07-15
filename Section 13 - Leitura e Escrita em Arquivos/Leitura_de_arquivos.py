'''
Leitura de Arquivos

Para ler o conteudeo de um arquivo em Python, utilizamos a função integrada open(),
queliteralmente significa 'abrir'.

open() - Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html

# OBS: Por padrão, a função open() abre o arquivo para a leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

_io.TextIOWrapper name = 'texto.txt' mode='r' encoding='UTF-8'

mode r - Modo de Leitura read()
'''

# Exemplo

arquivo = open('texto.txt')

# print(arquivo)

# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

ret = arquivo.read()

print(type(ret))

print(ret)

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como cursor quando estamos escrevendo.
#print(arquivo.read())

# OBS: a Função read() lê todo o conteúdo do arquivo.


