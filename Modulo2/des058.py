'''from random import randint
comp = randint(0, 10)
# print(comp)
escolha = -1
soma = 1
print('Pensei em um número de 0 a 10. Tente adivinhar qual é:')
while escolha != comp:
    escolha = int(input('Digite sua escolha: '))
    if escolha > comp:
        print('Você errou. Meu número é menor que {}'.format(escolha))
    elif escolha < comp:
        print('Você errou. Meu número é maior que {}'.format(escolha))
    soma += 1
print('Você acertou o número que pensei em {} tentativas. Número {}.'.format(soma-1, comp))'''

from random import randint
comp = randint(0, 10)
print('Pensei em um número de 0 a 10. Tente adivinhar qual é:')
acertou = False
soma = 0
while not acertou:
    escolha = int(input('Digite sua escolha: '))
    soma += 1
    if escolha == comp:
        acertou = True
    else:
        if escolha < comp:
            print('Mais... tente outro número')
        elif escolha > comp:
            print('Menos... tente outro número')
print('Acertou com {} tentativas.'.format(soma))
