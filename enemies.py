import pygame

class enemies(object):

    walkRight = [pygame.image.load('rightrat.png')]
    walkLeft = [pygame.image.load('leftrat.png')]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.velocity = 3

    def draw(self, screen):
        screen.blit(pygame.image.load('rightrat.png'), (self.x, self.y))