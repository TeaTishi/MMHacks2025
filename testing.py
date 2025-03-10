import pygame
import os

WIDTH = 1920
HEIGHT = 1080
background_colour = pygame.image.load('assets/background.png')
background_colour = pygame.transform.scale(background_colour, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('M')

clock = pygame.time.Clock()
FPS = 60

pygame.font.init()
font = pygame.font.SysFont('Arial', 74)

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
        self.onground = True
        self.health = 3
        self.max_health = 3
        self.jump_sound = pygame.mixer.Sound("assets/sound/jump.wav")

    def draw(self, screen):
        if self.x_velocity >= 0:
            screen.blit(pygame.image.load("assets/player/player.png"), self.rect)
        elif self.x_velocity < 0:
            screen.blit(pygame.image.load("assets/player/playerLeft.png"), self.rect)

    def get_damage(self):
        if self.health > 0:
            self.health -= 1

    def get_health(self):
        if self.health > self.max_health:
            self.health -= 1

    def update(self, tilemap, scroll_offset):
        self.rect.x += self.x_velocity
        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity

        self.tileCollisions(tilemap, scroll_offset)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def jump(self):
        if self.onground:
            self.y_velocity = self.jumppower
            self.onground = False
            self.jump_sound.play()

    def tileCollisions(self, tilemap, scroll_offset):
        self.onground = False
        for loc in tilemap.tilemap:
            tile = tilemap.tilemap[loc]
            tile_rect = pygame.Rect(
                tile['pos'][0] * tilemap.tile_size,
                (tile['pos'][1] * tilemap.tile_size) - scroll_offset,  # Adjust Y position with scroll_offset
                tilemap.tile_size,
                tilemap.tile_size
            )

            if self.rect.colliderect(tile_rect):
                # Calculate overlap in x and y directions
                dx = self.rect.centerx - tile_rect.centerx
                dy = self.rect.centery - tile_rect.centery

                # Calculate absolute overlap in x and y directions
                abs_dx = abs(dx)
                abs_dy = abs(dy)

                # Resolve collision based on the direction of overlap
                if abs_dx > abs_dy:
                    # Horizontal collision (left or right)
                    if dx > 0:
                        # Player is to the right of the tile
                        self.rect.left = tile_rect.right
                    else:
                        # Player is to the left of the tile
                        self.rect.right = tile_rect.left
                    self.x_velocity = 0  # Stop horizontal movement
                else:
                    # # Vertical collision (top or bottom)
                    # if dy > 0:
                    #     # Player is below the tile
                    #     self.rect.bottom = tile_rect.top
                    #     self.y_velocity = 0
                    #     self.onground = True
                    # else:
                    #     # Player is above the tile
                    #     self.rect.top = tile_rect.bottom
                    #     self.y_velocity = 0

            # if self.rect.colliderect(tile_rect):
                    if self.y_velocity > 0:
                        self.rect.bottom = tile_rect.top
                        self.y_velocity = 0
                        self.onground = True
                
            #     if self.x_velocity > 0:
            #         self.rect.right = tile_rect.left +1
            #     elif self.x_velocity < 0:
            #         self.rect.left = tile_rect.right -1


class Enemy(object):
    # walkRight = [pygame.image.load('assets/rats/rightrat_resized.png')]
    # walkLeft = [pygame.image.load('assets/rats/leftrat_resized.png')]

    def __init__(self, x, y, width, height, end, walkRight, walkLeft):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.velocity = 2
        self.rect = pygame.Rect(x, y, width, height)
        self.walkRight = walkRight
        self.walkLeft = walkLeft 

    def draw(self, screen, scroll_offset):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.velocity > 0:
            screen.blit(self.walkRight[0], (self.x, self.y - scroll_offset))
        else:
            screen.blit(self.walkLeft[0], (self.x, self.y - scroll_offset))

        self.rect.x = self.x
        self.rect.y = self.y - scroll_offset

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
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collided = False
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, scroll_offset):
        if self.collided:
            screen.blit(pygame.image.load("assets/rats/evilBoss.png"), (self.x, self.y - scroll_offset))
        else:
            screen.blit(pygame.image.load("assets/cat/cat.png"), (self.x, self.y - scroll_offset))
        self.rect.x = self.x
        self.rect.y = self.y - scroll_offset


class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        # Example tilemap generation with tiles placed at specific coordinates

        self.tilemap['16;10'] = {'type': 'grass', 'variant': 0, 'pos': (16, 10)}
        self.tilemap['14;9'] = {'type': 'grass', 'variant': 0, 'pos': (14, 9)}
        self.tilemap['12;8'] = {'type': 'grass', 'variant': 0, 'pos': (12, 8)}
        self.tilemap['10;7'] = {'type': 'grass', 'variant': 0, 'pos': (10, 7)}
        self.tilemap['8;6'] = {'type': 'grass', 'variant': 0, 'pos': (8, 6)}


        for i in range(28):
            self.tilemap[str(7 + i) + ';14'] = {'type': 'grass', 'variant': 0, 'pos': (7 + i, 14)}
            self.tilemap[str(i) + ';21'] = {'type': 'grass', 'variant': 0, 'pos': (i, 21)}
            self.tilemap[str(7 + i) + ';28'] = {'type': 'grass', 'variant': 0, 'pos': (7 + i, 28)}

        for i in range(9):
            self.tilemap['7;' + str(5+i)] = {'type': 'grass', 'variant': 0, 'pos': (7, 5+i)}

        for i in range(4):
            self.tilemap[str(18+i) + ';11'] = {'type': 'grass', 'variant': 0, 'pos': (18+i, 11)}
            

        for i in range(60):
            self.tilemap['1;' + str(i)] = {'type': 'grass', 'variant': 0, 'pos': (1, i)}
            self.tilemap['34;' + str(i)] = {'type': 'grass', 'variant': 0, 'pos': (34, i)}

            self.tilemap['2;' + str(i)] = {'type': 'grass', 'variant': 0, 'pos': (2, i)}
            self.tilemap['35;' + str(i)] = {'type': 'grass', 'variant': 0, 'pos': (35, i)}

            self.tilemap['3;' + str(i)] = {'type': 'grass', 'variant': 0, 'pos': (3, i)}
            self.tilemap['36;' + str(i)] = {'type': 'grass', 'variant': 0, 'pos': (36, i)}

            self.tilemap['4;' + str(i)] = {'type': 'grass', 'variant': 0, 'pos': (4, i)}
            self.tilemap['33;' + str(i)] = {'type': 'grass', 'variant': 0, 'pos': (33, i)}

        for i in range(36):
            self.tilemap[str(i) + ';60'] = {'type': 'grass', 'variant': 0, 'pos': (i, 60)}




    def render(self, surf, scroll_offset):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            tile_image = self.game.assets[tile['type']][tile['variant']]  # Get the tile image
            x_pos = tile['pos'][0] * self.tile_size  # X coordinate of the tile
            y_pos = tile['pos'][1] * self.tile_size  # Y coordinate of the tile

            surf.blit(tile_image, (x_pos, y_pos - scroll_offset))

        for tile in self.offgrid_tiles:
            tile_image = self.game.assets[tile['type']][tile['variant']]
            surf.blit(tile_image, tile['pos'])


class Game:
    def __init__(self):
        self.assets = {}
        self.load_assets()

    def load_assets(self):
        img_path = 'assets/grass/1.png'
        if os.path.exists(img_path):
            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (50, 50))
            img = img.convert()  # Convert the image for better performance
            self.assets['grass'] = [img]
        else:
            print(f"Error: {img_path} not found!")

        # Load heart images
        empty_heart_path = 'assets/heart/emptyHeart.png'
        filled_heart_path = 'assets/heart/filledHeart.png'

        if os.path.exists(empty_heart_path) and os.path.exists(filled_heart_path):
            self.assets['empty_heart'] = pygame.transform.scale(pygame.image.load(empty_heart_path), (30, 30))
            self.assets['filled_heart'] = pygame.transform.scale(pygame.image.load(filled_heart_path), (30, 30))
        else:
            print(f"Error: Heart images not found!")

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

def start_screen():
    background_colour = pygame.image.load('assets/background.png')
    background_colour = pygame.transform.scale(background_colour, (WIDTH, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Start the game if SPACE is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

        # Draw start screen
        # screen.fill((0, 0, 0))  # Black background
        


        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        start_text = font.render("(Press SPACE to Start)", True, (255, 255, 255))
        title = font.render("SEWAGE SEARCH", True, (255, 0, 0))
        
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 50))
        screen.blit(title, (WIDTH // 2 - start_text.get_width() // 2 + 45, HEIGHT // 2 - 105))

        pygame.display.update()

# def start_screen(): FOR NORMAL BG
#     # Load and scale the background image
#     background_colour = pygame.image.load('assets/background.png')
#     background_colour = pygame.transform.scale(background_colour, (WIDTH, HEIGHT))

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return

#             # Start the game if SPACE is pressed
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     return

#         # Draw the background image
#         screen.blit(background_colour, (0, 0))

#         # Draw start screen text
#         start_text = font.render("Press SPACE to Start", True, (255, 255, 255))
#         title = font.render("SEWAGE SEARCH", True, (255, 255, 255))
#         screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 50))
#         screen.blit(title, (WIDTH // 2 - start_text.get_width() // 2 + 25, HEIGHT // 2 - 105))

#         pygame.display.update()

start_screen()

player = Player(WIDTH / 2, HEIGHT / 2, 50, 50)

rat1_walkRight = [pygame.image.load("assets/rats/cuteRat2.png")]
rat1_walkLeft = [pygame.image.load("assets/rats/cuteRatLeft2.png")]
rat2_walkLeft = [pygame.image.load("assets/rats/leftrat_resized.png")]
rat2_walkRight = [pygame.image.load("assets/rats/rightrat_resized.png")]
rat = Enemy(500, 650, 100, 100, 1500, rat1_walkRight, rat1_walkLeft)
rat3 = Enemy(620, 1000, 100, 100, 1300, rat1_walkRight, rat1_walkLeft)
rat2 = Enemy(100, 1317, 100, 100, 1200, rat2_walkRight, rat2_walkLeft)

rat4 = Enemy(620, 1450, 100, 100, 1300, rat1_walkRight, rat1_walkLeft)
rat5 = Enemy(620, 2750, 100, 100, 1300, rat2_walkRight, rat2_walkLeft)
rat6 = Enemy(620, 1500, 100, 100, 1300, rat2_walkRight, rat2_walkLeft)

rat7 = Enemy(620, 2000, 100, 100, 1300, rat2_walkRight, rat2_walkLeft)
rat8 = Enemy(620, 2500, 100, 100, 1300, rat2_walkRight, rat2_walkLeft)
rat9 = Enemy(620, 3000, 500, 500, 1300, rat2_walkRight, rat2_walkLeft)



cat = Cat(WIDTH/2, 2950, 100, 100, 1000)  # Create cat instance

sound = Sound(music_path="assets/sound/bgmusic.mp3", volume=0.5)
sound.play_music()

game = Game()
tilemap = Tilemap(game, tile_size=50)

# Scrolling variables
scroll_offset = 0
scroll_threshold = HEIGHT / 3 # Define a threshold for scrolling

def redrawGameWindow():
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(background_colour, (0, -scroll_offset))  # Background scroll
    screen.blit(background_colour, (0, -scroll_offset + HEIGHT))  # Continuous background scroll
    tilemap.render(screen, scroll_offset)  # Render tiles with scroll

    player.draw(screen)
    rat.draw(screen, scroll_offset)
    rat3.draw(screen, scroll_offset)
    rat2.draw(screen, scroll_offset)
    rat6.draw(screen, scroll_offset)
    rat4.draw(screen, scroll_offset)
    rat5.draw(screen, scroll_offset)

    rat7.draw(screen, scroll_offset)
    rat8.draw(screen, scroll_offset)
    rat9.draw(screen, scroll_offset)



    cat.draw(screen, scroll_offset)  # Draw the cat

    # Draw hearts (player's health) in the top-left corner
    heart_x = 250  # X position for the first heart
    heart_y = 150  # Y position for the hearts

    for i in range(player.health):
        screen.blit(game.assets['filled_heart'], (heart_x + i * 40, heart_y))  # Draw filled hearts
    for i in range(player.max_health - player.health):
        screen.blit(game.assets['empty_heart'], (heart_x + (player.health + i) * 40, heart_y))  # Draw empty hearts

    pygame.display.update()

def check_collision(player, enemy):
    return player.rect.colliderect(enemy.rect)  

def game_over_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Restart the game if 'R' is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    return

        # Draw game over screen
        screen.fill((0, 0, 0))  # Black background
        game_over_text = font.render("Game Over", True, (255, 0, 0))  # Red text
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))  # White text
        quit_text = font.render("Press Q to Quit", True, (255, 255, 255))  # White text

        # Center the text on the screen
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))
        screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 100))

        pygame.display.update()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x_velocity = -player.speed
    elif keys[pygame.K_d]:
        player.x_velocity = player.speed
    else:
        player.x_velocity = 0

    if keys[pygame.K_w]:
        player.jump()

    player.update(tilemap, scroll_offset)

    # Scroll background when player drops past a certain threshold
    if player.rect.bottom > HEIGHT - scroll_threshold:
        scroll_offset += 10  # Adjust the scrolling speed

    # Check collisions
    if check_collision(player, rat):
        player.get_damage()
    
    if check_collision(player, cat):
        cat.collided = True
        result = game_over_screen()
        if result == "restart":
            # Reset game state
            player = Player(WIDTH / 2, HEIGHT / 2, 50, 50)
            scroll_offset = 0
        else:
            running = False


    if player.health <= 0:
        result = game_over_screen()
        if result == "restart":
            # Reset game state
            player = Player(WIDTH / 2, HEIGHT / 2, 50, 50)
            scroll_offset = 0
        else:
            running = False

    redrawGameWindow()

pygame.quit()