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

def main(screen):



    running = True
    while running: 
        for event in pygame.event.get():            
            if event.type == pygame.QUIT: 
                running = False



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