import os 
import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).conver()
    img.set_colerkey((0, 0, 0))
    return img

def load_images(path):iamges = []
for img_name in os.listdir(BASE_IMG_PATH + path):
    images.append(load_image(path + '/' +img_name))