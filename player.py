#import dat other file bullshit
from settings import Settings
from enemy import Enemy

#import dem modules
import pygame

class Player:
    def __init__(self, game):
        """Initialize the Player"""
        self.settings =  game.settings #initialize player's settings
        self.x = self.settings.screen_WIDTH / 2 #center horizontally
        self.y = self.settings.screen_HEIGHT / 2 #center vertically
        """self.rect = pygame.Rect(0,0,15,15) #make da hitbox
        self.rect.center = game.rect.center"""
        self.inventory = [] #mechanic: only FIVE items at a time
        self.base_IMAGE = pygame.image.load('sprites\manWalk\manwalk-0.png').convert()
        self.IMAGE = pygame.transform.scale(self.base_IMAGE, (64,64))
        self.rect = self.IMAGE.get_rect()
        self.rect.center = (200, 300)
        


        #We have to initialize the directions, I guess...
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False


    def draw(self,game):
        """Draw da player"""

        game.screen.blit(self.IMAGE, self.rect)

        #get all of dis movement down below
        if self.moving_down == True:
            self.rect.y += self.settings.player_SPEED
        if self.moving_left == True:
            self.rect.x -= self.settings.player_SPEED
        if self.moving_up == True:
            self.rect.y -= self.settings.player_SPEED
        if self.moving_right == True:
            self.rect.x += self.settings.player_SPEED


    def die(self, enemy):
        """check if I should die yet"""
        #how tf do we check collisions for Player/Little_Shit?

    
    def check_hidden(self, game, map):
        """Hidden? Hidden."""
        #Need to check Player/Hiding_Place collisions


    def pickUp(self, inv, newItem):
        """Too many items, I am now overencumbered, damn"""
        if len(inv) >= 5:
            print("Your inventory is full.")
        else:
            inv.append(newItem)
            print(f"{newItem} added ot inventory.")
        return inv

    #how will we add a flashlight mechanic?

#---------Special Traits---------#

#These traits will be specific to other things that are not the player