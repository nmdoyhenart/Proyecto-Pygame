import pygame
from elementos import *

tiempo_transcurrido = lambda contador, fps: contador // fps

def tiempo(ventana, FUENTE: str, contador: int, limite_tiempo: int, fps: int):
    """Grafico para mostrar el contador.

    Args:
        ventana: surface: Superficie, FUENTE: str: String, contador: int: Numerico, limite_tiempo: int: Numerico, fps: int: Numerico.
    """
    time_x = 5
    time_y = 5
    time_ancho = 40
    time_alto = 30
    temporizador = pygame.Rect(time_x, time_y, time_ancho, time_alto)
    pygame.draw.rect(ventana, NEGRO, temporizador)
    text_tiempo = FUENTE.render(f"{contador // 20}", True, BLANCO)
    ventana.blit(text_tiempo, (time_x + 10, time_y + 5))
    
    retorna = False
    tiempo_real = tiempo_transcurrido(contador, fps)
    if tiempo_real >= limite_tiempo:
        retorna = True
    return retorna
    
def tiempo_espera(contador_espera: int, limite: int, fps: int):
    """Calcula el tiempo en el cual te hecha del programa.

    Args:
        contador_espera: int: Numerico, limite: int: Numerico, fps: int: Numerico.
    """
    retorna = False
    tiempo_real = tiempo_transcurrido(contador_espera, fps)
    if tiempo_real >= limite:
        retorna = True
    return retorna

def fuera_de_tiempo(ventana: int, FUENTE: str):
    """Grafica que notifica la expulsión del programa.
    Args:
        ventana: int: Numerico, FUENTE: str: String
    """
    eliminado_x = 200
    eliminado_y = 350
    eliminado_ancho = 400
    eliminado_alto = 35
    eliminacion_cuadro = pygame.Rect(eliminado_x, eliminado_y, eliminado_ancho, eliminado_alto)
    pygame.draw.rect(ventana, NEGRO, eliminacion_cuadro)
    text_eliminacion = FUENTE.render(f"Usted ha excedido el tiempo y perdio.", True, BLANCO)
    ventana.blit(text_eliminacion, (eliminado_x + 10, eliminado_y + 5))