# Standard Libraries

import sys
import time
import random
import os
from pathlib import Path
from random import randint

# Pip installed libraries

import pygame

from assets.background import BackGround
from assets import settings


class Savefile:
    def __init__(self, path='', name='1'):
        self.path = path
        if not os.path.isfile(self.path):
            Path(self.path).touch()
            self.high_score = 0;
        else:
            self.name = name
            self.high_score = int(self.load_file())

    def save_file(self):
        with open(self.path, "w") as f:
            f.write(str(self.high_score))
            return

    def load_file(self):
        with open(self.path, "r") as f:
            data = f.readlines()
            for line in data:
                words = line.split()
                if words[0]:
                    return words[0]
                else:
                    return 0;

    def delete_file(self):
        return None

    def create_file(self):
        return None
