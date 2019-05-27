import sys

import pygame

from assets.background import BackGround
from assets import settings

pygame.init()

# Variable used in the game 

score = 0
font = pygame.font.Font(None, 36)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Functions used in the game


def load_settings():
    pygame.display.set_caption("Some Video Game")

def load_splash_screen():
    text = font.render("Presented by", True, WHITE)
    screen.blit(text, [450, 300])
 
    text = font.render("GusBuzzGames", True, RED)
    screen.blit(text, [450, 330])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            return
        elif event.type == pygame.KEYDOWN:
            return

# Game Script Starting Point

screen = pygame.display.set_mode(settings.SIZE)

load_settings()
load_splash_screen()

pygame.mixer.init()
pygame.mixer.music.load(settings.MAIN_TUNE)
pygame.mixer.music.play(settings.INFINITE_MUSIC_LOOP)

backGround = BackGround(settings.BACKGROUND_IMAGE, settings.BACKGROUND_IMAGE_STARTING_POINT)

text = font.render("Current Score", True, WHITE)
screen.blit(text, [10, 10])
 
text = font.render(score, True, WHITE)
screen.blit(text, [10, 40])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen.fill(settings.BLACK)
        screen.blit(backGround.image, backGround.rect)
        pygame.display.flip()

