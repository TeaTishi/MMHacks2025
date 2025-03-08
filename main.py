import pygame


WIDTH = 1024
HEIGHT = 800
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main (window):
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()