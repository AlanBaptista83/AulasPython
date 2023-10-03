'''def leiaInt(num):
    while True:
        num = input('Digite um número: ')
        if num.isdigit():
            break
        else:
            print('Erro. Você não digitou um número válido.')
    return num'''


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro. Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
