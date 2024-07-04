"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame

def efecto_de_sonido():
    """Efecto de sonido al seleccionar las opciones varias.

    Args:
        -
    """
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(r"recursos\pop.mp3")
    sonido_fondo.set_volume(0.7)
    sonido_fondo.play()

def derrota():
    """Efecto de sonido al NO coincidir con el publico.

    Args:
        -
    """
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(r"recursos\error.mp3")
    sonido_fondo.set_volume(0.7)
    sonido_fondo.play()

def comodin_usado():
    """Efecto de sonido al seleccionar un comodin ya utilizado.

    Args:
        -
    """
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(r"recursos\error windows.mp3")
    sonido_fondo.set_volume(5.0)
    sonido_fondo.play()

def respuesta_correcta_sonido():
    """Efecto de sonido al coincidir con el publico.

    Args:
        -
    """
    pygame.mixer.init()
    sonido_fondo = pygame.mixer.Sound(r"recursos\respuesta_correcta.mp3")
    sonido_fondo.set_volume(0.7)
    sonido_fondo.play()

def musica_fondo():
    """Musica de fondo al iniciar el juego.

    Args:
        -
    """
    pygame.mixer.init()
    musica__fondo_siempre = pygame.mixer.Sound(r"recursos\musica de fondo.mp3")
    musica__fondo_siempre.set_volume(0.01)
    musica__fondo_siempre.play()