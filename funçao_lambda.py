def funcao(arg, arg2):
    return arg * arg2


var = funcao(5, 99)
print(var)

a = lambda x, y: x * y
print(a(5, 99))

lista = [
    ['P1', 15],
    ['P2', 54],
    ['P3', 6],
    ['P4', 8],
    ['P5', 25],
]

'''
def func(item):
    return item[1]
'''
'''
lista.sort(key=lambda item: item[1], reverse=True)
'''

print(sorted(lista, key=lambda i : i[1]))

    