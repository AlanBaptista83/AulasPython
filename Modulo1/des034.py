salario = float(input('Qual o salário do funcionário? R$'))
'''if salario <= 1250.00:
    novo = salario * 1.15
else:
    novo = salario * 1.1
print('Quem ganhava R${:.2f} passará a ganhar R${:.2f} agora.'.format(salario, novo) )'''
print('Novo salario R${:.2f}'.format(salario * 1.15) if salario <= 1250.00 else 'Novo salário {:.2f}.'.format(salario * 1.10))
