import pygame
from elementos import *
from funciones_base import *


def dibujar_boton_top(ventana, fuente, evento, estado):
    """dibuja el boton para que se muestre el top de jugadores con mas puntos

    Args:
        ventana (surface): superficie donde se desarrolla el juego
        fuente (font): fuente que se usa
        evento (event): vento que se realiza en el momento
        estado (str): estado actual

    Returns:
        str: estado actual
    """
    x = 50
    y = 50
    boton_altura = 50
    boton_ancho = 115
    tupla_dimensiones = (x, y, boton_ancho, boton_altura)
    texto_boton = "VER TOP"
    top = dibujar_boton_rectang(ventana, tupla_dimensiones, fuente, texto_boton, ROJO_CLARO)
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if top.collidepoint(evento.pos):
            estado = "top jugadores"
    return estado


def determinar_top_5(lists):
    """Donde se aplica el ordenamiento en el top.

    Args:
        listas: list: Lista.
    """
    top_5 = []
    for item in lists:
        top_5.append(item)
        for i in range(len(top_5) - 1, 0, -1):
            if top_5[i][1] > top_5[i - 1][1]:
                top_5[i], top_5[i - 1] = top_5[i - 1], top_5[i]
        if len(top_5) > 5:
            top_5.pop()

    return top_5


def dibujar_top_5(ventana, lista_top, fuente):
    """Donde se dibujan los cambios.

    Args:
        pantalla: surface: superficie, lista_top: list: Lista, fuente: str: String.
    """
    dimensiones = (200, 200, 300, 300)
    titulo = "Top 5 jugadores"
    titulo_superficie = dibujar_boton_rectang(ventana, dimensiones, fuente, titulo, VERDE_CLARO)
    y_jugadores = titulo_superficie.y + 40
    for i, item in enumerate(lista_top):
        texto = f"{i+1}. {item[0]}  Puntos:{item[1]}"
        superficie_texto = fuente.render(texto, True, NEGRO)
        ventana.blit(superficie_texto, (titulo_superficie.x + 5, y_jugadores))
        y_jugadores += superficie_texto.get_height() + 10


def top_cinco(ventana, fuente, lista_jugadores):
    """Aplicamos todas las funciones para el muestreo.

    Args:
        ventana: surface: superficie, fuente: str: String lista_jugadores: list: Lista.
    """

    top = determinar_top_5(lista_jugadores)
    dibujar_top_5(ventana, top, fuente)
