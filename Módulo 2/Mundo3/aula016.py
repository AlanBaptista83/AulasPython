'''lanche1 = 'Hambúrguer'
lanche1 = 'Suco'
print (lanche1)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print('QUantos itens nessa Tupla: ',len(lanche))


# com ou sem parenteses
print (lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-4:])
# lanche[1] = 'Refrigerante'  # Tuplas são imutáveis quando em execução
'''
# Duas formas de usar as Tuplas
#for cont in lanche:  # Sem precisar da posição
#    print(f'Eu vou comer {cont}')
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
for pos, cont in enumerate(lanche):
    print(f'Eu vou comer {cont} na posição {pos}')

# for cont in range (0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
'''
print(sorted(lanche))  # Coloca em ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # A ordem influência na formação de soma de Tuplas
print(c)
c = b + a
print(c)
print(len(c))
print(c.count(5)) # Quantidade de vezes que um número (no caso 5) aparecem na tupla
print(c.index(8))  # em que posição está o número 8 na tupla c - Posição 1 (começa do 0)
print(c.index(5, 1)) # Em que posição está o número 5 à partir da posição 1

pessoa = ('Gustavo', 39, 'M', 99,88)
print(pessoa)'''

'''pessoa = ('Gustavo', 39, 'M', 99,88)
# del(pessoa) # pode apagar uma tupla inteira
del(pessoa[0]) # mas não pode apagar algo de dentro da Tupla
print(pessoa)'''