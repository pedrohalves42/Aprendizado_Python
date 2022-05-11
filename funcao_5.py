'''
crie uma função1 que recebe uma funçao2 como parametro e retorne o valor da funcção executada
'''

def ola_mundo():
    return 'Ola Mundo!'

def mestre(funcao):
    return funcao()
executando = mestre(ola_mundo)
print(executando)