print('-=-' *20)
print('Analisador de triãngulos')
print('-=-' * 20)
t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))
'''maior = t1
soma = t2 + t3
if t2 > t1 and t2 > t3:
    maior = t2
    soma = float(t1 + t3)
if t3 > t1 and t3 > t2:
    maior = t3
    soma = float(t1 + t2)
# print('Maior lado é {}'.format(maior)) - Descobrindo a maior reta
#print (maior, soma)
if maior < soma:
    print('Esses segmentos de reta formam um triãngulo!')
else:
    print('Esses segmentos de reta não formam um triângulo!')'''
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')
