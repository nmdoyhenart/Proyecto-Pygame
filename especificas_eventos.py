"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame

def efecto_de_sonido():
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(r"TP-PYGAME-COLLAB-main\recursos\pop.mp3")
    sonido_fondo.set_volume(0.7)
    sonido_fondo.play()

def derrota():
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(r"TP-PYGAME-COLLAB-main\recursos\error.mp3")
    sonido_fondo.set_volume(0.7)
    sonido_fondo.play()

def comodin_usado():
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(r"TP-PYGAME-COLLAB-main\recursos\error windows.mp3")
    sonido_fondo.set_volume(0.7)
    sonido_fondo.play()

def respuesta_correcta_sonido():
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(r"TP-PYGAME-COLLAB-main\recursos\respuesta_correcta.mp3")
    sonido_fondo.set_volume(0.7)
    sonido_fondo.play()
