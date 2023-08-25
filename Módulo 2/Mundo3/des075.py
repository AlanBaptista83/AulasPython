numero = (int(input('Digite um  número: ')),
          int(input('Digite outro  número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O valor 3 apareceu na posição {numero.index(3)+1}.')
else:
    print(f'O número 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: ')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
