"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
import random
import time

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)

ANCHO_VENTANA = 800
ALTO_VENTANA = 600

VENTANA1 = (ANCHO_VENTANA, ALTO_VENTANA)

pygame.init()

ventana = pygame.display.set_mode(VENTANA1)
pygame.display.set_caption("Tot or trivia")

icono = pygame.image.load(r"TP-PYGAME-COLLAB/recursos/logo.jpg")
pygame.display.set_icon(icono)

fondo = pygame.image.load(r"TP-PYGAME-COLLAB\recursos\fondo.jpg")
fondo = pygame.transform.scale(fondo, VENTANA1)

fuente = pygame.font.Font(None, 36)

preguntas = [
    {
        "Preguntas": "¿Cual es la capital de Argentina?",
        "Opciones": ["La plata", "La pampa", "Buenos aires", "Tierra del fuego"],
        "Correcta": 2,
        "Puntos": 100
    },
    {
        "Preguntas": "¿Cuanto es 2 + 2?",
        "Opciones": ["3", "4", "5", "6"],
        "Correcta": 1,       
        "Puntos": 100
    },
    {
        "Pregunta": "¿Cuál es la capital de España?",
        "Opciones": ["Madrid", "Barcelona", "Sevilla", "Valencia"],
        "Correcta": 0,       
        "Puntos": 100
    },
    {
        "Pregunta": "¿Cuánto es 5 * 6?",
        "Opciones": ["30", "28", "35", "25"],
        "Correcta": 2,        
        "Puntos": 100
    },
    {
        "Pregunta": "¿Cuál es el río más largo del mundo?",
        "Opciones": ["Amazonas", "Nilo", "Yangtsé", "Misisipi"],
        "Correcta": 1,        
        "Puntos": 100
    },
    {
        "Pregunta": "¿Quién escribió 'Cien años de soledad'?",
        "Opciones": ["Gabriel García Márquez", "Pablo Neruda", "Julio Cortázar", "Jorge Luis Borges"],
        "Correcta": 0,        
        "Puntos": 100
    },
    {
        "Pregunta": "¿Cuál es el resultado de 7 + 8?",
        "Opciones": ["15", "16", "14", "13"],
        "Correcta": 0,        
        "Puntos": 100
    },
    {
        "Pregunta": "¿Qué país tiene la mayor población del mundo?",
        "Opciones": ["India", "Estados Unidos", "Indonesia", "China"],
        "Correcta": 0,        
        "Puntos": 100
    },
    {
        "Pregunta": "¿Cuál es el idioma oficial de Brasil?",
        "Opciones": ["Español", "Portugués", "Inglés", "Francés"],
        "Correcta": 1,        
        "Puntos": 100
    },
    {
        "Pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "Opciones": ["1937", "1938", "1939", "1940"],
        "Correcta": 2,        
        "Puntos": 100
    }
]

bandera = True

while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
     
    ventana.blit(fondo,(0,0))

    pygame.display.update()

pygame.quit()