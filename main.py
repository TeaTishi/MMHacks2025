import pygame
import os

#from MMHacks2025.enemies import background_colour


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(self.COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.speed = 5

        self.health = 3
        self.max_health = 3

    def draw(self, screen):
        screen.blit(pygame.image.load("assets/player/player.png"), self.rect)

    def get_damage(self):
        if self.health > 0:
            self.health -= 1

    def get_health(self):
        if self.health > self.max_health:
            self.health -= 1

    def update(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT



class Enemy(object):
    walkRight = [pygame.image.load('assets/rats/rightrat_resized.png')]
    walkLeft = [pygame.image.load('assets/rats/leftrat_resized.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.velocity = 3
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.velocity > 0:
            screen.blit(self.walkRight[0], (self.x, self.y))
        else:
            screen.blit(self.walkLeft[0], (self.x, self.y))

        self.rect.x = self.x
        self.rect.y = self.y

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
        else:
            if self.x + self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1

class Cat(object):
    #walkRight = [pygame.image.load('assets/rats/rightrat_resized.png')]
    #walkLeft = [pygame.image.load('assets/rats/leftrat_resized.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        # self.walkCount = 0
        # self.velocity = 3
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        screen.blit(pygame.image.load("assets/cat/cat.png"), self.rect)

        # img = pygame.image.load(img_path)
        # img = pygame.transform.scale(img, (50, 50))
        # img = img.convert()  # Convert the image for better performance
        # self.assets['grass'] = [img]  # Store the image under the 'grass' key

        self.rect.x = self.x
        self.rect.y = self.y

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

class Game:
    def __init__(self):
        self.assets = {}
        self.load_assets()

    def load_assets(self):
        # Path to the image
        img_path = 'assets/grass/1.png'
        if os.path.exists(img_path):
            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (50, 50))
            img = img.convert()  # Convert the image for better performance
            self.assets['grass'] = [img]  # Store the image under the 'grass' key
        else:
            print(f"Error: {img_path} not found!")  # Print error if image is missing


pygame.init()

WIDTH = 1920
HEIGHT = 1080
#background_colour = (234, 212, 252)
background_colour = pygame.image.load('assets/background.jpg')
background_colour = pygame.transform.scale(background_colour, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('M')

clock = pygame.time.Clock()
FPS = 60

player = Player(WIDTH / 2, HEIGHT / 2, 50, 50)
rat = Enemy(100, 100, 100, 100, 1000)
cat= Cat(WIDTH / 2, HEIGHT / 2, WIDTH / 2, HEIGHT, 1000)

game = Game() 

tilemap = Tilemap(game, tile_size=50)

def redrawGameWindow():
    #screen.fill(background_colour)
    tilemap.render(screen) 
    player.draw(screen)
    rat.draw(screen)
    cat.draw(screen)
    pygame.display.update()

def check_collision(player, enemy):
    return player.rect.colliderect(enemy.rect)

def check_collision (player, cat):
    return player.rect.colliderect(cat.rect)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image
    screen.blit(background_colour, (0, 0))

    # Update the display
    #pygame.display.flip()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x_velocity = -player.speed
    elif keys[pygame.K_d]:
        player.x_velocity = player.speed
    else:
        player.x_velocity = 0

    if keys[pygame.K_w]:
        player.y_velocity = -player.speed
    elif keys[pygame.K_s]:
        player.y_velocity = player.speed
    else:
        player.y_velocity = 0

    player.update()

    if check_collision(player, rat):
        player.get_damage()
        print("you lose!")

    if check_collision(player, cat):
        print("you win!")

    redrawGameWindow()

pygame.quit()