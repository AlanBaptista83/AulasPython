v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
'''if v1 > v2 and v1 > v3:
    print('O maior valor é {}'.format(v1))
else:
    if v2 > v3:
        print('O maior valor é {}'.format(v2))
    else:
        print('O maior valor é {}'.format(v3))
if v1 < v2 < v3:
    print('O menor valor é {}'.format(v1))
else:
    if v2 < v3:
        print('O menor valor é {}'.format(v2))
    else:
        print('O menor valor é {}'.format(v3))'''
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
print('O menor valor é {}'.format(menor))
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print('O maior valor é {}'.format(maior))
