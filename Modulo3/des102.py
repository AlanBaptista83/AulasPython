def fatorial(a=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param a: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número a.
    """
    f = 1
    for i in range(a, 0, -1):
        f *= i
        if show:
            if i == 1:
                print('1 = ', end='')
            else:
                print(f'{i} x ', end='')
    return f


# Programa Principal
print(fatorial(5, show=False))
#help(fatorial)
