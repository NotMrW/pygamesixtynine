#import modules
import random
import pygame

#import classes from other files
from settings import Settings
from player import Player
from enemy import Enemy
from bullet import Bullet



class Game():
    frame_count = 0
    def __init__(self):
        """Initialize da Gaem"""
        self.settings = Settings() #initialize settings
        self.clock = pygame.time.Clock() #get a clock going
        self.screen = pygame.display.set_mode((self.settings.screen_WIDTH, self.settings.screen_HEIGHT)) #set the screen up
        self.rect = self.screen.get_rect() #get that rect
        pygame.display.set_caption("Try me") #name game window
        self.running = True #I guess we can have a loop for the gaem...dwa
         
        self.player = Player(self) #initialize player
        self.settings =  Settings() #initialize player's settings
        #We have to initialize the directions, I guess...
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        self.bullets = pygame.sprite.Group() #stuff the bulltes in one, plural group
        self.enemies = pygame.sprite.Group() #Get the little shits into a plural group



    def draw(self,game):
        """Draw da Gaem"""
        pygame.draw.rect(game.screen, self.color, self.rect)



        
        
        #img = pygame.image.load("your_image.png/jpg") #load the image for the icon onto variable
        #pygame.display.set_icon(img) #set the image variable for the window icon

    def run(self): 
        """"Da function to run da gaem"""
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
                        


            collisions = pygame.sprite.spritecollide(self.player, self.enemies, True) #Player/Little_shit collisions
            collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True) #Bullet/Little_shit collisions
            game.screen.fill('black') #fill the screen with racism
            bullet = Bullet(self) #stuff the bullet into a variable
            self.bullets.add(bullet) #stuff the bullet variable into a plural list
            for bullet in self.bullets: #check dem bullets
                if bullet.rect.left > self.settings.screen_WIDTH or bullet.rect.right < 0: #kill the bullets if they go off-screen
                    bullet.kill() #KILL
                if bullet.rect.top > self.settings.screen_HEIGHT or bullet.rect.bottom < 0: #kill the bullets if they go off-screen, twice
                    bullet.kill() #KILL THEM ALL
                bullet.draw(self) #Draw moar bullet
                bullet.update() #Updates them there bullets
            enemy = Enemy(self) #just stuff the enemies into a single variable, this is beyond explaination

            if random.random() >.8: #Oh, we have GAMBLING?! RANDOMIZATION?!
                self.enemies.add(enemy) #spawn the cannon fodder
            for enemy in self.enemies: #Gotta check the WHOLE DAMN LIST OF ENEMIES
                #if random.random() < self.settings.ENEMY_FLASH_RATE: #Hmm...
                enemy.draw(self) #OH, that makes more sense in terms of "flash_rate"
                enemy.update(self.player) #draw those little shits
            self.player.update()
            print(self.player)
            self.player.draw(self) #draw the player
            pygame.display.flip() #flippity flip; We actually don't know what this does #Google what it does instead of writing a useless comment.
            self.clock.tick(self.settings.FPS) #initalizes frame rate
            self.frame_count += 1


game = Game() #Define gaem as Gaem
game.run() #Run dat shit
