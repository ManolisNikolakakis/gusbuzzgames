# Standard Libraries

import sys
import time
import random
from random import randint

# Pip installed libraries

import pygame

from assets.background import BackGround
from assets import settings

# Import classes

from text import Text
from letter import Letter
from savefile import Savefile
from difficulty import Difficulty

# Import other python files

import helperFunctions as hf

pygame.init()

### Variables used in the game ###

score = 0
font = pygame.font.Font(None, 36)
counter_starting_value = 3
counter = counter_starting_value
letter_sprite = {}

### Functions used in the game ###

def game_bootloader():
	# pygame.display.set_icon(surface) // add some sort of icon to the game
    pygame.display.set_caption("Project Jacob")

def load_splash_screen():

    screen.fill(settings.BLACK)

    text = font.render("Presented by...", True, settings.WHITE)
    screen.blit(text, [350, 270])

    text = font.render("GusBuzzGames", True, settings.WHITE)
    screen.blit(text, [350, 300])

    pygame.display.flip()

    time.sleep(1)

def game_over():
    screen.fill(settings.BLACK)

    text = font.render(settings.text_game_over, True, settings.RED)
    screen.blit(text, [270, 270])

    pygame.display.flip() 

    time.sleep(2)

    text = font.render(settings.text_retry, True, settings.WHITE)
    screen.blit(text, [270, 320])  
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                ready_to_start()
                return

def ready_to_start():

    screen.fill(settings.BLACK)

    start_message = Text(settings.text_start, 310, 270, settings.RED)
    start_message.print_on_screen(font, screen)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                counter = counter_starting_value
                return

def refill_screen():

    screen.fill(settings.BLACK)
    screen.blit(backGround.image, backGround.rect)

    text = font.render("High Score", True, settings.WHITE)
    screen.blit(text, [settings.WIDTH - 150, 10])

    text = font.render(str(savefile.high_score), True, settings.WHITE)
    screen.blit(text, [settings.WIDTH - 150, 40])

    text = font.render("Current Score", True, settings.WHITE)
    screen.blit(text, [10, 10])

    text = font.render(str(score), True, settings.WHITE)
    screen.blit(text, [10, 40])

    text = font.render("Random Letter", True, settings.WHITE)
    screen.blit(text, [10, 70])
 
    text = font.render(current_letter.value, True, settings.WHITE)
    screen.blit(text, [10, 100])

    text = font.render("Countdown", True, settings.WHITE)
    screen.blit(text, [10, 150])

    text = font.render(str(counter), True, settings.WHITE)
    screen.blit(text, [10, 180])

    if difficulty.value == 'EASY':
        screen.blit(difficulty.letter_sprite[current_letter.value],(current_letter.width, current_letter.height))
    
    pygame.display.flip()

### Game Script Starting Point ###

screen = pygame.display.set_mode(settings.SIZE)

clock = pygame.time.Clock()
clock.tick(60)

pygame.time.set_timer(pygame.USEREVENT, 1000)

game_bootloader()
load_splash_screen()
difficulty = Difficulty(screen, font, counter_starting_value)
savefile = Savefile(settings.SAVE_LOCATION)
ready_to_start()
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
                    game_over()
                    score = hf.set_score_to_zero(score)
            current_letter.randomize_attributes(difficulty.letters)
        elif event.type == pygame.USEREVENT:
            counter = counter - 1
            if counter < 0:
                counter = counter_starting_value
                core = hf.decrease_score(score)
                if score < 0:
                    game_over()
                    score = hf.set_score_to_zero(score)
                current_letter.randomize_attributes(difficulty.letters)
        break
    refill_screen()
