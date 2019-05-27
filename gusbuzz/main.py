# Standard Libraries

import sys
import time
import random

# Pip installed libraries

import pygame

from assets.background import BackGround
from assets import settings

pygame.init()

# Variable used in the game 

score = "0"
font = pygame.font.Font(None, 36)
current_letter = random.choice(settings.LETTERS_EASY)

# Functions used in the game


def load_settings():
	# pygame.display.set_icon(surface)
    screen.fill(settings.BLACK)
    pygame.display.set_caption("Some Video Game")

def load_splash_screen():

    text = font.render("Presented by...", True, settings.WHITE)
    screen.blit(text, [350, 270])

    text = font.render("GusBuzzGames", True, settings.WHITE)
    screen.blit(text, [350, 300])

    pygame.display.flip()

    time.sleep(1)
    
    text = font.render("PRESS F TO CONTINUE", True, settings.RED)
    screen.blit(text, [310, 380])      

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                return

def refill_screen():

    screen.fill(settings.BLACK)
    screen.blit(backGround.image, backGround.rect)

    text = font.render("Current Score", True, settings.WHITE)
    screen.blit(text, [10, 10])
 
    text = font.render(score, True, settings.WHITE)
    screen.blit(text, [10, 40])

    text = font.render("Random Letter", True, settings.WHITE)
    screen.blit(text, [10, 70])
 
    text = font.render(current_letter, True, settings.WHITE)
    screen.blit(text, [10, 100])
        
    pygame.display.flip()

# Game Script Starting Point

screen = pygame.display.set_mode(settings.SIZE)

load_settings()
load_splash_screen()

pygame.mixer.init()
pygame.mixer.music.load(settings.MAIN_TUNE)
pygame.mixer.music.play(settings.INFINITE_MUSIC_LOOP)

backGround = BackGround(settings.BACKGROUND_IMAGE, settings.BACKGROUND_IMAGE_STARTING_POINT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == settings.MATCHING_EVENTS_TO_LETTERS[current_letter]:
        	    score = int(score) + 10
        	    score = str(score)
            else:
                score = int(score) - 10
                score = str(score)
            current_letter = random.choice(settings.LETTERS_EASY)

    refill_screen()

        

