"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import time
from archivos import *
from funciones_base import *
from funciones_de_tiempo import *
from funciones_ver_top import *
from funciones_estado_principal import *
from funciones_segundo_estado import *
from funciones_tercer_estado import *
from funciones_ganar_o_perder import *
from funciones_de_comodines import *

def accionar_estado_principal(ventana, fuente, eventos: list, evento, database: dict):
    """Funcion que acciona el primer estado del juego.

    Args:
        ventana: surface: Superficie, fuente: font: Fuente python, eventos: list: Lista, evento: event: Evento, database: dict: Diccionario.
    """
    inicio = funcion_principal(ventana, fuente, eventos, evento, database["preguntas"], database["monedas_base"], database["estado"], database["comprobar_ing_nombre"], database["nombre_jugador"])
    database["estado"] = inicio["estado"]
    pregunta_aleatoria = inicio["pregunta_aleatoria"]
    database["monedas_base"] = inicio["puntos_jugador"]
    database["nombre_jugador"] = inicio["nombre_jugador"]
    database["comprobar_ing_nombre"] = inicio["input_nombre"]
    jugador_puntos = [database["nombre_jugador"], database["monedas_base"]]
    database["tiempo para responder"] = time.time()
    feedback_principal = {"base de datos": database,
                          "pregunta_aleatoria": pregunta_aleatoria,
                          "jugador": jugador_puntos}

    return feedback_principal

def accionar_segundo_estado(ventana, fuente, ventana_dimension: int, evento, database: dict, pregunta_aleatoria: list):
    """Funcion que acciona el segundo estado del juego.

    Args:
        ventana: surface: Superficie, fuente: font: Fuente python, ventana_dimension: int: Numerico, evento: event: Evento, database: dict: Diccionario, pregunta_aleatoria: list: Lista.
    """
    juego = arranque_juego(fuente, ventana, evento, pregunta_aleatoria, database)
    back_comodines = dibujar_comodines(ventana, database["comodin_uno"], database["comodin_dos"], database["comodin_tres"], evento, database["estado"])
    habilitar_sonido = 0
    database["estado"] = juego["estado"]
    color_decision = juego["color"]
    if juego["bandera"]:
        if database["habilitar_comodin_tres"] == 1:
            database["habilitar_comodin_tres"] = 2
        else:
            database["lista_jueces"] = decisiones_jueces(5)

    activacion_comodin_uno = activar_comodin_uno(database["comodin_uno"], back_comodines, database["preguntas"], pregunta_aleatoria)
    database["comodin_uno"] = activacion_comodin_uno["comodin_uno"]
    pregunta_aleatoria = activacion_comodin_uno["pregunta_aleatoria"]

    activacion_comodin_dos = activar_comodin_dos(database["comodin_dos"], back_comodines, database["estado"], database["preguntas"], pregunta_aleatoria)
    database["comodin_dos"] = activacion_comodin_dos["comodin_dos"]
    pregunta_aleatoria = activacion_comodin_dos["pregunta_aleatoria"]
    database["estado"] = activacion_comodin_dos["estado"]
    database["tiempo_comodin_dos"] = activacion_comodin_dos["tiempo_comodin"]

    activacion_comodin_tres = activar_comodin_tres(ventana, database["comodin_tres"], back_comodines, database["habilitar_comodin_tres"], database["contador_tiempo"], database["lista_jueces"])
    database["comodin_tres"] = activacion_comodin_tres["comodin_tres"]
    database["habilitar_comodin_tres"] = activacion_comodin_tres["habilitar_comodin"]
    database["contador_tiempo"] = activacion_comodin_tres["contador_tiempo"]
    database["lista_jueces"] = activacion_comodin_tres["lista_jueces"]

    tiempo_actual = time.time()
    database["fuera de tiempo"] = tiempo(ventana, fuente, tiempo_actual, database["tiempo para responder"], 15)
    if database["fuera de tiempo"]:
        database["tiempo para responder"] = time.time()
        database["estado"] = "tiempo excedido"

    tiempo_inicio = 0
    if database["estado"] == "tercer estado":
        tiempo_inicio = time.time()

    volver = boton_vuelta(ventana, ventana_dimension, evento)
    if volver:
        database["estado"] = "principal" 

    feedback_estado_dos = {"base de datos": database,
                          "pregunta_aleatoria": pregunta_aleatoria,
                          "sonido": habilitar_sonido,
                          "color_desicion": color_decision,
                          "tiempo": tiempo_inicio
                          }

    return feedback_estado_dos

def accionar_tercer_estado(ventana, fuente, database: dict, fuente_porcentaje, color_decision: str, tiempo_inicio: int, puntos: list, lista_jugadores: list, pregunta_aleatoria: list, habilitar_sonido: str, jugador_puntos: int):
    """Funcion que acciona el tercer estado del juego.

    Args:
        ventana: surface: Superficie, fuente: font: Fuente python, database: dict: diccionario, fuente_porcentaje: font: Fuente python, color_decision: str: String, tiempo_inicio: int: Numerico, puntos: list: lista, lista_jugadores: list: Lista, pregunta_aleatoria: list: Lista, habilitar_sonido: str: String, jugador_puntos: int: Numerico.
    """
    tiempo_actual = time.time()

    if database["comodin_dos"] == True:
        comprobar_eleccion = activar_estado_tres(ventana, fuente_porcentaje, color_decision, database["lista_jueces"], database["comodin_tres"], database["contador_tiempo"])
    else:
        comodin_dos_time = tiempo_actual - database["tiempo_comodin_dos"]
        if comodin_dos_time < 4:
            comprobar_eleccion = True
        else:
            database["tiempo_comodin_dos"] = 10
            comprobar_eleccion = activar_estado_tres(ventana, fuente_porcentaje, color_decision, database["lista_jueces"], database["comodin_tres"], database["contador_tiempo"])

    habilitar_sonido = efecto_de_sonido_ganar_perder(ventana, fuente, comprobar_eleccion, habilitar_sonido)
    transcurrido = tiempo_actual - tiempo_inicio
    if transcurrido >= 3:
        if comprobar_eleccion:
            database["respuestas_correctas"] += 1
            database["monedas_base"] = monedas_incrementales(puntos, database["monedas_base"], database["respuestas_correctas"])
            pregunta_aleatoria = random.randint(0, len(database["preguntas"]) - 1)
            jugador_puntos[1] = database["monedas_base"]
            jugador_puntos = [database["nombre_jugador"], database["monedas_base"]]
            database["estado"] = "segundo estado"
            database["tiempo para responder"] = time.time()

        else:
            lista_jugadores.append(jugador_puntos)
            guardar_puntos("Puntos.json",lista_jugadores)
            database = reiniciar_main(database)
            jugador_puntos = []
    
    feedback_estado_tres = {"base de datos": database,
                          "pregunta_aleatoria": pregunta_aleatoria,
                          "sonido": habilitar_sonido}
    return feedback_estado_tres