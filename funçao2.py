'''

def funcao(var):
    return var

variavel = funcao('Valor que eu quero')
if variavel:
    print(variavel)
else:
    print('Nada')
'''
'''

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


divide = divisao(999, 13)
if divide:
    print(divide)
else:
    print('Conta invalida.')
'''


def dumb():
    return [1, 2, 4, 5, 6, 7]


var = dumb()
print(var, type(var))
