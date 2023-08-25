times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fluminense', 'Grêmio', 'Athletico PR', 'Bragantino', 'Fortaleza',
         'Cuiabá', 'São Paulo', 'Atlético MG', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos',
         'Vasco', 'Coritiba', 'América MG')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
for t in times:
    print(t)

print('-=-'*40)
print(f'Os quadro times na zona de rebaixamento são: {times[-4:]}')
print('-=-'*40)
print(f'Times em ordem alfabética{sorted(times)}')
print('-=-'*40)
print(f'O Vasco está na posição {times.index("Vasco")+1}')
print('-=-'*40)
print(times.index('Vasco'))
