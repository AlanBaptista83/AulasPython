num = int(input('Digite um número inicial: '))
razao = int(input('Digite um número para a razão de uma Progressão: '))
print('Progressão aritinética de {} à partir do número {} é:'.format(razao, num))
proximo = num
print(num, end=' → ')
cont = 9
final = 0
while cont != 0:
    print(num + razao, end=' → ')
    num = num + razao
    cont = cont - 1
opcao = int(input('\nDeseja mostrar mais quantos termos: '))
cont = opcao
while opcao != 0:
    while cont != 0:
        print(num + razao, end=' → ')
        num = num + razao
        cont = cont -1
    final = final + opcao
    opcao = int(input('\nDeseja mostrar mais quantos termos: '))
    cont = opcao
final = 10 + final
print('Foram apresentados {} termos.'.format(final))
print('Fim')