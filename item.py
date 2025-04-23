
#import files
from spritesheet import SpriteSheet
from settings import Settings

#import modules
import pygame

class Medkit(pygame.sprite.Sprite):
    def __init__(self, game):
        """This will heal the PLAYER"""
        self.game = game
        self.settings = game.settings
        self.x = -5
        self.y = -5
        self.HEAL = self.settings.medkit_HEAL
