'''
Decoradores (decorators)

O que são decorators ?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também sõo exemplos de Higher Order Functions;
- Decorators tem uma sintaxe po´rpria, usando '@' (Syntact Sugar / Açucar Sintático)

/---------------------------------------/
/        Function Decorator             /
----------------------------------------

-----------------------------------------
/ / -------------------------------------/ /
/ /           Função decorada           / /
/ / -------------------------------------/
/ ---------------------------------------

# Decorators como funções (Sintaxe não recomenda / Sem açucar sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) á Geek University')


# Testando 1

# saudacao()

teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

raiva_educada()


# Decorators com syntax sugar (Açucar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()
'''

# OBS: Não confunda Decorator com Decorator Function
