
# import pygame

# class Player(pygame.sprite.sprite):
#     COLOR = (255, 0,0)
#     x_coord =0
#     y_coord =0
#     def __init__ (self, x_coord, y_coord, width, height):
#         self.rect = pygame.Rect(x, y, width, height)
#         self.x_velocity = 0
#         self.y_velocity = 0
#         self.mask = None
#         self.direction = "left"
#         self.animation_count = 0

#     def move(self, dx,dy):
#         self.rect.x_coord += dx
#         self.rect.y += dy

#     def move_left (self, velocity):
#         self.x_velocity = -vel       
#         if self.direction != "left":
#             self.direction = "left"
#             self.animation_count =0

#     def move_right (self,velcoity):
#         self.x_velocity = vel
#         if self.direction != "right":
#             self.direction = "right"
#             self.animation_count =0

#     def loop(self,fps):
#         self.move(self.x_velocity, self.y_velocity)

#     def draw(self, win):
#         pygame.draw.rect(win, self.COLOR, self.rect)

import pygame


class Player:
    def __init__ (self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos - list(pos)
        self.size = size
        self.velocity = [0,0]

    def update(self, movement = (0,0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    def render (self, surf):
        surf.blit(self.game.assets["player"], self.pos)