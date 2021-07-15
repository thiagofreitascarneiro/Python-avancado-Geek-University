'''
O bloco Try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Previnindo que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //xecução problemática
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.
try:
    len(5)
except:
    print('Deu algum problema')


# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma genérica não é a mlehor forma de tratamento de erros. O ideal é SEMPRE
tratar de forma especifica.

# Exemplo 3 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente.')

# Exemplo 4 - Tratando um erro específico

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    #len(5)
    #geek()
except NameError as err:
    print(f'Deu NameError: {err}')
except TypeError as erra:
    print(f'Deu TypeError: {erra}')
except:
    print('Deu um erro diferente')

# Podemos efetuar diversos tratamentos de uma só vez.
'''



def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Geek'}

print(pega_valor(dic, 'nome'))