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
        self.color = (255, 200, 255) #Mmm, colors...
 
        self.rect.center = (self.x, self.y) #Get a center
 
        self.direction = self.get_direction(game) #WHICH WAY WE HEADED?
 
    def get_direction(self, game):
        """'Which wey do I go?'"""
        mouse_at_fire = pygame.mouse.get_pos() #GO TO THAT WIERD TRIANGLE!
        distance = [ #How far?
            mouse_at_fire[0] - game.player.x, #That far horizontally
            mouse_at_fire[1] - game.player.y #that far vertically
        ]
        normalize = math.sqrt(distance[0]**2 + distance[1]**2) #normalize dat sexy distance
        self.direction = [distance[0]/normalize, distance[1]/normalize] #OHH, so that's the direction we're going...
        return self.direction #Direction received, firing in...fuck it
 
    def draw(self, game):
        """FIRE!"""
        pygame.draw.rect(game.screen, self.color, self.rect) #GIMME DA RECT!
 
   
    def update(self):
        """Right, need to update to keep moving..."""
        self.x += self.direction[0] * self.settings.bullet_SPEED #KEEP MOVING, horizontally
        self.y += self.direction[1] * self.settings.bullet_SPEED #KEEP MOVING, vertically
        self.rect.topleft = (self.x, self.y) #identify the topleft of dat rect
        print(self.direction) #printy print
 