"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
from especificas import *

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)
ROJO_CLARO = (255, 150, )

ANCHO_VENTANA = 800
ALTO_VENTANA = 600

VENTANA1 = (ANCHO_VENTANA, ALTO_VENTANA)

pygame.init()

ventana = pygame.display.set_mode(VENTANA1)
pygame.display.set_caption("Tot or trivia")

icono = pygame.image.load(r"TP-PYGAME-COLLAB/recursos/logo.jpg")
pygame.display.set_icon(icono)

fondo = pygame.image.load(r"TP-PYGAME-COLLAB\recursos\fondo.jpg")
fondo = pygame.transform.scale(fondo, VENTANA1)

fuente = pygame.font.Font(None, 36)

input = pygame.Rect(210, 400, 120, 90)
color = ROJO
color_inactivo = AZUL
color_activo = ROJO
color = color_inactivo
activo = False
texto = ""

bandera = True

while bandera:
   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if input.collidepoint(evento.pos):
                efecto_de_sonido()                 
                activo = not activo
            color = color_activo if activo else color_inactivo

    ventana.blit(fondo,(0,0))
 
    texto_superficie = fuente.render("This or that", False, BLANCO)

    ventana.blit(texto_superficie, (input.x + 5, input.y + 5))
    pygame.draw.rect(ventana, color, input, 2)

    pygame.display.update()

pygame.quit()