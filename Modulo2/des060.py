# Jeito 1 _ Alan
''' num = int(input('Calculando um fatorial\nDigite um número: '))
fatorial = num
c = num - 1
while c != 0:
    fatorial = fatorial * c
    c = c - 1
print('O fatorial de {}! é igual a {}'.format(num, fatorial))  '''

# forma 2 _ usando método
'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

# Jeito 3 _ parecido com o do guanabara _ aparecer a multiplicação
num = int(input('Calculando um fatorial\nDigite um número: '))
c = num
fatorial = 1
print('Calculando {}! = '.format(num), end='')

while c > 0:
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial = fatorial * c
    c = c - 1  # c -= 1
print('{:.0f}'.format(fatorial))
