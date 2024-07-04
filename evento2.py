"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import random
from evento1 import *

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)

tupla = (ROJO, AZUL)

color_aleateorio = random.choice(tupla)


def decisiones_jueces():
    respuestas = [ROJO, AZUL]
    lista_decisiones = []
    for i in range(10):
        decision = random.randint(0, 1)
        lista_decisiones.append(respuestas[decision])
    return lista_decisiones

def jueces_funcion(decision: list[tuple]):
    decision_x = 40
    decision_y = 40
    coordenada_x = 100
    coordenada_y = 370
    personajes = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\guampa.png")
    personajes = pygame.transform.scale(personajes, (100, 150))

    midecision = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
    midecision = pygame.transform.scale(midecision, (decision_x,decision_y))

    for i in range(5):
        if coordenada_x <= 500:
            
                if decision[0] is ROJO or decision[0] is AZUL:
                    decisiones = pygame.Rect(coordenada_x + 30, coordenada_y, decision_x, decision_y)
                    # decisiones_2 = pygame.Rect(coordenada_x + 30, coordenada_y - 100, decision_x, decision_y)
                    pygame.draw.rect(ventana, decision[i], decisiones)
            #        pygame.draw.rect(ventana, decision[i + 5], decisiones_2)
            
                ventana.blit(midecision, (coordenada_x + 30, coordenada_y, decision_x, decision_y))
                ventana.blit(midecision, (coordenada_x + 30, coordenada_y -100, decision_x, decision_y))

            ventana.blit(personajes, (coordenada_x, 200))
            # ventana.blit(personajes, (coordenada_x, 300))

            coordenada_x += 100
        else:
            coordenada_x = 100
