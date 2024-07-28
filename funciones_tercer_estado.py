"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
from funciones_ganar_o_perder import *
from funciones_base import *
from archivos import *
from elementos import *
from efectos_de_sonido import *
from especificas_evento import *

def activar_estado_tres(ventana, fuente, color_decision: str, lista_jueces: list, comodin_tres, contador_tiempo: int):
    """Lo relacionado con el tercer estado.

   Args:
        ventana: surface: Superficie, fuente: font: Fuente python, color_decision: str: String, lista_jueces: list: Lista, comodin_tres: flag: Bandera, contador_tiempo: int: Numerico.
    """
    tribuna(ventana)
    jueces_funcion(ventana, lista_jueces, comodin_tres, contador_tiempo)
    cuadro_porcentaje(ventana, fuente, lista_jueces)
    comprobar_eleccion = comprobacion(lista_jueces, color_decision)

    return comprobar_eleccion

def funcion_comodin_tres(ventana, lista_jueces: list, comodin_tres, contador_tiempo: int):
    """Funcionamiento del tercer comodin.

   Args:
        ventana: surface: Superficie, lista_jueces: list: Lista, comodin_tres: flag: Bandera, contador_tiempo: int: Numerico.
    """
    tribuna(ventana)
    jueces_funcion(ventana, lista_jueces, comodin_tres, contador_tiempo)

def efecto_de_sonido_ganar_perder(ventana, fuente, comprobar_eleccion, habilitar_sonido: int):
    """Comprobación para activar efecto de sonido.

   Args:
        ventana: surface: Superficie, fuente: font: Fuente python, comprobar_eleccion, habilitar_sonido: int: Numerico.
    """
    if comprobar_eleccion:
        if habilitar_sonido == 0:
            respuesta_correcta_sonido()
        pantalla_ganador(ventana, fuente)
    else:
        if habilitar_sonido == 0:
            derrota()
        pantalla_eliminado(ventana, fuente)

    habilitar_sonido += 1

    return habilitar_sonido

def tribuna(ventana):
    """Función que implementa la tribuna en el juego en todo momento.

    Args:
        ventana: Surface
    """
    tribuna = pygame.image.load(r"recursos\tribuna_jueces.png")
    tribuna = pygame.transform.scale(tribuna, (600, 500))
    ventana.blit(tribuna, (55, 85))


def jueces_funcion(ventana, lista_jueces: list[tuple], comodin_tres, contador_tiempo: int):
    """Muestra la votación de los jueces, rojo o azul.

    Args:
        ventana: surface: Superficie, lista_jueces: list[tuple]: Busca dentro de la lista la tupla decision, comodin_tres: flag: Bandera, contador_tiempo: int: Numerico.
    """
    decision_x = 40
    decision_y = 40
    coordenada_x = 100
    coordenada_y = 320
    personajes = pygame.image.load(r"recursos\personaje.png")
    personajes = pygame.transform.scale(personajes, (100, 150))

    midecision = pygame.image.load(r"recursos\incognita.png")
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
    
def cuadro_porcentaje(ventana, fuente_porcentaje, decision: list):
    """Grafica el porcentaje de la decision de los jueces mediante una barra.

    Args:
        ventana: surface: Superficie, fuente_porcentaje: font: Fuente, decision: list: Lista.
    """
    porcentaje_tupla = porcentaje_decision(decision)

    cuadro_porcentaje_ancho = 400
    cuadro_porcentaje_alto = 60

    cuadro_porcentaje_x = 150
    cuadro_porcentaje_y = 20

    ancho_azul = (porcentaje_tupla[0] / 100 ) * cuadro_porcentaje_ancho
    ancho_rojo = (porcentaje_tupla[1] / 100 ) * cuadro_porcentaje_ancho
    dibujar_rectangulo(ventana, (cuadro_porcentaje_x, cuadro_porcentaje_y, ancho_azul, cuadro_porcentaje_alto), AZUL)
    dibujar_rectangulo(ventana, (cuadro_porcentaje_x + ancho_azul, cuadro_porcentaje_y, ancho_rojo, cuadro_porcentaje_alto), ROJO)

    coordenadas_rojo = (cuadro_porcentaje_x + cuadro_porcentaje_ancho - 55, cuadro_porcentaje_y + 20)
    blitear_texto(ventana, fuente_porcentaje, f"{porcentaje_tupla[1]}%", coordenadas_rojo, NEGRO, None)

    coordenadas_azul = (cuadro_porcentaje_x + 5, cuadro_porcentaje_y + 20)
    blitear_texto(ventana, fuente_porcentaje, f"{porcentaje_tupla[0]}%", coordenadas_azul, NEGRO, None)

    dibujar_borde(ventana, (cuadro_porcentaje_x, cuadro_porcentaje_y, cuadro_porcentaje_ancho, cuadro_porcentaje_alto), NEGRO, 2)