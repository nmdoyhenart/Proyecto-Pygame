"""
Modulo todo lo que no tiene que ver con pygame
"""
from elementos import *
from archivos import *
import pygame

pygame.init()
ancho_caja = 400
alto_caja = 100
y_caja = 270
x_caja = 150
rect_caja = pygame.Rect(x_caja, y_caja, ancho_caja, alto_caja)
color_inactivo = pygame.Color('lightskyblue3')
color_activo = pygame.Color('dodgerblue2')
texto_caja = ""
activo = False

def fondo(ventana: int, DIMENSION: int):
    """Función que implementa el fondo del juego en todo momento.

    Args:
        ventana: int: Numerico, DIMENSION: int: Numerico.
    """
    fondo = pygame.image.load(r"recursos\fondo.jpg")
    fondo = pygame.transform.scale(fondo, DIMENSION)

    ventana.blit(fondo, (0, 0))    

def titulo_ventana():
    """Asigna el titulo de la ventana.

    Args:
        -
    """
    pygame.display.set_caption("Tot or trivia")

def icono_ventana():
    """Creacion del icono de la ventana.

    Args:
        -
    """
    icono = pygame.image.load(r"recursos\logo.jpg")
    pygame.display.set_icon(icono)
    
def crear_ventana():
    """Creacion de la ventana Pygame, define las meididas.

    Args:
        -
    """
    ancho_ventana = 700
    alto_ventana = 700
    ventana_dimension = (ancho_ventana, alto_ventana)
    ventana = pygame.display.set_mode(ventana_dimension)
    return ventana, ventana_dimension

def dibujar_boton_rectangulo(ventana: int, tupla_dimensiones: tuple, fuente: str, texto_boton: str, color_boton: str):
    """Actualiza constantemente las monedas haciendolas incrementales.

    Args:
        puntos: list: Lista donde se guardan los puntos, monedas_base: int: Numerico, posicion: int: Numerico.
    """
    x = tupla_dimensiones[0]
    y = tupla_dimensiones[1]
    boton_ancho = tupla_dimensiones[2]
    boton_alto = tupla_dimensiones[3]

    boton = pygame.Rect(x, y, boton_ancho, boton_alto)
    pygame.draw.rect(ventana, color_boton, boton)
    pygame.draw.rect(ventana, NEGRO, boton, 2)
    texto_superficie = fuente.render(f"{texto_boton}", True, BLANCO)
    ventana.blit(texto_superficie, (boton.x + 5, boton.y + 5))
    
    return boton

def monedas_incrementales(puntos: list, monedas_base: int, posicion: int):
    """Actualiza constantemente las monedas haciendolas incrementales.

    Args:
        puntos: list: Lista donde se guardan los puntos, monedas_base: int: Numerico, posicion: int: Numerico.
    """
    monedas_base += puntos[posicion - 1]
    return monedas_base


def jueces_decision(decision: list):
    """Cuenta los colores asigandos aleatoriamente.

    Args:
        decision: list: Lista que contiene la decisión final  
    """
    contador_rojo = 0
    contador_azul = 0
    for elementos in decision:
        if elementos == ROJO:
            contador_rojo += 1
        else:
            contador_azul += 1
    if contador_rojo > contador_azul:
        retorna = ROJO
    else:
        retorna = AZUL
    return retorna

def comprobacion_voto_jueces(voto_jueces: list, mi_decision: tuple):
    """Comprueba los votos de los jueces

    Args:
        voto_jueces: list: Lista, mi_decision: tuple: Tupla.
    """
    color_decidido = jueces_decision(voto_jueces)
    if color_decidido == mi_decision:
        retorna = True
    else:
        retorna = False
    return retorna

def porcentaje_decision(decision: list):
    """Calcula el porcentaje de decisión de los jueces

    Args:
        decision: list: Lista que contiene la decisión final  
    """
    contador_rojo = 0
    contador_azul = 0
    for elementos in decision:
        if elementos == ROJO:
            contador_rojo += 1
        else:
            contador_azul += 1
    
    porcentaje_azul = (contador_azul * 100) // 5
    porcentaje_rojo = (contador_rojo * 100) // 5

    return (porcentaje_azul, porcentaje_rojo)