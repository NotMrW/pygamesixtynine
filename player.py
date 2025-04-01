from settings import Settings


import pygame

class Player:
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

    
    def check_hidden(self, game, map): #add a hiding mechanic
        collisions = pygame.sprite.spritecollide


    def pickUp(self, inv, newItem): #limited inventory mechanic
        if len(inv) >= 5:
            print("Your inventory is full.")
        else:
            inv.append(newItem)
            print(f"{newItem} added ot inventory.")
        return inv

    #how will we add a flashlight mechanic?

#---------Special Traits---------#

#These traits will be specific to other things that are not the player