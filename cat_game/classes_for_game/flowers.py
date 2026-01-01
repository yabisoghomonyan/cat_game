import pygame
class Flowers:
    def __init__(self,screen1):
        self.screen=screen1
        self.image1=pygame.image.load('pictures/flower1.png')
        self.image2=pygame.image.load('pictures/flower2.png')
        self.image3=pygame.image.load('pictures/flower3.png')
        self.rect1=self.image1.get_rect()
        self.rect2=self.image2.get_rect()
        self.rect3=self.image3.get_rect()
        self.screen_rect=screen1.get_rect()
    def blitme(self):
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)
        self.screen.blit(self.image3, self.rect3)