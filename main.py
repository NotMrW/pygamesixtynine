#import modules
import random
import pygame
from bullet import Bullet

#import classes from other files
from settings import Settings
from player import Player
from enemy import Basic_MF



class Game():
    def __init__(self): #initalize the gaem
        self.settings = Settings() #initialize settings
        self.clock = pygame.time.Clock() #get a clock going
        self.screen = pygame.display.set_mode((self.settings.screen_WIDTH, self.settings.screen_HEIGHT)) #set the screen up
        self.rect = self.screen.get_rect() #get that rect
        pygame.display.set_caption("Try me") #name game window
        self.running = True #I guess we can have a loop for the gaem...
        
        self.player = Player(self) #initialize player
        self.enemy = Basic_MF(self) #initialize enemy
        self.bullets = pygame.sprite.Group()
        
        
        #img = pygame.image.load("your_image.png/jpg") #load the image for the icon onto variable
        #pygame.display.set_icon(img) #set the image variable for the window icon

    def run(self): #make function to run da gaem
        while self.running: #we use "running" value here for loop? Huh, neat
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False #We always need to be able to run from the gaem
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.player.moving_left = True
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.player.moving_right = True
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.player.moving_up = True
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.player.moving_down = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.player.moving_left = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.player.moving_right = False
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.player.moving_up = False
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.player.moving_down = False




            game.screen.fill('black')
            bullet = Bullet(self)
            self.bullets.add(bullet)
            for bullet in self.bullets:
                bullet.draw(self)
                bullet.update()
            ##all_sprites.update()
            self.player.draw(self) #draw the player
            self.enemy.draw(Basic_MF)
            pygame.display.flip()
            self.clock.tick(self.settings.FPS) #initalizes frame rate

game = Game()
game.run()
