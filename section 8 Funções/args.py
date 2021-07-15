'''
Entendedno o *args

- O *args é um parâmetro, como outro qualquer, Isso significa que você pode chama-lo
de qualquer coisa, desde que começe com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo.

Mas o que é *args?

O parâmetro *args utilizado em uma função, coloca os valores extrar informados
como entrada em uma tupola. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

#print(soma_todos_numeros(4, 6)) #TypeError

#print(soma_todos_numeros(4, 6, 7, 9)) #TypeError

# Entendendo o args

def soma_todos_numeros(*args):
    return sum(args)



soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(1, 2, 3)
soma_todos_numeros(1, 3)
soma_todos_numeros(1, 2, 3, 4, 6)

print(soma_todos_numeros(23.4, 12.5))

# Entendendo o args

def soma_todos_numeros(nome, email, *args):
    return sum(args)



soma_todos_numeros('Bob', 'Jack')
soma_todos_numeros('Bob', 'Jack', 1)
soma_todos_numeros('Bob', 'Jack', 1, 2, 3)
soma_todos_numeros('Bob', 'Jack', 1, 3)
soma_todos_numeros('Bob', 'Jack', 1, 2, 3, 4, 6)

print(soma_todos_numeros('Bob', 'Jack', 23.4, 12.5))

# Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza quem você é'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
'''

def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6]

# Desempacotador


print(soma_todos_numeros())
print(soma_todos_numeros(numeros)) # TypeError
print(soma_todos_numeros(*numeros)) # o * asterisco serve para que informamos ao Python que estamos
# passando como argumento uma coleção de dados. Desta forma, ele vai saber que precisará antes
# desempacotar estes dados.


