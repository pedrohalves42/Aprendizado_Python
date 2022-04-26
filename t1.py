while True:
    cpf = input('Digite um CPF válido: ')
    car = [',', '.', ' ', ' ']
    for c, v in enumerate(car):
        cpf = cpf.replace(v, '')

    if len(cpf) != 11:
        print('Números de caracteres inválidos e/ou caracteres não permitidos.')
        print('Caracteres permitidos: "." "," "-"')
        continue
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            novo_cpf += str(d)
            total = 0
    if cpf == novo_cpf:
        print('Válido')
    else:
        print('Inválido')
    option = ' '
    while option not in 'SsNn':
        option = str(input('Quer continuar? [S/N]: '))
    if option in 'Nn':
        break