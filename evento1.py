"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
from evento2 import *
from especificas_eventos import *
from funcionalidad import *
from archivos import *

leer_preguntas()

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

icono = pygame.image.load(r"recursos\logo.jpg")
pygame.display.set_icon(icono)



fuente = pygame.font.Font(None, 36)


# incognita = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
# incognita = pygame.transform.scale(incognita, (40, 40))


color = ROJO
color_inactivo = AZUL
color_activo = ROJO
color = color_inactivo
activo = False
texto = ""

def fondo():
    fondo = pygame.image.load(r"recursos/fondo.jpg")
    fondo = pygame.transform.scale(fondo, VENTANA1)

    ventana.blit(fondo, (0, 0))    

def tribuna():
    tribuna = pygame.image.load(r"recursos\tribuna_mejorada.png")
    tribuna = pygame.transform.scale(tribuna, (600, 500))
    ventana.blit(tribuna, (50, 20))


def jueces_funcion(decision: tuple):
    decision_x = 40
    decision_y = 40
    coordenada_x = 100
    coordenada_y = 370
    personajes = pygame.image.load(r"recursos\guampa.png")
    personajes = pygame.transform.scale(personajes, (100, 150))

    midecision = pygame.image.load(r"recursos\incognita.png")
    midecision = pygame.transform.scale(midecision, (decision_x,decision_y))


    for i in range(6):
        if coordenada_x <= 500:
            if decision is ROJO or decision is AZUL:
                decisiones = pygame.Rect(coordenada_x + 30, coordenada_y, decision_x, decision_y)
                decisiones_2 = pygame.Rect(coordenada_x + 30, coordenada_y - 100, decision_x, decision_y)
                pygame.draw.rect(ventana, decision, decisiones)
                pygame.draw.rect(ventana, decision, decisiones_2)
            else:
                ventana.blit(midecision, (coordenada_x + 30, coordenada_y, decision_x, decision_y))
                ventana.blit(midecision, (coordenada_x + 30, coordenada_y -100, decision_x, decision_y))



            ventana.blit(personajes, (coordenada_x, 200))
            ventana.blit(personajes, (coordenada_x, 300))

            coordenada_x += 100
        else:
            coordenada_x = 100
       

def button_tot():
    #Todo lo relacionado con el button de this or that
    input_tot = pygame.Rect(275, 750, 150, 90)

    texto_superficie = fuente.render("This or that", True, BLANCO)
    pygame.draw.rect(ventana, color, input_tot)
    ventana.blit(texto_superficie, (input_tot.x + 5, input_tot.y + 5))
    #pygame.draw.rect(ventana, color, input_tot, 2)

def monedas_contador(monedas_base):
    #Todo lo relacionado con el contador d monedas
    monedas = pygame.Rect(ANCHO_VENTANA - 100, 80, 100, 30)
    moneda_icon = pygame.image.load(r"recursos\moneda.png")
    moneda_icon = pygame.transform.scale(moneda_icon, (40, 30))


    texto_monedas = fuente.render(str(monedas_base), True, BLANCO)
    pygame.draw.rect(ventana, NEGRO, monedas, 0)
    ventana.blit(texto_monedas, (monedas.x , monedas.y ))
    ventana.blit(moneda_icon, (ANCHO_VENTANA - 35, 80))

def vuelta():
    punto_vuelta = pygame.image.load(r"recursos\X_vuelta.png")
    punto_vuelta= pygame.transform.scale(punto_vuelta , (30, 30))

    
    ventana.blit(punto_vuelta, (ANCHO_VENTANA - 35, ALTO_VENTANA - 35))


def mi_personaje():
    x_personaje = 150
    y_personaje = 150
    personajes = pygame.image.load(r"recursos\guampa.png")
    personajes = pygame.transform.scale(personajes, (400, 600))
    ventana.blit(personajes,(x_personaje, y_personaje))

def decision_personaje(estado, color):
    if estado:
        midecision = pygame.image.load(r"recursos\incognita.png")
        midecision = pygame.transform.scale(midecision, (160,140))
        ventana.blit(midecision, (150 + 115, 150 + 280))
    else:
        mi_decision = pygame.Rect(150 + 115, 150 + 280, 160,140)
        pygame.draw.rect(ventana, color, mi_decision)

def texto_pregunta_opciones(ventana, fuente, pregunta):
    ancho = 500
    alto = 50
    x = 100
    y = 600
    cuadro_preg = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(ventana, GRIS, cuadro_preg)
    pygame.draw.rect(ventana, NEGRO, cuadro_preg, 2)
    texto_preg = fuente.render(f"{pregunta['Pregunta']}", True, NEGRO)
    ventana.blit(texto_preg, (x + 3, y + 15))
    
    opciones = pregunta["Opciones"]
    cantidad_opciones = len(opciones)
    opciones_mezcladas = random.sample(opciones, len(opciones))
    x = 100
    y = 650
    boton_altura = 90
    boton_ancho = 250

    
    for i in range(cantidad_opciones):
        rojo = pygame.Rect(x, y, boton_ancho, boton_altura)
        pygame.draw.rect(ventana, ROJO, rojo)
        pygame.draw.rect(ventana, NEGRO, rojo, 2)
        texto_superficie = fuente.render(opciones_mezcladas[i], True, NEGRO)
        ventana.blit(texto_superficie, (rojo.x + 5, rojo.y + 5))
    else:
        azul = pygame.Rect(x + boton_ancho, y, boton_ancho, boton_altura)
        pygame.draw.rect(ventana, AZUL_CLARO, azul)
        pygame.draw.rect(ventana, NEGRO, azul, 2)
        texto_superficie = fuente.render(opciones_mezcladas[i], True, BLANCO)
        ventana.blit(texto_superficie, (azul.x + 10, azul.y + 10))

bandera = True
monedas_base = 0
estado = "principal"
boton_decision = True
color_decision = None
while bandera:
    for evento in pygame.event.get():
        try:
            if estado == "principal":
                #Dependiendo del estado del juego, se habilitan los botones o no
                input_tot = pygame.Rect(275, 750, 150, 90)
            elif estado == "segundo estado":
                punto_vuelta = pygame.Rect(ANCHO_VENTANA - 35, ALTO_VENTANA - 35, 30, 30)
                button_rojo = pygame.Rect(180, 650, 150, 90)
                button_azul = pygame.Rect(180 + 180, 650, 150, 90)

            if evento.type == pygame.QUIT:
                #Salida del juego por la "X" 
                bandera = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                #Cuando detecta que se apreta en click izq del mouse, 
                #elige como proseguir dependiendo donde toco(que boton)
                if input_tot.collidepoint(evento.pos):
                    estado = "segundo estado"
                elif punto_vuelta.collidepoint(evento.pos):
                    estado = "principal"
                    boton_decision = True

                elif button_rojo.collidepoint(evento.pos) or button_azul.collidepoint(evento.pos):
                    boton_decision = False
                    if button_rojo.collidepoint(evento.pos):
                        color_decision = ROJO
                    else:
                        color_decision = AZUL
        except:
            pass
        
    """Esta parte llama a las funciones que se encargan de ilustrar los botones, fondo, y partes
    visuales del programa. Esto dependiendo del estado en que este el programa."""
    
    fondo()
    if estado == "principal":
        tribuna()
        jueces_funcion(None)
        button_tot()

    elif estado == "segundo estado":
        decision_personaje(boton_decision, color_decision)
        mi_personaje()
        texto_pregunta_opciones(ventana, fuente, lista_preferencias[0])
        vuelta()
        
    elif estado == "tercer estado":
        pass
        

    monedas_contador(monedas_base)

    
    
    pygame.display.flip()

pygame.quit()