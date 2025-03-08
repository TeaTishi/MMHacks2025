import pygame

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

class Health:
    def __init__(self, max_health, heart_filled_path, heart_unfilled_path, x=10, y=10, spacing=5):
        self.max_health = max_health
        self.heart_filled = pygame.image.load(heart_filled_path)
        self.heart_unfilled = pygame.image.load(heart_unfilled_path)  # Load unfilled heart image
        self.heart_size = self.heart_filled.get_size()  # Get the size of the heart images
        self.x = x
        self.y = y
        self.spacing = spacing

    def draw(self, screen, current_health):
        for i in range(self.max_health):
            if i < current_health:
                screen.blit(self.heart_filled, (self.x + i * (self.heart_size[0] + self.spacing), self.y))
            else:
                screen.blit(self.heart_unfilled, (self.x + i * (self.heart_size[0] + self.spacing), self.y))

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

health_display = Health(
    max_health=3,
    heart_filled_path="assets/heart/filledHeart.png",
    heart_unfilled_path="assets/heart/emptyHeart.png",
    x=10,
    y=10,
    spacing=5
)

player = Player(WIDTH / 2, HEIGHT / 2, 50, 50)
rat = Enemy(100, 100, 100, 100, 1000)

def redrawGameWindow():
    #screen.fill(background_colour)
    player.draw(screen)
    rat.draw(screen)
    health_display.draw(screen, player.health)
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
    redrawGameWindow()


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

    redrawGameWindow()

pygame.quit()