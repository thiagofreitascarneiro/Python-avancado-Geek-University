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

lista = [1, 2, 3, 4, 5]
print(soma(123))
