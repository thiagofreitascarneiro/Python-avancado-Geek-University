'''
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DO USUÁRIO DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.

# Else - É executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# Finally
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o finally')


# OBS: O bloco finally é SEMPRE executado. Independete se houve exceção ou não.

# O finally, geralmente é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b


num1 = int(input('informe o primeiro número: '))
try:
    num2 = int(input('informe o primeiro número: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexo CORRETO
# obs: você é responsável pelas entradas das funcções.

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por zero'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Exemplo mais complexo Genérico
# obs: você é responsável pelas entradas das funcções.

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

'''

# Exemplo mais complexo Semi-Genérico
# obs: você é responsável pelas entradas das funcções.

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

