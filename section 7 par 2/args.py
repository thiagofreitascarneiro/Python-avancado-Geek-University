'''

Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar qualquer coisa,
desde que comece com asterisco.

Ex:
*xis

Mas por convenção, utilizamos *args para defini-lo.

Mas o que é o *args ?

O parâmetro * args utilizzado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutveis.

# exemplos

def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(3, 4, 5, 6))


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eun não tenho certeza quem você é ...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

def soma_todos_numeros(*args):
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 4, 5, 6, 7]

#Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos
# passando como argumentos uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar estes dados.

'''



