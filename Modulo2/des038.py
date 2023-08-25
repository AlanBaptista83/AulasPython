n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
maior = n1
if n1 > n2:
    print('O primeiro valor  {} é maior que o segundo {} digitado.'.format(maior, n2))
elif n2 > n1:
    maior = n2
    print('O segundo valor {} é maior que o primeiro {} digitado.'.format(maior, n1))
elif n2 == n1:
    print('Os números digitados são iguais: {}'.format(n1))
