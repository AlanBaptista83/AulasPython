'''sexo = ' '
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite qual o seu sexo [ M / F ]: ')).upper()
    if sexo != 'F' and sexo != 'M':
        print('Você não digitou uma opção valida. Tente novamente!')
    else:
        if sexo == 'F':
            print('Entendi, você é uma pessoa do sexo feminino.')
        else:
            print('Entendi, você é uma pessoa do sexo masculino.')
print('Fim.')'''

sexo = ' '
# while sexo not in 'MmFf': # forma simplificada
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite qual o seu sexo [ M / F ]: ')).upper().strip()[0] #Fatiamento para pegar a 1 letra digitada
    if sexo != 'F' and sexo != 'M':
        print('Você não digitou uma opção valida. Tente novamente!')
    '''else:
        if sexo == 'F':
            print('Entendi, você é uma pessoa do sexo feminino.')
        else:
            print('Entendi, você é uma pessoa do sexo masculino.')'''
print('Você digitou que é do sexo {}.\nFim.'.format(sexo))
