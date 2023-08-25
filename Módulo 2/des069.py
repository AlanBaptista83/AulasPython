contidade = masc = menoridadef = 0
while True:
    print('-=-' * 30)
    print('Cadastre uma pessoa')
    while True:
        try:
            idade = int(input('Digite a idade: '))
            break
        except ValueError:
            print('Não é uma idade valida. tente novamente')
    sexo = str(input('Digite o sexo [M / F]: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        while sexo != 'M' and sexo != 'F':
            print('Opção Inválida. Digite M para Masculino e F para Feminino!')
            sexo = str(input('Digite o sexo [M / F]: ')).upper()
    if idade > 18:
        contidade += 1
    if idade < 20 and sexo == 'F':
        menoridadef += 1
    if sexo == 'M':
        masc += 1
    cont = str(input('Quer continuar? [S/N]')).upper().strip()
    if cont != 'S' and cont != 'N':
        while cont != 'S' and cont != 'N':
            print('Opção Inválida. Digite S para Sim e N para Não!')
            cont = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if cont == 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de {contidade} pessoas com mais de 18 anos')
print(f'Ao todo temos {masc} homens cadastrado(s)')
print(f'E temos {menoridadef} mulheres com menos de 20 anos')
