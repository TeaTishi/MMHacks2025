# import the pygame module 
import pygame 

# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 

# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((300, 300)) 

# Set the caption of the screen 
pygame.display.set_caption('Geeksforgeeks') 

# Fill the background colour to the screen 
screen.fill(background_colour) 

# Update the display using flip 
pygame.display.flip() 

# Variable to keep our game loop running 
running = True

# game loop 
while running: 
	
# for loop through the event queue 
	for event in pygame.event.get(): 
	
		# Check for QUIT event	 
		if event.type == pygame.QUIT: 
			running = False
import pygame

class Object(pygame.sprite.Sprite):
    def __init__ (self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
    
    def draw (self, win):
        win.blit(self.image, (self.rect.x, self. rect.y))


class Block(Object):
    def __init__ (self, x, y, size):
        super().__init__(x, y, size, size)
        block = load_block(size)
        self.image.blit(block, (0,0))
        self.mask = pygame.mask.from_surface(self.image)

def get_block(size):
    path = join("assests", "Terrain", "Terrain.png")
    image - pygame.image.load(path).conver_alpha()
    surface = pygame.Surface((size, seize), pygame.SCRALPHA, 32)
    rect = pygame.Rect(96, 0, size, size) # change these two values and size the two numbers are the chord of the starting pic
    surface.blit(image, (0,0), rect) #1:04:38
    return pygame.transform.scale2x(surface)


  
# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 
  
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((300, 300)) 
  
# Set the caption of the screen 
pygame.display.set_caption('Geeksforgeeks') 
  
# Fill the background colour to the screen 
screen.fill(background_colour) 
  
# Update the display using flip 
pygame.display.flip() 
  
# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False