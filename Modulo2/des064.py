n = int(input('Digite um número ou [999] para sair: '))
soma = 0
cont = 0
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('digite outro número ou digite [999] para sair: '))
print('Você inseriu {} números e a soma deles foi {}!'.format(cont, soma))
