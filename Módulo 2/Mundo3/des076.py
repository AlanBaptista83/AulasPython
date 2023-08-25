produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 20,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-=-' * 14)
print(f'{"LISTAGEM DE PREÇOS":^40}')  # Alinhado centralizado e usar sempre f strig {} e aspas duplas "
print('-=-' * 14)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=' ')
    if pos % 2 == 1:
        print(f'R$ {produtos[pos]:>7.2f}')
