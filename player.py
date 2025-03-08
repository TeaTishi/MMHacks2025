
x_coord =0
y_coord =0

class Player(pygame.sprite.sprite):
    COLOR = (255, 0,0)
    def __init__ (self, x_coord, y_coord, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_velocity = 0
        self.y_velocity = 0
        self.mask = None

    def move(self, dx,dy):
        self.rect.x_coord += dx
        self.rect.y += dy

    def move_left (self, velocity):
        self.x_velocity = -vel

    def move_right (self,velcoity):
        self.x_velocity = +vel