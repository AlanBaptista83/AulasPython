'''s = 0
for c in range(0, 500, 3):
    if c % 2 != 0:
        print(c, end=' ')
        s += c
print(s)'''

#Fazendo o inverso - FOR com todos os impares e verificar se é divisível por 3
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        s += c
        cont += 1 #cont = cont + 1
print('\nA minha soma de todos os {} números foi {}'.format(cont, s))
