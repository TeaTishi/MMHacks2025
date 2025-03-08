import pygame
import os

# Game class to manage assets and loading images
class Game:
    def __init__(self):
        self.assets = {}
        self.load_assets()

    def load_assets(self):
        # Load images for 'grass' type from the assets folder
        grass_images = []
        img_path = os.path.join('assets/grass/', '1.png')  # Ensure you're using the correct file path and extension
        if os.path.exists(img_path):
            img = pygame.image.load(img_path).convert()  # Load the image and convert it for better performance
            # Check if the image is larger than expected and scale it down to 16x16
            if img.get_width() > 6000 and img.get_height() > 6000:
                img = pygame.transform.scale(img, (16, 16))  # Scale the image to 16x16 pixels
            else:
                print(f"Warning: Image is already small or the scaling is not needed. Size: {img.get_width()}x{img.get_height()}")
            grass_images.append(img)  # Append the scaled image to the list
        else:
            print(f"Error: {img_path} not found!")  # If the image doesn't exist, print an error
        self.assets['grass'] = grass_images  # Store the scaled image under the 'grass' type

# Tilemap class to manage and render the tiles
class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        # Example tilemap generation with tiles placed at specific coordinates
        for i in range(10):
            self.tilemap[str(50 + 5*i) + ';75'] = {'type': 'grass', 'variant': 0, 'pos': (50 + 5*i, 75)}
            self.tilemap['75;' + str(5 + i)] = {'type': 'grass', 'variant': 0, 'pos': (75, 5 + i)}

    def render(self, surf):
        # Render each tile from the tilemap
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            tile_image = self.game.assets[tile['type']][tile['variant']]  # Get the scaled tile image
            surf.blit(tile_image, (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))

        # Optionally, render any offgrid tiles if needed (not used here)
        for tile in self.offgrid_tiles:
            tile_image = self.game.assets[tile['type']][tile['variant']]
            surf.blit(tile_image, tile['pos'])

# Initialize pygame
pygame.init()

# Set up the screen and window
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((1920, 1080))
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

pygame.quit()
