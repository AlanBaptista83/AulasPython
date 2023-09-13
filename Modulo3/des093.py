jogador = dict()
gols = list()
gol = total = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {i}: '))
    total += gol
    gols.append(gol)
jogador['gols'] = gols[:]
jogador['total'] = total  # Em vez do contador total poderia criar jogador['total'] = sum(partidas)
# jogador['total'] = sum(gols)
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v} ')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(0, len(gols)):  # Poderia usar o for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {gols[i]} gols.')
print('=-' * 30)
print(f'Foi um total de {jogador["total"]} gols.')
