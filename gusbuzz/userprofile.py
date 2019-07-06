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
    def __init__(self, screen, font, counter_starting_value = 0):
    	self.all_profiles = parse_all_profiles()
    	self.name = None
    	self.name = profile_selection(self, screen, font)
        self.resources_path = 'resources/' + self.name + '/'
        self.savefile = Savefile('resources/profiles/savefiles' + self.name + '.txt')
        # self.avatar = "some image"
        # self.preferences = "some dictionary"
        # self.achievements = "some dictionary"

    def profile_selection(self, screen, font):
        text = font.render("Press A: Load Existing Profile", True, settings.RED)
        screen.blit(text, [310, 380])   

        text = font.render("Press B: Create New Profile", True, settings.RED)
        screen.blit(text, [310, 410])   

        text = font.render("Press C: Delete existing profile", True, settings.RED)
        screen.blit(text, [310, 440])    

        pygame.display.flip()

        while not self.name:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    self.name = load_new_profile()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    self.name = create_new_profile()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    self.name = delete_profile()
        return 

    def create_new_profile(self, screen, font):
    	text = font.render("Press B: Create New Profile", True, settings.RED)
    	exit = None
    	#add code to receive new name
        pygame.display.flip()


        subprocess.call(['mkdir resources/' + self.name])
    	pass

    def load_existing_profile(self, screen, font):
    	# click appropriate
    	pass

    def delete_profile(self, screen, font):
    	subprocess.call(['rmdir -rf resources/' + self.name])
    	pass

    def parse_all_profiles():
    	pass



