valor = float(input('Digite o valor do imóvel a ser adquirido: R$'))
salario = float(input('Digite qual a sua renda pessoal (salário): R$'))
anos = int(input('Em quantos anos pretende pagar o emprestimo? (em anos)'))
prestacao = valor / (anos * 12)
if prestacao >= salario * 0.3:
    print('Infelizmente não podemos realizar seu empréstimo!')
    print('Sua prestação seria de R${:.2f} e é maior que 30% (R${:.2f}) que sua renda atual de R${:.2f} por mês.'.format(prestacao, salario * 0.3, salario))
else:
    print('Seu emprétimo foi aprovado e sua prestação será de R$ {:.2f} por mês'.format(prestacao))
print('Volte sempre!')