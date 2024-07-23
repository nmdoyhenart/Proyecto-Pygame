"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
import random
from funciones_base import dibujar_boton_rectang
from funciones_tercer_estado import *
from archivos import *
from elementos import *
from efectos_de_sonido import *

def arranque_juego(fuente, ventana, evento, pregunta_aleatoria: int, database: dict):
    """Funcion que ejecuta el juego

    Args:
        fuente: font: fuente python, ventana: surface: superficie, evento: event: Evento, pregunta_aleatoria: int: Numerico, database: dict: Diccionario.
    """
    estado = "segundo estado"
    preguntas = database["preguntas"]
    columna_con_la_pregunta = preguntas[pregunta_aleatoria]
    decision = True
    color = None
    tupla_decision = rojo_azul(fuente, ventana, columna_con_la_pregunta[1], columna_con_la_pregunta[2])
    rojo = tupla_decision[0]
    azul = tupla_decision[1]
    bandera_jueces = False
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if rojo.collidepoint(evento.pos) or azul.collidepoint(evento.pos):
            bandera_jueces = True
            if rojo.collidepoint(evento.pos):
                color = ROJO
                decision = False
                estado = "tercer estado"
            else:
                color = AZUL
                decision = False
                estado = "tercer estado"
            efecto_de_sonido()
    decision_personaje(ventana, decision, color)
    mi_personaje(ventana)

    retorna = { "estado": estado, 
              "color": color, 
              "bandera": bandera_jueces}
    texto_pregunta(columna_con_la_pregunta[0], ventana, fuente)

    return retorna

def rojo_azul(fuente, ventana, opcion_roja: str, opcion_azul: str):
    """Función que crea ambos botones

    Args:
        fuente: font: fuente python, ventana: surface: superficie, opcion_roja: str: String, opcion_azul: str: String.
    """   
    x = 100
    y = 600
    boton_altura = 90
    boton_ancho = 250 
    dimenciones_rojo = (x, y, boton_ancho, boton_altura)
    rojo = dibujar_boton_rectang(ventana, dimenciones_rojo, fuente, opcion_roja, ROJO)

    dimensiones_azul = (x + boton_ancho, y, boton_ancho, boton_altura)
    azul = dibujar_boton_rectang(ventana, dimensiones_azul, fuente, opcion_azul, AZUL)

    return (rojo, azul)

def texto_pregunta(pregunta: str, ventana, fuente):
    """Grafica para las preguntas.

    Args:
        pregunta: str: String, ventana: surface: Superficie, fuente: font: fuente python.
    """
    ancho = 500
    alto = 50
    x = 100
    y = 550
    cuadro_preg = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(ventana, GRIS, cuadro_preg)
    pygame.draw.rect(ventana, NEGRO, cuadro_preg, 2)
    texto_preg = fuente.render(f"{pregunta}", True, NEGRO)
    ventana.blit(texto_preg, (x + 3, y + 15))

def mi_personaje(ventana):
    """Creación de la interfaz del personaje.

    Args:
        ventana: surface: superficie del juego
        """
    x_personaje = 150
    y_personaje = 150
    personajes = pygame.image.load(r"recursos\personaje.png")
    personajes = pygame.transform.scale(personajes, (400, 600))
    ventana.blit(personajes,(x_personaje, y_personaje))

def decision_personaje(ventana, estado: bool, color: tuple):
    """Muestra la decision del personaje principal.

    Args:
        ventana: surface: Superficie, estado: bool: Booleano, color: tuple: Tupla.
    """
    if estado:
        midecision = pygame.image.load(r"recursos\incognita.png")
        midecision = pygame.transform.scale(midecision, (160,140))
        ventana.blit(midecision, (150 + 115, 150 + 280))
    else:
        mi_decision = pygame.Rect(150 + 115, 150 + 280, 160,140)
        pygame.draw.rect(ventana, color, mi_decision)

def decisiones_jueces(iteraciones: int):
    """Función que selecciona aleatoriamente las respuestas.

    Args:
        iteraciones: int: Numerico. 
    """
    respuestas = [ROJO, AZUL]
    lista_decisiones = []
    for i in range(iteraciones):
        decision = random.randint(0, 1)
        lista_decisiones.append(respuestas[decision])

    return lista_decisiones