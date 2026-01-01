import pygame
class Wall:
    def __init__(self,screen1):
        self.screen=screen1
        self.image=pygame.image.load('pictures/wall.png')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery+40
    def blitme(self):#նկարտ ավելացնելու համար
        self.screen.blit(self.image, self.rect)