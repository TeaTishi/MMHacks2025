import pygame

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3+i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3+i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'grass', 'variant': 1, 'pos': (10, 5+i)}

    def render(self,surf):
        for loc in self.ktilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile['type]']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1]*self.tile_size))

        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type]']][tile['variant']], tile['pos'])



pygame.init()

background_colour = (234, 212, 252) 
  
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((1920, 1080)) 
  
# Set the caption of the screen 
pygame.display.set_caption('Geeksforgeeks') 
  
# Fill the background colour to the screen 
screen.fill(background_colour) 
  
# Update the display using flip 
pygame.display.flip() 

tilemap = Tilemap(tile_size=16)
  
# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False



