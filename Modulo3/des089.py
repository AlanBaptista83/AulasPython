sala = list()
resp = 'S'
sair = i = 0
while resp not in 'Nn':
    n = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    sala.append([n, [n1, n2], m])
    resp = str(input('Quer continuar? [S/N] '))
    while resp not in 'SsNn':
        resp = str(input('Digite S ou N. Quer continuar? [S/N] '))
print('-=' * 15)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
for i in range(0, len(sala)):
    print(f'{i:<4} {sala[i][0]:<10} {sala[i][2]:>8}')
print('-=' * 30)
while True:
    sair = int(input('Mostrar nota de qual aluno: (999 interrompe) '))
    if sair == 999:
        print('Finalizando...')
        break
    if sair >= len(sala):
        print('Não existe esse aluno!')
    if sair < len(sala):
        print(f'As notas do {sala[sair][0]} são {sala[sair][1]}')
print('Volte sempre!')
