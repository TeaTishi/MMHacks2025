# import pygame 


# WIDTH = 1920
# HEIGHT = 1080
# background_colour = (234, 212, 252) 

# FPS = 60
  
# screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
  
# pygame.display.set_caption('M') 
  
# screen.fill(background_colour) 

# pygame.display.flip() 

# # def get_background(name):
#     # image = pygame.image.load(join("assests", name))





# running = True
# while running: 

#     player = Player()
#     for event in pygame.event.get():            
#         if event.type == pygame.QUIT: 
#             running = False


# def main (window):
#     clock = pygame.time.Clock()
#     background, bg_image = get_background("background.jpg")
    
#     player = Player (100,100,50,50)

#     run = True
#     while run:
#         clock.tick(FPS)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 break
#         draw(window, background, bg_image, player)

#     pygame.quit()
#     quit()

# if __name__ == "__main__":
#     main(window)



# player.py
# import pygame

# class Player(pygame.sprite.Sprite):
#     COLOR = (255, 0, 0)
    
#     def __init__(self, x, y, width, height):
#         super().__init__()
#         self.image = pygame.Surface([width, height])
#         self.image.fill(self.COLOR)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.x_velocity = 0
#         self.y_velocity = 0

#     def draw(self, screen):
#         screen.blit(self.image, self.rect)

# game.py
import pygame
from player import Player

def main():
    pygame.init()

    WIDTH = 1920
    HEIGHT = 1080
    background_colour = (234, 212, 252)
    FPS = 60

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('My Game')

    clock = pygame.time.Clock()
    player = Player(50, 50, 50, 50)  # Creating an instance of Player

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(background_colour)
        player.draw("player.png",screen)  # Draw the player on the screen

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()

