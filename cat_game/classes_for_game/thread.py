import pygame
class Thread:
    def __init__(self,screen1):
        self.screen=screen1
        self.image=pygame.image.load('pictures/thread.png')
        self.rect = self.image.get_rect()#նկարի սահմանները իմանալու համար
        self.screen_rect = screen1.get_rect()#տարածության սահմանները իմանալու համար
        self.rect.centerx=self.screen_rect.centerx+30# կենտրոն
        self.rect.bottom=self.screen_rect.bottom# եզր
        self.speed=1
        self.width=self.screen_rect.width
    def blitme(self):
        self.screen.blit(self.image, self.rect)