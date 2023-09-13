valores = list()  # poderia no lugar do {} usar list()
valores.append({'Nome', 'Alan'})
valores.append({'Nome', 'Pedro'})
valores.append({'Nome', 'Maria'})
print(valores)
'''for cont in range(0, 5):  # Lista para inserir valores pelo usuário usando for
    valores.append(int(input('Digite um valor: ')))

for posicao, v in enumerate(valores):  # primeiro 'posicao' é a posição e o segundo item 'v' o valor
    print(f'Na posição {posicao} encontrei o valor {v}.')
print('cheguei ao final da lista')'''

'''a = [2, 3, 4, 7]
b = a  # uma vez que iguala uma lista o python faz uma ligação entre elas
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b = a[:]  # B recebe todos os valores de A [:] fatiamento - Copia de A sem ligação com B
b[2] = 8  # Altera na lista b e na A tb
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
