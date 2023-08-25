'''opcao = 1
c = 0
while opcao > -1:
    opcao = int(input('Quer ver a tabuada de qual valor? '))
    if opcao > 0:
        for c in range(1, 11):
            print(f'{c} x {opcao} = {c * opcao}')
        print('-'*20)
    elif opcao == 0:
        print('Tabuada de 0 é zero.')
        opcao = int(input('Quer ver a tabuada de qual valor? '))
    else:
        print('')
print('Volte sempre!')'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('Programa de tabuada encerrado. Volte sempre!')

