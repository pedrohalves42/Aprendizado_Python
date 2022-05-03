'''
Crie uma funcao que receba 2 numeros. o primeiro e um valor e o segundo um percentual(ex 10%)
retorne o valor do primeiro numero somado do aumento do percentual do mesmo
'''


def aumento_percecntual(valor, percentual):
    print(valor + (valor * percentual / 100))


aumento_percecntual(50, 10)
aumento_percecntual(589,25)
aumento_percecntual(9800,90)