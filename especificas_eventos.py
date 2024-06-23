"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame

def efecto_de_sonido():
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(r"TP-PYGAME-COLLAB\recursos\pop.mp3")
    sonido_fondo.set_volume(0.7)
    sonido_fondo.play()

# def musica_fondo():
#     pygame.mixer.init()
#     sonido_fondo = pygame.mixer.Sound(r"Recursos/musica.mp3")
#     sonido_fondo.set_volume(0.2)
#     sonido_fondo.play()