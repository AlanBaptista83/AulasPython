lista = list()
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um número inteiro na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(lista)
print(f'Menor valor da lista é {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...', end='')
print(f'\nMaior valor da lista é {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...', end=' ')


# print(f'O menor número dessa lista está na posição {lista.index(min(lista))} e é o {min(lista)}')
# print(f'O maior número dessa lista está na posição {lista.index(max(lista))} e é o {max(lista)}')
# print(f'Maior valor da lista é {maior} na posição {lista.index(maior)}')
# print(f'Menor valor da lista é {menor} na posição {lista.index(menor)}')