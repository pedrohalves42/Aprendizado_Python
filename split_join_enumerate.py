'''string = "O Brasil e o pais do futebol, o Brasil é penta"
list_1 = string.split(' ')
list_2 = string.split('/')
'''
'''for valor in list_1:
    print(f'{valor} apareceu {list_1.count(valor)}x na frase ')
'''
'''palavra = ''
contagem = 0
for val in list_1:
    qtd_vezes = list_1.count(val)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = val
print(f'A palavra que apareceu mais vezes e {palavra} ({contagem})x')
'''
'''for valor in list_2:
    print(valor.strip().capitalize())
'''
'''string = 'O Brasil e penta'
lista = string.split()

for v1, v2 in enumerate(lista):
    print(v1)
    print('*'*20)
    print(v2)
'''
lista = ['Luiz','Joao','Maria']
n1, n2, *outra_lista = lista

print(n2)