def troque(a, b):
    c = a
    a = b
    b = c
    return f'A troca dos valores foram: {a} {b}'


print(troque(2, 3))