'''for c in range(6, -1, -1):
    print(c)
print('FIM')

for c in range(0, 6, 2):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(1, n+1):
    print(c)
print('FIM')

inicio = int(input('Digite um número inicial: '))
final = int(input('Digite um número final: '))
passo = int(input('Digite um número para pular: '))
for c in range(inicio, final+1, passo):
    print(c)
print('FIM')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n #s = s + n
print('A soma dos seus valores foi {}'.format(s))
