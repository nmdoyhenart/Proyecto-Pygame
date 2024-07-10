import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Manejador de Eventos en Pygame')

# Definir colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Definir la posición inicial de un círculo
circle_pos = [400, 300]
circle_radius = 50

# Bucle principal del juego
running = True
while running:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                circle_pos[0] -= 5
            elif event.key == pygame.K_RIGHT:
                circle_pos[0] += 5
            elif event.key == pygame.K_UP:
                circle_pos[1] -= 5
            elif event.key == pygame.K_DOWN:
                circle_pos[1] += 5

    # Dibujar en la pantalla
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, circle_pos, circle_radius)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
