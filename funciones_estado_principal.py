
import pygame
import random
from funciones_base import *
from elementos import *
from efectos_de_sonido import *
from archivos import *
from funciones_ver_top import *

#------------------------------------------------------------------------------------------------------------------
def funcion_principal(ventana, fuente, eventos, evento, preguntas, monedas_base, estado, activo, nombre_jugador):
    """_summary_

    Args:
        ventana (surface): _description_
        fuente: font: fuente que usara el texto
        eventos (list): lista de los eventos que se esta llevando a cabo
        evento (event): evento que se esta llevando a cabo
        preguntas (_type_): _description_
        monedas_base (int): cantidad de monedas
        estado (_type_): _description_
        activo: bool
        nombre_jugador (str): nombre del jugador ingresado

    Returns:
        _type_: _description_
    """
    ingrese_nombre(fuente, ventana, activo)
    nombre_jugador, activo = manejar_caja_texto(eventos, nombre_jugador, AZUL_CLARO, AZUL, fuente, ventana, activo)
    pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
    inicio = boton_inicio(fuente, ventana, evento, estado)
    estado = dibujar_boton_top(ventana, fuente, evento, estado)
    if inicio:
        if nombre_jugador == "":
            nombre_jugador = "Jugador"
        estado = "segundo estado"
    back_inicio = {"estado": estado,
                   "pregunta_aleatoria": pregunta_aleatoria,
                   "puntos_jugador": monedas_base,
                   "nombre_jugador": nombre_jugador,
                   "input_nombre": activo} 
    return back_inicio


def boton_inicio(FUENTE, ventana, evento, estado):
    """Boton para comenzar el juego.

    Args:
        -
    """
    if estado == "principal":
        centro = (350,549)
        radio = 60
        input = pygame.Rect(275, 500, 150, 90)
        texto_superficie = FUENTE.render("Jugar", True, BLANCO)
        rectangulo_texto = texto_superficie.get_rect(center = input.center)
        pygame.draw.circle(ventana, ROJO, centro, radio)
        ventana.blit(texto_superficie, rectangulo_texto)
        inicio = False    
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if input.collidepoint(evento.pos):
                inicio = True
                
                efecto_de_sonido()
    return inicio


def ingrese_nombre(fuente, ventana, activo):
    """Función que grafica un texto guia.

    Args:
        fuente: font: fuente que usara el texto
        ventana: surface: superficie de la pantalla
        activo: bool
    """
    input = pygame.Rect(275, 200, 150, 90)
    texto = "¡Ingrese su nombre!"
    if activo:
        contorno = AZUL
    else:
        contorno = AZUL_CLARO

    texto_superficie = fuente.render(texto, True, BLANCO, contorno)
    rectangulo_texto = texto_superficie.get_rect(center = input.center)
    ventana.blit(texto_superficie, rectangulo_texto)


def manejar_caja_texto(eventos, texto, color_inactivo, color_activo, fuente, ventana, activo):
    """Función que implementa un cuadro de texto interactivo.
    Args:
        eventos, texto, color_inactivo, color_activo, fuente, ventana, activo
    """
    ancho_caja = 400
    alto_caja = 100
    y_caja = 270
    x_caja = 150
    rect = pygame.Rect(x_caja, y_caja, ancho_caja, alto_caja)

    if activo:
        color = color_activo
    else:
        color = color_inactivo

    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            if activo:
                if evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif evento.key == pygame.K_ESCAPE:
                    texto = ""
                else:
                    if len(texto) < 20 and evento.unicode.isalpha():
                        texto += evento.unicode
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(evento.pos):
                activo = not activo


    pygame.draw.rect(ventana, BLANCO, rect)
    pygame.draw.rect(ventana, color, rect, 2)
    texto_superficie = fuente.render(texto, True, (0, 0, 0))
    texto_rect = texto_superficie.get_rect(center=(rect.x + rect.width / 2, rect.y + rect.height / 2))
    ventana.blit(texto_superficie, texto_rect.topleft)

    return texto, activo

#-------------------------------------------------------------------------------------------------------------------




def monedas_contador(monedas_base, ANCHO_VENTANA, FUENTE, ventana):
    """Grafica interactiva de las monedas.
    Args:
        monedas_base (int): cantidad de monedas
        ANCHO_VENTANA (int): ancho de la ventana/pantalla
        FUENTE (font): _description_
        ventana (surface): _description_
    """
    monedas = pygame.Rect(ANCHO_VENTANA - 100, 80, 100, 30)

    texto_monedas = FUENTE.render(str(monedas_base), True, BLANCO)
    pygame.draw.rect(ventana, NEGRO, monedas, 0)
    ventana.blit(texto_monedas, (monedas.x + 5, monedas.y + 3 ))
    escalar_imagen(ventana, (45, 30),(ANCHO_VENTANA - 35, 80), r"TP-PYGAME-COLLAB-main\recursos\moneda.png")


def boton_vuelta(ventana, dimension, evento):
    """Punto de retorno para volver al menu principal.
    Args:
        ventana (surface): _description_
        dimension (tuple): tupla con ancho y alto de la ventana
        evento (event): evento que se esta llevando a cabo

    Returns:
        bool: retorna un booleano dependiendo si toco o no el boton de vuelta
    """
    ancho_ventana = dimension[0]
    alto_ventana = dimension[1]
    x = ancho_ventana - 35
    y = alto_ventana - 35
    ancho = 30
    alto = 30
    vuelta_boton = pygame.Rect(x, y, ancho, alto)

    punto_vuelta = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\X_vuelta.png")
    punto_vuelta= pygame.transform.scale(punto_vuelta , (ancho, alto))
    ventana.blit(punto_vuelta, (x, y))
    retorno = False
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if vuelta_boton.collidepoint(evento.pos):
            retorno = True
    return retorno


