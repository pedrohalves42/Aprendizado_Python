'''
Crie uma funcao que receba 2 numeros. o primeiro e um valor e o segundo um percentual(ex 10%)
retorne o valor do primeiro numero somado do aumento do percentual do mesmo
'''


def aumento_percecntual(valor, percentual):
    return valor + (valor * percentual / 100)


ap = aumento_percecntual(50, 10)
ap1 = aumento_percecntual(589, 25)
ap2 = aumento_percecntual(9800, 90)
print(ap, ap1, ap2)

