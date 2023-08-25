# Jeito 1 - Usando o replace - pesquisa na internet
'''frase = str(input('Digite uma frase: ')).strip().upper()
nova = frase.replace(" ", "")
inverso = ''
for letra in range(len(nova)-1, -1, -1):
    inverso += nova[letra]
#print(nova, inverso)
if nova == inverso:
    print('Sua frase "{}" é um palíndromo! \nOu seja pode ler do final para o início ou do início para o final que serão iguais.'.format(frase))
else:
    print('Sua frase não é um palíndromo')'''

# Jeito 2 - guanabara - divide em lista, troca o espaço
'''palavras = frase.split()
junto = ''. join(palavras)''' # retira os espaços por o que estiver dentro das aspas ''

# Jeito 3 - usando o fateamento de do início ao final mas ao contrario (inicio:final:ao contrario) ( : :-1)
frase = str(input('Digite uma frase: ')).strip().upper()
nova = frase.replace(" ", "")
inverso = nova[::-1]
print('O inverso de {} é {}'.format(nova, inverso))
if nova == inverso:
    print('Sua frase "{}" é um palíndromo! \nOu seja pode ler do final para o início ou do início para o final que serão iguais.'.format(frase))
else:
    print('Sua frase não é um palíndromo')