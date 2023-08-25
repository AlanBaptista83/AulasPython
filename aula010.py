#tempo = int(input('Gosta anos tem seu carro?'))
#if tempo <=3:
#    print('Carro novo!')
#else:
#    print('Carro velho!')
#print('FIM')

#Código simplificado para IF
#print('Carro Novo' if tempo<=3 else 'Carro Velho')

#nome = str(input('Digite seu nome:'))
#if  nome =='Alan':
#    print ('Que nome bonito!')
#else:
#    print('Seu nome é muito normal')
#print ('Bom dia,{}!'.format(nome))

n1 = float(input('Digite sua nota 1:'))
n2 = float(input('Digite sua nota 2:'))
m = (n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
#if m >= 6.0:
#    print('Sua média foi boa!')
#else:
#    print('Sua média foi ruim. Precisa estudar mais')
print('Parabéns!' if m>=6.0 else 'ESTUDE MAIS!')
