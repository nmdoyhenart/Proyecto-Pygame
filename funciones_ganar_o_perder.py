import pygame
from elementos import *


def ganador(ventana, FUENTE):
    """Se muestra si el publico coincidio con tu respuesta.
    Args:
        ventana (surface): _description_
        fuente (font): _description_
    """ 
    ganador_ancho = 400
    ganardor_alto = 100

    ganador_x = 150
    ganador_y = 500

    imagen1_ancho = 200
    imagen1_alto = 100

    imagen1_x = 0
    imagen1_y  = 500

    imagen2_ancho = 200
    imagen2_alto = 100

    imagen2_x = 500
    imagen2_y = 500

    imagen1 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\festejo1.jpg")
    imagen1 = pygame.transform.scale(imagen1, (imagen1_ancho, imagen1_alto))
    ventana.blit(imagen1, (imagen1_x, imagen1_y))

    imagen2 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\festejo2.jpg")
    imagen2 = pygame.transform.scale(imagen2, (imagen2_ancho, imagen2_alto))
    ventana.blit(imagen2, (imagen2_x, imagen2_y))

    aviso_ganador = pygame.Rect(ganador_x, ganador_y, ganador_ancho, ganardor_alto)
    pygame.draw.rect(ventana, GRIS, aviso_ganador)
    pygame.draw.rect(ventana, VERDE, aviso_ganador, 2)
    texto_ganador = FUENTE.render(f"Coincidiste con el publico!", False, NEGRO)
    ventana.blit(texto_ganador, (ganador_x + 60, ganador_y + 30))


def pantalla_eliminado(ventana, FUENTE):
    """Aviso de descalificación.

   Args:
        ventana (surface): superficie de la pantalla
        fuente (font): fuente del texto
    """
    eliminado_ancho = 400
    eliminado_alto = 160

    eliminado_x = 150
    eliminado_y = 500

    imagen1_ancho = 150
    imagen1_alto = 160

    imagen1_x = 0
    imagen1_y  = 500

    imagen2_ancho = 150
    imagen2_alto = 160

    imagen2_x = 550
    imagen2_y = 500

    imagen1 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\derrota1.jpg")
    imagen1 = pygame.transform.scale(imagen1, (imagen1_ancho, imagen1_alto))
    ventana.blit(imagen1, (imagen1_x, imagen1_y))

    imagen2 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\derrota2.jpg")
    imagen2 = pygame.transform.scale(imagen2, (imagen2_ancho, imagen2_alto))
    ventana.blit(imagen2, (imagen2_x, imagen2_y))

    aviso_eliminado = pygame.Rect(eliminado_x, eliminado_y, eliminado_ancho, eliminado_alto)
    pygame.draw.rect(ventana, NEGRO, aviso_eliminado)
    texto_eliminado = FUENTE.render(f"PERDISTE :P", False, BLANCO)
    ventana.blit(texto_eliminado, (eliminado_x + 100, eliminado_y + 60))


def reiniciar_main(database: dict):
    """Reinicia el diccionario `database`, volviendo a una version inicial.

    Args:
        database (dict): diccionario que se va a reiniciar

    Returns:
        dict: el mismo dict `database` pero ya reiniciado al estado inicial
    """
    database["respuestas_correctas"] = 0
    database["contador_tiempo"] = 0
    database["comodin_uno"] = True
    database["comodin_dos"] = True
    database["comodin_tres"] = True
    database["habilitar_comodin_tres"] = 0
    database["estado"] = "principal"
    database["nombre_jugador"] = ""
    database["monedas_base"] = 0
    database["jugador_puntos"] = []
    database["tiempo para responder"] = 0
    database["fuera de tiempo"] = False
    return database
