'''
def func():
    print(variavel)


def func2(arg=None):
    global variavel
    variavel = 'Outro valor'
    print(variavel)
    return arg


func()
func2()
print(variavel)
'''
'''

def func():
    print(variavel)


def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
outra_variavel = func2(arg=variavel)
print(variavel)
print(outra_variavel)
'''


def func():
    outra_variavel = 'Luiz Otavio'
    return outra_variavel


def func2(arg):
    print(arg)


var = func()
func2(var)
