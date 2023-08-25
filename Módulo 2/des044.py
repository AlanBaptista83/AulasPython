print('{:=^40}'.format(' Lojas Guanabara '))
preço = float(input('Digite o valor das compras: R$ '))
forma = int(input('''Qual a forma de pagamento?
 Digite 1 - dinheiro/pix (10% de desconto)
 Digite 2 - À vista no cartão (5% de desconto)
 Digite 3 - 2x no cartão (preço normal sem juros)
 Digite 4 - 3x ou mais no cartão (20% de juros)
 --> '''))
if forma == 1:
    print('Sua compra sairá por R${:.2f} no dinheiro ou pix e terá 10% de desconto.'.format(preço * 0.9))
elif forma == 2:
    print('Sua compra sairá por R${:.2f} à vista no cartão com 5% de desconto.'.format(preço * 0.95))
elif forma == 3:
    print('Sua compra sairá por R${:.2f} em 2x de R${:.2f} no cartão.'.format(preço, preço / 2))
elif forma == 4:
    parcelas = int(input('Em quantas vezes você deseja dividir? '))
    if parcelas <= 10: #necessário tratar if com 1 ou 2 parcelas
        print('Sua compra sairá por R${:.2f} em {}x de R${:.2f} no cartão com juros de 20%.'.format(preço * 1.2, parcelas, preço * 1.2 / parcelas))
    else:
        print('Parcelamos em no máximo 10 vezes')
else:
    print('Opção invalida. Refaça a compra.')
