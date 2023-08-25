'''import math
cateto1 = int(input('Digite um número inteiro para um lado do triângulo: '))
cateto2 = int(input('Digite outro número para outro lado do triângulo '))
# hipotenusa = math.sqrt(cateto1 * cateto1 + cateto2 * cateto2)
# print('A soma do quadrado dos catetos {} e {} é igual a raiz quadrada da hipotenuza {}.'.format(cateto1, cateto2, hipotenusa))
print('A hipotenusa de um triangulo com os lados {} e {} é {}'.format(cateto1, cateto2, math.hypot(cateto1,cateto2)))

co = float(input('Digite comprimento do cateto oposto: '))
ca = float(input('Digite comprimento do cateto adjascente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print ('A hipotenusa é {}.'.format((hi)))'''

from math import hypot
co = float(input('Digite comprimento do cateto oposto: '))
ca = float(input('Digite comprimento do cateto adjascente: '))
hi = hypot(co, ca)
print('A Hipotenusa dos catetos {:.2f} e {:.2f} é igual {:.2f}.'.format(ca, co, hi))
