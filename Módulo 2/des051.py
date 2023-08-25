# jeito guanabara de fazer
'''primeiro = int(input('Digite um número inicial: '))
razao = int(input('Digite um número para a razão de uma Progressão: '))
print('Progressão aritinética de {} à partir do número {} é:'.format(razao, primeiro))
décimo = primeiro + (10 - 1) * razao
for c in range(primeiro, décimo + razao, razao):
    print(c, end=' → ')
print('Acabou!')'''

num = int(input('Digite um número inicial: '))
razao = int(input('Digite um número para a razão de uma Progressão: '))
print('Progressão aritinética de {} à partir do número {} é:'.format(razao, num))
proximo = num
print(num, end=' → ')
for c in range(0, 9):
    proximo = proximo + razao
    print(proximo, end=' → ')
print('Acabou!')