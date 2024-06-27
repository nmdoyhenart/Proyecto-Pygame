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

def preguntas_respuestas(lista_preferencias: list):
    monedas = 0
    lista_puntos = cargar_puntos()
    ingreso_juego = True

    while ingreso_juego:
        for i in range(len(lista_preferencias)):
            aleatoria = random.randint(0, len(lista_preferencias) - 1)
            pregunta_seleccionada = lista_preferencias[aleatoria]
            
            print(pregunta_seleccionada["Pregunta"])
            for j in range(len(pregunta_seleccionada["Opciones"])):
                print(f"{j + 1}. {pregunta_seleccionada['Opciones'][j]}")
            
            respuesta = int(input("Seleccione la respuesta (1 o 2): "))
            
            while respuesta not in [1, 2]:
                print("Seleccione una opción existente.")
                respuesta = int(input("Seleccione la respuesta (1 o 2): "))
            
            respuesta_publico = random.randint(1, 2)

            if respuesta == respuesta_publico:
                monedas = monedas_incrementales(PUNTOS, monedas)
                print(f"\n¡Respuesta correcta! Usted suma {monedas} monedas!!\n")
            else:
                print("\nNo coincidiste con el público.")
                print(f"Ha recaudado {monedas} monedas.")
                if not preguntar_seguir_jugando():
                    ingreso_juego = False
                    break
        
        lista_puntos.append(monedas)
        guardar_puntos(lista_puntos)

def preguntar_seguir_jugando():
    aux = True
    while aux:
        continuar = input("¿Desea jugar otra vez? (si/no): ").lower().strip()
        if continuar == 'si':
            break