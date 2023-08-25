'''num = int(input('Digite um número entre 0 e 20: '))
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onde', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    if 0 > num or num > 20:
        num = int(input('Resposta inválida. Digite um número entre 0 e 20: '))
    else:
        break
# while num in (0, 20):
print(f'Você digitou o número {extenso[num]}')'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onde', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    else:
        print('Tente novamente.', end=' ')
print(f'Você digitou o número {extenso[num]}')