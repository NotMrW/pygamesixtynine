#import modules
import random
import pygame

#import classes from other files
from settings import Settings
from player import Player



class Game():
    def __init__(self):
        self.settings = Settings() #initialize settings
        self.clock = pygame.time.Clock() #get a clock going
        self.screen = pygame.display.set_mode((self.settings.screen_WIDTH, self.settings.screen_HEIGHT)) #set the screen up
        self.rect = self.screen.get_rect()
        pygame.display.set_caption("Try me") #name game window
        self.running = True
        
        self.player = Player(self) #initialize player
        
        
        #img = pygame.image.load("your_image.png/jpg") #load the image for the icon onto variable
        #pygame.display.set_icon(img) #set the image variable for the window icon

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.player.draw(self) #draw the player
            pygame.display.flip()
            self.clock.tick(self.settings.FPS) #initalizes frame rate

game = Game()
game.run()
