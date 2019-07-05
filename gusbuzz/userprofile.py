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

class UserProfile:
    def __init__(self, name, screen, font, counter_starting_value = 0):
    	self.name = name
        self.resources_path = 'resources/' + self.name + '/'
        self.savefile = Savefile('resources/profiles/savefiles' + self.name + '.txt')
        self.avatar = "some image"
        self.preferences = "some dictionary"
        self.achievements = "some dictionary"

    def create_new_profile():
        subprocess.call(['mkdir resources/' + self.name])
    	pass

    def load_new_profile():
    	pass

    def delete_profile():
    	subprocess.call(['rmdir -rf resources/' + self.name])
    	pass