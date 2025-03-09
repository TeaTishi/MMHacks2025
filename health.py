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
        self.speed = 10
        self.gravity = 3
        self.jumppower = -30
        self.gravity = 3
        self.jumppower = -30
        self.onground = True
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

    def update(self,tilemap):
        self.rect.x += self.x_velocity

        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity

        self.tileCollisions(tilemap)
        
        # if self.rect.bottom >= HEIGHT:
        #     self.rect.bottom = HEIGHT
        #     self.y_velocity = 0
        #     self.on_ground = True
        # else:
        #     self.on_ground = False

        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.right > WIDTH:
        #     self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def jump(self):
        if self.on_ground:
            self.y_velocity = self.jumppower
            self.on_ground = False

    def tileCollisions(self, tilemap):
        self.on_ground = False

        for loc in tilemap.tilemap:
            tile = tilemap.tilemap[loc]
            tile_rect = pygame.Rect(
                tile['pos'][0] * tilemap.tile_size,
                tile['pos'][1] * tilemap.tile_size,
                tilemap.tile_size,
                tilemap.tile_size
            )

            if self.rect.colliderect(tile_rect):
                if self.y_velocity > 0:
                    self.rect.bottom = tile_rect.top
                    self.y_velocity = 0
                    self.on_ground = True
                # elif self.y_velocity < 0:
                #     self.rect.top = tile_rect.bottom
                #     self.y_velocity = 0



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
        for i in range(28):
            self.tilemap[str(3 + i) + ';7'] = {'type': 'grass', 'variant': 0, 'pos': (3 + i, 7)}
            self.tilemap[str(7 + i) + ';14'] = {'type': 'grass', 'variant': 0, 'pos': (7 + i, 14)} 

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

class Sound:
    def __init__(self, music_path, volume=0.5):
        pygame.mixer.init()

        self.music_path = music_path
        self.volume = volume
        self.load_music()

    def load_music(self):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.set_volume(self.volume)

    def play_music(self, loops=-1):
        pygame.mixer.music.play(loops)

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_sound_effect(self, sound_path, volume=0.5):
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(volume)
        sound.play()


pygame.init()

WIDTH = 1020
HEIGHT = 680
FPS = 60
#background_colour = (234, 212, 252)
background_colour = pygame.image.load('assets/background.png')
background_colour = pygame.transform.scale(background_colour, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('M')

clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)

player = Player(WIDTH / 2, HEIGHT / 2, 50, 50)
rat = Enemy(100, 300, 100, 100, 1000)
cat= Cat(WIDTH / 2, HEIGHT / 2, WIDTH / 2, HEIGHT, 1000)

sound = Sound(music_path="assets/sound/bgmusic.mp3", volume=0.5)
sound.play_music()

game = Game() 

tilemap = Tilemap(game, tile_size=50)

def redrawGameWindow():
    #screen.fill(background_colour)
    tilemap.render(screen) 
    player.draw(screen)
    rat.draw(screen)
    cat.draw(screen)

    elapsed_time = pygame.time.get_ticks() // 1000
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    timer_text = f"{minutes:02}:{seconds:02}"
    timer_surface = font.render(timer_text, True, (255, 255, 255))
    screen.blit(timer_surface, (WIDTH - 200, 20))
    pygame.display.update()

def check_collision(player, enemy):
    return player.rect.colliderect(enemy.rect)

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
        player.jump()

    player.update(tilemap)

    if check_collision(player, rat):
        player.get_damage()

    redrawGameWindow()

pygame.quit()