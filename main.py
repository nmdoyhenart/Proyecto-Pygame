"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
import time
from archivos import *
from funciones import *
from parte_pygame import *

lista_puntos = cargar_puntos()

tiempo_transcurrido = lambda contador, fps: contador // fps

ANCHO_VENTANA = 700
ALTO_VENTANA = 700

VENTANA_DIMENSION = (ANCHO_VENTANA, ALTO_VENTANA)

fuente = pygame.font.Font(None, 36)

fuente_porcentaje = pygame.font.Font(None, 30)

ventana = pygame.display.set_mode(VENTANA_DIMENSION)

icono_ventana()
titulo_ventana()

bandera = True
estado = "principal"
preguntas = leer_preguntas("Preguntas.csv")
monedas_base = 0
habilitar_sonido = 0 
respuestas_correctas = 0
color_decision = None
comodin_uno = True
comodin_dos = True
tiempo_comodin_dos = 0
comodin_tres = True
habilitar_comodin_tres = 0
contador_tiempo = 0
puntos = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]
activo = False

pygame.init()

while bandera:
    fondo(ventana, VENTANA_DIMENSION)
    monedas_contador(monedas_base, VENTANA_DIMENSION[0], fuente, ventana)
    
    eventos = pygame.event.get()

    for event in eventos:
        if event.type == pygame.QUIT:
            bandera = False

    if estado == "principal":
        ingrese_nombre()
        texto_caja, activo = manejar_caja_texto(eventos, texto_caja, rect_caja, color_inactivo, color_activo, fuente, ventana, activo)
        pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
        inicio = funcion_principal(fuente, ventana, event, estado)
        if inicio:
            estado = "segundo estado"

    elif estado == "segundo estado":
        juego = arranque_juego(fuente, ventana, event, pregunta_aleatoria)
        back_comodines = comodines(ventana, comodin_uno, comodin_dos, comodin_tres, event, estado)
        habilitar_sonido = 0
        estado = juego[0]
        color_decision = juego[1]
        if juego[2]:
            if habilitar_comodin_tres == 1:
                habilitar_comodin_tres = 2
            else:
                lista_jueces = decisiones_jueces(5)

        if comodin_uno != back_comodines[0] or comodin_dos != back_comodines[1] or comodin_tres != back_comodines[2]:
            comodin_uno = back_comodines[0]
            comodin_dos = back_comodines[1]
            comodin_tres = back_comodines[2]
            estado = back_comodines[3]
            
            if comodin_uno == False:
                pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
            if comodin_dos == False:
                pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
                tiempo_comodin_dos = time.time()
            if comodin_tres == False:
                if habilitar_comodin_tres == 0:
                    habilitar_comodin_tres = 1
                    lista_jueces = decisiones_jueces(5)
                    funcion_comodin_tres(ventana, lista_jueces, comodin_tres, contador_tiempo)
                if contador_tiempo == 0:
                    pygame.display.flip()
                    time.sleep(2)
                    contador_tiempo = 10
                
        if estado == "tercer estado":
            tiempo_muerto = time.time()

        volver = vuelta(ventana, VENTANA_DIMENSION, event)
        if volver:
            estado = "principal" 
            
    elif estado == "tercer estado":
        tiempo_actual = time.time()

        if comodin_dos == True:
            comprobar_eleccion = estado_tres(ventana, fuente_porcentaje, color_decision, lista_jueces, comodin_tres, contador_tiempo)
        else:
            comodin_dos_time = tiempo_actual - tiempo_comodin_dos
            if comodin_dos_time < 4:
                comprobar_eleccion = True
            else:
                tiempo_comodin_dos = 10
                comprobar_eleccion = estado_tres(ventana, fuente_porcentaje, color_decision, lista_jueces, comodin_tres, contador_tiempo)

        habilitar_sonido = ganar_perder(ventana, fuente, comprobar_eleccion, habilitar_sonido)

        transcurrido = tiempo_actual - tiempo_muerto
        if transcurrido >= 3:
            if comprobar_eleccion:
                respuestas_correctas += 1
                monedas_base = monedas_incrementales(puntos, monedas_base, respuestas_correctas)
                lista_puntos.append(monedas_base)
                pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
                estado = "segundo estado"
            else:
                guardar_puntos(lista_puntos)
                respuestas_correctas = 0
                contador_tiempo = 0
                comodin_uno = True
                comodin_dos = True
                bandera_comodin_dos = True
                comodin_tres = True
                habilitar_comodin_tres = 0
                estado = "principal"
                monedas_base = 0
    
    pygame.display.flip()

pygame.quit()