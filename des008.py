med = float(input('Digite uma medida em metros: '))
#cent = med*100
#mili = med*1000
print('{} metros correspondem a {:.0f} centímetros!'.format(med, med*100), end=' ')
print('Mas também podem ser {:.0f} milímetros'.format(med*1000))
