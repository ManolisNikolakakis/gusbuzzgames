# Standard Libraries

import sys
import time
import random
from random import randint

# Pip installed libraries

import pygame

from assets.background import BackGround
from assets import settings

# Potentially better done as subclass of text.py


class Difficulty:
    def __init__(self, screen, font, counter_starting_value=0):
        self.letter_sprite = {}
        self.letters = []
        self.mode = False
        self.counter_starting_value = counter_starting_value
        self.difficulty_selection(screen, font)
        self.load_letters()
        if self.mode == 'EASY':
            self.load_images(self.mode, self.letter_sprite)

    def load_images(self, difficulty, letter_sprite):
        for letter in self.letters:
            self.letter_sprite[letter] = pygame.image.load(
                settings.sprites_directory + letter.lower() + settings.sprites_format)

    def difficulty_selection(self, screen, font):
        text = font.render(settings.text_easy_mode, True, settings.RED)
        screen.blit(text, [310, 380])

        text = font.render(settings.text_medium_mode, True, settings.RED)
        screen.blit(text, [310, 410])

        text = font.render(settings.text_hard_mode, True, settings.RED)
        screen.blit(text, [310, 440])

        pygame.display.flip()

        while not self.mode:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    self.mode = 'EASY'
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    self.mode = 'MEDIUM'
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                    self.mode = 'HARD'
        return

    def load_letters(self):
        self.letters = settings.MODE[self.mode]
