alt = float(input('Quantos metros de altura tem a parede a ser pintada? '))
largura = float(input('E quantos metros de largura? '))
area = alt * largura
pintura = area / 2
print('Você possui uma área de {} metros e vai precisar de comprar {} litros de tinta'.format(area, pintura))
