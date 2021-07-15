'''
Listas Aninhadas

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

# Exemplos

Em Python nós temos as Listas

numeros = [1, 2, 3, 4, 5]

# Como fazemos para acessar os daods ?

print(listas[0][1]) #2
print(listas[2][1]) #8

for lista in listas:
    for num in lista:
        print(num)


listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(listas)
print(type(listas))


# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
'''

