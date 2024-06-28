"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
from evento2 import *
from especificas_eventos import *
from modulo_preguntas import *
from archivos import *
import random

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (128, 191, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)
ROJO_CLARO = (255, 150, 136)

tupla = (ROJO, AZUL)


PUNTOS = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]

lista_preferencias = [{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver el amanecer", "Ver el atardecer"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser invisible", "Poder volar"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Tener siempre razón", "Tener siempre la última palabra"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["No volver a dormir", "No volver a comer"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Viajar por el mundo", "Quedarte en tu ciudad"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser rico", "Ser feliz"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["No tener internet", "No tener teléfono"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver una serie completa", "Leer una saga completa"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Vivir en una mansión", "Vivir en una cabaña en el bosque"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser el protagonista de una película", "Ser el director de una película"]}, {"Pregunta": "¿Qué prefieres?", "Opciones": ["Nadar en el mar", "Nadar en un lago"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Escuchar música rock", "Escuchar música clásica"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Bailar salsa", "Bailar hip-hop"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Comer pizza", "Comer sushi"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Jugar al fútbol", "Jugar al baloncesto"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Visitar museos de arte", "Visitar museos de historia"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Montar en bicicleta", "Montar en moto"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Leer novelas de ciencia ficción", "Leer novelas de misterio"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Tomar té", "Tomar café"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Aprender un nuevo idioma", "Aprender a tocar un instrumento musical"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ir al cine", "Ir al teatro"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Cantar en la ducha", "Bailar en la ducha"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Caminar por la playa al amanecer", "Caminar por la montaña al atardecer"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Practicar yoga", "Practicar pilates"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Hacer senderismo", "Hacer escalada"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver una película de comedia", "Ver una película de terror"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ir de compras", "Ir de excursión"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Jugar videojuegos", "Jugar juegos de mesa"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Hacer ejercicio al aire libre", "Hacer ejercicio en el gimnasio"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Preparar comida italiana", "Preparar comida asiática"]}]

guardar_preguntas(lista_preferencias, "Preguntas.csv")

ANCHO_VENTANA = 700
ALTO_VENTANA = 900

VENTANA1 = (ANCHO_VENTANA, ALTO_VENTANA)

pygame.init()

FUENTE = pygame.font.Font(None, 36)


ventana = pygame.display.set_mode(VENTANA1)
pygame.display.set_caption("Tot or trivia")

icono = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\logo.jpg")
pygame.display.set_icon(icono)





# incognita = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
# incognita = pygame.transform.scale(incognita, (40, 40))


color = ROJO
color_inactivo = AZUL
color_activo = ROJO
color = color_inactivo
activo = False
texto = ""

def fondo():
    fondo = pygame.image.load(r"TP-PYGAME-COLLAB-main/recursos/fondo.jpg")
    fondo = pygame.transform.scale(fondo, VENTANA1)

    ventana.blit(fondo, (0, 0))    

def tribuna():
    tribuna = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\tribuna_mejorada.png")
    tribuna = pygame.transform.scale(tribuna, (600, 500))
    ventana.blit(tribuna, (50, 20))

def decisiones_jueces():
    respuestas = [ROJO, AZUL]
    lista_decisiones = [AZUL]
    for i in range(9):
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
            
            try:
                if decision[0] is ROJO or decision[0] is AZUL:
                    decisiones = pygame.Rect(coordenada_x + 30, coordenada_y, decision_x, decision_y)
                    decisiones_2 = pygame.Rect(coordenada_x + 30, coordenada_y - 100, decision_x, decision_y)
                    pygame.draw.rect(ventana, decision[i], decisiones)
                    pygame.draw.rect(ventana, decision[i + 5], decisiones_2)
            
            except:
                ventana.blit(midecision, (coordenada_x + 30, coordenada_y, decision_x, decision_y))
                ventana.blit(midecision, (coordenada_x + 30, coordenada_y -100, decision_x, decision_y))



            ventana.blit(personajes, (coordenada_x, 200))
            ventana.blit(personajes, (coordenada_x, 300))

            coordenada_x += 100
        else:
            coordenada_x = 100
       

def button_tot():
    #Todo lo relacionado con el button de this or that
    input_tot = pygame.Rect(275, 750, 150, 90)

    texto_superficie = FUENTE.render("This or that", True, BLANCO)
    pygame.draw.rect(ventana, color, input_tot)
    ventana.blit(texto_superficie, (input_tot.x + 5, input_tot.y + 5))
    #pygame.draw.rect(ventana, color, input_tot, 2)

def monedas_contador(monedas_base):
    #Todo lo relacionado con el contador d monedas
    monedas = pygame.Rect(ANCHO_VENTANA - 100, 80, 100, 30)
    moneda_icon = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\moneda.png")
    moneda_icon = pygame.transform.scale(moneda_icon, (40, 30))


    texto_monedas = FUENTE.render(str(monedas_base), True, BLANCO)
    pygame.draw.rect(ventana, NEGRO, monedas, 0)
    ventana.blit(texto_monedas, (monedas.x , monedas.y ))
    ventana.blit(moneda_icon, (ANCHO_VENTANA - 35, 80))

def vuelta():
    punto_vuelta = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\X_vuelta.png")
    punto_vuelta= pygame.transform.scale(punto_vuelta , (30, 30))

    
    ventana.blit(punto_vuelta, (ANCHO_VENTANA - 35, ALTO_VENTANA - 35))


def mi_personaje():
    x_personaje = 150
    y_personaje = 150
    personajes = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\guampa.png")
    personajes = pygame.transform.scale(personajes, (400, 600))
    ventana.blit(personajes,(x_personaje, y_personaje))

def decision_personaje(estado, color):
    if estado:
        midecision = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
        midecision = pygame.transform.scale(midecision, (160,140))
        ventana.blit(midecision, (150 + 115, 150 + 280))
    else:
        mi_decision = pygame.Rect(150 + 115, 150 + 280, 160,140)
        pygame.draw.rect(ventana, color, mi_decision)

def botones_azul_rojo(opcion_azul: str, opcion_roja: str):
    x = 100
    y = 650
    boton_altura = 90
    boton_ancho = 250
    # def texto(opcion_azul, boton_ancho, x, y):
    #     largo_pixel = FUENTE.size(opcion_azul)
    #     textoooo = ""
    #     largo_text = 0
    #     if largo_pixel[0] > (boton_ancho - 10):
    #         texto_dividido = opcion_azul.split()
    #         contado = 0
    #         for i in range (len(texto_dividido)):
    #             largo_text += FUENTE.size(texto_dividido[i])[0]
    #             textoooo += f"{texto_dividido[i]} "
    #             if largo_text >= (boton_ancho - 15) and contado == 0:
    #                 contado += 1
    #                 texto_2 = textoooo
    #                 textoooo = f""

    #         texto_superficie = FUENTE.render(f"{texto_2}", True, BLANCO)
    #         ventana.blit(texto_superficie, (x , y ))
    #         texto_superficie_2 = FUENTE.render(f"{textoooo}", True, BLANCO)
    #         ventana.blit(texto_superficie_2, (x, (y + 36)))

    #     else:
    #         texto_superficie_2 = FUENTE.render(f"{opcion_azul}", True, BLANCO)
    #         ventana.blit(texto_superficie_2, (x, y))
        

    rojo = pygame.Rect(x, y, boton_ancho, boton_altura)
    pygame.draw.rect(ventana, ROJO, rojo)
    pygame.draw.rect(ventana, NEGRO, rojo, 2)
    texto_superficie = FUENTE.render(f"{opcion_roja}", True, NEGRO)
    ventana.blit(texto_superficie, (rojo.x + 5, rojo.y + 5))

    azul = pygame.Rect(x + boton_ancho, y, boton_ancho, boton_altura)
    pygame.draw.rect(ventana, AZUL_CLARO, azul)
    pygame.draw.rect(ventana, NEGRO, azul, 2)
    #texto(opcion_azul, boton_ancho, azul.x + 5, azul.y + 5)
    texto_superficie = FUENTE.render(f"{opcion_azul}", True, BLANCO)
    ventana.blit(texto_superficie, (azul.x + 5, azul.y + 5))

def texto_pregunta(pregunta: str):
    ancho = 500
    alto = 50
    x = 100
    y = 600
    cuadro_preg = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(ventana, GRIS, cuadro_preg)
    pygame.draw.rect(ventana, NEGRO, cuadro_preg, 2)
    texto_preg = FUENTE.render(f"{pregunta}", True, NEGRO)
    ventana.blit(texto_preg, (x + 3, y + 15))












bandera = True
monedas_base = 0
estado = "principal"
boton_decision = True
color_decision = None
preguntas = leer_preguntas("Preguntas.csv")

clock = pygame.time.Clock()

while bandera:
    for evento in pygame.event.get():
        try:
            if estado == "principal":
                #Dependiendo del estado del juego, se habilitan los botones o no
                input_tot = pygame.Rect(275, 750, 150, 90)
            elif estado == "segundo estado":
                punto_vuelta = pygame.Rect(ANCHO_VENTANA - 35, ALTO_VENTANA - 35, 30, 30)
                button_rojo = pygame.Rect(180, 650, 150, 90)
                button_azul = pygame.Rect(180 + 180, 650, 150, 90)

            if evento.type == pygame.QUIT:
                #Salida del juego por la "X" 
                bandera = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                #Cuando detecta que se apreta en click izq del mouse, 
                #elige como proseguir dependiendo donde toco(que boton)
                if input_tot.collidepoint(evento.pos):
                    estado = "segundo estado"
                    pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
                    pregunta_resp = preguntas[pregunta_aleatoria]

                elif punto_vuelta.collidepoint(evento.pos):
                    estado = "principal"
                    boton_decision = True

                elif button_rojo.collidepoint(evento.pos) or button_azul.collidepoint(evento.pos):
                    boton_decision = False
                    estado = "tercer estado"
                    lista_jueces = decisiones_jueces()

                    if button_rojo.collidepoint(evento.pos):
                        color_decision = ROJO
                    else:
                        color_decision = AZUL
        except:
            pass
        
        
        
    """Esta parte llama a las funciones que se encargan de ilustrar los botones, fondo, y partes
    visuales del programa. Esto dependiendo del estado en que este el programa."""
    fondo()
    if estado == "principal":
        tribuna()
        jueces_funcion(None)
        button_tot()
    elif estado == "segundo estado":
        decision_personaje(boton_decision, color_decision)
        mi_personaje()
        
        texto_pregunta(pregunta_resp["Pregunta"])
        botones_azul_rojo(pregunta_resp["Opciones"][0], pregunta_resp["Opciones"][1])
        
    elif estado == "tercer estado":
        tribuna()
        jueces_funcion(lista_jueces)
        vuelta()
        

    monedas_contador(monedas_base)

    
    clock.tick(20)
    pygame.display.flip()

pygame.quit()
