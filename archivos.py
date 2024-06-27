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

# Archivo CSV para acumular y cargar preguntas
lista_preferencias = [{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver el amanecer", "Ver el atardecer"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser invisible", "Poder volar"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Tener siempre razón", "Tener siempre la última palabra"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["No volver a dormir", "No volver a comer"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Viajar por el mundo", "Quedarte en tu ciudad"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser rico", "Ser feliz"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["No tener internet", "No tener teléfono"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver una serie completa", "Leer una saga completa"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Vivir en una mansión", "Vivir en una cabaña en el bosque"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser el protagonista de una película", "Ser el director de una película"]}
]

# Función para guardar las preguntas en un archivo CSV
def guardar_preguntas():
    with open('Preguntas.csv','w', encoding = 'utf-8') as archivo:
        archivo.write('Pregunta,Opciones\n')
        for pregunta in lista_preferencias:
            opciones = ','.join(pregunta["Opciones"])
            archivo.write(f'{pregunta["Pregunta"]},{opciones}\n')

# Leer las preguntas desde un archivo CSV
def leer_preguntas(lista_preferencias):
    lista_preferencias = []
    with open('Preguntas.csv','r', encoding = 'utf-8') as archivo:
        for linea in archivo:
            pregunta = linea.strip().split(',')
            opciones_str = linea.strip()
            opciones = opciones_str.split(',')
            pregunta_dict = {"Pregunta": pregunta, "Opciones": opciones}
            lista_preferencias.append(pregunta_dict)
    
    return lista_preferencias