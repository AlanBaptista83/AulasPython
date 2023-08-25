from random import randint
from time import sleep
n = randint(0,5) # Faz o computador pensar
#print('Pensei no número {}'.format(n)) - teste para saber qual o número inteiro foi randomizado
print ('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print ('-=-' * 20)
escolhido = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2) # Faz o processamento aguardar 2 segundos
if escolhido == n:
    print('Você adivinhou o número que escolhi. Parabéns!')
else:
    print('Não acertou. Eu pensei no número {} e não no {}!'.format(n, escolhido))
print ('FIM')
