import math
a = float(input('Digite um ângulo qualquer: '))
a1 = math.radians(a)
print('O cosseno de {} é {:.2f}'.format(a, math.cos(a1)))
print('O seno de {} é {:.2f}'.format(a, math.sin(a1)))
print('A tangente de {} é {:.2f}'.format(a, math.tan(a1)))
