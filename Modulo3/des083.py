lista = list()
expr = (str(input('Digite uma expressão: ')))
for c in expr:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:  # lista == ' ':
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print(f'A expressão é válida.')
else:
    print(f'A expressão está errada.')


