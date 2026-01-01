import pygame
class Cat:
    def __init__(self,screen1):
        self.screen=screen1
        self.image=pygame.image.load('pictures/cat.png').convert_alpha()
        self.image_right=pygame.transform.flip(self.image, True, False) 
        self.image_left=pygame.transform.flip(self.image, False, False) 
        self.rect = self.image.get_rect()#նկարի սահմանները իմանալու համար
        self.screen_rect = screen1.get_rect()#տարածության սահմանները իմանալու համար
        self.rect.centerx=self.screen_rect.centerx# կենտրոն
        self.rect.bottom=self.screen_rect.bottom# եզր
        self.jumping=False#թռնելու համար
        self.falling=False#իջնելու համար
        self.moving_right=False
        self.moving_left=False
        self.gravity= 1
        self.speed=1
        self.color1=(100, 50, 9)
        self.jump_start_y =0
        self.jump_height=150
        self.height=self.image.get_height()
        self.bottom_jump=self.rect.bottom
        self.eaten=0
        self.paused=False
    def blitme(self):#նկարտ ավելացնելու համար
        self.screen.blit(self.image, self.rect)
    def face_right(self):
        self.image = self.image_right
    def face_left(self):
        self.image=self.image_left