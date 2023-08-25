n = s =0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

# print('A soma vale {}'.format(s))

# Usando uma fString
print(f'A soma vale {s}')
print(f'QUal o valor de n {n}')

nome = 'jose'
idade = 33
salario = 987.35
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}')
