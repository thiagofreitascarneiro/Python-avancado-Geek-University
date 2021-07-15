def nota(a, b, c, d=''):
    if d == 'D':
        total = a + b + c
        print(f'O total das notas são: {total/3}')
    elif d == 'P':
        nota1 = a * 5
        nota2 = b * 3
        nota3 = c * 2
        total = nota1 + nota2 + nota3
        print(f'O total das notas ponderadas são: {total/10}')



nota(5, 5, 10, 'P')

