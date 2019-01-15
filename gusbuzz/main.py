import sys

import pygame

from assets.background import BackGround
from assets import settings

screen = pygame.display.set_mode(settings.SIZE)

pygame.mixer.init()
pygame.mixer.music.load(settings.MAIN_TUNE)
pygame.mixer.music.play(settings.INFINITE_MUSIC_LOOP)

backGround = BackGround(settings.BACKGROUND_IMAGE, settings.BACKGROUND_IMAGE_STARTING_POINT)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(settings.BLACK)
        screen.blit(backGround.image, backGround.rect)
        pygame.display.flip()
