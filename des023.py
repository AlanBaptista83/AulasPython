num = int(input('Digite um numero inteiro entre 0 e 9999: '))
milhar = num // 1000 % 10
centena = num // 100 % 10
dezena = num // 10 % 10
unidade = num // 1 % 10
print('Unidades: {}'.format(unidade))
print('Dezenas: {}'.format(dezena))
print('Centenas: {}'.format(centena))
print('Milhar: {}'.format(milhar))
