def sorteia():
    from random import randint
    for i in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
        print(f'{num}', end=' ', flush=True)
        sleep(0.5)

def somaPar(lst):
    soma = 0
    for i in range(0, len(lst)): # for i in lst:
        if lst[i] % 2 == 0:  # if valor % 2 == 0:
            soma += lst[i]  # soma += i
    print(f'{lst}, temos {soma}.', end=' ', flush=True)

# Programa Principal
from time import sleep
lista = list()
print('Sorteando os valores da lista: ', end=' ', flush=True)
sorteia()
print('\nSomando os valores pares de ', end=' ', flush=True)
somaPar(lista)
