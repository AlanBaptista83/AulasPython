from time import sleep
num = int(input('Digite um número inteiro: '))
print('-=-' *20)
print('Conversão de números')
escolha = int(input('[ 1 ] para binário \n[ 2 ] para octal \n[ 3 ] para hexadecimal \n--> '))
print ('CONVERTENDO...')
sleep(2)
#print (escolha)
if escolha == 1:
    '''for c in num:
        v = ord(c)
        print(c, v, f'{v:b}', sep='\t')'''
    print('O número inteiro {} é o número {} em binário.'.format(num, bin(num)[2:])) #fatiando a string - [2:] Elimina as posições 0 e 1
elif escolha == 2:
    print('O número inteiro {} é o número {} em octal.'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número inteiro {} é o número {} em hexadecimal.'.format(num, hex(num)[2:]))
else:
    print('Você não escolheu uma opção valida para conversão. FIM')