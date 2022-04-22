for n in range(10):
    print(n)

for n in range(100):
    if n % 8 == 0:
        print(n)

print('*' * 20)
texto = 'python'
nova_string = ''
for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'o':
        nova_string += letra.upper()
    elif letra == 'p':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
