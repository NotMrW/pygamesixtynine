#import dat other file bullshit
from settings import Settings
from enemy import Enemy
from spritesheet import SpriteSheet

#import dem modules
import pygame

class Player:
    def __init__(self, game):
        """Initialize the Player"""
        self.settings =  game.settings #initialize player's settings
        self.x = self.settings.screen_WIDTH / 2 #center horizontally
        self.y = self.settings.screen_HEIGHT / 2 #center vertically
        self.spritesheet = SpriteSheet("sprites\manWalk.png")
        self.sprites = self.spritesheet.get_images(0,0,128,64,8)
        self.image = self.sprites[0]
        self.inventory = [] #mechanic: only FIVE items at a time
        self.rect = self.image.get_rect()
        self.rect.center = game.rect.center
        

        #We have to initialize the directions, I guess...
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        #frames
        self.frame = 0


    def draw(self,game):
        """Draw da player"""

        game.screen.blit(self.image, self.rect.topleft) #blit dat shit

    def update(self):
        #get all of dis movement down below
        self.frame = (self.frame+1)% len(self.sprites)
        self.image = self.sprites[self.frame]
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