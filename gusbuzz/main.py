import sys

import pygame

from assets.background import BackGround

size = width, height = 900, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

pygame.mixer.init()
pygame.mixer.music.load('resources/sounds/Game_Tune_1_Sample_1.mp3')
pygame.mixer.music.play(-1)

backGround = BackGround('resources/images/game_image.jpg', [0, 0])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(black)
        screen.blit(backGround.image, backGround.rect)
        pygame.display.flip()
