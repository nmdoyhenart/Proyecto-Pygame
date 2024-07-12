import pygame
import time
import random
from funciones_tercer_estado import *
from archivos import *
from elementos import *
from efectos_de_sonido import *


def arranque_juego(FUENTE, ventana, evento, pregunta_aleatoria):
    """Crea los dos botones para seleccionar las opciones.

    Args:
        opcion_azul: str: String, opcion_roja: str: String.
    """
    estado = "segundo estado"
    preguntas = leer_preguntas("Preguntas.csv")
    pregunta_resp = preguntas[pregunta_aleatoria]
    decision = True
    color = None
    tupla_decision = rojo_azul(FUENTE, ventana, pregunta_resp["Opciones"][0], pregunta_resp["Opciones"][1])
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

    retorna = [estado, color, bandera_jueces]
    texto_pregunta(pregunta_resp["Pregunta"], ventana, FUENTE)

    return retorna

def rojo_azul(FUENTE, ventana, opcion_roja, opcion_azul):
    x = 100
    y = 600
    boton_altura = 90
    boton_ancho = 250 

    rojo = pygame.Rect(x, y, boton_ancho, boton_altura)
    pygame.draw.rect(ventana, ROJO, rojo)
    pygame.draw.rect(ventana, NEGRO, rojo, 2)
    texto_superficie = FUENTE.render(f"{opcion_roja}", True, NEGRO)
    ventana.blit(texto_superficie, (rojo.x + 5, rojo.y + 5))

    azul = pygame.Rect(x + boton_ancho, y, boton_ancho, boton_altura)
    pygame.draw.rect(ventana, AZUL_CLARO, azul)
    pygame.draw.rect(ventana, NEGRO, azul, 2)
    texto_superficie = FUENTE.render(f"{opcion_azul}", True, BLANCO)
    ventana.blit(texto_superficie, (azul.x + 5, azul.y + 5))

    return (rojo, azul)


def texto_pregunta(pregunta: str, ventana, FUENTE):
    """Grafica para las preguntas.

    Args:
        pregunta: str: String.
    """
    ancho = 500
    alto = 50
    x = 100
    y = 550
    cuadro_preg = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(ventana, GRIS, cuadro_preg)
    pygame.draw.rect(ventana, NEGRO, cuadro_preg, 2)
    texto_preg = FUENTE.render(f"{pregunta}", True, NEGRO)
    ventana.blit(texto_preg, (x + 3, y + 15))


def mi_personaje(ventana):
    """Creación de la interfaz del personaje.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    x_personaje = 150
    y_personaje = 150
    personajes = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\personaje.png")
    personajes = pygame.transform.scale(personajes, (400, 600))
    ventana.blit(personajes,(x_personaje, y_personaje))


def decision_personaje(ventana, estado: bool, color: str):
    """Comprueba si el título existe y lo elimina de la lista.

    Args:
        estado: bool: Devuelve True o False, color: str: String.
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


def comodines(ventana: int, comodin_uno: bool, comodin_dos: bool, comodin_tres: bool, evento, estado):
    """Comprueba si el título existe y lo elimina de la lista.

    Args:
        ventana: int: Numerico, comodin_uno: Bandera, comodin_dos: Bandera, comodin_tres: Bandera.
    """
    x_comodines = 10
    y_caja = 500
    ancho_comodin = 30
    alto_comodin = 30
    y_comodin1 = y_caja
    y_comodin2 = y_comodin1 + alto_comodin + 10
    y_comodin3 = y_comodin2 + alto_comodin + 10

    coordenadas_1 = (x_comodines, y_comodin1)
    coordenadas_2 = (x_comodines, y_comodin2)
    coordenadas_3 = (x_comodines, y_comodin3)

    if comodin_uno:
        comodin1 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\comodin1.png")
        comodin1 = pygame.transform.scale(comodin1, (ancho_comodin, alto_comodin))
        ventana.blit(comodin1, coordenadas_1)
    else:
        comodin1 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
        comodin1 = pygame.transform.scale(comodin1, (ancho_comodin, alto_comodin))
        ventana.blit(comodin1, coordenadas_1)

    if comodin_dos:
        comodin2 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\comodin2.png")
        comodin2 = pygame.transform.scale(comodin2, (ancho_comodin, alto_comodin))
        ventana.blit(comodin2, coordenadas_2)
    else:
        comodin2 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
        comodin2 = pygame.transform.scale(comodin2, (ancho_comodin, alto_comodin))
        ventana.blit(comodin2, coordenadas_2)

    if comodin_tres:
        comodin3 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\comodin3.png")
        comodin3 = pygame.transform.scale(comodin3, (ancho_comodin, alto_comodin))
        ventana.blit(comodin3, coordenadas_3)
    else:
        comodin3 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
        comodin3 = pygame.transform.scale(comodin3, (ancho_comodin, alto_comodin))
        ventana.blit(comodin3, coordenadas_3)
    
    boton_comodin_1 = pygame.Rect(x_comodines, y_comodin1, ancho_comodin, alto_comodin)
    boton_comodin_2 = pygame.Rect(x_comodines, y_comodin2, ancho_comodin, alto_comodin)
    boton_comodin_3 = pygame.Rect(x_comodines, y_comodin3, ancho_comodin, alto_comodin)

    tupla_rect = (boton_comodin_1, boton_comodin_2, boton_comodin_3)

    back = botones_comodines(tupla_rect, evento,comodin_uno, comodin_dos, comodin_tres, estado)

    return back
 

def botones_comodines(tupla_rect, evento,comodin_uno: bool, comodin_dos: bool, comodin_tres: bool, estado):
    REC_COMODIN1 = tupla_rect[0]
    REC_COMODIN2 = tupla_rect[1]
    REC_COMODIN3 = tupla_rect[2]
    
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
                #estado = "tercer estado"
                comodin_tres = False
                efecto_de_sonido()
            else:
                comodin_usado()

    back = (comodin_uno, comodin_dos, comodin_tres, estado)

    return back

def logica_comodines(ventana, comodin_uno, comodin_dos, comodin_tres, estado, back_comodines, preguntas, pregunta_aleatoria, habilitar_comodin_tres, contador_tiempo):
    tiempo_comodin_dos = 0
    if comodin_uno != back_comodines[0] :
        comodin_uno = back_comodines[0]
        if comodin_uno == False:
            pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
    if comodin_dos != back_comodines[1] :
        comodin_dos = back_comodines[1]
        estado = back_comodines[3]
        if comodin_dos == False:
            pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
            tiempo_comodin_dos = time.time()
    if comodin_tres != back_comodines[2]:
        comodin_tres = back_comodines[2]
        if comodin_tres == False:
            if habilitar_comodin_tres == 0:
                habilitar_comodin_tres = 1
                lista_jueces = decisiones_jueces(5)
                funcion_comodin_tres(ventana, lista_jueces, comodin_tres, contador_tiempo)
            if contador_tiempo == 0:
                pygame.display.flip()
                time.sleep(2)
                contador_tiempo = 10
    return comodin_uno, comodin_dos, comodin_tres, estado, pregunta_aleatoria, tiempo_comodin_dos, lista_jueces, habilitar_comodin_tres, contador_tiempo


