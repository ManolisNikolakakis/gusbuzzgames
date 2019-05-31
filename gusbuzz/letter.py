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

class Letter:
    def __init__(self, value = '0', width = 0, height = 0, sprite = 0):
        self.value = str(value)
        self.width = width
        self.height = height
        self.sprite = sprite
        #self.font = font to be implemented, needed if not sprite available

    def randomize_attributes(self, difficulty):
        self.value = random.choice(difficulty)
        self.width = randint(150, settings.WIDTH - 200)
        self.height = randint(0, 500)
