pessoas = list()
dados = list()
resp = ' '
total = maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    total += 1
    resp = str(input('Deseja inserir nova pessoa e peso? [S/N] ')).upper().strip()
    if resp not in "SN":
        resp = str(input('Resposta inválida. Deseja inserir nova pessoa e peso? [S/N] '))
    else:
        if resp == 'N':
            break
for i in range(0, total):
    if i == 0:
        menorpeso = maiorpeso = pessoas[i][1]
    elif pessoas[i][1] > maiorpeso:
        maiorpeso = pessoas[i][1]
    elif pessoas[i][1] < menorpeso:
        menorpeso = pessoas[i][1]

print(f'Foram cadastras {total} pessoas.')
print(f'O maior peso foi {maiorpeso}Kg de', end=' ')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O maior peso foi {menorpeso}kg de', end=' ')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')
