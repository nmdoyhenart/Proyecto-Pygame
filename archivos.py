"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import json
# Archivo JSON para acumular y cargar los puntos

def cargar_puntos(path):
    """Carga los puntos del archivo JSON una vez que lo encuentra.

    Args:
        -
    """
    try:
        with open(path, "r") as archivo:
            aux = json.load(archivo)
            return aux["Puntos"]
    except FileNotFoundError:
        return []
    

def guardar_puntos(path ,puntos_existentes: list):
    """Almacena los puntos en el archivo JSON, agregando los nuevos puntos a los existentes.

    Args:
        lista_puntos (list): Lista donde se encuentran los datos, cada uno siendo una tupla con un string y un entero.
    """
   
    puntos_dict = {"Puntos": puntos_existentes}
    with open(path, "w") as archivo:
        json.dump(puntos_dict, archivo, indent=4)


# Función para guardar las preguntas en un archivo CSV
def guardar_preguntas(lista: list, nombre_archivo: str):
    """Creacion de preguntas y opciones en un archivo CSV

    Args:
        lista: list: Lista que guarda elementos, nombre_archivo: str: String
    """
    with open(nombre_archivo, 'w', newline='', encoding ='utf-8') as archivo:
        for elemento in lista:
            archivo.write(f"{elemento[0]},{elemento[1]},{elemento[2]}\n")


def leer_preguntas(nombre_archivo: str)-> list[dict]:
    """Lectura del archivo CSV.

    Args:
        nombre_archivo: str -> list[dict], un Str que devuelve una lista con un diccionario
    """
    lista_leida = []
    with open(nombre_archivo, 'r', encoding ='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            preguntas_opciones = linea.strip().split(',')
            lista_leida.append(preguntas_opciones)

    return lista_leida

