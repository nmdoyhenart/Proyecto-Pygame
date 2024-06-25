"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
from evento2 import *
from especificas_eventos import *
from modulo_preguntas import *

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (128, 191, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)
ROJO_CLARO = (255, 150, 136)

tupla = (ROJO, AZUL)

PUNTOS = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]


ANCHO_VENTANA = 700
ALTO_VENTANA = 900

VENTANA1 = (ANCHO_VENTANA, ALTO_VENTANA)

pygame.init()

ventana = pygame.display.set_mode(VENTANA1)
pygame.display.set_caption("Tot or trivia")

icono = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\logo.jpg")
pygame.display.set_icon(icono)

fondo = pygame.image.load(r"TP-PYGAME-COLLAB-main/recursos/fondo.jpg")
fondo = pygame.transform.scale(fondo, VENTANA1)

jueces = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\guampa.png")
jueces = pygame.transform.scale(jueces, (100, 150))

tribuna = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\tribuna transparente.png")
tribuna = pygame.transform.scale(tribuna, (750, 600))

decision = color_aleateorio
moneda = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\moneda.png")
moneda = pygame.transform.scale(moneda, (40, 30))

fuente = pygame.font.Font(None, 36)

monedas = pygame.Rect(ANCHO_VENTANA - 100, 80, 100, 30)
input = pygame.Rect(180, 650, 150, 90)

incognita = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
incognita = pygame.transform.scale(incognita, (40, 40))

color = ROJO
color_inactivo = AZUL
color_activo = ROJO
color = color_inactivo
activo = False
texto = ""

bandera = True
monedas_base = 0
while bandera:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if input.collidepoint(evento.pos):
                efecto_de_sonido()
                activo = not activo
                monedas_base = monedas_incrementales(PUNTOS, monedas_base)


            if activo:
                color = color_activo
            else:
                color = color_inactivo
    
    ventana.blit(fondo, (0, 0))    
    ventana.blit(tribuna, (0, 0))



    x = 100
    y = 370
    for i in range(10):
        decisiones = pygame.Rect(x+30 ,y, 40, 40)
        if x <= 500:
            pygame.draw.rect(ventana, decision, decisiones)
            #ventana.blit(incognita,(x +30, y))
            ventana.blit(jueces, (x, 300))
            x += 100
        else:
            x = 100
       


    #Todo lo relacionado con el button de this or that
    texto_superficie = fuente.render("This or that", True, BLANCO)
    pygame.draw.rect(ventana, color, input)
    ventana.blit(texto_superficie, (input.x + 5, input.y + 5))
    pygame.draw.rect(ventana, color, input, 2)

    #Todo lo relacionado con el contador d monedas
    texto_monedas = fuente.render(str(monedas_base), True, BLANCO)
    pygame.draw.rect(ventana, NEGRO, monedas, 0)
    ventana.blit(texto_monedas, (monedas.x , monedas.y ))
    ventana.blit(moneda, (ANCHO_VENTANA - 35, 80))
    
    pygame.display.flip()

pygame.quit()