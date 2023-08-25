soma = 0
for c in range(1, 7):
    num = int(input('Digite o {} número: '.format(c)))
    resto = num % 2
     if resto == 0:
        soma = soma + num
print('A soma dos número pares foi {}'.format(soma))
