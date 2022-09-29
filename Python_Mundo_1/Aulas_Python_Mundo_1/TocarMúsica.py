# Tem duas formas para tocar música

# Primeira forma é importando a biblioteca *playsound* e utilizando os comandos abaixo:
import playsound
playsound.playsound('C:\\Users\lucas\Músicas\ex021.mp3')

# Segunda forma é importando a biblioteca *pygame* e utilizando os comandos abaixo:
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
