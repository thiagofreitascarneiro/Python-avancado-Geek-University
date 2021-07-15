def soma(num):
    if num > 0:
        num = str(num)
        lista = list(num)
        soma = 0
        for valor in lista:
            soma = soma + int(valor)
        return f'A soma dos digitos é de {soma}'
    else:
        print('Numero invalido')


print(soma(123))
