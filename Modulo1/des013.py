nome = input('Digite seu nome: ')
print('Olá {}!'.format(nome))
salario = float(input('Qual o seu salário atual? R$ '))
print('Estamos muito felizes com seu desempenho profissional!')
print('Queremos lhe recompensar por isso...')
print('O que acha de receber um aumento de 15% no seu salário?')
print('Em vez de R${:.2f} seu novo salário será R${:.2f}'.format(salario, salario*1.15))
print('Você mereceu cada centavo! Bom trabalho')
