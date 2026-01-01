import pygame
class Cabinet:
    def __init__(self,screen1):
        self.screen=screen1
        self.image=pygame.image.load('pictures/cabinet.png')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.x=self.screen_rect.left
        self.rect.bottom=self.screen_rect.bottom
    def blitme(self):#նկարտ ավելացնելու համար
        self.screen.blit(self.image, self.rect)