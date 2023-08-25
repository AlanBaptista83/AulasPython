count = p = S = maior = menor = 0
while not p == 'N':
    n = int(input('\033[30mDigite um número inteiro:\033[m '))
    p = str(input('\033[30mQuer continuar? [\033[m \033[32mS\033[m/ \033[31mN\033[m \033[30m]\033[m: ')).upper().strip()
    if p != 'S' and p != 'N':
        while p != 'S' and p != 'N':
            p = str(input(('\033[30mDigite apenas\033[m \033[32mS para SIM \033[30mou \033[31mN para NÃO:\033[m '))).upper().strip()
    if n > maior:
        maior = n
    if count == 0:
        menor = n
    if n < menor:
        menor = n
    count += 1
    S = S + n
    if p == 'N':
        break

mem = S / count

print('\nA média dos \033[33m{} valores\033[m é \033[34m{}\033[m'.format(count, mem))
print('O \033[35mmaior\033[m valor é \033[35m{}\033[m e o \033[36mmenor\033[m é \033[36m{}\033[m'.format(maior, menor))