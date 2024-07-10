"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
from parte_pygame import *

lista_puntos = cargar_puntos()

pygame.init()


tiempo_transcurrido = lambda contador, fps: contador // fps


ANCHO_VENTANA = 700
ALTO_VENTANA = 700

VENTANA1 = (ANCHO_VENTANA, ALTO_VENTANA)

FUENTE = pygame.font.Font(None, 36)

FUENTE_PORCENTAJE = pygame.font.Font(None, 30)

ventana = pygame.display.set_mode(VENTANA1)
pygame.display.set_caption("Tot or trivia")

icono = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\logo.jpg")
pygame.display.set_icon(icono)

#--------------------------------------------------------------------------------------------------------------
#VARIABLES PARA LA FUNCIONALIDAD DEL JUEGO
bandera = True
monedas_base = 0
respuestas_correctas = 0
estado = "principal"
boton_decision = True
color_decision = None
preguntas = leer_preguntas("Preguntas.csv")
contador_comodin_dos = 0
contador_comodin_tres = 0
contador_espera = 0
comodin_uno = True
comodin_dos = True
comodin_tres = True
bandera_espera = False
fps = 20
clock = pygame.time.Clock()

#--------------------------------------------------------------------------------------------------------------

#JUEGO THIS OR THAT

musica_fondo()
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
                        lista_jueces = decisiones_jueces(5)

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
                        lista_jueces = decisiones_jueces(5)
                        respuestas_correctas += 1
                        monedas_base = monedas_incrementales(PUNTOS, monedas_base, respuestas_correctas)
                        comodin_dos = False
                        efecto_de_sonido()
                    else:
                        comodin_usado()

                elif REC_COMODIN3.collidepoint(evento.pos):
                    if comodin_tres == True:
                        comodin_tres = False
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
        jueces_funcion([0,0,0,0,0] , comodin_tres, contador_comodin_tres)
        boton_jugar()
    elif estado == "segundo estado":
        decision_personaje(boton_decision, color_decision)
        mi_personaje()
        texto_pregunta(pregunta_resp["Pregunta"])
        comodines(ventana, comodin_uno, comodin_dos, comodin_tres)
        vuelta()
        botones_azul_rojo(pregunta_resp["Opciones"][0], pregunta_resp["Opciones"][1])

        if comodin_dos == False:
            if contador_comodin_dos < 10:
                estado = "tercer estado"
                pregunta_aleatoria = random.randint(0, len(preguntas) - 1)
                pregunta_resp = preguntas[pregunta_aleatoria]
                contador_comodin_dos += 10
    
        if comodin_tres == False:
            contador_comodin_tres += 1
            if contador_comodin_tres < 60:
                jueces_funcion(lista_jueces, comodin_tres, contador_comodin_tres)
            

        time = tiempo(contador, 15, fps)
        contador += 1    
        if time :
            estado = "tiempo excedido"
        
    elif estado == "tercer estado":
        tribuna()
        jueces_funcion(lista_jueces, comodin_tres, contador_comodin_tres)
        cuadro_porcentaje(lista_jueces)
        ganador()
        contador_espera += 1
        bandera_espera = tiempo_espera(contador_espera, 3, fps)
        
        if bandera_espera :
            lista_jueces = decisiones_jueces(5)
            contador_espera = 0
            bandera_espera = not bandera_espera
            estado = "segundo estado"
        
    elif estado == "eliminado":
        pantalla_eliminado()
        comodin_uno = True
        comodin_dos = True
        comodin_tres = True
        monedas_base = 0
        contador_comodin_tres = 0
        contador_comodin_dos = 0
        respuestas_correctas = 0
        contador_espera += 1
        bandera_espera = tiempo_espera(contador_espera, 3, fps)
        if bandera_espera :
            contador_espera = 0
            bandera_espera = not bandera_espera
            estado = "principal"
        
    elif estado == "tiempo excedido":
        comodin_uno = True
        comodin_dos = True
        comodin_tres = True
        monedas_base = 0
        contador_comodin_tres = 0
        contador_comodin_dos = 0
        respuestas_correctas = 0
        contador_espera += 1
        bandera_espera = tiempo_espera(contador_espera, 3, fps)
        if bandera_espera :
            contador_espera = 0
            bandera_espera = not bandera_espera
            estado = "principal"
        fuera_de_tiempo()
        vuelta()
    
    guardar_puntos(lista_puntos)

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()

