def voto(n):
    from datetime import date  # Economiza memória usar o import dentro da função apenas - pode usar o datetime ou date
    idade = date.today().year - n
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional!'
    elif idade < 16:
        return f'Com {idade} anos: Não pode votar.'
    elif 65 >= idade >= 18:  # Poderia usar o else:
        return f'Com {idade} anos: Voto Obrigatório.'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
