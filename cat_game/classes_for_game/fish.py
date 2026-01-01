import pygame
import random
from pygame.sprite import Sprite
class Fish(Sprite):
    def __init__(self,screen1):
        super().__init__()
        self.screen=screen1
        self.image1=pygame.image.load('pictures/fish1.png')
        self.image2=pygame.image.load('pictures/fish2.png')
        self.image = random.choice([self.image1,self.image2])
        self.rect = self.image.get_rect()
        self.screen_rect = screen1.get_rect()
