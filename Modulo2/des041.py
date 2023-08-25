from datetime import date
print('-=-' *20)
print('Confederação Nacional de Natação')
print('Categorias: \nAté 9 anos: Mirim \nAté 14 anos: Infantil \nAté 19 anos: Junior \nAté 20 anos: Sênior \nAcima: Master')
nasc = int(input('Digite o ano do seu nascimento: '))
ano = date.today().year
categoria = ano - nasc
idade = ano - nasc
if categoria <= 9:
    print('Você tem {} anos e está na Categoria Mirim'.format(idade))
#elif categoria >9 and categoria <= 14:
elif categoria <= 14:
    print('Você tem {} anos e está na Categoria Infantil'.format(idade))
#elif categoria >14 and categoria <=19:
elif categoria <= 19:
    print('Você tem {} anos e está na Categoria Junior'.format(idade))
#elif categoria >19 and categoria <=20:
elif categoria <= 20:
    print('Você tem {} anos e está na Categoria Sênior'.format(idade))
else:
    print('Você tem {} anos e está na Categoria Master'.format(idade))
