nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito {}!'.format(nome))
elif nome == 'Alan' or nome == 'Matheus' or nome == 'Maria':
    print('Que nome diferente, {}!'.format(nome))
elif nome == 'Nathalia':
    print('Nome da minha esposa!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia!')