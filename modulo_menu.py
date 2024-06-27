"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
from os import system
from funcionalidad import *

def elegir_opcion():
    opcion = input("""Bienvenido al juego "This or that"\n1- Jugar\n2- Salir\n
Elija una opción: """)

    return opcion

leer_preguntas(lista_preferencias)

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