from random import randint
from time import sleep
from operator import itemgetter
jogador = dict()
ranking = list()
for i in range(1, 5):
    jogador[i] = randint(1, 6)
    print(f'O jogador{i} tirou {jogador[i]} no dado.')
    sleep(0.5)
# print(jogador)
print('---' * 30)
print('Ranking dos jogadores: ')
print('---' * 30)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)  # itemgetter (0)=chave (1)=valor
# print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: jogador {v[0]} com {v[1]} no dado.')
    sleep(0.5)
