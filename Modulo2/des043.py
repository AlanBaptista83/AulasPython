print('-=-' *20)
print('Calculando seu IMC')
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc <18.5:
    print('Você está abaixo do peso ideal.')
#elif imc >=18.5 and imc <=25:
elif 25 > imc >= 18.5:
    print('Você está no peso ideal.')
elif 30 > imc >= 25:
    print('Você está com sobrepeso.')
elif 40 > imc >= 30:
    print('Você está com Obsidade.')
elif imc >= 40:
# else:
    print('Você está com Obsidade Mórbida.')
