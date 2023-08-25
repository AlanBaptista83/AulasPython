from datetime import date
nasc = int(input('Digite seu ano de nascimento (4 dígitos): '))
# Se importar o dateime inteiro import datetime
'''data = datetime.date.today()
ano = data.year'''
ano = date.today().year
alist = ano - 18
#print(data, ano)
if alist == nasc:
    print('Você tem 18 anos e tem que se alistar no exército esse ano.')
elif alist < nasc:
    falta = nasc - alist
    print('Falta {} anos para você se alistar no exército.'.format(falta))
else:
    passou = alist - nasc
    print('Você já se alistou no exército ou passou {} ano(s) de se alistar.'.format(passou))
