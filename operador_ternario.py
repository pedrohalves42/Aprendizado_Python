'''logged_user = False
msg = 'Usuario logado' if logged_user else 'Usuario precisa logar '
print(msg)
'''
idade = input('Qual sua idade? ')
if not  idade.isnumeric():
    print('Você precisa digitar apenas numeros!!')
else:
    idade = int(idade)
    e_de_maior= (idade >=18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
    print(msg)