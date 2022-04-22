variavel = ['Luiz','Pedro','Joao']
'''for valor in variavel:
    if valor.startswith('J'):
        print(f'O Valor {valor}  começa com jota')
    else:
        print(f'O valor {valor} não começa com Jota ')
'''
começa_com_j = False
'''for valor in variavel:
    if valor.lower().startswith('j'):
        começa_com_j = True

if começa_com_j:
    print('Existe uma palavra que começa com J. ')
else:
    print('Não existe uma palavra que começa com J. ')
'''
for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)