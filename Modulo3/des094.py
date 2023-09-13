pessoa = dict()
lista = list()
somaidades = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    # validação de sexo M ou F
    '''pessoa['sexo'] = str(input('Sexo: [M/F] '))
    while pessoa['sexo'] not in "MmFf":
        pessoa['sexo'] = str(input('Resposta Inválida. Sexo? [M/F]')).upper().strip()'''

    # Validação 2 _ guanabara de sexo M ou F
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO. Favor digitar M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    somaidades += pessoa['idade']
    lista.append(pessoa.copy())

    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while resp not in "SN":
        resp = str(input('''Resposta Inválida. Responda apenas S ou N.
                         Deseja continuar? [S/N]''')).upper().strip()
    if resp == 'N':
        break
print('-=' * 30)
print(lista)
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')
media = somaidades / len(lista)
print(f'A média das idades foi de {media:5.2f} anos.')
print(f'As mulheres são: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=', ')
print()
print('-=' * 30)
print(f'Pessoas com idade acima da média de idade são: ')
for p in lista:
    if p["idade"] > media:
        print('    ', end='')
        for k, v in p.items():
            if k != 'sexo':
                print(f'{k} = {v}; ', end='')
        print()
print('-=' * 30)
print('Encerrado!')
print('-=' * 30)