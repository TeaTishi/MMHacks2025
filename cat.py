import pygame

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

        self.rect.x = self.x
        self.rect.y = self.y
