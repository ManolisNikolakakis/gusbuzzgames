import pygame

from assets import settings


class BackGround(pygame.sprite.Sprite):

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, settings.SIZE)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
