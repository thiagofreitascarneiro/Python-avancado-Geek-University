'''
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos
que criamos neste curso são módulos Python prontos para serem utilizados

# importando uma função especifica do nosso módulo
from funcoes_com_parametro import soma

soma(123)

# Importando todo o módulo (Temos acesso a todos os lementos do módulo)
import funcoes_com_parametro as fcp

# Estamos acessando e imprimindo uma variável contida no módulo
print(fcp.lista)

valor = map(fcp.soma(sum(fcp.lista)), fcp.lista)
print(valor)
'''


