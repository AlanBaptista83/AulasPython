soma = cont = 0
sair = ' '
while True:
    num = int(input('Digite um número para somar (999 para parar):'))
    if num == 999:
        sair = str(input('Deseja realmente sair? [S/N] ')).upper().strip()
        if sair == 'S':
            break
        elif sair == 'N':
            print('continuando...')
        else:
            while sair != 'S' and sair != 'N':
                sair = str(input('Opção inválida. Digote \33[33mS para sair\33[m e \33[31mN para continuar\33[m.\nDeseja realmente sair? [S/N]')).upper().strip()
    if num == 999 and sair == 'N':
        soma = soma
        cont = cont
    else:
        soma += num
        cont += 1

print(f'Você digitou {cont} valores e a soma dos números foi {soma}')
