
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra \33[31m{p.upper()}\33[m temos', end=' ',)
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f' \33[33m{letra}\33[m', end=' ')

