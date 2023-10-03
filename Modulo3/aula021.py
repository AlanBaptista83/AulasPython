def ParouImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número inteiro: '))
if ParouImpar(num):  # Se Verdadeiro atende o if, se falso atende o else
    print('É par!')
else:
    print('É ímpar!')


'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
f1 = fatorial(4)
f2 = fatorial(5)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''



'''def contador(i, f, p):
    """ # basta digitar 3 aspas e dar enter.              ### docstrings
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    Criado por Alan Baptista
    """
    c = i
    while c <=f:
        print(f' {c}',end='..')
        c += p
    print('FIM!')


contador(2,10,2)
help(contador)'''


'''def somar(a=0, b=0, c=0):           # Parametros opcionais
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()
# somar(3, 3, 5, 6) erro'''

'''def funcao(n1):  # ESCOPO DE VARIÁVEIS
    print(f'N1 ainda puxando da global {n1}')
    n1 = 4
    print(f'N1 local vale {n1}')


n1 = 2
print(f'N1 global vale {n1}')
funcao(n1)
print(f'N1 global continua valendo {n1}')'''

'''def teste(b):
    global a  # Faz a variável global ser alterada. Sem esse parametro seria criado outro "a" dentro do DEF
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f' A fora vale {a}')'''

