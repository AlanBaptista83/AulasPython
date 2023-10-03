def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato == False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato == False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')  # 8 casas (00000,00) e alinhado a direita


def menu(msg):
    tam = len(msg)
    print('-' * (tam+8))
    print(f'{msg}'.center(tam+8))
    print('-' * (tam + 8))


def resumo(p=0, aum=10, red=5):
    menu('RESUMO DO VALOR')
    print(f'O preço analisado: \t\t\t{moeda(p)}')
    print(f'A metade de {moeda(p)}: \t{(metade(p, True))}')
    print(f'O dobro de {moeda(p)}:  \t{(dobro(p, True))}')
    print(f'Aumentando {aum}%, temos: \t\t{(aumentar(p, aum, True))}')
    print(f'Reduzindo {red}%, temos: \t\t{(diminuir(p, red, True))}')
    print('-' * 20)
