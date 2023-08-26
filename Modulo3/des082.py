lista = list()
impar = list()
par = list()
resp = ' '
while True:
    if resp in 'N':
        break
    lista.append(int(input('Digite um número: ')))
    while True:
        resp = str(input('Inserir novo número? [S/N] ')).upper().strip()
        if resp in 'SN':
            break
        if resp not in 'SN':
            print('Resposta inválida.', end=' ')
print(f'A lista digitada foi {lista}')
'''for c in range(0, len(lista)):  # Poderia usar o Enumerate (abaixo)
    if lista[c] % 2 == 0:
        par.append(lista[c])
    # else:
    elif lista[c] % 2 == 1:
        impar.append(lista[c])
print(f'A lista de números pares é {par}')
print(f'A lista de números ímpares é {impar}')'''

for c, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
