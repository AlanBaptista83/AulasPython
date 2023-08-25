maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1: # dica guanabara para a primeira ocorrência - tanto maior quanto menor são o 1º peso
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg e o menor foi {}Kg'.format(maior, menor))
