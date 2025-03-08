import pygame 


WIDTH = 1920
HEIGHT = 1080
background_colour = (234, 212, 252) 

FPS = 60
  
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
  
pygame.display.set_caption('M') 
  
screen.fill(background_colour) 

pygame.display.flip() 

# def get_background(name):
    # image = pygame.image.load(join("assests", name))

clock = pygame.time.Clock()

running = True
while running: 
    for event in pygame.event.get():            
        if event.type == pygame.QUIT: 
            running = False
    
    pygame.display.update()
    clock.tick(FPS)