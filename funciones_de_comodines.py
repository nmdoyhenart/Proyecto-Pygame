import pygame
import random
import time
from funciones_base import *
from efectos_de_sonido import *
from funciones_tercer_estado import *
from funciones_segundo_estado import *


def dibujar_comodines(ventana: int, comodin_uno: bool, comodin_dos: bool, comodin_tres: bool, evento, estado: str)-> dict:
    """Comprueba si el título existe y lo elimina de la lista.

    Args:
        ventana: surface
        comodin_uno: bool
        comodin_dos: bool
        comodin_tres: bool
        evento: event
        estado: str:
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


def alternar_comodines(ventana, comodin_uno, comodin_dos, comodin_tres, dimension_comodin, coordenadas):
    """al accionarse los comodines, reemplaza sus iconos con una cruz roja

    Args:
        ventana (surface): superficie donde se ejecuta  el juego
        comodin_uno (bool): bandera que muestra si el comodin esta activo o ya fue usado
        comodin_dos (bool): bandera que muestra si el comodin esta activo o ya fue usado
        comodin_tres (bool): bandera que muestra si el comodin esta activo o ya fue usado
        dimension_comodin (tuple): tupla con las dimenciones de ancho y alto de los botones de los comodines
        coordenadas (tuple): tupla con las coordenadas de los comodines
    """
    coordenadas_1 = coordenadas[0]
    coordenadas_2 = coordenadas[1]
    coordenadas_3 = coordenadas[2]

    if comodin_uno:
        escalar_imagen(ventana, dimension_comodin, coordenadas_1, r"TP-PYGAME-COLLAB-main\recursos\comodin1.png")
    else:
        escalar_imagen(ventana, dimension_comodin, coordenadas_1, r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
    if comodin_dos:
        escalar_imagen(ventana, dimension_comodin, coordenadas_2, r"TP-PYGAME-COLLAB-main\recursos\comodin2.png")
    else:
        escalar_imagen(ventana, dimension_comodin, coordenadas_2, r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
    if comodin_tres:
        escalar_imagen(ventana, dimension_comodin, coordenadas_3, r"TP-PYGAME-COLLAB-main\recursos\comodin3.png")
    else:
        escalar_imagen(ventana, dimension_comodin, coordenadas_3, r"TP-PYGAME-COLLAB-main\recursos\cruz.png")


def botones_comodines(diccionario_botones: dict, evento, comodin_uno: bool, comodin_dos: bool, comodin_tres: bool, estado: str)-> dict:
    """funcion que capta cuando un comodin es accionado y procede a llamar a su ejecucion de ser asi

    Args:
        diccionario_botones (dict): diccionario con los rect/surface de los comodines
        evento (event): evento que se realiza en la actualidad
        comodin_uno (bool): bandera que muestra si el comodin esta activo o ya fue usado
        comodin_dos (bool): bandera que muestra si el comodin esta activo o ya fue usado
        comodin_tres (bool): bandera que muestra si el comodin esta activo o ya fue usado
        estado (str): estado actual del programa

    Returns:
        dict: _description_
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


def activar_comodin_uno(comodin_uno: bool, back_comodines: dict, preguntas: list, pregunta_aleatoria: int):
    """funcion que activa el uso del comodin uno

    Args:
        comodin_uno (bool): bandera que muestra si el comodin esta activo o ya fue usado
        back_comodines (dict): diccionario que actualiza si el comodin fue usado
        preguntas (list): lista de las preguntas y respuestas
        pregunta_aleatoria (int): posicion aleatoria de la pregunta actual

    Returns:
        dict: diccionario que ejecuta el accionar del comodin uno
    """
    if comodin_uno != back_comodines["comodin_uno"] :
        comodin_uno = back_comodines["comodin_uno"]
        if comodin_uno == False:
            pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
    back_comodin_uno = {"comodin_uno": comodin_uno,
                        "pregunta_aleatoria": pregunta_aleatoria}
    return back_comodin_uno


def activar_comodin_dos(comodin_dos: bool, back_comodines: dict, estado: str, preguntas: list, pregunta_aleatoria: int):
    """funcion de activacion del comodin dos

    Args:
        comodin_dos (bool): bandera que muestra si el comodin esta activo o ya fue usado
        back_comodines (dict): diccionario que actualiza si el comodin fue usado
        estado (str): estado que se muestra del juego
        preguntas (list): lista de las preguntas y respuestas
        pregunta_aleatoria (int): posicion aleatoria de la pregunta actual

    Returns:
        dict: diccionario que ejecuta el accionar del comodin dos
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




def activar_comodin_tres(ventana, comodin_tres: bool, back_comodines: dict, habilitar_comodin_tres: int, contador_tiempo: int, lista_jueces: list):
    """funcion de activacion del comodin dos


    Args:
        ventana (surface): _description_
        comodin_tres (bool):  bandera que muestra si el comodin esta activo o ya fue usado
        back_comodines (dict): diccionario que actualiza si el comodin fue usado
        habilitar_comodin_tres (int): auxiliar del comodin tres
        contador_tiempo (int): tiempo que se muestra el comodin
        lista_jueces (list): lista actual de jueces

    Returns:
        _type_: _description_
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
                time.sleep(2)
                contador_tiempo = 10
    back_comodin_tres = {"comodin_tres": comodin_tres,
                         "habilitar_comodin": habilitar_comodin_tres,
                         "contador_tiempo": contador_tiempo,
                         "lista_jueces": lista_jueces}
    return back_comodin_tres
