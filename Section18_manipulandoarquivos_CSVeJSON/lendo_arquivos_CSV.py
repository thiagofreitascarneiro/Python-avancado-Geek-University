'''
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Seprados por Vírgula.

# Separados por vírgula
1, 2, 3, 4, 5

"geek", "university", "python"

# Separados por ponto e vírgula
1; 2; 3; 4; 5

"geek"; "university"; "python"

# Separador por espaço

1 2 3 4 5

"geek" "university" "python"

http://dados.gov.br/dataset

# Possivel de se trabalhar, mas não é o ideal (trabalhoso)
with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    #print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)


A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictREader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

# Reader
from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros')

'''

# DictReader

from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        #Cada linhaé um OrderedDict
        print(f'{linha["Nome"]} nasceu no(a)(s) {linha["País"]} e mede {linha["Altura (em cm)"]}')

