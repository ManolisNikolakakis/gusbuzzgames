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
current_letter = None
difficulty = None
difficulty_selected = False

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

def difficulty_selection(difficulty):
    text = font.render("PRESS E FOR EASY (4 letters)", True, settings.RED)
    screen.blit(text, [310, 380])   

    text = font.render("PRESS M FOR MEDIUM (8 letters)", True, settings.RED)
    screen.blit(text, [310, 410])   

    text = font.render("PRESS H FOR HARD (19 letters)", True, settings.RED)
    screen.blit(text, [310, 440])    

    pygame.display.flip()

    difficulty_selected = False

    while not difficulty_selected:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                difficulty = settings.LETTERS_EASY
                return difficulty
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                difficulty = settings.LETTERS_MEDIUM
                return difficulty
            if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                difficulty = settings.LETTERS_HARD
                return difficulty

def ready_to_start():
    screen.fill(settings.BLACK)

    text = font.render("PRESS F TO START", True, settings.RED)
    screen.blit(text, [310, 270])    

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

    text = font.render("Countdown", True, settings.WHITE)
    screen.blit(text, [10, 150])

    text = font.render(str(counter), True, settings.WHITE)
    screen.blit(text, [10, 180])
        
    pygame.display.flip()

# Game Script Starting Point

screen = pygame.display.set_mode(settings.SIZE)

clock = pygame.time.Clock()
clock.tick(60)

counter = 3
pygame.time.set_timer(pygame.USEREVENT, 1000)

load_settings()
load_splash_screen()
difficulty = difficulty_selection(difficulty)
ready_to_start()

current_letter = random.choice(difficulty)

pygame.mixer.init()
pygame.mixer.music.load(settings.MAIN_TUNE)
pygame.mixer.music.play(settings.INFINITE_MUSIC_LOOP)

backGround = BackGround(settings.BACKGROUND_IMAGE, settings.BACKGROUND_IMAGE_STARTING_POINT)
start_ticks= clock.tick() #starter tick

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == settings.MATCHING_EVENTS_TO_LETTERS[current_letter]:
        	    score = int(score) + 10
        	    score = str(score)
        	    counter = 3
            else:
                score = int(score) - 10
                score = str(score)
            current_letter = random.choice(difficulty)
            start_ticks=pygame.time.get_ticks() #starter tick
        elif event.type == pygame.USEREVENT:
            print ("SHABLAGOO")
            counter = counter - 1
            if counter < 0:
                score = int(score) - 10
                score = str(score)
                current_letter = random.choice(difficulty)
                counter = 3
                refill_screen()
        break

    refill_screen()

        

