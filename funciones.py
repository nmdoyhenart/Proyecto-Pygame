"""
Modulo todo lo que no tiene que ver con pygame
"""
from elementos import *
from archivos import *
import pygame
import random

pygame.init()
ancho_caja = 400
alto_caja = 100
y_caja = 270
x_caja = 150
rect_caja = pygame.Rect(x_caja, y_caja, ancho_caja, alto_caja)
color_inactivo = pygame.Color('lightskyblue3')
color_activo = pygame.Color('dodgerblue2')
color_fondo = pygame.Color('white')
texto_caja = ""
activo = False

def manejar_caja_texto(eventos, texto, rect, color_inactivo, color_activo, fuente, ventana, activo):
    """Función que implementa un cuadro de texto interactivo.
    Args:
        eventos, texto, rect, color_inactivo, color_activo, fuente, ventana, activo
    """
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


    pygame.draw.rect(ventana, color_fondo, rect)
    pygame.draw.rect(ventana, color, rect, 2)
    
    texto_superficie = fuente.render(texto, True, (0, 0, 0))
    texto_rect = texto_superficie.get_rect(center=(rect.x + rect.width / 2, rect.y + rect.height / 2))
    ventana.blit(texto_superficie, texto_rect.topleft)

    return texto, activo



def boton_top(ventana, fuente, evento, estado):
    x = 50
    y = 50
    boton_altura = 50
    boton_ancho = 115

    top = pygame.Rect(x, y, boton_ancho, boton_altura)
    pygame.draw.rect(ventana, ROJO_CLARO, top)
    pygame.draw.rect(ventana, NEGRO, top, 2)
    texto_superficie = fuente.render(f"VER TOP", True, BLANCO)
    ventana.blit(texto_superficie, (top.x + 5, top.y + 5))
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if top.collidepoint(evento.pos):
            estado = "top jugadores"
    return estado


def top_5_jugadores(lists):
    top_5 = []
    for item in lists:
        top_5.append(item)
        for i in range(len(top_5) - 1, 0, -1):
            if top_5[i][1] > top_5[i - 1][1]:
                top_5[i], top_5[i - 1] = top_5[i - 1], top_5[i]

        if len(top_5) > 5:
            top_5.pop()

    return top_5


def dibujar_top_5(pantalla, lista_top, fuente):
    rectangulo = pygame.Rect(200, 200,300, 400)
    titulo = "Top 5 jugadores"
    pygame.draw.rect(pantalla, GRIS, rectangulo)
    pygame.draw.rect(pantalla, NEGRO, rectangulo, 2)  # Borde negro

    superficie_titulo = fuente.render(titulo, True, NEGRO)
    pantalla.blit(superficie_titulo, (rectangulo.x + 10, rectangulo.y + 10))

    y_offset = rectangulo.y + 40

    for i, item in enumerate(lista_top):
        texto = f"{i+1}. {item[0]}  Puntos:{item[1]}"
        superficie_texto = fuente.render(texto, True, NEGRO)
        pantalla.blit(superficie_texto, (rectangulo.x + 5, y_offset))
        y_offset += superficie_texto.get_height() + 5


def top_cinco(ventana, fuente, lista_jugadores):
    top = top_5_jugadores(lista_jugadores)

    dibujar_top_5(ventana, top, fuente)



def monedas_incrementales(puntos: list, monedas_base: int, posicion: int):
    """Actualiza constantemente las monedas haciendolas incrementales.

    Args:
        puntos: list: Lista donde se guardan los puntos, monedas_base: int: Numerico, posicion: int: Numerico.
    """
    monedas_base += puntos[posicion - 1]
    return monedas_base


def jueces_decision(decision: list):
    """Cuenta los colores asigandos aleatoriamente.

    Args:
        decision: list: Lista que contiene la decisión final  
    """
    contador_rojo = 0
    contador_azul = 0
    for elementos in decision:
        if elementos == ROJO:
            contador_rojo += 1
        else:
            contador_azul += 1
    if contador_rojo > contador_azul:
        retorna = ROJO
    else:
        retorna = AZUL
    return retorna

def comprobacion(voto_jueces: list, mi_decision: tuple):
    color_decidido = jueces_decision(voto_jueces)
    if color_decidido == mi_decision:
        retorna = True
    else:
        retorna = False
    return retorna

def porcentaje_decision(decision: list):
    """Calcula el porcentaje de decisión de los jueces

    Args:
        decision: list: Lista que contiene la decisión final  
    """
    contador_rojo = 0
    contador_azul = 0
    for elementos in decision:
        if elementos == ROJO:
            contador_rojo += 1
        else:
            contador_azul += 1
    
    porcentaje_azul = (contador_azul * 100) // 5
    porcentaje_rojo = (contador_rojo * 100) // 5

    return (porcentaje_azul, porcentaje_rojo)