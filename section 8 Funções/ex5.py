def calc_esfera(raio):
    v = 4/3 * raio * raio**3
    return v

num = int(input('Digite um número para o calculo do volume de uma esfera: '))

print(f'{calc_esfera(num):.2f}')

valor = lambda raio: 4/3 * raio * raio**3

print(valor(num))
