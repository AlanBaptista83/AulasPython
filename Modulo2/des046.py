from time import sleep
print('Contagem regressiva...')
for c in range (10, -1, -1):
    print(c, end='')
    sleep(0.5)
    print(' - ', end='')
    sleep(0.5)
print('FELIZ ANO NOVO!')