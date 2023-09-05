lista = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
par = somaterc = maiorseg = 0
for i in range(0, 3):
    for j in range(0, 3):
        if i == 1 and j == 0:
            maiorseg = lista[1][0]
        lista[i][j] = int(input(f'Digite um valor para [{i}, {j}] '))
        if lista[i][j] % 2 == 0:
            par += lista[i][j]
        if j == 2:
            somaterc += lista[i][2]
        if i == 1:
            if lista[1][j] > maiorseg:
                maiorseg = lista[1][j]
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {lista[i][j]:^5} ]', end=' ')
    print()
print(f'A soma dos números pares foi {par}.')
print(f'A soma dos números da terceira coluna foi {somaterc}')
print(f'O maior número da segunda linha é o {maiorseg}')
