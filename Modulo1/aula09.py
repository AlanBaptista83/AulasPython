frase = str('Curso em Vídeo Python')
#pega do 9 ao 20, pulando de 2 em 2 (salta um caracter)
print (frase[9:21:2])

#Do início ao índice
print (frase[:5])

#de um ponto até o final
print (frase[15:])

#Começa no 9, até o final (nada) e pulando de 3 em tres (salta dois caracteres)
print (frase[9::3])

#tamanho da frase - len
print (len(frase))

#Contar quantas vezes um caracter se repete, em um determinado intervalo (0 a 12)
print(frase.count('o',0,13))

# procura um conjunto de caracteres e indica a posição inicial dela. Se resultado for -1 é que não encontrou nenhuma
print(frase.find('Python'))
print(frase.lower().find('Python'))

# indica se tem ou não uma palavra na frase
print ('Curso' in frase)

#encontrar uma palavra e substituir por outra
print (frase.replace('Python','Android'))

#Método - Colocar tudo em maiúsculas
print (frase.upper())

# Método - Colocar tudo em minúsculas
print (frase.lower())

#Método - Só primeira letra mantem em Maiúscula, resto minúsculas
print (frase.capitalize())

# Método - Cada primeira letra da palavra fica em Maiúsculas
print (frase.title())

#método - retira espaços desnecessários antes ou depois
print (frase.strip())

#Método - retira espaços à direita
print(frase.rstrip())

#Método - retira espaços à esquerda
print(frase.lstrip())

#Dividir a string em cada palavra uma lista
print(frase.split())

lista = ('frase', 'teste', 'lista')
#juntar as frase colocando o separador que está entre aspas '-'
print('-'.join(lista))


print('''Se eu digitar um texto muito grande:
kmas eoiusdfkjsdf lçjsdflkjsd lkjsd flkjas dflç
 
  laskdfj lskdfj lkjasd fl teste''')

#troca = ('Curso  em vídeo Python')
troca = ('Curso Android em vídeo Android')
troca = troca.replace('Android','Python')
print(troca)

dividido = frase.split()
print(dividido)
print(dividido[2] [3:])
