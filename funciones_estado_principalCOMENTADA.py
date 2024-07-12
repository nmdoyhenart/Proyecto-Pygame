import pygame
from funciones_baseCOMENTADA import *
from elementos import *
from efectos_de_sonido import *
from archivos import *

#-------------------------------------------------------------------------------------------------------------------

def funcion_principal(FUENTE: str, ventana: int, evento: list, estado: list):
    """Donde se desarolla el juego.

    Args:
        FUENTE: str: String, ventana: int: Numerico, evento: list: Lista, estado: list: Lista.
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

def ingrese_nombre(fuente: str, ventana: int):
    """Función que grafica un texto guia.

    Args:
        fuente: str: String, ventana: int: Numerico.
    """
    input = pygame.Rect(275, 200, 150, 90)
    texto = "¡Ingrese su nombre!"
    texto_superficie = fuente.render(texto, True, BLANCO)
    rectangulo_texto = texto_superficie.get_rect(center = input.center)
    ventana.blit(texto_superficie, rectangulo_texto)


def manejar_caja_texto(eventos: list, texto: str, rect_caja: int, color_inactivo: str, color_activo: str, fuente: str, ventana: int, activo: bool):
    """Función que grafica la caja de texto para ingresar tu nombre.

    Args:
        eventos: list: Lista, texto: str: String, rect_caja: int: Numerico, color_inactivo: str: String, color_activo: str: String, fuente: str: String, ventana: int: Numerico, activo: bool: Bandera.
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
            if rect_caja.collidepoint(evento.pos):
                activo = not activo


    pygame.draw.rect(ventana, BLANCO, rect_caja)
    pygame.draw.rect(ventana, color, rect_caja, 2)
    
    texto_superficie = fuente.render(texto, True, (0, 0, 0))
    texto_rect = texto_superficie.get_rect(center=(rect_caja.x + rect_caja.width / 2, rect_caja.y + rect_caja.height / 2))
    ventana.blit(texto_superficie, texto_rect.topleft)

    return texto, activo

#-------------------------------------------------------------------------------------------------------------
def monedas_contador(monedas_base: int, ANCHO_VENTANA: int, FUENTE: str, ventana: int):
    """Grafica interactiva de las monedas.

    Args:
        monedas_base: int: Numerico, ANCHO_VENTANA: int: Numerico, FUENTE: str: String, ventana: int: Numerico.
    """
    monedas = pygame.Rect(ANCHO_VENTANA - 100, 80, 100, 30)
    moneda_icon = pygame.image.load(r"recursos\moneda.png")
    moneda_icon = pygame.transform.scale(moneda_icon, (40, 30))

    texto_monedas = FUENTE.render(str(monedas_base), True, BLANCO)
    pygame.draw.rect(ventana, NEGRO, monedas, 0)
    ventana.blit(texto_monedas, (monedas.x , monedas.y ))
    ventana.blit(moneda_icon, (ANCHO_VENTANA - 35, 80))


def punto_vuelta(ventana: int, dimension: int, evento: list):
    """Punto de retorno para volver al menu principal.

    Args:
        ventana: int: Numerico, dimension: int: Numerico, evento: list: Lista.
    """
    ancho_ventana = dimension[0]
    alto_ventana = dimension[1]
    x = ancho_ventana - 35
    y = alto_ventana - 35
    ancho = 30
    alto = 30
    vuelta_boton = pygame.Rect(x, y, ancho, alto)

    punto_vuelta = pygame.image.load(r"recursos\X_vuelta.png")
    punto_vuelta= pygame.transform.scale(punto_vuelta , (ancho, alto))
    ventana.blit(punto_vuelta, (x, y))
    retorno = False
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if vuelta_boton.collidepoint(evento.pos):
            retorno = True
    return retorno