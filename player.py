from settings import Settings
import pygame

class Player:
    def __init__(self, game):
        self.settings =  game.settings #initialize player's settings
        self.x = 500
        self.rect = pygame.Rect(0,0,15,15)
        self.color = (255, 235, 205) #placeholder
        self.rect.center = game.rect.center

    def draw(self,game):
        pygame.draw.rect(game.screen,self.color, self.rect)