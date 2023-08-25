'''n = int(input('Digite um número: '))
cont = 1
média = 0
soma= copia = maior = menor = n
sair = 'S'
while sair == 'S':
    n = int(input('Digite outro número: '))
    soma = soma + n #  soma += 1
    cont = cont + 1
    sair = str(input('Deseja continuar [S/N]: ').upper()).strip()[0]
    if copia < n:
        maior = n
    elif copia > n:
        menor = n
    copia = n
media = soma / cont
print('Você digitou {} número(s) e a média foi {}.'.format(cont, media))
print('O maior número foi o {} e o menor {}.'.format(maior, menor))
print('A soma deles foi {}!'.format(soma))'''

resp = 'S'
soma = quant = média = maior = menor = 0
while resp == 'S':
    núm = int(input('Digite um número: '))
    resp = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    if resp != 'S' and resp != 'N':
        while resp != 'S' and resp != 'N':
            resp = str(input(('\033[97mDigite apenas\033[m \033[32mS para SIM \033[97mou \033[31mN para NÃO:\033[m '))).upper().strip()
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))

'''l = []
p1 = 'S'
while p1 in 'Ss':
    num = int(input('Digite um numero : '))
    p1 = input('Quer continuar ? [S/N]').strip().upper()
    l.append(num)
    if p1 == 'N':
        break
print(f'Você digitou {len(l)} numeros e a media foi {sum(l) / len(l)} \n O maior valor foi {max(l)} e o menor foi {min(l)}')'''