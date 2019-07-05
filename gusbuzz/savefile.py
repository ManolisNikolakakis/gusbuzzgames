# Standard Libraries

import sys
import time
import random
from random import randint

# Pip installed libraries

import pygame

from assets.background import BackGround
from assets import settings

class Savefile:
    def __init__(self, path = '', name = '1'):
        self.path = path
        self.name = name
        self.high_score = int(self.load_high_score())

    def save_high_score(self):
        with open(self.path, "w") as f:
            f.write(str(self.high_score))
            return

    def load_high_score(self):
        with open(self.path, "r") as f:
            data = f.readlines()
            for line in data:
                words = line.split()
                return words[0]

    def delete_file(self):
        return None

    def create_file(self):
        return None