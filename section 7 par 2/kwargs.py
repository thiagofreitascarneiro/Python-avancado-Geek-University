'''
**Kargs

Podeíamos chamar este parâmetro de **xis, mas convensão chamamos de **Kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em
uma tupla, o Kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicioário.

# Exemplo

def cores_favoritas(**Kwargs):
    for pessoa, cor in Kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS - Os parâmetros *args e Kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')

def cumprimento_especial(**Kwargs):
    if 'geek' in Kwargs and Kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in Kwargs:
        return f"{Kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Desempacotar com ** Kwargs

def mostra_nomes(**Kwargs):
    return f"{Kwargs['nome']} {Kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))
'''


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = [1, 2, 3]
conjunto = [1, 2, 3]

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS! Os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da função.

# exemplo ERRADO
dicionario = dict(d=1, e=2, f=3)

# TypeError
soma_multiplos_numeros(**dicionario)



