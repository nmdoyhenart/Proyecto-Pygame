"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
import random
from archivos import *
from funciones import *
# from parte_pygame import caja_de_texto

lista_puntos = cargar_puntos()

tiempo_transcurrido = lambda contador, fps: contador // fps

ANCHO_VENTANA = 700
ALTO_VENTANA = 700

VENTANA_DIMENSION = (ANCHO_VENTANA, ALTO_VENTANA)

FUENTE = pygame.font.Font(None, 36)

FUENTE_PORCENTAJE = pygame.font.Font(None, 30)

ventana = pygame.display.set_mode(VENTANA_DIMENSION)

titulo_ventana()
icono_ventana()

pygame.init()

bandera = True
estado = "principal"
preguntas = leer_preguntas("Preguntas.csv")
monedas_base = 0
fps = 20
clock = pygame.time.Clock()

respuestas_correctas = 0
boton_decision = True
color_decision = None
contador_comodin_dos = 0
contador_comodin_tres = 0
contador_espera = 0
comodin_uno = True
comodin_dos = True
comodin_tres = True
bandera_espera = False

while bandera:
    fondo(ventana, VENTANA_DIMENSION)
    monedas_contador(0, VENTANA_DIMENSION[0], FUENTE, ventana)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            #Salida del juego por la "X" 
            bandera = False
    if estado == "principal":
        # caja_de_texto()
        pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
        inicio = funcion_principal(FUENTE, ventana, evento, estado)
        if inicio:
            estado = "segundo estado"
    elif estado == "segundo estado":
        juego = start_play(FUENTE, ventana, evento, VENTANA_DIMENSION, pregunta_aleatoria)
        estado = juego[0]
        volver = vuelta(ventana, VENTANA_DIMENSION, evento)
        if volver:
            estado = "principal" 
    elif estado == "tercer estado":
        pass
            
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
