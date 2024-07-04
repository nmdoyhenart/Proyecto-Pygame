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


def preguntas_respuestas(lista_preferencias: list):
    monedas = 0
    lista_puntos = cargar_puntos()
    ingreso_juego = True

    while ingreso_juego:
        for i in range(len(lista_preferencias)):
            aleatoria = random.randint(0, len(lista_preferencias) - 1)
            pregunta_seleccionada = lista_preferencias[aleatoria]
            
            print(pregunta_seleccionada["Pregunta"])
            for j in range(len(pregunta_seleccionada["Opciones"])):
                print(f"{j + 1}. {pregunta_seleccionada['Opciones'][j]}")
            
            respuesta = int(input("Seleccione la respuesta (1 o 2): "))
            
            while respuesta not in [1, 2]:
                print("Seleccione una opción existente.")
                respuesta = int(input("Seleccione la respuesta (1 o 2): "))
            
            respuesta_publico = random.randint(1, 2)

            if respuesta == respuesta_publico:
                monedas = monedas_incrementales(PUNTOS, monedas)
                print(f"\n¡Respuesta correcta! Usted suma {monedas} monedas!!\n")
            else:
                print("\nNo coincidiste con el público.")
                print(f"Ha recaudado {monedas} monedas.")
                if not preguntar_seguir_jugando():
                    ingreso_juego = False
                    break
        
        lista_puntos.append(monedas)
        guardar_puntos(lista_puntos)

def preguntar_seguir_jugando():
    aux = True
    while aux:
        continuar = input("¿Desea jugar otra vez? (si/no): ").lower().strip()
        if continuar == 'si':
            break



# def decisiones_jueces():
#     respuestas = [ROJO, AZUL]
#     lista_decisiones = []
#     for i in range(11):
#         decision = random.randint(0, 1)
#         lista_decisiones.append(respuestas[decision])
#     return lista_decisiones

# def jueces_funcion(decision: list[tuple]):
#     decision_x = 40
#     decision_y = 40
#     coordenada_x = 100
#     coordenada_y = 370
#     personajes = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\guampa.png")
#     personajes = pygame.transform.scale(personajes, (100, 150))

#     midecision = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
#     midecision = pygame.transform.scale(midecision, (decision_x,decision_y))

#     for i in range(5):
#         if coordenada_x <= 500:
#             try:
#                 if decision[0] is ROJO or decision[0] is AZUL:
#                     decisiones = pygame.Rect(coordenada_x + 30, coordenada_y, decision_x, decision_y)
#                     decisiones_2 = pygame.Rect(coordenada_x + 30, coordenada_y - 100, decision_x, decision_y)
#                     pygame.draw.rect(ventana, decision[i], decisiones)
#                     pygame.draw.rect(ventana, decision[i + 5], decisiones_2)
#             except:
#                 ventana.blit(midecision, (coordenada_x + 30, coordenada_y, decision_x, decision_y))
#                 ventana.blit(midecision, (coordenada_x + 30, coordenada_y -100, decision_x, decision_y))

#             ventana.blit(personajes, (coordenada_x, 200))
#             ventana.blit(personajes, (coordenada_x, 300))

#             coordenada_x += 100
#         else:
#             coordenada_x = 100
