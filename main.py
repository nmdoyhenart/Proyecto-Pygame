"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
from archivos import *
from accionar_estados import *

ventana, ventana_dimension = crear_ventana()
icono_ventana()
titulo_ventana()
fuente = pygame.font.Font(None, 36)
fuente_porcentaje = pygame.font.Font(None, 30)
bandera = True
color_decision = None
lista_jugadores = cargar_puntos("Puntos.json")
preguntas = leer_preguntas("Preguntas.csv")
puntos = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]
database = {"estado": "principal",
            "nombre_jugador": "",
            "puntos": puntos,
            "monedas_base": 0,
            "respuestas_correctas": 0,
            "comodin_uno": True,
            "comodin_dos": True,
            "comodin_tres": True,
            "comprobar_ing_nombre": False,
            "tiempo_comodin_dos" : 0,
            "habilitar_comodin_tres" : 0,
            "contador_tiempo" : 0,
            "tiempo para responder": 0,
            "fuera de tiempo": False,
            "preguntas": preguntas,
            "lista_jueces": []
            }

pygame.init()
musica_fondo()
while bandera:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            bandera = False
    fondo(ventana, ventana_dimension)
    monedas_contador(database["monedas_base"], ventana_dimension[0], fuente, ventana)

    if database["estado"] == "principal":
        feedback_principal = accionar_estado_principal(ventana, fuente, eventos, evento, database)
        database = feedback_principal["base de datos"]
        pregunta_aleatoria = feedback_principal["pregunta_aleatoria"]
        jugador_puntos = feedback_principal["jugador"]

    elif database["estado"] == "segundo estado":
        feedback_estado_dos = accionar_segundo_estado(ventana, fuente, ventana_dimension, evento, database, pregunta_aleatoria)
        database = feedback_estado_dos["base de datos"]
        pregunta_aleatoria = feedback_estado_dos["pregunta_aleatoria"]
        habilitar_sonido = feedback_estado_dos["sonido"]
        color_decision = feedback_estado_dos["color_desicion"]
        tiempo_muerto = feedback_estado_dos["tiempo"]

    elif database["estado"] == "tercer estado":
        feedback_estado_tres = accionar_tercer_estado(ventana, fuente, database, fuente_porcentaje, color_decision, tiempo_muerto, puntos, lista_jugadores, pregunta_aleatoria, habilitar_sonido, jugador_puntos)

        database = feedback_estado_tres["base de datos"]
        pregunta_aleatoria = feedback_estado_tres["pregunta_aleatoria"]
        habilitar_sonido = feedback_estado_tres["sonido"]

    elif database["estado"] == "top jugadores":
        top_cinco(ventana, fuente, lista_jugadores)
        volver = boton_vuelta(ventana, ventana_dimension, evento)
        if volver:
            database["estado"] = "principal" 

    elif database["estado"] == "tiempo excedido":
        fuera_de_tiempo(ventana, fuente)
        tiempo_fuera = tiempo_espera(database, 4, lista_jugadores, jugador_puntos)
        if tiempo_fuera:
            database = reiniciar_main(database)

    pygame.display.flip()
pygame.quit()