'''def contador(i, f, p):
    from time import sleep
    if p == 0:
        p = 1
    if p < 0:
        p = -p
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if i > f:
        if p >= 0:
            p = -p
    for c in range(i, f+p, p):
        print(f'{c}', end=' ')
        sleep(0.3)
    print('FIM!')
    print('-=' * 30)


# Programa Principal
contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
final = int(input('Final: '))
passo = int(input('Passos: '))
contador(inicio, final, passo)'''
from time import sleep
def contador(i, f, p):
    if p < 0:
        p = -p
    if p == 0:
        p = 1
    print('-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True) # não ligar o buffer de tela para não agarrar o sleep. Não precisou
            sleep(0.2)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont -= p
        print('FIM!')

#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)