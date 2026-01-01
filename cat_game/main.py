import pygame
from pygame.sprite import Group
import pygame
from pygame.sprite import Group

from classes_for_game import Cat, Thread, Fish, Cabinet, Wall, Flowers, Music
import function as fun
def start():
    pygame.init()
    screen=pygame.display.set_mode((800,800))
    pygame.display.set_caption('Game')  
    screen1=pygame.Surface((400,400))
    my_cat=Cat(screen1)
    my_thread=Thread(screen1)
    my_cabinet=Cabinet(screen1)
    my_music=Music(screen1)
    my_wall=Wall(screen1)
    my_flowers=Flowers(screen1)
    fishes=Group()
    color=(255, 192, 203)
    offset = (200, 200)
    sound=pygame.mixer.Sound('music/cat_music.mp3')
    while True:
        screen.fill(color)
        screen1.fill(my_cat.color1)
        fun.music_rect(my_music,my_cabinet)
        my_music.blitme()
        my_wall.blitme()
        fun.flower_rect(my_flowers,my_wall)
        my_flowers.blitme()
        my_cat.blitme()
        my_thread.blitme()
        my_cabinet.blitme()
        fun.fish_movements(my_cat,fishes,my_thread,my_cabinet,my_wall)
        fishes.draw(screen1)# Նկարել բոլոր ձկները screen1-ի վրա
        screen.blit(screen1,offset)#screen-ին ավելացնում է screen1 offset  կետից սկսած
        fun.cat_movements(my_cat,my_thread,fishes,offset,Fish,screen,my_cabinet,my_wall)
        if my_cat.rect.colliderect(my_music.rect):
            sound.play()
        pygame.display.update()
start()