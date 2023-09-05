nome = list()
nota = list()
media = list()
sala = list()
resp = 'S'
sair = i = 0

while resp not in 'Nn':
    n = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    nome.append(n)
    nota.append(n1)
    nota.append(n2)
    nome.append(nota[:])
    nome.append(m)
    sala.append(nome[:])
    nome.clear()
    nota.clear()
    media.clear()
    resp = str(input('Quer continuar? [S/N] '))
    while resp not in 'SsNn':
        resp = str(input('Digite S ou N. Quer continuar? [S/N] '))
print('''-=' * 30
No. Nome        Média
----------------------''')
for i in range(0, len(sala)):
    print(f'{i} {sala[i][0]:>6} {sala[i][2]:>13}')
print('-=' * 30)
while sair != 999:
    sair = int(input('Mostrar nota de qual aluno: (999 interrompe) '))
    if sair != 999:
        print(f'As notas do {sala[sair][0]} são {sala[sair][1]}')
print('Volte sempre!')