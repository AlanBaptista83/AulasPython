from time import sleep
time = list()
jogador = dict()
partidas = list()
resp = ' '
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}: ')))
    jogador['partidas'] = tot
    jogador['total'] = sum(partidas)
    jogador['gols'] = partidas[:]
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Resposta inválida. Responda S para SIM e N para NÃO"')
    if resp in 'N':
        break
print(' Cod  / Nome  / Partidas / Total Gols / Gols')
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>4} ', end=' / ')
    for d in v.values():
        print(f'{str(d):<6}', end=' / ')
    print()
print('-' * 50)
while True:
    pesq = int(input('Qual jogador você quer pesquisar? Digite pelo Código: (999 para sair) '))
    if pesq == 999:
        break
    if pesq >= len(time):
        print('ERRO. Não existe esse jogador na pesquisa. Tente outro código.')
    else:
        print('-=' * 30)
        print(f'Pesquisando o jogador {time[pesq]["nome"]}...')
        sleep(1)
        print('-=' * 30)
        print(f'{time[pesq]["nome"]} fez {time[pesq]["partidas"]} partidas e: ')
        for i, v in enumerate(time[pesq]['gols']):
            print(f'    => Na partida {i+1}, fez {v} gols.')
        print(f'Foi um total de {time[pesq]["total"]} gols.')
    print('-=' * 30)
print('Volte Sempre!')
