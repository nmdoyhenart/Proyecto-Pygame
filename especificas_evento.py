"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
from elementos import *

def monedas_incrementales(puntos: list, monedas_base: int, posicion: int):
    """Actualiza constantemente las monedas haciendolas incrementales.

    Args:
        puntos: list: Lista donde se guardan los puntos, monedas_base: int: Numerico, posicion: int: Numerico.
    """
    monedas_base += puntos[posicion - 1]
    return monedas_base

def jueces_decision(decision: list):
    """Cuenta los colores asigandos aleatoriamente.

    Args:
        decision: list: Lista que contiene la decisión final  
    """
    contador_rojo = 0
    contador_azul = 0
    for elementos in decision:
        if elementos == ROJO:
            contador_rojo += 1
        else:
            contador_azul += 1
    if contador_rojo > contador_azul:
        retorna = ROJO
    else:
        retorna = AZUL
    return retorna

def comprobacion(voto_jueces: list, mi_decision: tuple):
    color_decidido = jueces_decision(voto_jueces)
    if color_decidido == mi_decision:
        retorna = True
    else:
        retorna = False
    return retorna

def porcentaje_decision(decision: list):
    """Calcula el porcentaje de decisión de los jueces

    Args:
        decision: list: Lista que contiene la decisión final  
    """
    contador_rojo = 0
    contador_azul = 0
    for elementos in decision:
        if elementos == ROJO:
            contador_rojo += 1
        else:
            contador_azul += 1
    
    porcentaje_azul = (contador_azul * 100) // 5
    porcentaje_rojo = (contador_rojo * 100) // 5

    return (porcentaje_azul, porcentaje_rojo)