nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média foi {:.1f}. REPROVADO!'.format(media))
elif 7 > media >=5:
#elif media >= 5 and media < 7:
    print('Sua média foi {:.1f}.RECUPERAÇÃO!'.format(media))
else:
    print('Sua média foi {:1.f}.APROVADO'.format(media))
