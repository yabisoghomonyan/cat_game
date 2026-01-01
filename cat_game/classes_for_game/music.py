import pygame
class Music:
    def __init__(self,screen1):
        self.screen=screen1
        self.image=pygame.image.load('pictures/music.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen1.get_rect()
    def blitme(self):#նկարտ ավելացնելու համար
        self.screen.blit(self.image, self.rect)