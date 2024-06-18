from modulo_preguntas import *
import random

puntos = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]

def monedas_incrementales(puntos: list, monedas_base: int):
    posicion = random.randint(0, len(puntos))
    print(posicion)

    monedas_base += puntos[posicion]
    print(monedas_base)
    return monedas_base