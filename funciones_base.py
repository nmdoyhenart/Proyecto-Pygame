"""
Modulo todo lo que no tiene que ver con pygame
"""
import pygame
from elementos import *
from archivos import *


pygame.init()

def titulo_ventana():
    """Asigna el titulo de la ventana.

    Args:
        -
        """
    pygame.display.set_caption("Tot or trivia")


def fondo(ventana, DIMENSION):
    """funcion que grafica el fondo el juego
    Args:
        ventana (surface): _description_
        DIMENSION (tuple): tamaño de la pantalla
    """
    fondo = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\fondo.jpg")
    fondo = pygame.transform.scale(fondo, DIMENSION)

    ventana.blit(fondo, (0, 0))    


def icono_ventana():
    """Creacion del icono de la ventana.

    Args:
        -
    """
    icono = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\logo.jpg")
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


def dibujar_boton_rectang(ventana, coord_dimensiones, fuente, texto_boton, color_boton):
    """Actualiza constantemente las monedas haciendolas incrementales.

    Args:
        puntos: list: Lista donde se guardan los puntos,
        monedas_base: int: Numerico
        posicion: int: Numerico.
    """
    x = coord_dimensiones[0]
    y = coord_dimensiones[1]
    boton_ancho = coord_dimensiones[2]
    boton_alto = coord_dimensiones[3]

    boton = pygame.Rect(x, y, boton_ancho, boton_alto)
    pygame.draw.rect(ventana, color_boton, boton)
    pygame.draw.rect(ventana, NEGRO, boton, 2)
    texto_superficie = fuente.render(f"{texto_boton}", True, NEGRO)
    ventana.blit(texto_superficie, (boton.x + 5, boton.y + 5))

    return boton


def blitear_texto(ventana, fuente, texto, tupla_coordenadas, color, backgraund):
    texto_superficie = fuente.render(texto, True, color, backgraund)
    ventana.blit(texto_superficie,tupla_coordenadas)


def dibujar_rectangulo(ventana, coord_dimensiones, color):
    x = coord_dimensiones[0]
    y = coord_dimensiones[1]
    rectangulo_ancho = coord_dimensiones[2]
    rectangulo_alto = coord_dimensiones[3]
    rectangulo = pygame.Rect(x, y, rectangulo_ancho, rectangulo_alto)
    pygame.draw.rect(ventana, color, rectangulo)


def dibujar_borde(ventana, coord_dimensiones, color, borde):
    cuadro_porcentaje = pygame.Rect(coord_dimensiones)
    pygame.draw.rect(ventana, color, cuadro_porcentaje, borde)



def escalar_imagen(ventana, dimensiones, coordenadas, path_imagen):
    ancho_imagen = dimensiones[0]
    alto_imagen = dimensiones[1]
    imagen = pygame.image.load(r"{0}".format(path_imagen))
    imagen = pygame.transform.scale(imagen, (ancho_imagen, alto_imagen))
    ventana.blit(imagen, coordenadas)


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


def comprobacion(voto_jueces: list, mi_decision: tuple):
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