print('-=-' *20)
print('Analisador de triãngulos')
print('-=-' * 20)
t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Podem formar um triângulo!')
    #if t1 == t2 and t1 == t3:
    if t1 == t2 ==t3:
        print('Triângulo Equilátero! Todos os lados iguais.')
        # poderia fazer o teste do escaleno primeiro e o isosceles seria o restante
    elif t1 == t2 or t1 == t3 or t2 == t3:
        print('Triângulo Isósceles! Dois lados iguais.')
    #if t1 != t2 != t3 != t1: Tem que validar o 1º com 3º tb. diferete de quando é igual.
    else:
        print('Triângulo Escaleno! Todos os lados diferentes.')
else:
    print('Não podem formar um triângulo!')