"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
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

def fondo(ventana, DIMENSION: int):
    """funcion que grafica el fondo el juego en todo momento.

    Args:
        ventana: surface: Superficie, DIMENSION: int: Numerico,
    """
    fondo = pygame.image.load(r"recursos\fondo.jpg")
    fondo = pygame.transform.scale(fondo, DIMENSION)

    ventana.blit(fondo, (0, 0))    

def icono_ventana():
    """Creacion del icono de la ventana.

    Args:
        -
    """
    icono = pygame.image.load(r"recursos\logo.jpg")
    pygame.display.set_icon(icono)

def crear_ventana():
    """Creacion de la ventana Pygame, define las medidas.

    Args:
        -
    """
    ancho_ventana = 700
    alto_ventana = 700
    ventana_dimension = (ancho_ventana, alto_ventana)
    ventana = pygame.display.set_mode(ventana_dimension)
    return ventana, ventana_dimension

def dibujar_boton_rectang(ventana, coord_dimensiones: int, fuente, texto_boton: str, color_boton: str):
    """Dibuja los botones.

    Args:
        ventana: surface: Superficie, coord_dimensiones: int: Numerico, fuente: font: Fuente python, texto_boton: str: String, color_boton: str: String,
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

def blitear_texto(ventana, fuente, texto: str, tupla_coordenadas: tuple, color: str, fondo):
    """Funcion que blitea texto

    Args:
        ventana: surface: Superficie, fuente: font: Fuente python, texto: str: String, tupla_coordenadas: tuple: Tupla, color: str: String, fondo: surface: superficie.
    """
    texto_superficie = fuente.render(texto, True, color, fondo)
    ventana.blit(texto_superficie,tupla_coordenadas)

def dibujar_rectangulo(ventana, coord_dimensiones: int, color: str):
    """Grafica el rectangulo.

    Args:
        ventana: surface: Superficie, coord_dimensiones: int: Numerico, color: str: String.
    """
    x = coord_dimensiones[0]
    y = coord_dimensiones[1]
    rectangulo_ancho = coord_dimensiones[2]
    rectangulo_alto = coord_dimensiones[3]
    rectangulo = pygame.Rect(x, y, rectangulo_ancho, rectangulo_alto)
    pygame.draw.rect(ventana, color, rectangulo)

def dibujar_borde(ventana, coord_dimensiones: int, color: str, borde):
    """Dibuja el borde.

    Args:
        ventana: surface: Superficie, coord_dimensiones: int: Numerico, color: str: String,  borde: surface: Superficie.
    """
    cuadro_porcentaje = pygame.Rect(coord_dimensiones)
    pygame.draw.rect(ventana, color, cuadro_porcentaje, borde)

def escalar_imagen(ventana, dimensiones: int, coordenadas: int, path_imagen):
    """Aplica las imagenes en el juego.

    Args:
        ventana: surface: Superficie, dimensiones: int: Numerico, coordenadas: int: Numerico, path_imagen.
    """
    ancho_imagen = dimensiones[0]
    alto_imagen = dimensiones[1]
    imagen = pygame.image.load(r"{0}".format(path_imagen))
    imagen = pygame.transform.scale(imagen, (ancho_imagen, alto_imagen))
    ventana.blit(imagen, coordenadas)