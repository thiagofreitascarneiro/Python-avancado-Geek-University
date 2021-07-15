'''
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama - É utilizado para permitir impressão de textos colorido no terminal.

Instalando um módulo - pip install colorama

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')

# instalando o pacote PDF
# Não funciono Windows

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

'''


