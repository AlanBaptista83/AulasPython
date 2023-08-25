'''for c in range(1, 10):
    print(c)
print('Fim')'''
'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''

'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
        # print(n)
print('Fim')'''

'''r = 'S'
while r == 'S': #  condição de parada
    c = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]')).upper()
print('Obrigado!')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    #  if n != 0: Outra forma de fazer a validação para não contar o 0 como par. Fiz usando a linha 30 reduzindo um na resposta
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números ímpares e {} números pares!'.format(impar, par - 1))
