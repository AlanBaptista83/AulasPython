from random import choice
print('Quem quer apagar o quadro?')
a1 = str(input('Digite o nome do aluno 1:'))
a2 = str(input('Digite o nome do aluno 2:'))
a3 = str(input('Digite o nome do aluno 3:'))
a4 = str(input('Digite o nome do aluno 4:'))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('No sorteio o aluno escolhido foi o {}!'.format(escolhido))
