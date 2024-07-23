"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
import time
from elementos import *
from funciones_base import *

tiempo_transcurrido = lambda tiempo_actual, tiempo_inicial: tiempo_actual - tiempo_inicial

def tiempo(ventana, FUENTE, tiempo_actual: int, tiempo_inicial: int, limite_tiempo: int):
    """Grafico para mostrar el contador.

    Args:
        ventana: surface: Superficie, FUENTE: font: Fuente python, tiempo_actual: int: Numerico, limite_tiempo: int: Numerico, tiempo_inicial: int: Numerico.
    """
    time_x = 5
    time_y = 5
    time_ancho = 40
    time_alto = 30
    escalar_imagen(ventana, (30,30), (time_x,time_y), r"recursos\tiempo corriendo.png")
    temporizador = pygame.Rect(time_x + 30, time_y, time_ancho, time_alto)
    pygame.draw.rect(ventana, NEGRO, temporizador)
    tiempo_contadoor = round(tiempo_actual - tiempo_inicial)
    text_tiempo = FUENTE.render(f"{tiempo_contadoor}", True, BLANCO)
    ventana.blit(text_tiempo, (time_x + 40, time_y + 5))
    
    retorna = False
    tiempo_real = tiempo_transcurrido(tiempo_actual, tiempo_inicial)
    if tiempo_real >= limite_tiempo:
        retorna = True
    return retorna

def tiempo_espera(database: dict, limite: int, lista_jugadores: list, jugador_puntos: list):
    """Calcula el tiempo en el cual te hecha del programa.

    Args:
        database: dict: Diccionario, limite: int: Numerico, fps: int: Numerico, lista_jugadores: list: Lista, jugador_puntos: list: Lista.
    """
    tiempo_actual = time.time()

    retorna = False
    tiempo_real = tiempo_transcurrido(tiempo_actual, database["tiempo para responder"] )
    if tiempo_real >= limite:
        lista_jugadores.append(jugador_puntos)
        guardar_puntos("Puntos.json",lista_jugadores)
        retorna = True
    return retorna

def fuera_de_tiempo(ventana, fuente):
    """Grafica que notifica la expulsión del programa.
    Args:
        ventana: surface: Superficie, fuente: font: Fuente python
    """
    eliminado_x = 125
    eliminado_y = 520
    eliminado_ancho = 450
    eliminado_alto = 35
    dibujar_boton_rectang(ventana, (eliminado_x, eliminado_y, eliminado_ancho, eliminado_alto), fuente, "Usted ha excedido el tiempo y perdio", ROJO_CLARO)
    escalar_imagen(ventana, (260, 360), (220, 170), r"recursos\TIME OUT.png")