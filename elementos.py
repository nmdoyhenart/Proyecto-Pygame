"""""
TP GRUPAL PYGAME

Intregrantes: Nicolás Doyhenart, Santino Fernandez
"""""
from archivos import *

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (128, 191, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)
VERDE = (0, 220, 0)
ROJO_CLARO = (255, 150, 136)
VERDE_CLARO = (144, 238, 144)

lista_preferencias = [
    ["¿Qué prefieres?", "Ver el amanecer", "Ver el atardecer"],
    ["¿Qué prefieres?", "Ser invisible", "Poder volar"],
    ["¿Qué prefieres?", "Tener razón", "Tener la última palabra"],
    ["¿Qué prefieres?", "No dormir", "No comer"],
    ["¿Qué prefieres?", "Viajar", "Quedarte en tu ciudad"],
    ["¿Qué prefieres?", "Ser rico", "Ser feliz"],
    ["¿Qué prefieres?", "No internet", "No teléfono"],
    ["¿Qué prefieres?", "Ver serie", "Leer saga"],
    ["¿Qué prefieres?", "Vivir en mansión", "Vivir en cabaña"],
    ["¿Qué prefieres?", "Ser protagonista", "Ser director"],
    ["¿Qué prefieres?", "Nadar en mar", "Nadar en lago"],
    ["¿Qué prefieres?", "Música rock", "Música clásica"],
    ["¿Qué prefieres?", "Bailar salsa", "Bailar hip-hop"],
    ["¿Qué prefieres?", "Comer pizza", "Comer sushi"],
    ["¿Qué prefieres?", "Jugar fútbol", "Jugar baloncesto"],
    ["¿Qué prefieres?", "Museos de arte", "Museos de historia"],
    ["¿Qué prefieres?", "Montar en bici", "Montar en moto"],
    ["¿Qué prefieres?", "Leer ciencia ficción", "Leer misterio"],
    ["¿Qué prefieres?", "Tomar té", "Tomar café"],
    ["¿Qué prefieres?", "Aprender idioma", "Aprender instrumento"],
    ["¿Qué prefieres?", "Ir al cine", "Ir al teatro"],
    ["¿Qué prefieres?", "Cantar en ducha", "Bailar en ducha"],
    ["¿Qué prefieres?", "Caminar playa", "Caminar montaña"],
    ["¿Qué prefieres?", "Practicar yoga", "Practicar pilates"],
    ["¿Qué prefieres?", "Hacer senderismo", "Hacer escalada"],
    ["¿Qué prefieres?", "Película comedia", "Película terror"],
    ["¿Qué prefieres?", "Ir de compras", "Ir de excursión"],
    ["¿Qué prefieres?", "Jugar videojuegos", "Jugar juegos mesa"],
    ["¿Qué prefieres?", "Ejercicio aire libre", "Ejercicio gimnasio"],
    ["¿Qué prefieres?", "Comida italiana", "Comida asiática"]]

guardar_preguntas(lista_preferencias, "Preguntas.csv")