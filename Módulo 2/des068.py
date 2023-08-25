from random import randint
soma = comp = cont = 0
print('-=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 20)
while True:
    num = int(input('Diga um número de 0 a 10: '))
    opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    if opcao != 'P' and opcao != 'I':
        while opcao != 'P' and opcao != "I":
            print('Opção Inválida. Digite P para par ou I para Ímpar! ')
            par = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    comp = randint(0, 10)
    soma = num + comp
    if soma % 2 == 0:
        if opcao == 'P':
            print(f'Você jogou {num} e o computador {comp}. A soma foi {soma} e é PAR!')
            print('Você GANHOU!')
            print('Vamos jogar novamente...')
            print('-=-' * 20)
            cont += 1
        elif opcao == 'I':
            print(f'Você jogou {num} e o computador {comp}. A soma foi {soma} e é PAR!')
            print('Você PERDEU!')
            break
    else:
        # print('Parte 2')
        if opcao == 'I':
            print(f'Você jogou {num} e o computador {comp}. A soma foi {soma} e é ÍMPAR!')
            print('Você GANHOU!')
            print('Vamos jogar novamente...')
            print('-=-' * 20)
            cont += 1
        elif opcao == 'P':
            print(f'Você jogou {num} e o computador {comp}. A soma foi {soma} e é ÍMPAR!')
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {cont} vezes! ')
