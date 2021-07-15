lista = [1, 2, 3, 4, 5, 7, 90, 100, 120, 70]

def pares(vetor):
    for v in vetor:
        if v % 2 == 0:
            print(f'{v}, ', end='')


pares(lista)