"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import random

puntos = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]

def monedas_incrementales(puntos: list, monedas_base: int):
    posicion = random.randint(0, len(puntos) - 1)
    monedas_base += puntos[posicion]
    return monedas_base

def preguntas_respuestas(lista_preguntas: list):
    aleatoria = random.randint(0, len(lista_preguntas) - 1)
    pregunta_seleccionada = lista_preguntas[aleatoria]
    
    print(pregunta_seleccionada["Pregunta"])
    for i in range(len(pregunta_seleccionada["Opciones"])):
        print(f"{i + 1}. {pregunta_seleccionada['Opciones'][i]}")
    
    respuesta = int(input("Seleccione la respuesta (1 o 2): "))
    
    while respuesta not in [1, 2]:
        print("Seleccione una opción existente.")
        respuesta = int(input("Seleccione la respuesta (1 o 2): "))
    
    if respuesta == pregunta_seleccionada["Correcta"]:
        moneda = monedas_incrementales(puntos, 0)  # Inicializar monedas_base en 0 y actualizar con puntos
        print(f"¡Respuesta correcta! Usted suma {moneda} monedas.")
    else:
        print("Incorrecto. La respuesta correcta era:", pregunta_seleccionada["Opciones"][pregunta_seleccionada["Correcta"] - 1])