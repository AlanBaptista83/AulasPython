'''def cabeca(msg):
    print('-=-' *10)
    print(msg)
    print('---' * 10)

# Programa Principal
cabeca('     Dados pessoais')
cabeca('     Endereço')
cabeca('     Contatos')'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# Programa Principal
soma(4, 5)
soma(b=2, a=1)'''

'''def contador(* num):  # Significa desempacotar o que vier de parametro
    cont = 0
    print(f'Recebi os valores: ', end='')
    for i in num:
        cont += 1
        print(f'{i} ', end='')
    print(f' e esse contador possui {cont} números.')
    print('FIM!')
    tam = len(num)
    print(f'{tam}')



#Programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 6, 2)'''
def dobra(lst):  # Chama uma lista usando qualquer nome
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)