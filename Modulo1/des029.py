velocidade = float(input('Qual é a velocidade atual do carro?'))
if  velocidade > 80:
    multa = float(velocidade - 80) * 7
    print('Você está acima da velocidade máxima que é 80Km/h.')
    print('Foi multado em R${:.2f}'.format(multa))
else:
    print('Siga a viagem! Você está dentro da velocidade permitida.')
print('Tenha um bom dia! Dirija com segurança!')
