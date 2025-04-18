#import modules
import random
import pygame
from pygame import mixer
import math

#import classes from other files
from settings import Settings
from player import Player
from enemy import Enemy
from enemy import BigEnemy
from bullet import Bullet



class Game():
    frame_count = 0
    def __init__(self):
        """Initialize da Gaem"""
        mixer.init()
        mixer.music.load("Audio\The _Beginning nor End_..mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        self.settings = Settings() #initialize settings
        self.clock = pygame.time.Clock() #get a clock going
        self.screen = pygame.display.set_mode((self.settings.screen_WIDTH, self.settings.screen_HEIGHT)) #set the screen up
        self.rect = self.screen.get_rect() #get that rect
        pygame.display.set_caption("Try me") #name game window
        
        self.score = 0
        pygame.font.init()
        self.font = pygame.font.Font(None, 36) #get a font for the score
        self.score_surface = self.font.render(str(self.score), True, (255, 255, 255)) #render the score as a surface


        self.player = Player(self) #initialize player

        self.bullets = pygame.sprite.Group() #stuff the bulltes in one, plural group
        self.enemies = pygame.sprite.Group() #Get the little shits into a plural groupww

        self.bigenemies_spawned = 0

        self.enemies_spawned = 0
        self.enemies_killed = 0

        self.wave_number = 1
        self.wave_surface = self.font.render(f"Wave: {self.wave_number}", True, (255, 255, 255)) 
        self.spawn_counter = 0
        self.level_threshold = 5 + 5*self.wave_number
        self.biglevel_threshold = math.floor(self.wave_number // 5)

        self.score = 0
        pygame.font.init()
        self.font = pygame.font.Font(None, 36) #get a font for the score
        self.score_surface = self.font.render(str(self.score), True, (255, 255, 255)) #render the score as a surface

        self.running = True #I guess we can have a loop for the gaem...dwa

    def draw(self,game):
        """Draw da Gaem"""
        pygame.draw.rect(game.screen, self.color, self.rect)

    def run(self): 
        """"Da function to run da gaem"""
        while self.running: #we use "running" value here for loop? Huh, neat
            print(self.settings.spawnrate)
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
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(self)
                        self.bullets.add(bullet)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.player.moving_left = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.player.moving_right = False
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.player.moving_up = False
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.player.moving_down = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        bullet = Bullet(self)
                        self.bullets.add(bullet)
                        

            bg_image = pygame.image.load('sprites\grasstile.png')
            bg_image = pygame.transform.scale(bg_image, (self.settings.screen_WIDTH, self.settings.screen_HEIGHT))
            game.screen.blit(bg_image, (0, 0))
            game.screen.blit(self.score_surface, (50,100))
            self.wave_surface = self.font.render(f"Wave: {self.wave_number}", True, (255, 255, 255))
            game.screen.blit(self.wave_surface, (50, 50))

            #killplayer_collisions = pygame.sprite.spritecollide(self.player, self.enemies, True) #Player/Little_shit collisions
            bullet_enemy_collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, False) #Bullet/Little_shit collisions
            bullet_bigenemy_collisions = pygame.sprite.groupcollide(self.bullets, self.big_enemies, True, False)

            
            if bullet_enemy_collisions:
                total_enemies_hit = list(bullet_enemy_collisions.values())[0]
                for enemy in total_enemies_hit:
                    enemy.hp -= 1
                    enemy.knockback(bullet)
                    if enemy.hp <= 0:
                        enemy.kill()
                        self.enemies_killed+=1
                        self.score+=1
                        self.score_surface = self.font.render(str(self.score), True, (255, 255, 255))
                        
 
            if bullet_bigenemy_collisions: #if bullets collided with Big Bois...
                total_enemies_hit = list(bullet_bigenemy_collisions.values())[0] #fill a list with big enemy collisions' values
                for bigenemy in total_enemies_hit: #loop through those listed collisions
                    bigenemy.hp -= 1 #subtract HP from EACH Big Boi
                    bigenemy.knockback(bullet)
                    if bigenemy.hp <= 0: #if the HP of a specific big boi is 0 or lower...
                        bigenemy.kill() #ded
                        self.score+=3 #one point!
                        self.score_surface = self.font.render(str(self.score), True, (255, 255, 255)) 
#old code
            """if bullet_enemy_collisions:

                self.score += total_enemies_hit  # Add the total to the score
                self.score_surface = self.font.render(str(self.score), True, (255, 255, 255))
                self.dead_enemy_number = self.score
            if bullet_bigenemy_collisions:
                total_bigenemies_hit = sum(len(bigenemies) for bigenemies in killbigenemy_collisions.values())
                self.score += total_bigenemies_hit*3  # Add the total to the score
                self.score_surface = self.font.render(str(self.score), True, (255, 255, 255))
                self.dead_enemy_number = self.score          
"""

            for bullet in self.bullets: #check dem bullets
                if bullet.rect.left > self.settings.screen_WIDTH or bullet.rect.right < 0: #kill the bullets if they go off-screen
                    bullet.kill() #KILL
                if bullet.rect.top > self.settings.screen_HEIGHT or bullet.rect.bottom < 0: #kill the bullets if they go off-screen, twice
                    bullet.kill() #KILL THEM ALL
                bullet.draw(self) #Draw moar bullet
                bullet.update() #Updates them there bullets
            

            enemy = Enemy(self) 
            
            
            self.player.update() #update the player, mainly its position, tho
            self.player.blit(self) #draw the player
            
            if self.enemies_spawned > 0.3*self.level_threshold:
                self.settings.spawnrate = 1
            if (self.enemies_spawned - self.enemies_killed) < 0.3*self.level_threshold:
                self.settings.spawnrate = 0.8

            if len(self.big_enemies) < self.biglevel_threshold and self.bigenemies_spawned < self.biglevel_threshold: #if the length of them big bois is higher than the threshold for em...
                self.enemies.add(BigEnemy(self)) #add them to the list
                self.bigenemies_spawned += 1 #increment the spawn counter

            if random.random() >self.settings.spawnrate and self.enemies_spawned < self.level_threshold: #if the Gambler is lucky...
                self.enemies.add(enemy) #add the cannon fodder
                self.enemies_spawned += 1 #add to the valuse of enemies spawned [DEBUGGING]
            for enemy in self.enemies: #Gotta check the WHOLE DAMN LIST OF ENEMIES
                #if random.random() < self.settings.ENEMY_FLASH_RATE: 
                enemy.draw(self) #Spawn the little twits
                enemy.update(self.player) #update those little shits
            pygame.display.flip() #updtae the ENTIRE display
            
            if self.enemies_killed >= self.level_threshold: #check if score == level score threshold
                self.wave_number += 1
                self.enemies_spawned = 0
                self.enemies_killed = 0
                self.level_threshold = 5 + 5*self.wave_number
                self.biglevel_threshold = math.floor(self.wave_number // 5)
                self.bigenemies_spawned = 0
            self.clock.tick(self.settings.FPS) #initalizes frame rate
            self.frame_count += 1


game = Game() 
game.run()
