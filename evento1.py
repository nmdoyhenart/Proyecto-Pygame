"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
import random
from evento2 import *
from especificas_eventos import *
from modulo_preguntas import *
from archivos import *

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (128, 191, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)
ROJO_CLARO = (255, 150, 136)

tupla = (ROJO, AZUL)

lista_puntos = []
cargar_puntos()

PUNTOS = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]

lista_preferencias = [{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver el amanecer", "Ver el atardecer"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser invisible", "Poder volar"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Tener siempre razón", "Tener siempre la última palabra"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["No volver a dormir", "No volver a comer"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Viajar por el mundo", "Quedarte en tu ciudad"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser rico", "Ser feliz"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["No tener internet", "No tener teléfono"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver una serie completa", "Leer una saga completa"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Vivir en una mansión", "Vivir en una cabaña en el bosque"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser el protagonista de una película", "Ser el director de una película"]}, {"Pregunta": "¿Qué prefieres?", "Opciones": ["Nadar en el mar", "Nadar en un lago"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Escuchar música rock", "Escuchar música clásica"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Bailar salsa", "Bailar hip-hop"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Comer pizza", "Comer sushi"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Jugar al fútbol", "Jugar al baloncesto"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Visitar museos de arte", "Visitar museos de historia"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Montar en bicicleta", "Montar en moto"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Leer novelas de ciencia ficción", "Leer novelas de misterio"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Tomar té", "Tomar café"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Aprender un nuevo idioma", "Aprender a tocar un instrumento musical"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ir al cine", "Ir al teatro"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Cantar en la ducha", "Bailar en la ducha"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Caminar por la playa al amanecer", "Caminar por la montaña al atardecer"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Practicar yoga", "Practicar pilates"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Hacer senderismo", "Hacer escalada"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver una película de comedia", "Ver una película de terror"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ir de compras", "Ir de excursión"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Jugar videojuegos", "Jugar juegos de mesa"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Hacer ejercicio al aire libre", "Hacer ejercicio en el gimnasio"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Preparar comida italiana", "Preparar comida asiática"]}]

guardar_preguntas(lista_preferencias, "Preguntas.csv")

ANCHO_VENTANA = 700
ALTO_VENTANA = 700

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
    lista_decisiones = []
    for i in range(11):
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
    

def jueces_decision(decision: list):
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

def comprobacion(voto_jueces, mi_decision):
    color_decidido = jueces_decision(voto_jueces)
    if color_decidido == mi_decision:
        retorna = True
    else:
        retorna = False
    return retorna


def button_tot():
    #Todo lo relacionado con el button de this or that
    input_tot = pygame.Rect(275, 500, 150, 90)

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
    y = 600
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

def comodines(ventana, comodin_uno_flag, comodin_dos_flag, comodin_tres_flag):
    x_caja = 10
    y_caja = 500
    ancho_comodin = 30
    alto_comodin = 30
    x_comodin1 = x_caja
    y_comodin1 = y_caja
    x_comodin2 = x_caja
    y_comodin2 = y_comodin1 + alto_comodin + 10
    x_comodin3 = x_caja
    y_comodin3 = y_comodin2 + alto_comodin + 10

    if comodin_uno_flag:
        comodin1 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\half.png")
        comodin1 = pygame.transform.scale(comodin1, (ancho_comodin, alto_comodin))
        ventana.blit(comodin1, (x_comodin1, y_comodin1))
    else:
        comodin1 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
        comodin1 = pygame.transform.scale(comodin1, (ancho_comodin, alto_comodin))
        ventana.blit(comodin1, (x_comodin1, y_comodin1))

    if comodin_dos_flag:
        comodin2 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\skip.png")
        comodin2 = pygame.transform.scale(comodin2, (ancho_comodin, alto_comodin))
        ventana.blit(comodin2, (x_comodin2, y_comodin2))
    else:
        comodin2 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
        comodin2 = pygame.transform.scale(comodin2, (ancho_comodin, alto_comodin))
        ventana.blit(comodin2, (x_comodin2, y_comodin2))

    if comodin_tres_flag:
        comodin3 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\meidaluna.png")
        comodin3 = pygame.transform.scale(comodin3, (ancho_comodin, alto_comodin))
        ventana.blit(comodin3, (x_comodin3, y_comodin3))
    else:
        comodin3 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
        comodin3 = pygame.transform.scale(comodin3, (ancho_comodin, alto_comodin))
        ventana.blit(comodin3, (x_comodin3, y_comodin3))



def texto_pregunta(pregunta: str):
    ancho = 500
    alto = 50
    x = 100
    y = 550
    cuadro_preg = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(ventana, GRIS, cuadro_preg)
    pygame.draw.rect(ventana, NEGRO, cuadro_preg, 2)
    texto_preg = FUENTE.render(f"{pregunta}", True, NEGRO)
    ventana.blit(texto_preg, (x + 3, y + 15))

def tiempo(contador, limite_tiempo, fps):
    time_x = 5
    time_y = 5
    time_ancho = 40
    time_alto = 30
    temporizador = pygame.Rect(time_x, time_y, time_ancho, time_alto)
    pygame.draw.rect(ventana, NEGRO, temporizador)
    text_tiempo = FUENTE.render(f"{contador // 20}", True, BLANCO)
    ventana.blit(text_tiempo, (time_x + 10, time_y + 5))
    retorna = False
    if (contador // fps) >= limite_tiempo:
        retorna = True
    return retorna
    
def fuera_de_tiempo():
    eliminado_x = 200
    eliminado_y = 350
    eliminado_ancho = 400
    eliminado_alto = 35
    eliminacion_cuadro = pygame.Rect(eliminado_x, eliminado_y, eliminado_ancho, eliminado_alto)
    pygame.draw.rect(ventana, NEGRO, eliminacion_cuadro)
    text_eliminacion = FUENTE.render(f"Usted ha excedido el tiempo y perdio.", True, BLANCO)
    ventana.blit(text_eliminacion, (eliminado_x + 10, eliminado_y + 5))

def pantalla_eliminado():
    eliminado_ancho = 400
    eliminado_alto = 200

    eliminado_x = 150
    eliminado_y = 250

    aviso_eliminado = pygame.Rect(eliminado_x, eliminado_y, eliminado_ancho, eliminado_alto)
    pygame.draw.rect(ventana, NEGRO, aviso_eliminado)
    texto_eliminado = FUENTE.render(f"PERDISTE :P", False, BLANCO)
    ventana.blit(texto_eliminado, (eliminado_x + 100, eliminado_y + 82))

def tiempo_espera(contador_espera, limite,fps):
    retorna = False
    if (contador_espera // fps) >= limite:
        retorna = True
    return retorna
    


bandera = True
monedas_base = 0
respuestas_correctas = 0
estado = "principal"
boton_decision = True
color_decision = None
preguntas = leer_preguntas("Preguntas.csv")
contador_comodin_dos = 0
contador_espera = 0
comodin_uno = True
comodin_dos = True
comodin_tres = True
bandera_espera = False
fps = 20

clock = pygame.time.Clock()
while bandera:
    for evento in pygame.event.get():
        try:
            if estado == "principal":
                #Dependiendo del estado del juego, se habilitan los botones o no
                input_tot = pygame.Rect(275, 500, 150, 90)
            elif estado == "segundo estado":
                punto_vuelta = pygame.Rect(ANCHO_VENTANA - 35, ALTO_VENTANA - 35, 30, 30)
                button_rojo = pygame.Rect(100, 600, 250, 90)
                button_azul = pygame.Rect(100 + 250, 600, 250, 90)
                REC_COMODIN1 = pygame.Rect(10, 500, 30, 30)
                REC_COMODIN2 = pygame.Rect(10, 540, 30, 30)
                REC_COMODIN3 = pygame.Rect(10, 580, 30, 30)

            if evento.type == pygame.QUIT:
                #Salida del juego por la "X" 
                bandera = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                #Cuando detecta que se apreta en click izq del mouse, 
                #elige como proseguir dependiendo donde toco(que boton)

                if input_tot.collidepoint(evento.pos):
                    if estado == "principal":
                        contador = 0
                        pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
                        pregunta_resp = preguntas[pregunta_aleatoria]
                        estado = "segundo estado"
                        efecto_de_sonido()

                elif punto_vuelta.collidepoint(evento.pos):
                    estado = "principal"
                    boton_decision = True
                    efecto_de_sonido()

                elif button_rojo.collidepoint(evento.pos) or button_azul.collidepoint(evento.pos):
                    contador = 0
                    if button_rojo.collidepoint(evento.pos):
                        color_decision = ROJO
                        boton_decision = False
                    elif button_azul.collidepoint(evento.pos):
                        color_decision = AZUL
                        boton_decision = False
                    estado = "tercer estado"
                    lista_jueces = decisiones_jueces()
                    efecto_de_sonido()
                    if respuestas_correctas <= 10:
                        respuestas_correctas +=1
                    
                    comprobar_eleccion = comprobacion(lista_jueces, color_decision)
                    if comprobar_eleccion:
                        respuesta_correcta_sonido()
                        monedas_base = monedas_incrementales(PUNTOS, monedas_base, respuestas_correctas)
                        lista_puntos.append(monedas_base)
                        pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
                        pregunta_resp = preguntas[pregunta_aleatoria]
                    else:
                        estado = "eliminado"
                        
                        derrota()
                elif REC_COMODIN1.collidepoint(evento.pos):
                    if comodin_uno == True:
                        contador = 0
                        pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
                        pregunta_resp = preguntas[pregunta_aleatoria]
                        comodin_uno = False
                        efecto_de_sonido()
                    else:
                        comodin_usado()
                elif REC_COMODIN2.collidepoint(evento.pos):
                    if comodin_dos == True:
                        contador = 0
                        lista_jueces = decisiones_jueces()
                        respuestas_correctas += 1
                        monedas_base = monedas_incrementales(PUNTOS, monedas_base, respuestas_correctas)
                        comodin_dos = False # Next
                        efecto_de_sonido()
                    else:
                        comodin_usado()
                elif REC_COMODIN3.collidepoint(evento.pos):
                    if comodin_tres == True:

                        comodin_tres = False   
                        # Half
                        efecto_de_sonido()
                    else:
                        comodin_usado()
        except:
            pass
        
        
    """Esta parte llama a las funciones que se encargan de ilustrar los botones, fondo, y partes
    visuales del programa. Esto dependiendo del estado en que este el programa."""
    fondo()
    monedas_contador(monedas_base)

    if estado == "principal":
        tribuna()
        jueces_funcion(None)
        button_tot()
    elif estado == "segundo estado":
        if comodin_dos == False:
            contador_comodin_dos += 1
            if contador_comodin_dos < 100:
                tribuna()
                jueces_funcion(lista_jueces)
            else:
                decision_personaje(boton_decision, color_decision)
                mi_personaje()
        else:
            decision_personaje(boton_decision, color_decision)
            mi_personaje()
            

        texto_pregunta(pregunta_resp["Pregunta"])
        comodines(ventana, comodin_uno, comodin_dos, comodin_tres)
        vuelta()
        botones_azul_rojo(pregunta_resp["Opciones"][0], pregunta_resp["Opciones"][1])
        time = tiempo(contador, 15, fps)
        contador += 1    
        if time :
            estado = "tiempo excedido"
        


    elif estado == "tercer estado":
        tribuna()
        jueces_funcion(lista_jueces)
        contador_espera += 1
        bandera_espera = tiempo_espera(contador_espera, 5, fps)
        if bandera_espera :
            contador_espera = 0
            bandera_espera = not bandera_espera
            estado = "segundo estado"
        

    elif estado == "eliminado":
        pantalla_eliminado()

        monedas_base = 0
        respuestas_correctas = 0
        contador_espera += 1
        bandera_espera = tiempo_espera(contador_espera, 5, fps)
        if bandera_espera :
            contador_espera = 0
            bandera_espera = not bandera_espera
            estado = "principal"
        

    elif estado == "tiempo excedido":
        fuera_de_tiempo()
        vuelta()
    
    guardar_puntos(lista_puntos)

    
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()