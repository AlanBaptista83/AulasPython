from datetime import date
atual = date.today().year
# print(atual)
soma = 0
menor = 0
c = 0
# maior = atual - 18 Não precisa. foi para dentro do if abaixo
# print(maior)
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if ano <= atual - 18:
        soma += 1
    else:
        menor += 1
print('Desse total de {} pessoas, {} são maiores de idades (nasceram até 2005)'.format(c, soma))
print('E {} pessoas são menores de idade'.format(menor))
