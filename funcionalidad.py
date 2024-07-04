"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
from archivos import *
import random

PUNTOS = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]

def monedas_incrementales(puntos: list, monedas_base: int, posicion: int):
    monedas_base += puntos[posicion - 1]
    return monedas_base
    
    return monedas_base