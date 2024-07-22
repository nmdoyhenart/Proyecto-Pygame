import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Eventos Propios en Pygame")

# Configurar el reloj
clock = pygame.time.Clock()
FPS = 60

# Crear un evento personalizado
MY_CUSTOM_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MY_CUSTOM_EVENT, 2000)  # Este evento se activará cada 2000 ms (2 segundos)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MY_CUSTOM_EVENT:
            print("Evento personalizado activado cada 2 segundos")
    
    # Actualizar el estado del juego (puedes añadir lógica aquí)
    
    # Dibujar en la pantalla
    screen.fill((0, 0, 0))
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Mantener los FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()