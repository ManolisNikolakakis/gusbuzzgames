# Standard Libraries

import sys
import time

# Pip installed libraries

import pygame

from assets.background import BackGround
from assets import settings

pygame.init()

# Variable used in the game 

score = "0"
font = pygame.font.Font(None, 36)

# Functions used in the game


def load_settings():
    pygame.display.set_caption("Some Video Game")

def load_splash_screen():

    text = font.render("Current Score", True, settings.WHITE)
    screen.blit(text, [10, 10])

    text = font.render("Presented by", True, settings.WHITE)
    screen.blit(text, [450, 300])

    text = font.render("GusBuzzGames", True, settings.RED)
    screen.blit(text, [450, 330])

    time.sleep(3)
    
    text = font.render("PRESS F TO CONTINUE", True, settings.RED)
    screen.blit(text, [450, 420])      

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                return

# Game Script Starting Point

screen = pygame.display.set_mode(settings.SIZE)
screen.fill(settings.BLACK)

load_settings()
load_splash_screen()

pygame.mixer.init()
pygame.mixer.music.load(settings.MAIN_TUNE)
pygame.mixer.music.play(settings.INFINITE_MUSIC_LOOP)

backGround = BackGround(settings.BACKGROUND_IMAGE, settings.BACKGROUND_IMAGE_STARTING_POINT)

text = font.render("Current Score", True, settings.WHITE)
screen.blit(text, [10, 10])
 
text = font.render(score, True, settings.WHITE)
screen.blit(text, [10, 40])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(settings.BLACK)
        screen.blit(backGround.image, backGround.rect)
        pygame.display.flip()

