'''
Crie uma funçao1 que recebe uma funcção2 como parametro e retorne o valor da funçaoo2
Faça a função1 executar duas funcções que recebam u, numero diferente de argumento
'''


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao}{nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, ' Luiz',saudacao='Boa noite')
print(executando2)
print(executando)
