'''lista = list()
par = list()
impar = list()
for i in range(0,7):
    num = int(input(f'Digite o {i + 1}º valor: '))
    if num % 2 == 0:
        par.append(num)
    if num % 2 == 1:
        impar.append(num)
lista.append(par)
lista.append(impar)
# print(lista)
par.sort()
print(f'Os valores pares digitados foram: {par}')
impar.sort()
print(f'Os valores ímpares digitados foram: {impar}')'''

num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}')
print(f'Os valores ímpares foram: {num[1]}')
