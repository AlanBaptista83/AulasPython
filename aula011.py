#print('\033[7;97mteste\033[m')

'''a = 3
b = 5
print('Os valores são \033[31m{} \033[me \033[35m{}\033[m!!!'.format(a, b))'''

'''nome = 'Alan'
print('Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))'''

nome = 'Alan'
#Criando variáveis para cada cor
'''limpa = '\033[m'
azul = '\033[34m'
amarelo = '\033[33m'
pretoebranco = '\033[7;97m'''

#criando uma váriavel única com várias cores - dicionário de cores
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;97m'
        }
print('Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
