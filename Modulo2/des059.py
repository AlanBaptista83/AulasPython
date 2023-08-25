from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('-=-' * 20)
    print('''   Menu
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Digite sua ação: '))
    if opcao == 1:
        print('A soma de {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação de {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {}, o número  maior é o {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {}, o número  maior é o {}'.format(n1, n2, n2))
        elif n1 == n2:
            print('Os números digitados foram igual: {} e não tem um maior'.format(n1))
    elif opcao == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro número: '))
        print
    elif opcao > 5 or opcao < 1:
        print('Opção inválida. Tente novamente.')
    if 1 <= opcao <= 3:
        sleep(2)
print('Finalizando...')
sleep(1)
print('Obrigado e volte sempre!')
