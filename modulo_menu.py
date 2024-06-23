"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
from os import system
from modulo_preguntas import *

def elegir_opcion():
    opcion = input("""Bienvenido al juego "This or that"\n1- Jugar\n2- Salir\n
Elija una opción: """)

    return opcion

lista_preguntas = [{"Pregunta": "¿Cual es la capital de Argentina?","Opciones": ["La plata", "Buenos aires"],"Correcta": 2},{"Pregunta": "¿Cuanto es 2 + 2?","Opciones": ["3", "4"],"Correcta": 2},{"Pregunta": "¿Cuál es la capital de España?", "Opciones": ["Madrid", "Barcelona"],"Correcta": 1},{"Pregunta": "¿Cuánto es 5 * 6?","Opciones": ["30", "35"],"Correcta": 2},{"Pregunta": "¿Cuál es el río más largo del mundo?","Opciones": ["Nilo", "Misisipi"],"Correcta": 1},{"Pregunta": "¿Quién escribió 'Cien años de soledad'?","Opciones": ["Gabriel García Márquez", "Jorge Luis Borges"],"Correcta": 1},{"Pregunta": "¿Cuál es el resultado de 7 + 8?","Opciones": ["15", "16"],"Correcta": 1},{"Pregunta": "¿Qué país tiene la mayor población del mundo?","Opciones": ["India", "Estados Unidos"],"Correcta": 1},{"Pregunta": "¿Cuál es el idioma oficial de Brasil?","Opciones": ["Español", "Portugués"],"Correcta": 2},{"Pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?","Opciones": ["1937", "1939"],"Correcta": 2}]

system("cls")

# datos_juego(lista_preguntas)

while True:
    opcion = elegir_opcion()
    match opcion:
        case "1":
            preguntas_respuestas(lista_preguntas)
            monedas_incrementales(lista_preguntas)
        case "2":
            print("Gracias por escogernos.")
            print("Saliendo del programa..")
            break
        case  _:
            print("\n- Seleccione una opcion valída.\n")