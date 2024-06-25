"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
from archivos import *
import random

PUNTOS = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]

def monedas_incrementales(puntos: list, monedas_base: int):
    posicion = random.randint(0, len(puntos) - 1)
    monedas_base += puntos[posicion]
    return monedas_base

def preguntas_respuestas(lista_preguntas: list):
    monedas = 0
    lista_puntos = cargar_puntos()
    for i in range(len(lista_preguntas)):
        aleatoria = random.randint(0, len(lista_preguntas) - 1)
        pregunta_seleccionada = lista_preguntas[aleatoria]
        
        print(pregunta_seleccionada["Pregunta"])
        for j in range(len(pregunta_seleccionada["Opciones"])):
            print(f"{j + 1}. {pregunta_seleccionada['Opciones'][j]}")
        
        respuesta = int(input("Seleccione la respuesta (1 o 2): "))
        
        while respuesta not in [1, 2]:
            print("Seleccione una opción existente.")
            respuesta = int(input("Seleccione la respuesta (1 o 2): "))
        
        if respuesta == pregunta_seleccionada["Correcta"]:
            monedas = monedas_incrementales(PUNTOS, monedas)
            print(f"¡Respuesta correcta! Usted suma {monedas} monedas!!.")
        else:
            print("Incorrecto. La respuesta correcta era:", pregunta_seleccionada["Opciones"][pregunta_seleccionada["Correcta"] - 1])
            print(f"Usted ha sido descalificado del juego")
            print(f"Ha recaudado {monedas} monedas.")
            break
    
    lista_puntos.append(monedas)
    guardar_puntos(lista_puntos)

# lista_puntos = []

# def monedas_incrementales(puntos: list, monedas_base: int):
#     posicion = random.randint(0, len(puntos) - 1)
#     monedas_base += puntos[posicion]

#     return monedas_base

# def preguntas_respuestas(lista_preguntas: list):
#     monedas = 0
#     for i in range(len(lista_preguntas)):
#         aleatoria = random.randint(0, len(lista_preguntas) - 1)
#         pregunta_seleccionada = lista_preguntas[aleatoria]
        
#         print(pregunta_seleccionada["Pregunta"])
#         for i in range(len(pregunta_seleccionada["Opciones"])):
#             print(f"{i + 1}. {pregunta_seleccionada['Opciones'][i]}")
        
#         respuesta = int(input("Seleccione la respuesta (1 o 2): "))
        
#         while respuesta not in [1, 2]:
#             print("Seleccione una opción existente.")
#             respuesta = int(input("Seleccione la respuesta (1 o 2): "))
        
#         if respuesta == pregunta_seleccionada["Correcta"]:
#             monedas = monedas_incrementales(puntos, monedas)
#             lista_puntos.append(monedas)
#             print(f"¡Respuesta correcta! Usted suma {monedas} monedas!!.")
#         else:
#             print("Incorrecto. La respuesta correcta era:", pregunta_seleccionada["Opciones"][pregunta_seleccionada["Correcta"] - 1])
#             print(f"Usted ha sido descalificado del juego")
#             print(f"Ha recaudado {monedas} monedas.")