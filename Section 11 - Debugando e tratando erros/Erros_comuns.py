'''
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do
nosso código.

Os erros mais comuns:

SyntaxError - Ocorre quando o Python encontra um erro de sintaxe. Ous seja, vocÊ escreveu algo
que o Python não reconhece como parte da linguagem.

# Exemplo SyntaxError

a)
def funcao()
    print('Geek University')

b - def = 1

c - return

2 - NameError - Ocorre quando uma variável ou função não foi definida.

# Exemplos NameError

a - print(geek)

a = 8

if a < 10:
    msg = 'É maior que 10'

print(msg)

3 - # - TypeError - Ocorre quando uma função/operação é aplicada a um tipo errado.

# Exemplo TypeError

print(len(5))

print('Geek' + str(4))

4 - IndexError - Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado
indexado utilizando um índice inválido.

# Exemplos IndexError

lista = ['Geek', ]
print(lista[0][10])

5 - ValueERror - Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo
correto mas valor inapropriado.

Exemplos ValueError

print(int('Geek'))

6 - KeyError - Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError

a -
dic = {'geek': 'university'}
print(dic['geek'])

7 - AttributeError - Ocorre quando uma variável não tem um atributo.

Exemplos AtributeError

a)tupla = (1,4,2, 3, 7 )
print(tupla.sort())

8 - IndentationError - Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError

a - def nova():
print('Geek')

'''





