"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import json
# Archivo JSON para acumular los puntos

def cargar_puntos():
    try:
        with open("puntos.json", "r") as file:
            return json.load(file)
    except:
        return []

def guardar_puntos(lista_puntos):
    with open("puntos.json", "w") as file:
        json.dump(lista_puntos, file)