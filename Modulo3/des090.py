aluno = dict()
situacao = ' '
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
# print(f'Nome é igual a {aluno["nome"]}.')
# print(f'Média é igual a {aluno["media"]}')
if aluno['media'] >= 7:
    # print('Situação é Aprovado')
    aluno['situacao'] = 'Aprovado'
elif  5 <= aluno['media'] < 7:
    # print('Situação é Em Recuperação')
    aluno['situacao'] = 'Recuperação'
elif aluno['media'] < 5:
    # print('Situação é Reprovado')
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}.')
