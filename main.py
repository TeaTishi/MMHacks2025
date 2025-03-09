
Bobwillrule
bobwillrule
Invisible

Tishi — Today at 9:48 PM
I think we gotta shrink screen'
Ka — Today at 9:48 PM
ohhh that looks really good
Tishi — Today at 9:48 PM
lemme try to fix
Ka — Today at 9:49 PM
waitt you actually have the "X" button to get out of the game
Tishi — Today at 9:50 PM
Image
it keep's printinf u win
Ka — Today at 9:50 PM
oh you can delete that. i had that before just to test the collisions'
Tishi — Today at 9:52 PM
okkk
IDK WHY HE SUDDENLY BECAME SLOW
Ka — Today at 9:53 PM
😭
Tishi — Today at 9:53 PM
wait wait
what exactly changed
Ka — Today at 9:54 PM
i think i might've pushed but there wasn't much changed except for resolving a merge conflict. i think that was what i last pushed
i didn't push that recently though. probably in the last 10 mins
Tishi — Today at 9:55 PM
could i revert then
Ka — Today at 10:01 PM
i think maybe?
i have never done that though before. i think we need like a "commit number from github"
Tishi — Today at 10:02 PM
its okay i got ittt
Ka — Today at 10:05 PM
wait
i'm going to push right now
Tishi — Today at 10:05 PM
okkk
Ka — Today at 10:07 PM
wait never mind
I'll be a couple mins
Tishi — Today at 10:07 PM
LMAo
okok
imma push new rat photos then
Ka — Today at 10:07 PM
i'm working in the main if that's ok
I'm just trying to put all the code that's creating the board into a function/method so that i can try and put a screen function/method before it
Tishi — Today at 10:08 PM
okkk
i think as long as u dont need testing and health then should be good
Ka — Today at 10:15 PM
ok i'm going to push in like a min
sorry i've just been trying to fix merge conflicts 😅
Tishi — Today at 10:17 PM
LMAO
Ka — Today at 10:18 PM
never mind again (more merge conflicts 😦 
Tishi — Today at 10:19 PM
:000
Ka — Today at 10:20 PM
import pygame
import os

from health import redrawGameWindow

# WIDTH = 1920
Expand
message.txt
10 KB
do you guys mind copying and pasting this in to see if it works on your end? i think because what i'm doing changes so many line of code, it's causing merge conflicts, but it's pretty much the same code except now it's calling functions to create the game
Thanks 😊
Ka — Today at 10:24 PM
wait I'm so sorry, wrong one. I'll send the new one in a bit (it keeps deleting each time there's a conflict)
Tishi — Today at 10:26 PM
😭😭😭
Ka — Today at 10:27 PM
import sys

import pygame
import os

from testing import scroll_threshold
Expand
message.txt
14 KB
Tishi — Today at 10:28 PM
is this for main?
Ka — Today at 10:29 PM
yeah that's what i have in my branch and i can't seem to merge and push it with the main
i'll keep trying though
Tishi — Today at 10:30 PM
Okay i added it
but it just looks the same
Ka — Today at 10:30 PM
okk thanks!
Tishi — Today at 10:30 PM
Image
Ka — Today at 10:31 PM
it should be basically the same, except i just made a new function to create the the game (the function is called createGame()  )
Tishi — Today at 10:31 PM
okkk
sounds good
okay pushed
Image
evil rat
Ka — Today at 10:33 PM
love it
Tishi — Today at 10:33 PM
looks disgusting
hugo's working on the map layout and stuff
Ka — Today at 10:33 PM
ok no worries
Tishi — Today at 10:34 PM
wait can u run and show me what the screen looks like for u
I'm trying to move the timer but i can see anything
Ka — Today at 10:34 PM
ok
Tishi — Today at 10:34 PM
tyty
Ka — Today at 10:34 PM
let me just clone again because the merge conflicts won't let me pull
Tishi — Today at 10:34 PM
okkk
Ka — Today at 10:37 PM
Image
^ I see this on my end
Also, thank you so much for pushing the change earlier!
Tishi — Today at 10:38 PM
okkkk
thank you!
woah health so perfectly placed
Tishi — Today at 10:38 PM
OFC
Bobwillrule — Today at 10:40 PM
Guys can I push main pls
Tishi — Today at 10:40 PM
sure!
Bobwillrule — Today at 10:40 PM
Or copy into main then push
Tishi — Today at 10:40 PM
@Ka that good with u
Ka — Today at 10:40 PM
I pushed
Yes, I'm done with main
Bobwillrule — Today at 10:41 PM
ok i will pull
Tishi — Today at 10:46 PM
2 windows open when we press play in main.py
Ka — Today at 10:47 PM
yeah!
i was just about to say
the first one is the new version (which looks great by the way) and then the second one is the older version
Tishi — Today at 10:49 PM
hugo pushed
map looks so good
Bobwillrule — Today at 10:49 PM
i pushed
Ka — Today at 10:50 PM
ok
Tishi — Today at 10:50 PM
To do:
scroll fix
start screen
game over
timer
change rats as progressed
health
cat
rats
map
acid
stop player from exiting game left and right
walking animation?
Ka — Today at 10:54 PM
i still have 2 windows showing...
Tishi — Today at 10:54 PM
Image
Ka — Today at 10:54 PM
try removing pygame.init() at the bottom of main.py
Tishi — Today at 10:54 PM
after deleting?
Ka — Today at 10:55 PM
^this might help prevent the 2 windows
Tishi — Today at 10:55 PM
I didnt do anything about the windows yet
Ka — Today at 10:55 PM
Oh I just pulled and I'm still getting another window show uo after closing the initial window
Tishi — Today at 10:57 PM
I dont think anyone did anything to fix it yeyt
Ka — Today at 10:58 PM
ok it's fixed on my end so i can push
Tishi — Today at 10:58 PM
okkk sound sgood
Ka — Today at 11:00 PM
ok it's pushed
Bobwillrule — Today at 11:10 PM
im going to work on main briefly if thats ok
Tishi — Today at 11:20 PM
import sys

import pygame
import os

from testing import scroll_threshold

WIDTH = 1920
HEIGHT = 1080
FPS = 60

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

    def draw(self, screen):
        screen.blit(pygame.image.load("assets/player/player.png"), self.rect)

    def get_damage(self):
        if self.health > 0:
            self.health -= 1

    def get_health(self):
        if self.health > self.max_health:
            self.health -= 1

    def update(self, tilemap):  # Removed scroll_offset here
        self.rect.x += self.x_velocity

        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity

        self.tileCollisions(tilemap)

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

    def tileCollisions(self, tilemap):
        self.onground = False

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
                    self.onground = True


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
... (257 lines left)
Collapse
message.txt
13 KB
﻿
import sys

import pygame
import os

from testing import scroll_threshold

WIDTH = 1920
HEIGHT = 1080
FPS = 60

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

    def draw(self, screen):
        screen.blit(pygame.image.load("assets/player/player.png"), self.rect)

    def get_damage(self):
        if self.health > 0:
            self.health -= 1

    def get_health(self):
        if self.health > self.max_health:
            self.health -= 1

    def update(self, tilemap):  # Removed scroll_offset here
        self.rect.x += self.x_velocity

        self.y_velocity += self.gravity
        self.rect.y += self.y_velocity

        self.tileCollisions(tilemap)

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

    def tileCollisions(self, tilemap):
        self.onground = False

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
                    self.onground = True


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
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        screen.blit(pygame.image.load("assets/cat/cat.png"), self.rect)

        self.rect.x = self.x
        self.rect.y = self.y


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


    def render(self, surf, scroll_offset):  # Added scroll_offset here
        # Render each tile from the tilemap
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            tile_image = self.game.assets[tile['type']][tile['variant']]  # Get the tile image
            x_pos = tile['pos'][0] * self.tile_size  # X coordinate of the tile
            y_pos = tile['pos'][1] * self.tile_size  # Y coordinate of the tile

            # Render the tile on the screen
            surf.blit(tile_image, (x_pos, y_pos - scroll_offset))  # Apply scroll offset

        # Optionally render any offgrid tiles if needed
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


def get_font(size):
    return pygame.font.SysFont('Arial', size)

def check_collision(player, enemy):
    return player.rect.colliderect(enemy.rect)

def check_collision (player, cat):
    return player.rect.colliderect(cat.rect)

def createGame():
    def redrawGameWindow():
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(background_colour, (0, -scroll_offset))  # Background scroll
        screen.blit(background_colour, (0, -scroll_offset + HEIGHT))  # Continuous background scroll
        tilemap.render(screen, scroll_offset)  # Render tiles with scroll

        player.draw(screen)
        rat.draw(screen)
        cat.draw(screen)  # Draw the cat

        # Draw hearts (player's health) in the top-left corner
        heart_x = 250  # X position for the first heart
        heart_y = 150  # Y position for the hearts

        for i in range(player.health):
            screen.blit(game.assets['filled_heart'], (heart_x + i * 40, heart_y))  # Draw filled hearts
        for i in range(player.max_health - player.health):
            screen.blit(game.assets['empty_heart'], (heart_x + (player.health + i) * 40, heart_y))  # Draw empty hearts

        elapsed_time = pygame.time.get_ticks() // 1000
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        timer_text = f"{minutes:02}:{seconds:02}"
        timer_surface = font.render(timer_text, True, (255, 255, 255))
        screen.blit(timer_surface, (WIDTH - 200, 20))
        pygame.display.update()

        pygame.display.update()



    background_colour = pygame.image.load('assets/background.png')
    background_colour = pygame.transform.scale(background_colour, (WIDTH, HEIGHT))

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('M')

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 74)

    player = Player(WIDTH / 2, HEIGHT / 2, 50, 50)
    rat = Enemy(100, 100, 100, 100, 1000)
    cat = Cat(WIDTH / 2, HEIGHT / 2, 100, 100, 1000)  # Create cat instance

    sound = Sound(music_path="assets/sound/bgmusic.mp3", volume=0.5)
    sound.play_music()

    game = Game()
    tilemap = Tilemap(game, tile_size=50)

    # Scrolling variables
    scroll_offset = 0
    scroll_threshold = HEIGHT / 3  # Define a threshold for scrolling

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the background image
        screen.blit(background_colour, (0, 0))

        # Update the display
        # pygame.display.flip()

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

        player.update(tilemap)

        # Scroll background when player drops past a certain threshold
        if player.rect.bottom > HEIGHT - scroll_threshold:
            scroll_offset += 10  # Adjust the scrolling speed

        # Check collisions
        if check_collision(player, rat):
            player.get_damage()
            print("you lose!")

        if check_collision(player, cat):
            print("you win!")

        redrawGameWindow()

#pygame.init()
createGame()
message.txt
13 KB