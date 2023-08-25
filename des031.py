distancia = float(input('Qual é a distância da sua passagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km.'.format(distancia))
'''if  distancia < 200:
    print('E o preço da sua passagem será de R${:.2f}.'.format(distancia*0.5))
else:
    print('O preço da sua passagem será de R${:.2f}.'.format(distancia*0.45))'''
preço = distancia*0.5 if distancia<=200 else distancia*0.45
print('Sua passagem custará R${:.2f}'.format(preço))
