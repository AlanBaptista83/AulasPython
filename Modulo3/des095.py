time = list()
jogador = dict()
partidas = list()
resp = ' '
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int (input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range (0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Resposta inválida. Responda S para SIM e N para NÃO"')
    if resp in 'N':
        break
print(' Cod Nome             Gols        Total de Gols')
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
'''print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
    for i, v in enumerate(jogador['gols']):
        print(f'    => Na partida {i}, fez {v} gols.')
    print(f'Foi um total de {jogador["total"]} gols.')
    resp = str(input('Deseja continuar: ')).upper().strip()'''