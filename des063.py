print('Sequencia de Fibonacci')
n = int(input('Quantos números de fibonacci deseja mostrar? '))
inicial = n
t1 = 0
t2 = 1
print(' {} → {}'.format(t1, t2), end=' → ')
n = n - 2
while n != 0:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    n = n - 1
    print(t3, end=' → ')
print('FIM\nEstes foram os {} primeiros números de Fibonacci.'.format(inicial))
