'''
Sistema de Arquivos - Manipulação

import os

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('frutas.txt')) # True

#Diretório
print(os.path.exists('teste')) # True
print(os.path.exists('outro')) # False

# Criando arquivos

# Não funcionou no Windows
os.mknod('arquivo_teste.txt')

# Criando diretório
os.mkdir('templates')

# Criando multi-diretórios (árvore de diretórios)
os.makedirs('templates2/geek/university')

#OBS - Se já existir, teremos um FileExisteError

os.makedirs('template3/novo/outro2', exist_ok=True)


# Renomear arquivos e diretórios
os.rename('templates2', 'geek2')

# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não exisitr vazio, teremos um OSError

#Arquivos
os.rename('frutas.txt', 'cesta.txt')

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles
# não vão para a lixeira. Eles somem.

os.remove('geek.txt')

# OBS: Se estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.

# OBS: se o arquivo não exisitr, teremos o FileNotFoundError

# Removendo diretórios vazios

os.rmdir('templates42')
# OBS: Se o diretório não exisitr teremos um FileNotFoundError

#Removendo uma árvore de arquivos
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)
# Podemos remover uma árvore de diretório vazios

os.removedirs('geek2/geek/university')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# Os arquivos temporários 'vivos' dentro dos blocos with.

https://docs.python.org/3/library/os.html?hightlight=os#module-os
'''



