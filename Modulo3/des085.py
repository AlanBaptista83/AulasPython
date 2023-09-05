lista = list()
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
print(lista)
par.sort()
print(par)
impar.sort()
print(impar)

