lista = list()
continuar = ' '
while True:
    if continuar == 'N':
        break
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado e não adicionado a lista.')
    continuar = str(input('Deseja continuar: [S/N] ')).upper().strip()
    if continuar not in 'SN':
        while continuar not in 'SN':
            if continuar not in 'S':
                continuar = str(input('Opção inválida. Deseja continuar: [S/N] ')).upper().strip()
            else:
                break


lista.sort()
print(f'Sua lista foi {lista}')

'''for p, v in enumerate(lista):
        if v in lista:
            lista.pop(p)
            print('Valor duplicado e não adicionado a lista.')
        else:
            print('Valor adicionado com sucesso...')
    while True:
        sair = str(input('Deseja continuar: [S/N] ')).upper().strip()
        if sair == 'SN':
            print('Opção inválida')
        else:
            break
    if sair == 'SN':
        break
print(f'Sua lista foi {lista.sort}')'''