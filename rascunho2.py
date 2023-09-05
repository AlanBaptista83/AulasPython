from random import sample
from time import sleep
lista = list()
print('-'*30)
print(f'      Jogo da Mega Sena:    ')
print('-'*30)
num = int(input('Quantos jogos você quer que eu sorteie: '))
for i in range(0, num):
    jogos = sample(range(1, 61), 6)
    jogos.sort()
    print(f'Jogo {i+1}: {jogos}')
    lista.append(jogos)
    sleep(0.5)
print(lista)