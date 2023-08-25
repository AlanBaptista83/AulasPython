num = [2, 4, 9, 1]
num[2] = 8 # Troca o 9 da posição 2 para o número 3
num.append(7)  # Adicionar o 7 no final da lista
#num.sort() #ordem alfabética
print(num)
#num.sort(reverse=True)  # ondem descrescente
num.insert(2, 2)  # inseri na posição 2 o número 0
num.insert(0, 9)
print(num)
'''num.pop()  # Elimina o último item da lista
print(num)
num.pop(4)  # Elimina o item da posição 3
print(num)
num.remove(2)  # remove o primeiro item dentro do () no caso o 2
num.remove(2)  # remove o primeiro item dentro do () no caso o 2'''
if 1 in num:
    num.remove(1)
else:
    print(f'Não encontrei o número 1')
print(num)
print(f'Essa lista tem {len(num)} elementos')
print(f' O menor número dessa lista é o {min(num)}')
print(f'O menor número está na posição {num.index(min(num))}')
