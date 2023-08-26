'''lista = list()
resp = ' '
while True:
    if resp == "N":
        break
    lista.append(int(input('Digite um número: ')))
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()
        if resp not in 'SN':
            print('Opção inválida!', end='')
        if resp in 'SN':
            break
print(lista)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 se encontra na lista')
else:
    print(f'O valor 5 não se encontra na lista')'''
lista = []
num5 = []
cont = 0
while True: # a estrutura while adiciona valores
            # e se o numero 5 for adicionado ele irá contar
    n = int(input("Digite um numero :"))
    r = str(input("Quer continuar ? [S/N]"))[0]
    lista.append(n)
    if n == 5:
        cont += 1
    if r in "Nn":
        break
for i, v in enumerate(lista): # essa estrutura utiliza o enumerate
                              # para encontrar a posição do 5 se estiver na "lista"
                              # ele joga a posição dele para a lista : num5
    if v == 5:
        print(i,v)
        num5.append(i+1)

print(f"Foram digitados {len(lista)} numeros ")

if 5 in lista: #se o valor 5 estiver na lista ele irá mostrar quantos tem , e qual é a sua respectiva posição
    print(f"O numero 5 esta na lista {lista},sendo que a lista contem {cont}")
    print(f'Estando nas posições {num5}, em ordem decrescente')
else:
    print('O numero 5 não esta na lista ')
lista.sort(reverse=True) #esse comando coloca a lista em ordem decrescente
print(f"Sendo em ordem decrescente {lista}")