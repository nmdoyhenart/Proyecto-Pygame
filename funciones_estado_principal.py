"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
import random
from funciones_base import *
from elementos import *
from efectos_de_sonido import *
from archivos import *
from funciones_ver_top import *

#------------------------------------------------------------------------------------------------------------------
def funcion_principal(ventana, fuente, eventos: list, evento, preguntas, monedas_base: int, estado: str, activo: bool, nombre_jugador: str):
    """Funcion que contiene la columna principal del juego.

    Args:
        ventana: surface: superficie, fuente: font: fuente python, eventos: list: lista, evento: event: Evento, preguntas: list: Lista, monedas_base: int: Numerico, estado: str: String, activo: bool: Booleano, nombre_jugador: str: String.
    """
    ingrese_nombre(fuente, ventana, activo)
    nombre_jugador, activo = manejar_caja_texto(eventos, nombre_jugador, AZUL_CLARO, AZUL, fuente, ventana, activo)
    pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
    inicio = boton_inicio(fuente, ventana, evento, estado)
    estado = dibujar_boton_top(ventana, fuente, evento, estado)
    if inicio:
        if nombre_jugador == "":
            nombre_jugador = "Jugador"
        estado = "segundo estado"
    back_inicio = {"estado": estado,
                   "pregunta_aleatoria": pregunta_aleatoria,
                   "puntos_jugador": monedas_base,
                   "nombre_jugador": nombre_jugador,
                   "input_nombre": activo} 
    return back_inicio

def boton_inicio(FUENTE, ventana, evento, estado: str):
    """Boton para comenzar el juego.

    Args:
        FUENTE: font: Fuente python, ventana: surface: Superficie, evento: event: Evento, estado: str: String
    """
    if estado == "principal":
        centro = (350,549)
        radio = 60
        input = pygame.Rect(275, 500, 150, 90)
        texto_superficie = FUENTE.render("Jugar", True, BLANCO)
        rectangulo_texto = texto_superficie.get_rect(center = input.center)
        pygame.draw.circle(ventana, ROJO, centro, radio)
        ventana.blit(texto_superficie, rectangulo_texto)
        inicio = False    
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if input.collidepoint(evento.pos):
                inicio = True
                
                efecto_de_sonido()
    return inicio

def ingrese_nombre(fuente, ventana, activo: bool):
    """Función que grafica un texto guia.

    Args:
        fuente: font: fuente python, ventana: surface: superficie, activo: bool: Booleano.
    """
    input = pygame.Rect(275, 200, 150, 90)
    texto = "¡Ingrese su nombre!"
    if activo:
        contorno = AZUL
    else:
        contorno = AZUL_CLARO

    texto_superficie = fuente.render(texto, True, BLANCO, contorno)
    rectangulo_texto = texto_superficie.get_rect(center = input.center)
    ventana.blit(texto_superficie, rectangulo_texto)

def manejar_caja_texto(eventos, texto: str, color_inactivo, color_activo, fuente, ventana, activo: bool):
    """Implementa un cuadro de texto interactivo.

    Args:
        eventos: event: Evento, texto: str: String, color_inactivo, color_activo, fuente: font: Fuente python, ventana: surface: Superficie, activo: bool: Booleano.
    """
    ancho_caja = 400
    alto_caja = 100
    y_caja = 270
    x_caja = 150
    rect = pygame.Rect(x_caja, y_caja, ancho_caja, alto_caja)

    if activo:
        color = color_activo
    else:
        color = color_inactivo

    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            if activo:
                if evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif evento.key == pygame.K_ESCAPE:
                    texto = ""
                else:
                    if len(texto) < 20 and evento.unicode.isalpha():
                        texto += evento.unicode
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(evento.pos):
                activo = not activo

    pygame.draw.rect(ventana, BLANCO, rect)
    pygame.draw.rect(ventana, color, rect, 2)
    texto_superficie = fuente.render(texto.title(), True, (0, 0, 0))
    texto_rect = texto_superficie.get_rect(center=(rect.x + rect.width / 2, rect.y + rect.height / 2))
    ventana.blit(texto_superficie, texto_rect.topleft)

    return texto, activo

#-------------------------------------------------------------------------------------------------------------------
def monedas_contador(monedas_base: int, ANCHO_VENTANA: int, FUENTE, ventana):
    """Grafica interactiva de las monedas.

    Args:
        monedas_base: int: Numerico, ANCHO_VENTANA: int: Numerico, FUENTE: font: Fuente python, ventana: surface: superficie.
    """
    monedas = pygame.Rect(ANCHO_VENTANA - 100, 80, 100, 30)

    texto_monedas = FUENTE.render(str(monedas_base), True, BLANCO)
    pygame.draw.rect(ventana, NEGRO, monedas, 0)
    ventana.blit(texto_monedas, (monedas.x + 5, monedas.y + 3 ))
    escalar_imagen(ventana, (45, 30),(ANCHO_VENTANA - 35, 80), r"recursos\moneda.png")

def boton_vuelta(ventana, dimension: tuple, evento):
    """Punto de retorno para volver al menu principal.

    Args:
        ventana: surface: Superficie, dimension: tuple: tupla, evento: event: evento.
    """
    ancho_ventana = dimension[0]
    alto_ventana = dimension[1]
    x = ancho_ventana - 35
    y = alto_ventana - 35
    ancho = 30
    alto = 30
    vuelta_boton = pygame.Rect(x, y, ancho, alto)

    punto_vuelta = pygame.image.load(r"recursos\X_vuelta.png")
    punto_vuelta= pygame.transform.scale(punto_vuelta , (ancho, alto))
    ventana.blit(punto_vuelta, (x, y))
    retorno = False
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if vuelta_boton.collidepoint(evento.pos):
            retorno = True
    return retorno