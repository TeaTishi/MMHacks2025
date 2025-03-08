import pygame


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

    def draw(self, screen):
        screen.blit(pygame.image.load("assets/player/player.png"), self.rect)


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

    def draw(self, screen):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.velocity > 0:
            screen.blit(self.walkRight[0], (self.x, self.y))
        else:
            screen.blit(self.walkLeft[0], (self.x, self.y))

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


pygame.init()

WIDTH = 1920
HEIGHT = 1080
background_colour = (234, 212, 252)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('M')

clock = pygame.time.Clock()
FPS = 60

player = Player(WIDTH / 2, HEIGHT / 2, WIDTH / 2, HEIGHT)
rat = Enemy(100, 100, 100, 100, 1000)

def redrawGameWindow():
    screen.fill(background_colour)
    player.draw(screen)
    rat.draw(screen)
    pygame.display.update()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    redrawGameWindow()

pygame.quit()