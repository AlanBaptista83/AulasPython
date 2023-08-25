import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('../music.mp3')
pygame.mixer.music.play(loops=22, start=20.0)
pygame.event.wait()

#Para quem não está conseguindo reproduzir ou precisou colocar um input(),
# o Pygame mudou um pouco desde a postagem do vídeo, agora é necessário iniciar o mixer e o pygame,
# além disso, como os comandos do mixer vem primeiro que o wait(),
# o mixer deve ser inicializado primeiro, podem testar e mudar a ordem dos inicializadores
# para comprovarem que não funciona. Essa é uma das formas corretas, mas colocar o input()
# não é legal pois força o programa a esperar que você insira algum valor manualmente,
# não encerrando o programa ao final da reprodução.

#from playsound import playsound
#playsound('teste.mp3')

#Se você quiser escolher qual musica(arquivo) você quer tocar basta adicionar um comando simples
#import pygame
#pygame.init()
#pygame.mixer.music.load(input('Digite um arquivo:'))
#pygame.mixer.music.play()
#input()
#pygame.event.wait()
#Com isso, você consegue digitar o nome do arquivo e toca-lo (contanto que ele esteja contido na pasta do seu código!)
