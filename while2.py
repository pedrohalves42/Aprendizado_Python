'''
contador = 1
soma = 1
while contador <= 10:
    print(contador,soma,)
    if contador > 5:
        break

    soma = soma + contador
    contador +=1
else:
    print('Você terminou')
print('Terminou')
'''
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
c = 0
nova_string = ''
input_do_usuario = input('Qual letra deseja colocar maiuscula: ')
while c < tamanho_frase:
    #print(frase[c],c)
    letra = frase[c]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    print(nova_string)
    c +=1
print(nova_string)