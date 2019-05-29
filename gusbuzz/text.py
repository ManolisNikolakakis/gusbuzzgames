# Standard Libraries

import sys
import time
import random
from random import randint

# Pip installed libraries

import pygame

from assets.background import BackGround
from assets import settings

class Text:
    def __init__(self, message = '0', width = 0, height	 = 0, color = 0):
        self.message = str(message)
        self.width = width
        self.height = height
        self.color = color
        #self.font = font to be implemented

    def print_on_screen(self, font, screen):
        text = font.render(self.message, True, self.color)
        screen.blit(text, [self.width, self.height])
