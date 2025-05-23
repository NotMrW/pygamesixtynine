#import dat other file bullshit
from settings import Settings
from spritesheet import SpriteSheet



#import dem modules
import pygame

class Player:
    def __init__(self, game):
        """Initialize the Player"""
        #Initialize a lot of things
        self.game = game
        self.settings =  game.settings #initialize player's settings
        self.x = self.settings.screen_WIDTH / 2 #center horizontally
        self.y = self.settings.screen_HEIGHT / 2 #center vertically
        self.HP = 50
        self.shield = 0
        self.spritesheet = SpriteSheet("sprites\manWalk.png")
        self.sprites = self.spritesheet.get_images(0,0,32,32,8)
        self.image = self.sprites[0]
        self.death_image = ("sprites/manFace.png")
        self.rect = self.image.get_rect()
        self.rect.center = game.rect.center
        self.weapon_list = ["pistol"]
        


        #Variables regarding certain status of the player
        self.status = "none"
        self.weapon = "pistol" #List: pistol, automatica, devlogger
        self.firing = False



        #We have to initialize the directions
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        


        #frames, what else can I say?
        self.frame = 0



    #blit dat madafookah because THIS AINT A SQUARE OR A CIRLCE!
    def blit(self,game):
        game.screen.blit(self.image, self.rect.topleft) #blit dat shit



    #MOVEMENT UPDATES!
    def update(self):
        """Get all of the movement for Player updated"""
        if self.game.frame_count % 15 == 0:
            self.frame = (self.frame+1)% len(self.sprites)
        self.image = self.sprites[self.frame]
        if self.moving_down == True:
            self.rect.y += self.settings.player_SPEED
            backwards_image = pygame.transform.rotate(self.image, 180)
            self.game.screen.blit(backwards_image, self.rect.topleft)
        if self.moving_left == True:
            self.rect.x -= self.settings.player_SPEED
        if self.moving_up == True:
            self.rect.y -= self.settings.player_SPEED
        if self.moving_right == True:
            self.rect.x += self.settings.player_SPEED
        

    
    #returns player position?
    def __str__(self):
        return f"Player at {self.x, self.y} - Rect: {self.rect.topleft}"



    #KNOCKBACK MECHANIC!
    def knockback(self, enemy, multiplier):
        self.rect.x += enemy.direction[0] * multiplier
        self.rect.y += enemy.direction[1] * multiplier
