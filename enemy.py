#import the modules, do you think it was going to be different?
import pygame

#import them other files' classes
from player import Player
from settings import Settings

class Basic_MF(Player):
    def __init__(self, game):
        self.settings =  game.settings #initialize player's settings
        self.x = self.settings.screen_WIDTH / 2 #center horizontally
        self.y = self.settings.screen_HEIGHT / 2 #center vertically
        self.rect = pygame.Rect(0,0,15,15) #make da hitbox
        self.color = (255, 235, 205) #placeholder
        self.rect.center = game.rect.center
        self.inventory = [] #mechanic: only FIVE items at a time

        #We have to initialize the directions, I guess...
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False


    def draw(self,game):
        pygame.draw.rect(game.screen, self.color, self.rect)

        #get all of dis movement down below
        if self.moving_down == True:
            self.rect.y += self.settings.player_SPEED
        if self.moving_left == True:
            self.rect.x -= self.settings.player_SPEED
        if self.moving_up == True:
            self.rect.y -= self.settings.player_SPEED
        if self.moving_right == True:
            self.rect.x += self.settings.player_SPEED