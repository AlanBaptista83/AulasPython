num = int(input('Digite um número para aparecer sua tabuada: '))
print('Está é a tabuada do {}'.format(num))
for s in range(0, 11):
    print('{} x {} = {}'.format(num, s, s * num))
