soma = contmaior = menorpreco = 0
produtobarato = cont = ''
while True:
    produto = str(input('Digite o produto: '))
    preco = float(input('Preço do produto: R$ '))
    soma += preco
    if preco == 1 or preco <= menorpreco:
        menorpreco = preco
        produtobarato = produto
    if preco > 1000:
        contmaior += 1
    cont = str(input('Deseja cadastrar mais produtos: [S/N]')).upper().strip()
    while cont not in 'SN':  # Enquanto não tiver SN faça
        '''if cont != 'N' and cont != 'S':
        while cont != 'N' and cont != 'S':'''
        print('Opção Inválida. Digite S para SIM ou N para NÃO!')
        cont = str(input('Deseja cadastrar mais produtos: ')).upper().strip()
    if cont == 'N':
        break
print('{:-^40}'.format('Fim do programa'))
print(f'O total gasto foi de R$ {soma:.2f}')
print(f'Sua compra possui {contmaior} produtos que custam mais de R$ 1000,00 (mil reais)')
print(f'O produto {produtobarato} é o que tem o menor preço na sua compra e custa R$ {menorpreco:.2f}')
