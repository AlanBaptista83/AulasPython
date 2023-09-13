'''pessoas = {'nome': 'Alan', 'sexo': 'M', 'idade': 40}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome'] = 'Matheus'
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
print(pessoas)

pessoas['peso'] = 75.6
print(pessoas)'''

brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'capital': 'Rio de Janeiro'}
estado2 = {'uf': 'Minas Gerais', 'capital': 'Belo Horizonte'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1]['capital'])
'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v, in e.items():
        print(f'O campo {k} tem valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
print(brasil[1])'''
