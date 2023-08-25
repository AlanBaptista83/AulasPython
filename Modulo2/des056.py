somaidade = 0
maior_idade = 0
c = ''
nome2 = ''
nomemaior = ''
fem = 0
idadefem = 0
sexomasc = 0
for c in range(1, 5):
    print('=-=-= Pessoa {} =-=-='.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()  # Usar o uper usar no ip 'Mm' ou 'Fm' para aceitar maiuscula ou minuscula
    somaidade = somaidade + idade
    if sexo in 'Mm':  # Forma de testar uma letra em maiuscula ou minuscula''
        sexomasc = 1
        if idade > maior_idade:
            maior_idade = idade
            nomemaior = nome
        if idade == maior_idade:
            nome2 = nome
    elif sexo in 'Ff':
        fem += 1
        if idade < 20:
            idadefem += 1
print('A média de idade desse grupo de {} pessoas foi {:.1f} anos'.format(c, somaidade / c))
if nome2 == '':
    if sexomasc == 1:
        print('{} é o homem mais velho desse grupo e tem {:.0f} anos.'.format(nomemaior, maior_idade))
    else:
        print('Não temos nesse grupo nenhum homem, portanto não temos nenhum mais velho!')
else:
    print('''Temos 2 homem com a mesma idade {} e {}.
    Ambos são os mais velhos e possuem {:.0f} anos.'''.format(nomemaior, nome2, maior_idade))
print('Desse grupo um total de {} são mulher e {} possuem menos de 20 anos.'.format(fem, idadefem))
