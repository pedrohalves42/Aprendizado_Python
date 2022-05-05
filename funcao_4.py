'''
Fizz Buzz - Se o parametro da funcção for divisivel por 3, retorne fizz, se o parametro da função for divisivel por 5
retorne buzz. Se o parametro da função for divisilve por 4 e por 3, retorne FizzBuzz, caso contrario, retorne
Numero invalido
'''
from random import  randint

def divisivel(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} e divisivel por 3 e 5 '
    if n % 5 == 0:
        return f'buzz, {n} e divisivel por 5'
    if n % 3 == 0:
        return f'Fizz, {n} e divisivel por 3 '
    return f'{n} não e divisivel.'

'''
print(divisivel(10))
print(divisivel(99))
print(divisivel(100034))
print(divisivel(7))
print(divisivel(3))
print(divisivel(15))
'''
for i in range(100):
    aleatorio = randint(0, 100)
    print(divisivel(aleatorio))