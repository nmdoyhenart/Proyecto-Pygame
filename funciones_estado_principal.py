import pygame
from funciones_base import *
from elementos import *
from efectos_de_sonido import *
from archivos import *


#-------------------------------------------------------------------------------------------------------------------

def funcion_principal(FUENTE, ventana, evento, estado):
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

def ingrese_nombre(fuente, ventana):
    input = pygame.Rect(275, 200, 150, 90)
    texto = "¡Ingrese su nombre!"
    texto_superficie = fuente.render(texto, True, BLANCO)
    rectangulo_texto = texto_superficie.get_rect(center = input.center)
    ventana.blit(texto_superficie, rectangulo_texto)


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


    pygame.draw.rect(ventana, BLANCO, rect)
    pygame.draw.rect(ventana, color, rect, 2)
    
    texto_superficie = fuente.render(texto, True, (0, 0, 0))
    texto_rect = texto_superficie.get_rect(center=(rect.x + rect.width / 2, rect.y + rect.height / 2))
    ventana.blit(texto_superficie, texto_rect.topleft)

    return texto, activo

#-------------------------------------------------------------------------------------------------------------------


def fondo(ventana, DIMENSION):
    """funcion que grafica el fondo el juego
    Args:
        ventana (surface): _description_
        DIMENSION (tuple): tamaño de la pantalla
    """
    fondo = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\fondo.jpg")
    fondo = pygame.transform.scale(fondo, DIMENSION)

    ventana.blit(fondo, (0, 0))    


def monedas_contador(monedas_base, ANCHO_VENTANA, FUENTE, ventana):
    """Grafica interactiva de las monedas.
    Args:
        monedas_base (int): cantidad de monedas
        ANCHO_VENTANA (int): ancho de la ventana/pantalla
        FUENTE (font): _description_
        ventana (surface): _description_
    """
    monedas = pygame.Rect(ANCHO_VENTANA - 100, 80, 100, 30)
    moneda_icon = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\moneda.png")
    moneda_icon = pygame.transform.scale(moneda_icon, (40, 30))

    texto_monedas = FUENTE.render(str(monedas_base), True, BLANCO)
    pygame.draw.rect(ventana, NEGRO, monedas, 0)
    ventana.blit(texto_monedas, (monedas.x , monedas.y ))
    ventana.blit(moneda_icon, (ANCHO_VENTANA - 35, 80))


def vuelta(ventana, dimension, evento):
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


