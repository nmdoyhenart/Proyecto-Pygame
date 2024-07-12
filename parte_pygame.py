import pygame
import random
from funciones import *
from elementos import *
from efectos_de_sonido import *
from archivos import *
pygame.init()

tiempo_transcurrido = lambda contador, fps: contador // fps

#-------------------------------------------------------------------------------------------------------------------

def funcion_principal(FUENTE, ventana, evento, estado):
    """Boton para comenzar el juego.

    Args:
        -
    """
    if estado == "principal":
        centro = (350,549)
        radio = 60
        input = pygame.Rect(275, 500, 150, 90)
        texto_superficie = FUENTE.render("Jugar", True, BLANCO)
        rectangulo_texto = texto_superficie.get_rect(center = input.center)
        pygame.draw.circle(ventana, ROJO, centro, radio)
        ventana.blit(texto_superficie, rectangulo_texto)
        inicio = False    
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if input.collidepoint(evento.pos):
                inicio = True
                contador = 0
                efecto_de_sonido()
    return inicio

#-------------------------------------------------------------------------------------------------------------------

def arranque_juego(FUENTE, ventana, evento, pregunta_aleatoria):
    """Crea los dos botones para seleccionar las opciones.

    Args:
        opcion_azul: str: String, opcion_roja: str: String.
    """
    estado = "segundo estado"
    preguntas = leer_preguntas("Preguntas.csv")
    pregunta_resp = preguntas[pregunta_aleatoria]
    decision = True
    color = None
    tupla_decision = rojo_azul(FUENTE, ventana, pregunta_resp["Opciones"][0], pregunta_resp["Opciones"][1])
    rojo = tupla_decision[0]
    azul = tupla_decision[1]
    bandera_jueces = False
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if rojo.collidepoint(evento.pos) or azul.collidepoint(evento.pos):
            bandera_jueces = True
            if rojo.collidepoint(evento.pos):
                color = ROJO
                decision = False
                estado = "tercer estado"
            else:
                color = AZUL
                decision = False
                estado = "tercer estado"
            efecto_de_sonido()
    decision_personaje(ventana, decision, color)
    mi_personaje(ventana)

    retorna = [estado, color, bandera_jueces]
    texto_pregunta(pregunta_resp["Pregunta"], ventana, FUENTE)

    return retorna

def rojo_azul(FUENTE, ventana, opcion_roja, opcion_azul):
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

    return (rojo, azul)


def texto_pregunta(pregunta: str, ventana, FUENTE):
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


def mi_personaje(ventana):
    """Creación de la interfaz del personaje.

    Args:
        lista_peliculas: list[dict]: Diccionario que contiene la información de las películas.
    """
    x_personaje = 150
    y_personaje = 150
    personajes = pygame.image.load(r"recursos\personaje.png")
    personajes = pygame.transform.scale(personajes, (400, 600))
    ventana.blit(personajes,(x_personaje, y_personaje))


def decision_personaje(ventana, estado: bool, color: str):
    """Comprueba si el título existe y lo elimina de la lista.

    Args:
        estado: bool: Devuelve True o False, color: str: String.
    """
    if estado:
        midecision = pygame.image.load(r"recursos\incognita.png")
        midecision = pygame.transform.scale(midecision, (160,140))
        ventana.blit(midecision, (150 + 115, 150 + 280))
    else:
        mi_decision = pygame.Rect(150 + 115, 150 + 280, 160,140)
        pygame.draw.rect(ventana, color, mi_decision)


def decisiones_jueces(iteraciones: int):
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


def comodines(ventana: int, comodin_uno: bool, comodin_dos: bool, comodin_tres: bool, evento, estado):
    """Comprueba si el título existe y lo elimina de la lista.

    Args:
        ventana: int: Numerico, comodin_uno: Bandera, comodin_dos: Bandera, comodin_tres: Bandera.
    """
    x_comodines = 10
    y_caja = 500
    ancho_comodin = 30
    alto_comodin = 30
    y_comodin1 = y_caja
    y_comodin2 = y_comodin1 + alto_comodin + 10
    y_comodin3 = y_comodin2 + alto_comodin + 10

    coordenadas_1 = (x_comodines, y_comodin1)
    coordenadas_2 = (x_comodines, y_comodin2)
    coordenadas_3 = (x_comodines, y_comodin3)

    if comodin_uno:
        comodin1 = pygame.image.load(r"recursos\comodin1.png")
        comodin1 = pygame.transform.scale(comodin1, (ancho_comodin, alto_comodin))
        ventana.blit(comodin1, coordenadas_1)
    else:
        comodin1 = pygame.image.load(r"recursos\cruz.png")
        comodin1 = pygame.transform.scale(comodin1, (ancho_comodin, alto_comodin))
        ventana.blit(comodin1, coordenadas_1)

    if comodin_dos:
        comodin2 = pygame.image.load(r"recursos\comodin2.png")
        comodin2 = pygame.transform.scale(comodin2, (ancho_comodin, alto_comodin))
        ventana.blit(comodin2, coordenadas_2)
    else:
        comodin2 = pygame.image.load(r"recursos\cruz.png")
        comodin2 = pygame.transform.scale(comodin2, (ancho_comodin, alto_comodin))
        ventana.blit(comodin2, coordenadas_2)

    if comodin_tres:
        comodin3 = pygame.image.load(r"recursos\comodin3.png")
        comodin3 = pygame.transform.scale(comodin3, (ancho_comodin, alto_comodin))
        ventana.blit(comodin3, coordenadas_3)
    else:
        comodin3 = pygame.image.load(r"recursos\cruz.png")
        comodin3 = pygame.transform.scale(comodin3, (ancho_comodin, alto_comodin))
        ventana.blit(comodin3, coordenadas_3)
    
    boton_comodin_1 = pygame.Rect(x_comodines, y_comodin1, ancho_comodin, alto_comodin)
    boton_comodin_2 = pygame.Rect(x_comodines, y_comodin2, ancho_comodin, alto_comodin)
    boton_comodin_3 = pygame.Rect(x_comodines, y_comodin3, ancho_comodin, alto_comodin)

    tupla_rect = (boton_comodin_1, boton_comodin_2, boton_comodin_3)

    back = botones_comodines(tupla_rect, evento,comodin_uno, comodin_dos, comodin_tres, estado)

    return back
 

def botones_comodines(tupla_rect, evento,comodin_uno: bool, comodin_dos: bool, comodin_tres: bool, estado):
    REC_COMODIN1 = tupla_rect[0]
    REC_COMODIN2 = tupla_rect[1]
    REC_COMODIN3 = tupla_rect[2]
    
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if REC_COMODIN1.collidepoint(evento.pos):
            if comodin_uno == True:
                comodin_uno = False
                efecto_de_sonido()
            else:
                comodin_usado()

        elif REC_COMODIN2.collidepoint(evento.pos):
            if comodin_dos == True:
                estado = "tercer estado"
                comodin_dos = False
                efecto_de_sonido()
            else:
                comodin_usado()

        elif REC_COMODIN3.collidepoint(evento.pos):
            if comodin_tres == True:
                #estado = "tercer estado"
                comodin_tres = False
                efecto_de_sonido()
            else:
                comodin_usado()

    back = (comodin_uno, comodin_dos, comodin_tres, estado)

    return back



#-------------------------------------------------------------------------------------------------------------------

def estado_tres(ventana, fuente, color_decision, lista_jueces, comodin_tres, contador_tiempo):

    tribuna(ventana)
    jueces_funcion(ventana, lista_jueces, comodin_tres, contador_tiempo)
    cuadro_porcentaje(ventana, fuente, lista_jueces)
    comprobar_eleccion = comprobacion(lista_jueces, color_decision)

    return comprobar_eleccion


def funcion_comodin_tres(ventana, lista_jueces, comodin_tres, contador_tiempo):
    tribuna(ventana)
    jueces_funcion(ventana, lista_jueces, comodin_tres, contador_tiempo)


def ganar_perder(ventana, fuente, comprobar_eleccion, habilitar_sonido):
    if comprobar_eleccion:
        if habilitar_sonido == 0:
            respuesta_correcta_sonido()
        ganador(ventana, fuente)
    else:
        if habilitar_sonido == 0:
            derrota()
        pantalla_eliminado(ventana, fuente)

    habilitar_sonido += 1
    return habilitar_sonido


def tribuna(ventana):
    """Función que implementa la tribuna en el juego en todo momento.

    Args:
        -
    """
    tribuna = pygame.image.load(r"recursos\tribuna_jueces.png")
    tribuna = pygame.transform.scale(tribuna, (600, 500))
    ventana.blit(tribuna, (55, 85))


def jueces_funcion(ventana, decision: list[tuple], comodin_tres: bool, contador_tiempo: int):
    """Muestra la votación de los jueces, rojo o azul.

    Args:
        decision: list[tuple]: Busca dentro de la lista la tupla decision, comodin_tres: bool: Bandera
    """
    decision_x = 40
    decision_y = 40
    coordenada_x = 100
    coordenada_y = 320
    personajes = pygame.image.load(r"recursos\personaje.png")
    personajes = pygame.transform.scale(personajes, (100, 150))

    midecision = pygame.image.load(r"recursos\incognita.png")
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
            if contador_tiempo < 10:
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

    
def cuadro_porcentaje(ventana, fuente_porcentaje, decision):
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

    texto_porcentaje_rojo = fuente_porcentaje.render(f"{porcentaje_tupla[1]}%", False, NEGRO)
    ventana.blit(texto_porcentaje_rojo, (cuadro_porcentaje_x + cuadro_porcentaje_ancho - 55, cuadro_porcentaje_y + 20))

    texto_porcentaje_azul = fuente_porcentaje.render(f"{porcentaje_tupla[0]}%", False, NEGRO)
    ventana.blit(texto_porcentaje_azul, (cuadro_porcentaje_x + 5, cuadro_porcentaje_y + 20))

    cuadro_porcentaje = pygame.Rect(cuadro_porcentaje_x, cuadro_porcentaje_y, cuadro_porcentaje_ancho, cuadro_porcentaje_alto)
    pygame.draw.rect(ventana, NEGRO, cuadro_porcentaje, 2)




#-------------------------------------------------------------------------------------------------------------------

def ganador(ventana, FUENTE):
    """Se muestra si el publico coincidio con tu respuesta.
    Args:
        ventana (surface): _description_
        fuente (font): _description_
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

    imagen1 = pygame.image.load(r"recursos\festejo1.jpg")
    imagen1 = pygame.transform.scale(imagen1, (imagen1_ancho, imagen1_alto))
    ventana.blit(imagen1, (imagen1_x, imagen1_y))

    imagen2 = pygame.image.load(r"recursos\festejo2.jpg")
    imagen2 = pygame.transform.scale(imagen2, (imagen2_ancho, imagen2_alto))
    ventana.blit(imagen2, (imagen2_x, imagen2_y))

    aviso_ganador = pygame.Rect(ganador_x, ganador_y, ganador_ancho, ganardor_alto)
    pygame.draw.rect(ventana, GRIS, aviso_ganador)
    pygame.draw.rect(ventana, VERDE, aviso_ganador, 2)
    texto_ganador = FUENTE.render(f"Coincidiste con el publico!", False, NEGRO)
    ventana.blit(texto_ganador, (ganador_x + 60, ganador_y + 30))


def pantalla_eliminado(ventana, FUENTE):
    """Aviso de descalificación.

   Args:
        ventana (surface): _description_
        fuente (font): _description_
    """
    eliminado_ancho = 400
    eliminado_alto = 160

    eliminado_x = 150
    eliminado_y = 500

    imagen1_ancho = 150
    imagen1_alto = 160

    imagen1_x = 0
    imagen1_y  = 500

    imagen2_ancho = 150
    imagen2_alto = 160

    imagen2_x = 550
    imagen2_y = 500

    imagen1 = pygame.image.load(r"recursos\derrota1.jpg")
    imagen1 = pygame.transform.scale(imagen1, (imagen1_ancho, imagen1_alto))
    ventana.blit(imagen1, (imagen1_x, imagen1_y))

    imagen2 = pygame.image.load(r"recursos\derrota2.jpg")
    imagen2 = pygame.transform.scale(imagen2, (imagen2_ancho, imagen2_alto))
    ventana.blit(imagen2, (imagen2_x, imagen2_y))

    aviso_eliminado = pygame.Rect(eliminado_x, eliminado_y, eliminado_ancho, eliminado_alto)
    pygame.draw.rect(ventana, NEGRO, aviso_eliminado)
    texto_eliminado = FUENTE.render(f"PERDISTE :P", False, BLANCO)
    ventana.blit(texto_eliminado, (eliminado_x + 100, eliminado_y + 60))


def fondo(ventana, DIMENSION):
    """funcion que grafica el fondo el juego
    Args:
        ventana (surface): _description_
        DIMENSION (tuple): tamaño de la pantalla
    """
    fondo = pygame.image.load(r"recursos\fondo.jpg")
    fondo = pygame.transform.scale(fondo, DIMENSION)

    ventana.blit(fondo, (0, 0))    


def monedas_contador(monedas_base, ANCHO_VENTANA, FUENTE, ventana):
    """Grafica interactiva de las monedas.
    Args:
        monedas_base (int): cantidad de monedas
        ANCHO_VENTANA (int): ancho de la ventana/pantalla
        FUENTE (font): _description_
        ventana (surface): _description_
    """
    monedas = pygame.Rect(ANCHO_VENTANA - 100, 80, 100, 30)
    moneda_icon = pygame.image.load(r"recursos\moneda.png")
    moneda_icon = pygame.transform.scale(moneda_icon, (40, 30))

    texto_monedas = FUENTE.render(str(monedas_base), True, BLANCO)
    pygame.draw.rect(ventana, NEGRO, monedas, 0)
    ventana.blit(texto_monedas, (monedas.x , monedas.y ))
    ventana.blit(moneda_icon, (ANCHO_VENTANA - 35, 80))


def vuelta(ventana, dimension, evento):
    """Punto de retorno para volver al menu principal.
    Args:
        ventana (surface): _description_
        dimension (tuple): tupla con ancho y alto de la ventana
        evento (event): evento que se esta llevando a cabo

    Returns:
        bool: retorna un booleano dependiendo si toco o no el boton de vuelta
    """
    ancho_ventana = dimension[0]
    alto_ventana = dimension[1]
    x = ancho_ventana - 35
    y = alto_ventana - 35
    ancho = 30
    alto = 30
    vuelta_boton = pygame.Rect(x, y, ancho, alto)

    punto_vuelta = pygame.image.load(r"recursos\X_vuelta.png")
    punto_vuelta= pygame.transform.scale(punto_vuelta , (ancho, alto))
    ventana.blit(punto_vuelta, (x, y))
    retorno = False
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if vuelta_boton.collidepoint(evento.pos):
            retorno = True
    return retorno


def tiempo(ventana, FUENTE, contador: int, limite_tiempo: int, fps: int):
    """Grafico para mostrar el contador.

    Args:
        ventana (surface): _description_
        FUENTE (font): _description_
        contador (int): _description_
        limite_tiempo (int): _description_
        fps (int): _description_

    Returns:
        _type_: _description_
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
    
def tiempo_espera(contador_espera: int, limite: int, fps: int):
    """Calcula el tiempo en el cual te hecha del programa.

    Args:
        contador_espera: int: Numerico, limite: int: Numerico, fps: int: Numerico.
    """
    retorna = False
    tiempo_real = tiempo_transcurrido(contador_espera, fps)
    if tiempo_real >= limite:
        retorna = True
    return retorna

def fuera_de_tiempo(ventana, FUENTE):
    """Grafica que notifica la expulsión del programa.
    Args:
        ventana (surface): _description_
        FUENTE (font): _description_
    """
    eliminado_x = 200
    eliminado_y = 350
    eliminado_ancho = 400
    eliminado_alto = 35
    eliminacion_cuadro = pygame.Rect(eliminado_x, eliminado_y, eliminado_ancho, eliminado_alto)
    pygame.draw.rect(ventana, NEGRO, eliminacion_cuadro)
    text_eliminacion = FUENTE.render(f"Usted ha excedido el tiempo y perdio.", True, BLANCO)
    ventana.blit(text_eliminacion, (eliminado_x + 10, eliminado_y + 5))