from archivos import guardar_preguntas

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (128, 191, 255)
GRIS = (200, 200, 200)
ROJO = (255, 0, 0)
VERDE = (0, 220, 0)
ROJO_CLARO = (255, 150, 136)

PUNTOS = [50, 100, 200, 250, 300, 400, 500, 600, 750, 1000]

lista_preferencias = [{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver el amanecer", "Ver el atardecer"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser invisible", "Poder volar"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Tener razón", "Tener la última palabra"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["No dormir", "No comer"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Viajar", "Quedarte en tu ciudad"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser rico", "Ser feliz"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["No internet", "No teléfono"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ver serie", "Leer saga"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Vivir en mansión", "Vivir en cabaña"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ser protagonista", "Ser director"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Nadar en mar", "Nadar en lago"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Música rock", "Música clásica"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Bailar salsa", "Bailar hip-hop"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Comer pizza", "Comer sushi"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Jugar fútbol", "Jugar baloncesto"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Museos de arte", "Museos de historia"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Montar en bici", "Montar en moto"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Leer ciencia ficción", "Leer misterio"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Tomar té", "Tomar café"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Aprender idioma", "Aprender instrumento"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ir al cine", "Ir al teatro"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Cantar en ducha", "Bailar en ducha"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Caminar playa", "Caminar montaña"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Practicar yoga", "Practicar pilates"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Hacer senderismo", "Hacer escalada"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Película comedia", "Película terror"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ir de compras", "Ir de excursión"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Jugar videojuegos", "Jugar juegos mesa"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Ejercicio aire libre", "Ejercicio gimnasio"]},{"Pregunta": "¿Qué prefieres?", "Opciones": ["Comida italiana", "Comida asiática"]}]

guardar_preguntas(lista_preferencias, "Preguntas.csv")
