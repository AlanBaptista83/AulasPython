'''def ajuda():
    a = ''
    while a != 'fim':
        print('\033[7;49;92m~' * 30, '\033[m')
        print('\033[7;49;92m   SISTEMA DE AJUDA PYHELP     \033[m')
        print('\033[7;49;92m~' * 30, '\033[m')
        a = str(input('Função ou Biblioteca > '))
        if a == 'fim':
            break
        help(a)



# Programa Principal
ajuda()
print('\033[1;49;95m~' * 30,'\033[m')
print('\033[1;49;95m   Até Logo        \033[m')
print('\033[1;49;95m~' * 30, '\033[m')'''
from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;99;41m',    # 1 - vermelho
     '\033[1;99;42m',    # 2 - verde
     '\033[1;99;43m',    # 3 - amarelo
     '\033[1;99;44m',    # 4 - azul
     '\033[1;99;45m',    # 5 - roxo
     '\033[7;99m'       # 6 - branco
     );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6])
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

#Programa Principaç
comando = ''
while True:
    título('SISTEMA de AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)