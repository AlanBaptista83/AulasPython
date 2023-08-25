'''nota50 = cont50 = cont20 = cont10 = cont1 = 0
valor = int(input('Que valor você quer sacar? R$'))
while valor != 0:
    while valor >= 50:
        valor -= 50
        cont50 += 1
    if cont50 != 0:
        print(f'{cont50:.0f} notas de R$50,00')
    while valor >= 20:
        valor -= 20
        cont20 += 1
    if cont20 != 0:
        print(f'{cont20:.0f} notas de R$20,00')
    while valor >= 10:
        valor -= 10
        cont10 += 1
    if cont10 != 0:
        print(f'{cont10:.0f} notas de R$10,00')
    while valor >= 1:
        valor -= 1
        cont1 += 1
    if cont1 != 0:
        print(f'{cont1:.0f} notas de R$1,00')
print('Volte sempre!')'''

valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
print('Volte Sempre')
