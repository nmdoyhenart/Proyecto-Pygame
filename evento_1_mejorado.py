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

fuente = pygame.font.Font(None, 36)


incognita = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
incognita = pygame.transform.scale(incognita, (40, 40))

#Botones importantes(tot, volver, etc)
input = pygame.Rect(180, 650, 150, 90)

color = ROJO
color_inactivo = AZUL
color_activo = ROJO
color = color_inactivo
activo = False
texto = ""

def ventana_principal():
    ventana.blit(fondo, (0, 0))    
    ventana.blit(tribuna, (0, 0))

def jueces_funcion():
    #Todo lo relacionado con el button de this or that
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
       

def button_tot():
    texto_superficie = fuente.render("This or that", True, BLANCO)
    pygame.draw.rect(ventana, color, input)
    ventana.blit(texto_superficie, (input.x + 5, input.y + 5))
    pygame.draw.rect(ventana, color, input, 2)

def monedas_contador(monedas_base):
    #Todo lo relacionado con el contador d monedas
    monedas = pygame.Rect(ANCHO_VENTANA - 100, 80, 100, 30)
    moneda_icon = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\moneda.png")
    moneda_icon = pygame.transform.scale(moneda_icon, (40, 30))


    texto_monedas = fuente.render(str(monedas_base), True, BLANCO)
    pygame.draw.rect(ventana, NEGRO, monedas, 0)
    ventana.blit(texto_monedas, (monedas.x , monedas.y ))
    ventana.blit(moneda_icon, (ANCHO_VENTANA - 35, 80))

def vuelta():
    punto_vuelta = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\X_vuelta.png")
    punto_vuelta= pygame.transform.scale(punto_vuelta , (30, 30))

    
    ventana.blit(punto_vuelta, (ANCHO_VENTANA - 35, ALTO_VENTANA - 35))

punto_vuelta = pygame.Rect(ANCHO_VENTANA - 35, ALTO_VENTANA - 35, 30, 30)




bandera = True
monedas_base = 0
estado = "segundo estado"
while bandera:
    for evento in pygame.event.get():
        #Salida del juego por la "X" 
        if evento.type == pygame.QUIT:
            bandera = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if input.collidepoint(evento.pos):
                estado = "principal"
            if punto_vuelta.collidepoint(evento.pos):
                estado = "segundo estado"
                
        


    if estado == "principal":
        ventana.fill(BLANCO)
        vuelta()
    else:
        ventana_principal()
        jueces_funcion()
        button_tot()
        

    monedas_contador(monedas_base)

    
    
    pygame.display.flip()

pygame.quit()