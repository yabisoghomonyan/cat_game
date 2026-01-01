import pygame
import sys
PAUSE_OVER = pygame.USEREVENT + 
def cat_fitting_with_fish(fishes, offset,Fish,screen):
        fish=Fish(screen)
        fishes.add(fish)
        mx, my = pygame.mouse.get_pos()
        local_x = mx - offset[0]
        local_y = my - offset[1]
        fish.rect.center = (local_x, local_y)
def cat_jump(cat,thread,fishes,offset,Fish,screen,cabinet,wall):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == PAUSE_OVER:
            cat.paused = False
            print(" I am hungry")
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                on=cat.rect.bottom>=cat.screen_rect.bottom
                off=cat.rect.colliderect(thread.rect) or cat.rect.bottom==thread.rect.top
                it=cat.rect.bottom==cabinet.rect.top
                out=cat.rect.bottom==wall.rect.top 
                if on or off or it or out:
                    cat.jumping=True
                    cat.falling=False
            if event.key==pygame.K_RIGHT:
                cat.moving_right=True
            if event.key==pygame.K_LEFT:
                cat.moving_left=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                cat.moving_right=False
            if event.key==pygame.K_LEFT:
                cat.moving_left=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                cat_fitting_with_fish(fishes,offset,Fish,screen)
def cat_jumps_to_the_wall(cat,wall):
    if cat.jumping:
        if not hasattr(cat, "bottom_jump"):
            cat.bottom_jump = cat.rect.bottom
        cat.rect.y -= cat.gravity
        if cat.bottom_jump - cat.rect.bottom >= cat.jump_height :
            cat.jumping = False
            cat.falling = True
            delattr(cat, "bottom_jump")
        if cat.rect.top<=wall.rect.bottom and cat.rect.colliderect(wall.rect) :
            cat.jumping = False
            cat.falling = True
def cat_falls(cat,thread,cabinet,wall):
    if cat.falling and cat.rect.bottom<cat.screen_rect.bottom :
        cat.rect.y+=cat.gravity
        off = cat.rect.colliderect(thread.rect) 
        it = cat.rect.colliderect(cabinet.rect)
        out= cat.rect.colliderect(wall.rect)
        if off:
            if cat.rect.centerx>=thread.rect.right:
                thread.rect.left-=cat.rect.width/2
                cat.rect.left=thread.rect.right
                cat.falling = True
            if cat.rect.centerx<=thread.rect.left:
                thread.rect.left+=cat.rect.width/2
                cat.rect.right=thread.rect.left
                cat.falling = True
            else:
                cat.rect.bottom=thread.rect.top
                cat.falling=False
        if it:
            if cat.rect.centerx >= cabinet.rect.right:
                cat.rect.left=cabinet.rect.right
                cat.falling = True
            else:
                cat.rect.bottom=cabinet.rect.top
                cat.falling=False
        if out:
            if cat.rect.centerx>=wall.rect.right:
                cat.rect.left=wall.rect.right
                cat.falling = True
            if cat.rect.centerx<=wall.rect.left:
                cat.rect.right=wall.rect.left
                cat.falling = True
            else:
                cat.rect.bottom=wall.rect.top
                cat.falling=False
        if not it:
            cat.falling=True
        if not off:
            cat.falling=True
        if cat.rect.bottom>=cat.screen_rect.bottom:
            cat.falling=False
def cat_moves_to_left(thread, cat,cabinet):
    if cat.moving_left:
        if cat.rect.left>cabinet.rect.left and not cat.rect.colliderect(cabinet.rect):
            cat.face_left()
            cat.rect.centerx -= cat.speed
            if cat.rect.colliderect(thread.rect):
                thread.rect.right-= thread.speed
                cat.rect.left = thread.rect.right
        if  cat.rect.colliderect(cabinet.rect):
            cat.rect.left=cabinet.rect.right
def cat_moves_to_right(thread, cat):
    if cat.moving_right and cat.rect.right < cat.screen_rect.right :
        cat.face_right()
        cat.rect.centerx += cat.speed
        if cat.rect.colliderect(thread.rect):
            thread.rect.left+= thread.speed
            cat.rect.right = thread.rect.left
def bounch_from_eges(cat,thread,cabinet):
    if thread.rect.right>=cat.screen_rect.right:
        thread.rect.right=cat.screen_rect.right-cat.rect.width-5
    if thread.rect.colliderect(cabinet.rect):
        thread.rect.left=cabinet.rect.right+cat.rect.width+10
def cat_eats_fish(fishes, cat):
    if getattr(cat, "paused", False):
        return  
    if not hasattr(cat, "eaten"):
        cat.eaten = 0

    for fish in fishes.copy():
        if cat.rect.colliderect(fish.rect) and cat.eaten < 3:
            fishes.remove(fish)
            cat.eaten += 1
            print(cat.eaten)
            if cat.eaten >= 3:
                delattr(cat, "eaten")
                cat.paused = True
                print(" I am full ")
                pygame.time.set_timer(PAUSE_OVER, 30_000, loops=1)

def fish_direction(fishes,thread,cabinet,wall):
    for fish in fishes:
        if fish.rect.bottom < fish.screen_rect.bottom:
            fish.rect.y += 2
        if fish.rect.colliderect(thread.rect):
            fish.rect.bottom=thread.rect.top
        if fish.rect.colliderect(cabinet.rect):
            fish.rect.bottom=cabinet.rect.top
        if fish.rect.colliderect(wall.rect):
            fish.rect.bottom=wall.rect.top
def music_rect(music,cabel):
    music.rect.bottom=cabel.rect.top
    music.rect.left=music.screen_rect.left
def flower_rect(flowers,wall):
    flowers.rect1.bottom=flowers.rect2.bottom=flowers.rect3.bottom=wall.rect.top
    flowers.rect1.centerx=wall.rect.left+20
    flowers.rect2.centerx=wall.rect.left+55
    flowers.rect3.centerx=wall.rect.right-20
def cat_movements(cat,thread,fishes,offset,Fish,screen,cabinet,wall):
    cat_jump(cat,thread,fishes,offset,Fish,screen,cabinet,wall)
    cat_jumps_to_the_wall(cat,wall)
    cat_falls(cat,thread,cabinet,wall)
    cat_moves_to_left(thread, cat,cabinet)
    cat_moves_to_right(thread, cat)
    bounch_from_eges(cat,thread,cabinet)
def fish_movements(cat,fishes,thread,cabinet,wall):
    cat_eats_fish(fishes, cat)

    fish_direction(fishes,thread,cabinet,wall)
