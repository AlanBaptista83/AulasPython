'''def escreva(txt):
    for i in range(0, len(txt)+2):
        print('~', end='')
    print(f'\n {txt} ')
    for i in range(0, len(txt)+2):
        print('~', end='')


# Programa Principal
texto = str(input('Digite algo: '))
escreva(texto)'''
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


# Programa Principal
texto = str(input('Digite algo: '))
escreva(texto)



