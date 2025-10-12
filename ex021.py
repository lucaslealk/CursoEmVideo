'''Faça um programa em python que abra e reproduza o áudio de um 
arquivo mp3.'''
import pygame 
#para inicializar o mixer e o pygame
pygame.mixer.init()
pygame.mixer.music.load('01.mp3')
pygame.mixer.music.play()
input('Agora você escuta? ')
#para esperar o evento acabar
pygame.event.wait()
