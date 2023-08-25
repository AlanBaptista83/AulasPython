num = int(input('Digite um número inicial: '))
razao = int(input('Digite um número para a razão de uma Progressão: '))
print('Progressão aritinética de {} à partir do número {} é:'.format(razao, num))
print(num, end=' → ')
cont = 9
while cont != 0:
    print(num + razao, end=' → ')
    num = num + razao
    cont = cont - 1
print('Fim')
