lista = [1, 2, 3, 4, 5, 7, 90, 100, 120, 70]
def programa(vetor):
    print(vetor)
    print(30 * '-')
    invertido = list(reversed(vetor))
    print(invertido)
    print(30 * '-')
    media = sum(vetor) / len(vetor)
    print(f'A média dos valores são {media:.2f}')
    print(30 * '-')


programa(lista)

