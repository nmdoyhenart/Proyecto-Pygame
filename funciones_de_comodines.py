"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
import random
import time
from funciones_base import *
from efectos_de_sonido import *
from funciones_tercer_estado import *
from funciones_segundo_estado import *

def dibujar_comodines(ventana, comodin_uno, comodin_dos, comodin_tres, evento, estado: str)-> dict:
    """Comprueba si el título existe y lo elimina de la lista.

    Args:
        ventana: surface: Superficie, comodin_uno: flag: Bandera, comodin_dos: flag: Bandera, comodin_tres: flag: Bandera, evento: event: Evento, estado: str: String.
    
    Returns:
        -> dict: Diccionario.
    """
    ancho_comodin = 30
    alto_comodin = 30
    dimension_comodin = (ancho_comodin, alto_comodin)
    x_comodines = 10
    y_comodin1 = 500
    y_comodin2 = y_comodin1 + alto_comodin + 10
    y_comodin3 = y_comodin2 + alto_comodin + 10

    coordenadas_1 = (x_comodines, y_comodin1)
    coordenadas_2 = (x_comodines, y_comodin2)
    coordenadas_3 = (x_comodines, y_comodin3)
    coordenadas = (coordenadas_1, coordenadas_2, coordenadas_3)

    alternar_comodines(ventana, comodin_uno, comodin_dos, comodin_tres, dimension_comodin, coordenadas)

    dict_rect_de_botones = {"boton_comodin_1": pygame.Rect(x_comodines, y_comodin1, ancho_comodin, alto_comodin),
    "boton_comodin_2": pygame.Rect(x_comodines, y_comodin2, ancho_comodin, alto_comodin),
    "boton_comodin_3": pygame.Rect(x_comodines, y_comodin3, ancho_comodin, alto_comodin) }

    back = botones_comodines(dict_rect_de_botones, evento,comodin_uno, comodin_dos, comodin_tres, estado)

    return back

def alternar_comodines(ventana, comodin_uno, comodin_dos, comodin_tres, dimension_comodin: tuple, coordenadas: tuple):
    """Dibuja lo grafico de los comodines, incluso el comodin usado.

    Args:
        ventana: surface: superficie, comodin_uno: flag: bandera, comodin_dos: flag: bandera, comodin_tres: flag: bandera, dimension_comodin: tuple: tupla, coordenadas: tuple: tupla.
    """
    coordenadas_1 = coordenadas[0]
    coordenadas_2 = coordenadas[1]
    coordenadas_3 = coordenadas[2]

    if comodin_uno:
        escalar_imagen(ventana, dimension_comodin, coordenadas_1, r"recursos\comodin1.png")
    else:
        escalar_imagen(ventana, dimension_comodin, coordenadas_1, r"recursos\cruz.png")
    if comodin_dos:
        escalar_imagen(ventana, dimension_comodin, coordenadas_2, r"recursos\comodin2.png")
    else:
        escalar_imagen(ventana, dimension_comodin, coordenadas_2, r"recursos\cruz.png")
    if comodin_tres:
        escalar_imagen(ventana, dimension_comodin, coordenadas_3, r"recursos\comodin3.png")
    else:
        escalar_imagen(ventana, dimension_comodin, coordenadas_3, r"recursos\cruz.png")

def botones_comodines(diccionario_botones: dict, evento, comodin_uno, comodin_dos, comodin_tres, estado: str)-> dict:
    """funcion que capta cuando un comodin es accionado y procede a llamar a su ejecucion de ser asi.

    Args:
        diccionario_botones: dict: diccionario, evento: event: evento, comodin_uno: flag: bandera, comodin_dos: flag: bandera, comodin_tres: flag: bandera, estado: str: String.

    Returns:
        dict: Diccionario
    """
    REC_COMODIN1 = diccionario_botones["boton_comodin_1"]
    REC_COMODIN2 = diccionario_botones["boton_comodin_2"]
    REC_COMODIN3 = diccionario_botones["boton_comodin_3"]

    if evento.type == pygame.MOUSEBUTTONDOWN:
        if REC_COMODIN1.collidepoint(evento.pos):
            if comodin_uno == True:
                comodin_uno = False
                efecto_de_sonido()
            else:
                comodin_usado()

        elif REC_COMODIN2.collidepoint(evento.pos):
            if comodin_dos == True:
                estado = "tercer estado"
                comodin_dos = False
                efecto_de_sonido()
            else:
                comodin_usado()

        elif REC_COMODIN3.collidepoint(evento.pos):
            if comodin_tres == True:
                comodin_tres = False
                efecto_de_sonido()
            else:
                comodin_usado()

    back = {"comodin_uno": comodin_uno,
            "comodin_dos": comodin_dos,
            "comodin_tres": comodin_tres,
            "estado": estado}

    return back

def activar_comodin_uno(comodin_uno, back_comodines: dict, preguntas: list, pregunta_aleatoria: int):
    """funcion que activa el uso del comodin uno

    Args:
        comodin_uno: flag: bandera, back_comodines: dict: diccionario, preguntas: list: lista, pregunta_aleatoria: int: Numerico.
    """
    if comodin_uno != back_comodines["comodin_uno"] :
        comodin_uno = back_comodines["comodin_uno"]
        if comodin_uno == False:
            pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
    back_comodin_uno = {"comodin_uno": comodin_uno,
                        "pregunta_aleatoria": pregunta_aleatoria}
    return back_comodin_uno


def activar_comodin_dos(comodin_dos, back_comodines: dict, estado: str, preguntas: list, pregunta_aleatoria: int):
    """funcion de activacion del comodin dos

    Args:
        comodin_dos: flag: bandera, back_comodines: dict: diccionario, estado: str: String, preguntas: list: lista, pregunta_aleatoria: int: Numerico.
    """
    tiempo_comodin_dos = 0
    if comodin_dos != back_comodines["comodin_dos"] :
        comodin_dos = back_comodines["comodin_dos"]
        estado = back_comodines["estado"]
        if comodin_dos == False:
            pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
            tiempo_comodin_dos = time.time()
    back_comodin_dos = {"comodin_dos": comodin_dos,
                        "pregunta_aleatoria": pregunta_aleatoria,
                        "estado": estado,
                        "tiempo_comodin": tiempo_comodin_dos}
    return back_comodin_dos

def activar_comodin_tres(ventana, comodin_tres, back_comodines: dict, habilitar_comodin_tres: int, contador_tiempo: int, lista_jueces: list):
    """funcion de activacion del comodin tres

    Args:
        ventana: surface: Superficie, comodin_tres: flag: bandera, back_comodines: dict: diccionario, habilitar_comodin_tres: int: Numerico, contador_tiempo: int: Numerico, lista_jueces: list: lista.
    """
    if comodin_tres != back_comodines["comodin_tres"]:
        comodin_tres = back_comodines["comodin_tres"]
        if comodin_tres == False:
            if habilitar_comodin_tres == 0:
                habilitar_comodin_tres = 1
                lista_jueces = decisiones_jueces(5)
                funcion_comodin_tres(ventana, lista_jueces, comodin_tres, contador_tiempo)
            if contador_tiempo == 0:
                pygame.display.flip()
                pygame.time.delay(2500)
                contador_tiempo = 10
    back_comodin_tres = {"comodin_tres": comodin_tres,
                         "habilitar_comodin": habilitar_comodin_tres,
                         "contador_tiempo": contador_tiempo,
                         "lista_jueces": lista_jueces}
    return back_comodin_tres