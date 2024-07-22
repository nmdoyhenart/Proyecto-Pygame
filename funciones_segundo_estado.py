import pygame
import random
from funciones_base import dibujar_boton_rectang
from funciones_tercer_estado import *
from archivos import *
from elementos import *
from efectos_de_sonido import *


def arranque_juego(fuente, ventana, evento, pregunta_aleatoria, database):
    """funcion que arranca y ejecuta el juego

    Args:
        fuente (font): fuente usada en el juego
        ventana (surface): superficie donde se desarrolla el juego
        evento (event): evento actual que se esta realizando
        pregunta_aleatoria (int): numero aleatorio de la posicion de 
        la pregunta que se va a mostrar
    Returns:
        dict: diccionario con los cambios que ocurren en la funcion
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


def rojo_azul(fuente, ventana, opcion_roja, opcion_azul):
    """Función que crea ambos botones

    Args:
        fuente: font: fuente de las cadenas del juego
        ventana: surface: superficie del juego
        opcion_roja: str: opcion que se muestra en el boton rojo
        opcion_azul: str: opcion que se muestra en el boton azul.
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
        pregunta: str: String.
        ventana: surface: superficie del juego
        fuente: font: fuente de las cadenas del juego

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
    personajes = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\personaje.png")
    personajes = pygame.transform.scale(personajes, (400, 600))
    ventana.blit(personajes,(x_personaje, y_personaje))


def decision_personaje(ventana, estado: bool, color):
    """Comprueba si el título existe y lo elimina de la lista.

    Args:
        ventana: surface: superficie del juego
        estado: bool: recibe True o False
        color: tuple: color que se pinta de acuerdo a la decision del usuario
    """
    if estado:
        midecision = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
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



