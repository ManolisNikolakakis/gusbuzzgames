# Import packages

import sys
import time
import random
from random import randint
import pygame

# Import settings and helpers

from assets.background import BackGround
from assets import settings
import helperFunctions as hf

# Import classes

from text import Text
from letter import Letter
from savefile import Savefile
from difficulty import Difficulty

# Import other python files

pygame.init()

### Variables used in the game ###

score = 0
counter_starting_value = 3
counter = counter_starting_value

### Game Script Starting Point ###

screen = pygame.display.set_mode(settings.SIZE)
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
clock.tick(60)

pygame.time.set_timer(pygame.USEREVENT, 1000)

hf.game_bootloader()
hf.load_splash_screen(screen, font)
difficulty = Difficulty(screen, font, counter_starting_value)
savefile = Savefile(settings.SAVE_LOCATION)
hf.ready_to_start(screen, font)
counter = counter_starting_value
hf.start_music()

current_letter = Letter()
current_letter.randomize_attributes(difficulty.letters)

backGround = BackGround(settings.BACKGROUND_IMAGE, settings.BACKGROUND_IMAGE_STARTING_POINT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            savefile.save_file()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == settings.MATCHING_EVENTS_TO_LETTERS[current_letter.value]:
        	    counter = counter_starting_value
        	    score, savefile.high_score = hf.increase_score(score, savefile.high_score)
            else:
                score = hf.decrease_score(score)
                if score < 0:
                    hf.game_over(screen, font)
                    score = hf.set_score_to_zero(score)
            current_letter.randomize_attributes(difficulty.letters)
        elif event.type == pygame.USEREVENT:
            counter = counter - 1
            if counter < 0:
                counter = counter_starting_value
                core = hf.decrease_score(score)
                if score < 0:
                    hf.game_over(screen, font)
                    score = hf.set_score_to_zero(score)
                current_letter.randomize_attributes(difficulty.letters)
        break
    hf.refill_screen(screen, backGround, font, score, current_letter, difficulty, savefile, counter)
