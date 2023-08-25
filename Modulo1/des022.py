nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('O número total de caracteres sem espaço é: ',len(nome) - nome.count(' '),'.')
dividido = nome.split()
#print(dividido)
#print('O primeiro nome é',dividido[0],'e tem',len(dividido [0]), 'caracteres.')

#outra maneira de contar quantas letrar tem o primeiro nome
print('Seu primeiro nome tem {} caracteres'.format(nome.find(' ')))
