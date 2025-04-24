
#import files
from spritesheet import SpriteSheet
from settings import Settings

#import modules
import pygame

class Medkit(pygame.sprite.Sprite):
    def __init__(self, game):
        """This will heal the PLAYER"""
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.x = 500
        self.y = 500
        self.HEAL = self.settings.medkit_HEAL

        self.spritesheet = SpriteSheet(r"sprites/radioBig.png")
        self.sprites = self.spritesheet.get_images(0,0,32,32,1)
        self.image = self.sprites[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = (500,500)
        self.rect.topleft = (500, 500)

        self.frame = 0
    def heal_player(self,player):
        if player:
            if self.rect.colliderect(player.rect):
                player.HP += self.HEAL #maybe we should add a damage variable?
                self.kill()
    def draw(self, game):
        game.screen.blit(self.image, self.rect.topleft)