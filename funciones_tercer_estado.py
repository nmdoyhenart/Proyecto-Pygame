import pygame
from funciones_ganar_o_perder import *
from funciones_base import *
from archivos import *
from elementos import *
from efectos_de_sonido import *

def estado_tres(ventana, fuente: str, color_decision: str, lista_jueces: list, comodin_tres: bool, contador_tiempo: int):
    """Lo relacionado con el tercer estado.

   Args:
        ventana: surface: Superficie, fuente: str: String, color_decision: str: String, lista_jueces: list: Lista, comodin_tres: bool: Bandera, contador_tiempo: int: Numerico.
    """
    tribuna(ventana)
    jueces_funcion(ventana, lista_jueces, comodin_tres, contador_tiempo)
    cuadro_porcentaje(ventana, fuente, lista_jueces)
    comprobar_eleccion = comprobacion_voto_jueces(lista_jueces, color_decision)

    return comprobar_eleccion

def funcion_comodin_tres(ventana, lista_jueces: list, comodin_tres: bool, contador_tiempo: int):
    """Lo relacionado con el tercer estado.

   Args:
        ventana: surface: Superficie, lista_jueces: list: Lista, comodin_tres: bool: Bandera, contador_tiempo: int: Numerico.
    """
    tribuna(ventana)
    jueces_funcion(ventana, lista_jueces, comodin_tres, contador_tiempo)

def ganar_perder(ventana, fuente: str, comprobar_eleccion, habilitar_sonido):
    """Lo relacionado con el tercer estado.

   Args:
        ventana: surface: Superficie, fuente: str: String, comprobar_eleccion, habilitar_sonido
    """
    if comprobar_eleccion:
        if habilitar_sonido == 0:
            respuesta_correcta_sonido()
        ganador(ventana, fuente)
    else:
        if habilitar_sonido == 0:
            derrota()
        pantalla_eliminado(ventana, fuente)

    habilitar_sonido += 1
    return habilitar_sonido

def tribuna(ventana):
    """Función que implementa la tribuna en el juego.

    Args:
        ventana: surface: Superficie.
    """
    tribuna = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\tribuna_jueces.png")
    tribuna = pygame.transform.scale(tribuna, (600, 500))
    ventana.blit(tribuna, (55, 85))

def jueces_funcion(ventana, lista_jueces: list[tuple], comodin_tres: bool, contador_tiempo: int):
    """Muestra la votación de los jueces, rojo o azul.

    Args:
        ventana: surface: Superficie, lista_jueces: list[tuple]: Lista que devuelve tupla, comodin_tres: bool: Bandera, contador_tiempo: int: Numerico.
    """
    decision_x = 40
    decision_y = 40
    coordenada_x = 100
    coordenada_y = 320
    personajes = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\personaje.png")
    personajes = pygame.transform.scale(personajes, (100, 150))

    midecision = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
    midecision = pygame.transform.scale(midecision, (decision_x,decision_y))

    for i in range(len(lista_jueces)):
        ventana.blit(midecision, (coordenada_x + 30, coordenada_y, decision_x, decision_y))
        coordenada_x += 100

    if lista_jueces[0] is ROJO or lista_jueces[0] is AZUL:
        coordenada_x = 100
        
        if comodin_tres:
            for i in range(len(lista_jueces)):

                decisiones = pygame.Rect(coordenada_x + 30, coordenada_y, decision_x, decision_y)
                pygame.draw.rect(ventana, lista_jueces[i], decisiones)
                coordenada_x += 100
        else:
            if contador_tiempo < 10:
                for i in range(2):
                    decisiones = pygame.Rect(coordenada_x + 30, coordenada_y, decision_x, decision_y)
                    pygame.draw.rect(ventana, lista_jueces[i], decisiones)
                    coordenada_x += 100
            else:
                for i in range(len(lista_jueces)):
                    decisiones = pygame.Rect(coordenada_x + 30, coordenada_y, decision_x, decision_y)
                    pygame.draw.rect(ventana, lista_jueces[i], decisiones)
                    coordenada_x += 100
            
    coordenada_x = 100
    for i in range(len(lista_jueces)):
        ventana.blit(personajes, (coordenada_x, 250))
        coordenada_x += 100

    
def cuadro_porcentaje(ventana, fuente_porcentaje: str, decision: list):
    """Grafica el porcentaje de la decision de los jueces.

    Args:
        ventana: surface: Superficie, fuente_porcentaje: str: String, decision: list: Lista.
    """
    porcentaje_tupla = porcentaje_decision(decision)

    cuadro_porcentaje_ancho = 400
    cuadro_porcentaje_alto = 60

    cuadro_porcentaje_x = 150
    cuadro_porcentaje_y = 20

    ancho_azul = (porcentaje_tupla[0] / 100 ) * cuadro_porcentaje_ancho
    cuadro_porcentaje_azul = pygame.Rect(cuadro_porcentaje_x, cuadro_porcentaje_y, ancho_azul, cuadro_porcentaje_alto)
    pygame.draw.rect(ventana, AZUL, cuadro_porcentaje_azul)

    ancho_rojo = (porcentaje_tupla[1] / 100 ) * cuadro_porcentaje_ancho

    cuadro_porcentaje_rojo = pygame.Rect(cuadro_porcentaje_x + ancho_azul, cuadro_porcentaje_y, ancho_rojo, cuadro_porcentaje_alto)
    pygame.draw.rect(ventana, ROJO, cuadro_porcentaje_rojo)

    texto_porcentaje_rojo = fuente_porcentaje.render(f"{porcentaje_tupla[1]}%", False, NEGRO)
    ventana.blit(texto_porcentaje_rojo, (cuadro_porcentaje_x + cuadro_porcentaje_ancho - 55, cuadro_porcentaje_y + 20))

    texto_porcentaje_azul = fuente_porcentaje.render(f"{porcentaje_tupla[0]}%", False, NEGRO)
    ventana.blit(texto_porcentaje_azul, (cuadro_porcentaje_x + 5, cuadro_porcentaje_y + 20))

    cuadro_porcentaje = pygame.Rect(cuadro_porcentaje_x, cuadro_porcentaje_y, cuadro_porcentaje_ancho, cuadro_porcentaje_alto)
    pygame.draw.rect(ventana, NEGRO, cuadro_porcentaje, 2)