"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import json
# Archivo JSON para acumular y cargar los puntos

def cargar_puntos():
    """Carga los puntos del archivo JSON una vez que lo encuentra.

    Args:
        -
    """
    try:
        with open("Puntos.json", "r") as archivo:
            aux = json.load(archivo)
            return aux["Puntos"]
    except FileNotFoundError:
        return []

def guardar_puntos(puntos_existentes: list):
    """Almacena los puntos en el archivo JSON, agregando los nuevos puntos a los existentes.

    Args:
        puntos_existentes: list: Lista donde se encuentran los datos.
    """
   
    puntos_dict = {"Puntos": puntos_existentes}
    with open("Puntos.json", "w") as archivo:
        json.dump(puntos_dict, archivo, indent=4)


# Función para guardar las preguntas en un archivo CSV
def guardar_preguntas(lista: list, nombre_archivo: str):
    """Creacion de preguntas y opciones en un archivo CSV

    Args:
        lista: list: Lista que almacena, nombre_archivo: str: String
    """
    with open(nombre_archivo, 'w', newline='', encoding ='utf-8') as archivo:
        archivo.write('Pregunta,Opciones\n')
        for elemento in lista:
            opciones = ','.join(elemento['Opciones'])
            archivo.write(f"{elemento['Pregunta']},{opciones}\n")

def leer_preguntas(nombre_archivo: str)-> list[dict]:
    """Lectura del archivo CSV.

    Args:
        (nombre_archivo: str)-> list[dict], un string que devuelve una lista con un diccionario.
    """
    lista_leida = []
    with open(nombre_archivo, 'r', encoding ='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            pregunta, opciones_uno, opciones_dos = linea.strip().split(',')
            lista_leida.append({"Pregunta": pregunta, "Opciones": [opciones_uno, opciones_dos]})

    return lista_leida