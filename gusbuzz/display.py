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

class Display:
    def __init__(self, screen, font, background, display_elements):
    	self.display_elements = display_elements
    	self.background = background 

    def display_all_individual_elements():
        for element in self.display_elements:
            element.print_display_element()


