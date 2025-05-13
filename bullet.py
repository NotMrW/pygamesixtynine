#import them modules
import pygame
import math

#import them other files, foo
from settings import Settings

#sexy sexy bullet class because why not
class Bullet(pygame.sprite.Sprite):
    def __init__(self, game):
        """Sexy Bullet Initialization"""
        super().__init__()
        self.settings = game.settings #initialize those beautiful settings
        self.x = game.player.rect.centerx #Get dat X coord
        self.y = game.player.rect.centery #get dat Y coord
        self.rect = pygame.Rect(self.x,self.y,5,5) #get dat rect
        self.color = (188, 181, 2) #Mmm, colors...
 
        self.rect.center = (self.x, self.y) #Get a center
 
        self.direction = self.get_direction(game) #WHICH WAY WE HEADED?
 
    def get_direction(self, game):
        """Calculate the direction of the bullet based on mouse position relative to the player."""
        mouse_at_fire = pygame.mouse.get_pos()  # Get mouse position
        distance = [
            mouse_at_fire[0] - self.x,  # Use bullet's x position
            mouse_at_fire[1] - self.y   # Use bullet's y position
        ]
        normalize = math.sqrt(distance[0]**2 + distance[1]**2)  # Normalize the distance
        if normalize == 0:  # Prevent division by zero
            return [0, 0]
        return [distance[0] / normalize, distance[1] / normalize]  # Return normalized direction
 
    def draw(self, game):
        """FIRE!"""
        pygame.draw.rect(game.screen, self.color, self.rect) #GIMME DA RECT!
 
   
    def update(self):
        """Right, need to update to keep moving..."""
        self.x += self.direction[0] * self.settings.bullet_SPEED #KEEP MOVING, horizontally
        self.y += self.direction[1] * self.settings.bullet_SPEED #KEEP MOVING, vertically
        self.rect.topleft = (self.x, self.y) #identify the topleft of dat rect
       


    #need to relocate this so we can test it
    def get_shotgun(self, game):
        dir = self.get_direction(game)
        theta = math.acos(dir[0])

        d_theta = 2
        bullet_1_x = math.cos(dir[0]+d_theta)
        bullet_1_y = math.sin(dir[1]+d_theta)
        bullet_2_x = math.cos(dir[0]-d_theta)
        bullet_2_y = math.sin(dir[1]-d_theta)