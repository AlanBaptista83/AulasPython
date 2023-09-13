from random import randint
from time import sleep
i = k = j = 0
lista = list()
temp = list()
jogos = int(input('Quantos jogos você deseja realizar: '))
for i in range(0, jogos):
    for j in range(0, 6):
        num = randint(1, 60)
        while num in temp:
            num = randint(1, 60)
        temp.append(num)
        temp.sort()
    lista.append(temp[:])
    temp.clear()
for k in range(0, jogos):
    print(f'Jogo {k+1}: {lista[k]}')
    sleep(1)
