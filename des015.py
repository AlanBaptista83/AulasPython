dias = int(input('Quantos dias você alugou um veículo? '))
km = float(input('Quantos Km você andou com o carro? '))
# preço_dias = dias * 60
# preço_km = km * 0.15
print('Com {} dias de aluguel e o valor de R$ 60,00 por dia, você precisa pagar R${:.2f}.'.format(dias, dias * 60))
print('Você andou {}Km no total. Esse quantitativo gera um pagamento de R${:.2f}.'.format(km, km * 0.15))
# preço =
print('O valor total do seu aluguel é R${:.2f}.'.format(((dias * 60) + (km * 0.15))))
