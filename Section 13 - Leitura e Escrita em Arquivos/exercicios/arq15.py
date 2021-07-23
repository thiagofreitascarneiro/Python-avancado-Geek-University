'''
Faça um programa que receba como entrada o ano corrente de dois arquivos:
um de entrada e outro de saída. Cada linha do arquivo de entrada contém o nome de
uma pessoa (ocupando 40 caracteres) e o seu ano de nascimento. O programa deverá
ler o arquivo de entrada e gerar um arvio de saída onde aparece o nome da pessoa
seguida por uma string que representa a sua idade.

    * Se a idade for menor que 18 anos, escreva "Menor de idade"
    * Se a idade for maior que 18 anos, escreva "Maior de idade"
    * Se a idade for igual a 18 anos, escreva "Entrando na maior idade"
'''

arquivo = input('Informe o nome do arquivo que deseja abrir: ')

data = input('Informe a Data de Hoje (DD MM AAA): ')
ano = data.split()
ano_hoje = int(ano[-1])

with open(f'{arquivo}', 'r') as arq:
    with open(f'{arquivo}.modi', 'w') as arq2:
        lista_arquivo = list(arq)
        for x in range(len(lista_arquivo)):
           pessoa = lista_arquivo[x].split()
           idade = ano_hoje - int(pessoa[-1])
           if len(pessoa) == 0:
               pass
           else:
               if idade == 18:
                   arq2.write(f'{" ".join(pessoa[0:2])} :   Entrando na maior idade ')
                   arq2.write('\n')
               elif idade > 18:
                   arq2.write(f'{" ".join(pessoa[0:2])} :   Maior de idade ')
                   arq2.write('\n')
               else:
                   arq2.write(f'{" ".join(pessoa[0:2])} :   Menor de idade')
                   arq2.write('\n')




