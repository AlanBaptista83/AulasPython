def area(larg, c):
    a = larg * c
    print(f'A área de um terreno {larg}x{c} é {a}m².')


# Programa Principal
print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m):'))
area(largura, comprimento)
