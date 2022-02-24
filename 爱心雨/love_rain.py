import sys
import pygame

pygame.init()
size = width, height = 480*2, 270*2
black = 0, 0, 0
screen = pygame.display.set_mode(size)

pygame.mixer.music.load('爱.mp3')   # 载入背景音乐文件
pygame.mixer.music.set_volume(0.3)

pygame.mixer.music.play(-1)

love_hearts, heart_rects = [], []

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            love_img = pygame.image.load('love.png')
            here = pygame.mouse.get_pos()
            init_rect = love_img.get_rect().move(here)
            love_hearts.append(love_img)
            heart_rects.append(init_rect)

    for i in range(len(love_hearts)):
        update_heart_rect = heart_rects[i].move([0, 1])
        heart_rects[i] = update_heart_rect
        # 处理边界
        if update_heart_rect.top > height:
            here2 = [heart_rects[i].left, -heart_rects[i].height]
            update_heart_rect = love_img.get_rect().move(here2)
            heart_rects[i] = update_heart_rect

    screen.fill(black)
    for heart, heart_rect in zip(love_hearts, heart_rects):
        screen.blit(heart, heart_rect)

    pygame.display.flip()
