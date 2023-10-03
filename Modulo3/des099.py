from time import sleep


def maior(* num):
    cont = m = 0
    print(f'Analisando os valores passados...', flush=True)
    sleep(0.5)
    '''for c in range(0, len(num)):
        print(f'{num[c]}', end=' ', flush=True)'''
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            m = valor
        else:
            if valor > m:
                m = valor
        cont += 1
    t = len(num)
    print(f'\nForam informandos {t} valores ao todo.')
    print(f'O maior número passado é o {m}')
    print('=-' * 30)


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
