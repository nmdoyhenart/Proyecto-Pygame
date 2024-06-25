
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

lista_preferencias = cargar_preguntas()

system("cls")

moneda_base = 0

while True:
    opcion = elegir_opcion()
    match opcion:
        case "1":
            preguntas_respuestas(lista_preferencias)
        case "2":
            print("Gracias por escogernos.")
            print("Saliendo del programa..")
            break
        case  _:
            print("\n- Seleccione una opcion valída.\n")