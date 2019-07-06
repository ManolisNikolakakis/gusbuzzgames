# Standard Libraries

import sys
import time
import random
from random import randint

# Pip installed libraries

import pygame

from 
from assets.background import BackGround
from assets import settings
import subprocess


# Potentially better done as subclass of text.py

class DisplayElement:
    def __init__(self, screen, font, counter_starting_value = 0):
    	self.quote = quote
    	self.color = color
    	self.width = width
    	self.height = height

    def print_display_element(self, font, screen):
    	text = font.render(self.quote, True, self.color)
    	screen.blit(text, [self.width, self.height])
