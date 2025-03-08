import pygame
import os

# Game class to manage assets and loading images
class Game:
    def __init__(self):
        self.assets = {}
        self.load_assets()

    def load_assets(self):
        # Path to the image
        img_path = 'assets/grass/1.png'
        if os.path.exists(img_path):
            img = pygame.image.load(img_path)  # Load the image
            img = pygame.transform.scale(img, (50, 50))  # Scale the image to 16x16
            img = img.convert()  # Convert the image for better performance
            self.assets['grass'] = [img]  # Store the image under the 'grass' key
        else:
            print(f"Error: {img_path} not found!")  # Print error if image is missing

# Tilemap class to manage and render the tiles
class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        # Example tilemap generation with tiles placed at specific coordinates
        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 0, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'grass', 'variant': 0, 'pos': (10, 5 + i)}

    def render(self, surf):
        # Render each tile from the tilemap
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            tile_image = self.game.assets[tile['type']][tile['variant']]  # Get the tile image
            x_pos = tile['pos'][0] * self.tile_size  # X coordinate of the tile
            y_pos = tile['pos'][1] * self.tile_size  # Y coordinate of the tile

            # Render the tile on the screen
            surf.blit(tile_image, (x_pos, y_pos))

        # Optionally render any offgrid tiles if needed
        for tile in self.offgrid_tiles:
            tile_image = self.game.assets[tile['type']][tile['variant']]
            surf.blit(tile_image, tile['pos'])

# Initialize pygame
pygame.init()

# Set up the screen and window
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((1920, 1080))  # Set screen size to fit your needs
pygame.display.set_caption('Tilemap Example')

# Initialize the game and load assets
game = Game()
tilemap = Tilemap(game, tile_size=50)

# Game loop
running = True
while running:
    screen.fill(background_colour)  # Fill the screen with a background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render the tilemap on the screen
    tilemap.render(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()




"""import pygame
import os

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 0, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'grass', 'variant': 0, 'pos': (10, 5 + i)}

    def render(self, surf):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))

        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])


class Game:
    def __init__(self):
        self.assets = {}
        self.load_assets()

    def load_assets(self):
        img_path = 'assets/grass/1.png'
        if os.path.exists(img_path):
            img = pygame.image.load(img_path)  # Load the image
            img = pygame.transform.scale(img, (50, 50))  # Scale the image to 16x16
            img = img.convert()  # Convert the image for better performance
            self.assets['grass'] = [img]  # Store the scaled and converted image under 'grass' key
        else:
            print(f"Error: {img_path} not found!")  # Print error if image is missing


# Initialize pygame
pygame.init()

# Set up the screen and window
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((1920, 1080))  # Set the display mode (resolution)
pygame.display.set_caption('Tilemap Example')

# Initialize the game and load assets
game = Game()
tilemap = Tilemap(game, tile_size=16)

# Game loop
running = True
while running:
    screen.fill(background_colour)  # Fill the screen with a background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render the tilemap on the screen
    tilemap.render(screen)

    # Update the display
    pygame.display.flip()

pygame.quit() """
