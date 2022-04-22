'''

while True:
    nome = input('Qual o seu nome? ')
    print(f'Olá {nome}')
print('Não sera executado')
'''
from builtins import input

'''
x = 0
while x < 10:
    if x == 3:
        x += 1
        continue
    print(x)
    x += 1
print('Acabou')
'''
'''
x = 0  # coluna
while x < 10:
    y = 0
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1

    x += 1
print('Acabou')
'''
while True:
    print()
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite um operador : ')
    sair = input('Deseja Sair [S/N]: ').lower()

    if sair == 's':
        break
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um numero!!')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador invalido!!')