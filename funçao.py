'''
def saudacao(msg='Ola', nome='usuario'):
    nome = nome.replace('a', '4')
    msg = msg.replace('e', '3')
    print(msg, nome)


saudacao(nome='Zezinho', msg='Hi')
saudacao('Oi', 'Amanda')
saudacao('Hello', 'Pedro')
saudacao('Esta bem', 'Maria')
'''


def saudacao(msg='Ola', nome='usuario'):
    nome = nome.replace('a', '4')
    msg = msg.replace('e', '3')
    return f'{msg},{nome}'


variavel = saudacao()
print(variavel)

