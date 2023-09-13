from datetime import date
cadastro = dict()
apos = 0
cadastro['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento (4 dígitos): '))
data = date.today().year  # poderia usar a função datetime.now().year
cadastro['idade'] = data - nascimento
cadastro['trabalho'] = int(input('Carteira de Trabalho (0 se não tem): '))
if cadastro['trabalho'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    apos = cadastro["idade"] + (35 - (data - cadastro["contratação"]))
    cadastro['aposentadoria'] = apos
for k, v in cadastro.items():
    print(f'  - {k} tem o valor de {v}')
