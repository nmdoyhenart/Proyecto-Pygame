import random

lista_preguntas = [
    {
        "Pregunta": "¿Cual es la capital de Argentina?",
        "Opciones": ["La plata", "Buenos aires"],
        "Correcta": 2
    },
    {
        "Pregunta": "¿Cuanto es 2 + 2?",
        "Opciones": ["3", "4"],
        "Correcta": 2       
    },
    {
        "Pregunta": "¿Cuál es la capital de España?",
        "Opciones": ["Madrid", "Barcelona"],
        "Correcta": 1
    },
    {
        "Pregunta": "¿Cuánto es 5 * 6?",
        "Opciones": ["30", "35"],
        "Correcta": 2       
    },
    {
        "Pregunta": "¿Cuál es el río más largo del mundo?",
        "Opciones": ["Nilo", "Misisipi"],
        "Correcta": 1        
    },
    {
        "Pregunta": "¿Quién escribió 'Cien años de soledad'?",
        "Opciones": ["Gabriel García Márquez", "Jorge Luis Borges"],
        "Correcta": 1        
    },
    {
        "Pregunta": "¿Cuál es el resultado de 7 + 8?",
        "Opciones": ["15", "16"],
        "Correcta": 1        
    },
    {
        "Pregunta": "¿Qué país tiene la mayor población del mundo?",
        "Opciones": ["India", "Estados Unidos"],
        "Correcta": 1        
    },
    {
        "Pregunta": "¿Cuál es el idioma oficial de Brasil?",
        "Opciones": ["Español", "Portugués"],
        "Correcta": 2        
    },
    {
        "Pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "Opciones": ["1937", "1939"],
        "Correcta": 2       
    }
]

def preguntas_respuestas(lista_preguntas: list):
    aleatoria = random.randint(0, len(lista_preguntas) - 1)
    pregunta_seleccionada = lista_preguntas[aleatoria]
    
    print(pregunta_seleccionada["Pregunta"])
    for i in range(len(pregunta_seleccionada["Opciones"])):
        print(f"{i + 1}. {pregunta_seleccionada['Opciones'][i]}")
    
    respuesta = int(input("Seleccione la respuesta (1 o 2): "))
    
    while respuesta not in [1, 2]:
        if respuesta not in [1, 2]:
            print("Seleccione una opcion existente.")
            respuesta = int(input("Seleccione la respuesta (1 o 2): "))
    
    if respuesta == pregunta_seleccionada["Correcta"]:
        print("¡Correcto!")
    else:
        print("Incorrecto. La respuesta correcta era:", pregunta_seleccionada["Opciones"][pregunta_seleccionada["Correcta"] - 1])

preguntas_respuestas(lista_preguntas)