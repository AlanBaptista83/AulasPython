real = float(input('Digite quanto dinheiro você tem na carteira agora: R$ '))
dolar = real // 3.27
resto = (real - dolar * 3.27)
print('Você pode comprar U${:.2f} com esses R${:.2f} que tem na carteira agora!'.format(dolar, real))
print('Ainda vai restar um total de R${:.2f} com você!'.format(resto))
