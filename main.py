#import modules
import random
import pygame
from bullet import Bullet

#import classes from other files
from settings import Settings
from player import Player
from enemy import Enemy



class Game():
    def __init__(self): #initalize the gaem
        self.settings = Settings() #initialize settings
        self.clock = pygame.time.Clock() #get a clock going
        self.screen = pygame.display.set_mode((self.settings.screen_WIDTH, self.settings.screen_HEIGHT)) #set the screen up
        self.rect = self.screen.get_rect() #get that rect
        pygame.display.set_caption("Try me") #name game window
        self.running = True #I guess we can have a loop for the gaem...
        
        self.player = Player(self) #initialize player
        self.settings =  Settings() #initialize player's settings
        #We have to initialize the directions, I guess...
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()


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
            self.rect.x += self.settings.player_SPEED #initialize enemy
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        
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



            collisions = pygame.sprite.spritecollide(self.player, self.enemies, True)
            collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
            game.screen.fill('black')
            bullet = Bullet(self)
            self.bullets.add(bullet)
            for bullet in self.bullets:
                bullet.draw(self)
                bullet.update()
            enemy = Enemy(self)
            if random.random() >.8:
                self.enemies.add(enemy)
                for enemy in self.enemies:
                    enemy.draw(self)
                    enemy.update(self.player)
            ##all_sprites.update()
            self.player.draw(self) #draw the player
            pygame.display.flip()
            self.clock.tick(self.settings.FPS) #initalizes frame rate

game = Game()
game.run()
