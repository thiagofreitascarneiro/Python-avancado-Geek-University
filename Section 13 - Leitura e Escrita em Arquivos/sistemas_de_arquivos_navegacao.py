'''
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer
uso do módulo os.

os - Operating System - Sistema Operacional

# Fazer o import
import os

# getcwd() - pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# PAra mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo

# OBS para usuários Windows
print(os.path.isabs('\PycharmProjects\pythonGeek'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name) # nt(windows)

print(os.getcwd())

res = os.path.join(os.getcwd(), 'geek')

os.chdir(res)
print(os.getcwd())


'''

# Fazer o import
import os

# Podemos listar os arquivos e diretórios com ais detalhe com scandir()

arquivos = list(os.scandir())

print(arquivos[0])

print(arquivos[0].inode)
print(arquivos[0].is_dir) # É um diretório ? Fasle
print(arquivos[0].is_file) # É um arquivo ? True
print(arquivos[0].is_symlink) # É um link simbólico ? False
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # Estatísticas..

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.

# scanner.close()


