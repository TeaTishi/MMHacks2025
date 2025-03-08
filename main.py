import pygame 


WIDTH = 1920
HEIGHT = 1080
background_colour = (234, 212, 252) 
  
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
  
pygame.display.set_caption('M') 
  
screen.fill(background_colour) 

pygame.display.flip() 

def get_background(name):
    image = pygame.image.load(join("assests", "Background", name))

def main(screen):
    running = True
    while running: 
        for event in pygame.event.get():            
            if event.type == pygame.QUIT: 
                running = False