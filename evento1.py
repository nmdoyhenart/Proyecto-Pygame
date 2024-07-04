"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
import pygame
import random
from efecto_de_sonido import *
from funcionalidad import *
from archivos import *

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (128, 191, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)
VERDE = (0, 220, 0)
ROJO_CLARO = (255, 150, 136)


lista_puntos = cargar_puntos()

PUNTOS = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]

lista_preferencias = [
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver el amanecer", "Ver el atardecer"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser invisible", "Poder volar"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Tener razón", "Tener la última palabra"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["No dormir", "No comer"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Viajar", "Quedarte en tu ciudad"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser rico", "Ser feliz"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["No internet", "No teléfono"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver serie", "Leer saga"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Vivir en mansión", "Vivir en cabaña"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser protagonista", "Ser director"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Nadar en mar", "Nadar en lago"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Música rock", "Música clásica"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Bailar salsa", "Bailar hip-hop"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Comer pizza", "Comer sushi"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Jugar fútbol", "Jugar baloncesto"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Museos de arte", "Museos de historia"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Montar en bici", "Montar en moto"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Leer ciencia ficción", "Leer misterio"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Tomar té", "Tomar café"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Aprender idioma", "Aprender instrumento"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Ir al cine", "Ir al teatro"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Cantar en ducha", "Bailar en ducha"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Caminar playa", "Caminar montaña"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Practicar yoga", "Practicar pilates"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Hacer senderismo", "Hacer escalada"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Película comedia", "Película terror"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Ir de compras", "Ir de excursión"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Jugar videojuegos", "Jugar juegos mesa"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Ejercicio aire libre", "Ejercicio gimnasio"]},
  {"Pregunta": "¿Qué prefieres?", "Opciones": ["Comida italiana", "Comida asiática"]}
]

guardar_preguntas(lista_preferencias, "Preguntas.csv")

ANCHO_VENTANA = 700
ALTO_VENTANA = 700

VENTANA1 = (ANCHO_VENTANA, ALTO_VENTANA)

tiempo_transcurrido = lambda contador, fps: contador // fps

pygame.init()

FUENTE = pygame.font.Font(None, 36)

FUENTE_PORCENTAJE = pygame.font.Font(None, 30)


ventana = pygame.display.set_mode(VENTANA1)
pygame.display.set_caption("Tot or trivia")

icono = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\logo.jpg")
pygame.display.set_icon(icono)


def fondo():
    """Función que implementa el fondo del juego en todo momento

    Args:
        -
    """
    fondo = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\fondo.jpg")
    fondo = pygame.transform.scale(fondo, VENTANA1)

    ventana.blit(fondo, (0, 0))    

def tribuna():
    """Función que implementa la tribuna en el juego en todo momento.

    Args:
        -
    """
    tribuna = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\tribuna_jueces.png")
    tribuna = pygame.transform.scale(tribuna, (600, 500))
    ventana.blit(tribuna, (55, 85))

def lista_decision(iteraciones: int):
    """Función que selecciona aleatoriamente las respuestas.

    Args:
        iteraciones: int: Numerico. 
    """
    respuestas = [ROJO, AZUL]
    lista_decisiones = []
    for i in range(iteraciones):
        decision = random.randint(0, 1)
        lista_decisiones.append(respuestas[decision])

    return lista_decisiones

def decisiones_jueces(comodin_tres: bool):
    """Selecciona la posición de la lista de decisiones de votación.

    Args:
        comodin_tres: bool: Bandera.
    """
    lista = lista_decision(5)

    return lista

def jueces_funcion(decision: list[tuple], comodin_tres: bool, contador: int):
    """Muestra la votación de los jueces, rojo o azul.

    Args:
        decision: list[tuple]: Busca dentro de la lista la tupla decision, comodin_tres: bool: Bandera
    """
    decision_x = 40
    decision_y = 40
    coordenada_x = 100
    coordenada_y = 320
    personajes = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\personaje.png")
    personajes = pygame.transform.scale(personajes, (100, 150))

    midecision = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
    midecision = pygame.transform.scale(midecision, (decision_x,decision_y))

    for i in range(len(decision)):
        ventana.blit(midecision, (coordenada_x + 30, coordenada_y, decision_x, decision_y))
        coordenada_x += 100

    if decision[0] is ROJO or decision[0] is AZUL:
        coordenada_x = 100
        
        if comodin_tres:
            for i in range(len(decision)):

                decisiones = pygame.Rect(coordenada_x + 30, coordenada_y, decision_x, decision_y)
                pygame.draw.rect(ventana, decision[i], decisiones)
                coordenada_x += 100
        else:
            if contador < 60:
                for i in range(2):
                    decisiones = pygame.Rect(coordenada_x + 30, coordenada_y, decision_x, decision_y)
                    pygame.draw.rect(ventana, decision[i], decisiones)
                    coordenada_x += 100
            else:
                for i in range(len(decision)):
                    decisiones = pygame.Rect(coordenada_x + 30, coordenada_y, decision_x, decision_y)
                    pygame.draw.rect(ventana, decision[i], decisiones)
                    coordenada_x += 100
            
    coordenada_x = 100
    for i in range(len(decision)):
        ventana.blit(personajes, (coordenada_x, 250))
        coordenada_x += 100
    
def jueces_decision(decision: list):
    """Cuenta los colores asigandos aleatoriamente.

    Args:
        decision: list: Lista que contiene la decisión final  
    """
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

def porcentaje_decision(decision: list):
    """SACA EL PORCENTAJE DE LA DECISION DEL LOS JUECES

    Args:
        decision: list: Lista que contiene la decisión final  
    """
    contador_rojo = 0
    contador_azul = 0
    for elementos in decision:
        if elementos == ROJO:
            contador_rojo += 1
        else:
            contador_azul += 1
    
    porcentaje_azul = (contador_azul * 100) // 5
    porcentaje_rojo = (contador_rojo * 100) // 5

    return (porcentaje_azul, porcentaje_rojo)

def cuadro_porcentaje(decision):
    """Grafica el porcentaje de la decision de los jueces

    Args:
        decision (list): lista de la decision de los jueces
    """
    porcentaje_tupla = porcentaje_decision(decision)

    cuadro_porcentaje_ancho = 400
    cuadro_porcentaje_alto = 60

    cuadro_porcentaje_x = 150
    cuadro_porcentaje_y = 20


    ancho_azul = (porcentaje_tupla[0] / 100 ) * cuadro_porcentaje_ancho
    cuadro_porcentaje_azul = pygame.Rect(cuadro_porcentaje_x, cuadro_porcentaje_y, ancho_azul, cuadro_porcentaje_alto)
    pygame.draw.rect(ventana, AZUL, cuadro_porcentaje_azul)

    ancho_rojo = (porcentaje_tupla[1] / 100 ) * cuadro_porcentaje_ancho

    cuadro_porcentaje_rojo = pygame.Rect(cuadro_porcentaje_x + ancho_azul, cuadro_porcentaje_y, ancho_rojo, cuadro_porcentaje_alto)
    pygame.draw.rect(ventana, ROJO, cuadro_porcentaje_rojo)

    texto_porcentaje_azul = FUENTE_PORCENTAJE.render(f"{porcentaje_tupla[1]}%", False, NEGRO)
    ventana.blit(texto_porcentaje_azul, (cuadro_porcentaje_x + cuadro_porcentaje_ancho - 55, cuadro_porcentaje_y + 20))
    texto_porcentaje_rojo = FUENTE_PORCENTAJE.render(f"{porcentaje_tupla[0]}%", False, NEGRO)
    ventana.blit(texto_porcentaje_rojo, (cuadro_porcentaje_x + 5, cuadro_porcentaje_y + 20))

    cuadro_porcentaje = pygame.Rect(cuadro_porcentaje_x, cuadro_porcentaje_y, cuadro_porcentaje_ancho, cuadro_porcentaje_alto)
    pygame.draw.rect(ventana, NEGRO, cuadro_porcentaje, 2)


def comprobacion(voto_jueces: list, mi_decision: tuple):
    color_decidido = jueces_decision(voto_jueces)
    if color_decidido == mi_decision:
        retorna = True
    else:
        retorna = False
    return retorna

def boton_jugar():
    """Boton para comenzar el juego.

    Args:
        -
    """
    centro = (350,549)
    radio = 60
    input = pygame.Rect(275, 500, 150, 90)
    texto_superficie = FUENTE.render("Jugar", True, BLANCO)
    rectangulo_texto = texto_superficie.get_rect(center = input.center)
    pygame.draw.circle(ventana, ROJO, centro, radio)
    ventana.blit(texto_superficie, rectangulo_texto)

def monedas_contador(monedas_base: int):
    """Grafica interactiva de las monedas.

    Args:
        monedas_base: int: Numerico.
    """
    monedas = pygame.Rect(ANCHO_VENTANA - 100, 80, 100, 30)
    moneda_icon = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\moneda.png")
    moneda_icon = pygame.transform.scale(moneda_icon, (40, 30))

    texto_monedas = FUENTE.render(str(monedas_base), True, BLANCO)
    pygame.draw.rect(ventana, NEGRO, monedas, 0)
    ventana.blit(texto_monedas, (monedas.x , monedas.y ))
    ventana.blit(moneda_icon, (ANCHO_VENTANA - 35, 80))

def vuelta():
    """Punto de retorno para volver al menu principal.

    Args:
        -
    """
    punto_vuelta = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\X_vuelta.png")
    punto_vuelta= pygame.transform.scale(punto_vuelta , (30, 30))
    ventana.blit(punto_vuelta, (ANCHO_VENTANA - 35, ALTO_VENTANA - 35))

def mi_personaje():
    """Creación de la interfaz del personaje.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    x_personaje = 150
    y_personaje = 150
    personajes = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\personaje.png")
    personajes = pygame.transform.scale(personajes, (400, 600))
    ventana.blit(personajes,(x_personaje, y_personaje))

def decision_personaje(estado: bool, color: str):
    """Comprueba si el título existe y lo elimina de la lista.

    Args:
        estado: bool: Devuelve True o False, color: str: String.
    """
    if estado:
        midecision = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\incognita.png")
        midecision = pygame.transform.scale(midecision, (160,140))
        ventana.blit(midecision, (150 + 115, 150 + 280))
    else:
        mi_decision = pygame.Rect(150 + 115, 150 + 280, 160,140)
        pygame.draw.rect(ventana, color, mi_decision)

def botones_azul_rojo(opcion_azul: str, opcion_roja: str):
    """Crea los dos botones para seleccionar las opciones.

    Args:
        opcion_azul: str: String, opcion_roja: str: String.
    """
    x = 100
    y = 600
    boton_altura = 90
    boton_ancho = 250 

    rojo = pygame.Rect(x, y, boton_ancho, boton_altura)
    pygame.draw.rect(ventana, ROJO, rojo)
    pygame.draw.rect(ventana, NEGRO, rojo, 2)
    texto_superficie = FUENTE.render(f"{opcion_roja}", True, NEGRO)
    ventana.blit(texto_superficie, (rojo.x + 5, rojo.y + 5))

    azul = pygame.Rect(x + boton_ancho, y, boton_ancho, boton_altura)
    pygame.draw.rect(ventana, AZUL_CLARO, azul)
    pygame.draw.rect(ventana, NEGRO, azul, 2)
    texto_superficie = FUENTE.render(f"{opcion_azul}", True, BLANCO)
    ventana.blit(texto_superficie, (azul.x + 5, azul.y + 5))

def comodines(ventana: int, comodin_uno: bool, comodin_dos: bool, comodin_tres: bool):
    """Comprueba si el título existe y lo elimina de la lista.

    Args:
        ventana: int: Numerico, comodin_uno: Bandera, comodin_dos: Bandera, comodin_tres: Bandera.
    """
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

    if comodin_uno:
        comodin1 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\comodin1.png")
        comodin1 = pygame.transform.scale(comodin1, (ancho_comodin, alto_comodin))
        ventana.blit(comodin1, (x_comodin1, y_comodin1))
    else:
        comodin1 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
        comodin1 = pygame.transform.scale(comodin1, (ancho_comodin, alto_comodin))
        ventana.blit(comodin1, (x_comodin1, y_comodin1))

    if comodin_dos:
        comodin2 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\comodin2.png")
        comodin2 = pygame.transform.scale(comodin2, (ancho_comodin, alto_comodin))
        ventana.blit(comodin2, (x_comodin2, y_comodin2))
    else:
        comodin2 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
        comodin2 = pygame.transform.scale(comodin2, (ancho_comodin, alto_comodin))
        ventana.blit(comodin2, (x_comodin2, y_comodin2))

    if comodin_tres:
        comodin3 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\comodin3.png")
        comodin3 = pygame.transform.scale(comodin3, (ancho_comodin, alto_comodin))
        ventana.blit(comodin3, (x_comodin3, y_comodin3))
    else:
        comodin3 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\cruz.png")
        comodin3 = pygame.transform.scale(comodin3, (ancho_comodin, alto_comodin))
        ventana.blit(comodin3, (x_comodin3, y_comodin3))

def texto_pregunta(pregunta: str):
    """Grafica para las preguntas.

    Args:
        pregunta: str: String.
    """
    ancho = 500
    alto = 50
    x = 100
    y = 550
    cuadro_preg = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(ventana, GRIS, cuadro_preg)
    pygame.draw.rect(ventana, NEGRO, cuadro_preg, 2)
    texto_preg = FUENTE.render(f"{pregunta}", True, NEGRO)
    ventana.blit(texto_preg, (x + 3, y + 15))

def tiempo(contador: int, limite_tiempo: int, fps: int):
    """Grafico para mostrar el contador.

    Args:
        contador: int: Numerico, limite_tiempo: int: Numerico, fps: int: Numerico.
    """
    time_x = 5
    time_y = 5
    time_ancho = 40
    time_alto = 30
    temporizador = pygame.Rect(time_x, time_y, time_ancho, time_alto)
    pygame.draw.rect(ventana, NEGRO, temporizador)
    text_tiempo = FUENTE.render(f"{contador // 20}", True, BLANCO)
    ventana.blit(text_tiempo, (time_x + 10, time_y + 5))
    retorna = False
    tiempo_real = tiempo_transcurrido(contador, fps)
    if tiempo_real >= limite_tiempo:
        retorna = True
    return retorna
    
def fuera_de_tiempo():
    """Grafica que notifica la expulsión del programa.

    Args:
        -
    """
    eliminado_x = 200
    eliminado_y = 350
    eliminado_ancho = 400
    eliminado_alto = 35
    eliminacion_cuadro = pygame.Rect(eliminado_x, eliminado_y, eliminado_ancho, eliminado_alto)
    pygame.draw.rect(ventana, NEGRO, eliminacion_cuadro)
    text_eliminacion = FUENTE.render(f"Usted ha excedido el tiempo y perdio.", True, BLANCO)
    ventana.blit(text_eliminacion, (eliminado_x + 10, eliminado_y + 5))

def pantalla_eliminado():
    """Aviso de descalificación.

    Args:
        -
    """
    eliminado_ancho = 400
    eliminado_alto = 200

    eliminado_x = 150
    eliminado_y = 250

    aviso_eliminado = pygame.Rect(eliminado_x, eliminado_y, eliminado_ancho, eliminado_alto)
    pygame.draw.rect(ventana, NEGRO, aviso_eliminado)
    texto_eliminado = FUENTE.render(f"PERDISTE :P", False, BLANCO)
    ventana.blit(texto_eliminado, (eliminado_x + 100, eliminado_y + 82))

def tiempo_espera(contador_espera: int, limite: int, fps: int):
    """Calcula el en el cual te hecha del programa.

    Args:
        contador_espera: int: Numerico, limite: int: Numerico, fps: int: Numerico.
    """
    retorna = False
    tiempo_real = tiempo_transcurrido(contador_espera, fps)
    if tiempo_real >= limite:
        retorna = True
    return retorna

def ganador():
    """Se muestra si el publico coincidio con tu respuesta.

    Args:
        -
    """ 
    ganador_ancho = 400
    ganardor_alto = 100

    ganador_x = 150
    ganador_y = 500

    imagen1_ancho = 200
    imagen1_alto = 100

    imagen1_x = 0
    imagen1_y  = 500

    imagen2_ancho = 200
    imagen2_alto = 100

    imagen2_x = 500
    imagen2_y = 500

    imagen1 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\festejo1.jpg")
    imagen1 = pygame.transform.scale(imagen1, (imagen1_ancho, imagen1_alto))
    ventana.blit(imagen1, (imagen1_x, imagen1_y))

    imagen2 = pygame.image.load(r"TP-PYGAME-COLLAB-main\recursos\festejo2.jpg")
    imagen2 = pygame.transform.scale(imagen2, (imagen2_ancho, imagen2_alto))
    ventana.blit(imagen2, (imagen2_x, imagen2_y))

    aviso_ganador = pygame.Rect(ganador_x, ganador_y, ganador_ancho, ganardor_alto)
    pygame.draw.rect(ventana, GRIS, aviso_ganador)
    pygame.draw.rect(ventana, VERDE, aviso_ganador, 2)
    texto_ganador = FUENTE.render(f"Coincidiste con el publico!", False, NEGRO)
    ventana.blit(texto_ganador, (ganador_x + 60, ganador_y + 30))

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
                        lista_jueces = decisiones_jueces(comodin_tres)

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
                        lista_jueces = decisiones_jueces(comodin_tres)
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
        ganador()
        cuadro_porcentaje(lista_jueces)
        contador_espera += 1
        bandera_espera = tiempo_espera(contador_espera, 3, fps)
        
        if bandera_espera :
            lista_jueces = decisiones_jueces(comodin_tres)
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