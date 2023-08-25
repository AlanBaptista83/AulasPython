'''import math
num = float(input('Digite um número que lhe mostraremos a sua parte inteira: '))
print('A parte inteira de {} é {}.'.format(num, math.floor(num)))

import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}.'.format(num, math.trunc(num)))

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}.'.format(num, trunc(num)))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua parte inteira é {}'.format(num, int(num)))
