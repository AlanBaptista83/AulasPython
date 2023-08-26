lista = list()
menor = maior = 0
for c in range(0, 5):
    n = (int(input('Digite um número: ')))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado no final da fila...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(lista)

'''lis = [ ]
for c in range(1, 10):
    n = int(input(f'Digite o {c}° número: '))
    if c == 1 or n >= lis[-1]:
        lis.append(n)
    elif n <= lis[0]:
        lis.insert(0, n)
    elif lis[0] <= n <= lis[1]:
        lis.insert(1, n)
    elif lis[1] <= n <= lis[2]:
        lis.insert(2, n)
    elif lis[2] <= n <= lis[3]:
        lis.insert(3, n)
    elif lis[3] <= n <= lis[4]:
        lis.insert(4, n)
    elif lis[4] <= n <= lis[5]:
        lis.insert(5, n)
    elif lis[5] <= n <= lis[6]:
        lis.insert(6, n)
    elif lis[6] <= n <= lis[7]:
        lis.insert(7, n)
    elif lis[7] <= n <= lis[8]:
        lis.insert(8, n)
    elif lis[8] <= n <= lis[9]:
        lis.insert(9, n)
print(lis)'''