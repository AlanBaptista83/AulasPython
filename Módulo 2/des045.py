import random
from time import sleep
print('-=-'*20)
print('Jogando JOKENPÔ')
print('-=-'*20)
opcao = int(input('Digite 1 para Pedra \nDigite 2 para Papel \nDigite 3 para Tesoura\n--> '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
lista = ['Pedra', 'Papel', 'Tesoura']
comp = random.choice(lista)
if opcao == 1:
    print('Eu escolhi {} e você {}.'.format(comp, 'Pedra'))
    if comp == 'Pedra':
        print('Empatamos!')
    elif comp == 'Papel':
        print('Você ganhou!')
    else:
        print('Eu ganhei!')
elif opcao == 2:
    print('Eu escolhi {} e você {}.'.format(comp, 'Papel'))
    if comp == 'Pedra':
        print('Você ganhou!')
    elif comp == 'Papel':
        print('Empatamos!')
    else:
        print('Eu ganhei!')
elif opcao == 3:
    print('Eu escolhi {} e você {}.'.format(comp, 'Tesoura'))
    if comp == 'Pedra':
        print('Eu ganhei!')
    elif comp == 'Papel':
        print('Você ganhou!')
    else:
        print('Empatamos!')
else:
    print('Opção invalida. Começe novamente.')
