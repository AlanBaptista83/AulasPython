n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
soma = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
#usar quantas casas decimais :.3f --> três casas decimais flutuantes
print(' A soma vale é {}, \n a divisão é {:.3f} \n e a multiplicação é {}'.format(soma, d, m), end=' ')
print('A divisão inteira é {} e a exponenciação é igual a {}'.format(di, e))
