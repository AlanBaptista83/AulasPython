nome = str(input('Digite seu nome completo:')).strip()
dividido = nome.split()
#print(dividido)
print('Seu primeiro nome é {}'.format(dividido[0]))
#print('Seu último nome é {}'.format(dividido[-1]))

#outra forma usando o len
#print('Seu último nome é {}'.format(dividido[len(dividido)-1]))

#Calculando os espaços
#nome = str(input('Escribe tu nombre completo: ')).strip().title()
#pri = nome.find(' ')
#print('Su primer nombre es {}'.format(nome[0:pri]))
#ult = nome.rfind(' ')
#print('Su último nombre es {}'.format(nome[ult:]))

print(f'Seu primeiro nome é:{nome.split()[0]}\nSeu ultimo nome é: {nome.split()[-1]}')