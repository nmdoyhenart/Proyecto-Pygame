"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import json
# Archivo JSON para acumular y cargar los puntos
# Cargar puntos
def cargar_puntos():
    try:
        with open("Puntos.json", "r", encoding ='utf-8') as archivo:
            aux = json.load(archivo)
            return aux["Puntos"]
    except (FileNotFoundError):
        return []
    except (json.JSONDecoder):
        return []

# Guardar puntos
def guardar_puntos(lista_puntos: list):
    puntos_dict = {"Puntos": lista_puntos}
    with open("Puntos.json", "w", encoding ='utf-8') as archivo:
        json.dump(puntos_dict, archivo, indent = 4, ensure_ascii = False)


# Función para guardar las preguntas en un archivo CSV
def guardar_preguntas(lista, nombre_archivo):
    with open(nombre_archivo, 'w', newline='', encoding ='utf-8') as archivo:
        archivo.write('Pregunta,Opciones\n')
        for elemento in lista:
            opciones = ','.join(elemento['Opciones'])
            archivo.write(f"{elemento['Pregunta']},{opciones}\n")

def leer_preguntas(nombre_archivo)-> list[dict]:
    lista_leida = []
    with open(nombre_archivo, 'r', encoding ='utf-8') as archivo:
        lineas = archivo.readlines()
        # el [1:] salta la primera línea que es la cabecera
        for linea in lineas[1:]:
            pregunta, opciones_uno, opciones_dos = linea.strip().split(',')
            lista_leida.append({"Pregunta": pregunta, "Opciones": [opciones_uno, opciones_dos]})
    return lista_leida
