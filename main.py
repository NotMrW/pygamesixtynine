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
from item import Medkit



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
        pygame.display.set_caption("SpriteGame") #name game window
        
        self.score = 0
        pygame.font.init()
        self.font = pygame.font.Font(None, 36) #get a font for the score
        self.score_surface = self.font.render(str(self.score), True, (255, 255, 255)) #render the score as a surface
        self.death_surface = self.font.render("YOU DIED", True, (255, 255, 255))


        self.player = Player(self) #initialize player
        self.medkits = pygame.sprite.Group()

        self.bullets = pygame.sprite.Group() #stuff the bulltes in one, plural group
        self.enemies = pygame.sprite.Group() #Get the little shits into a plural group
        self.big_enemies = pygame.sprite.Group()

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
            print(self.player.HP)
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
                        if random.random() <= 0.02:
                            self.medkits.add(medkit)
                        
            if bullet_bigenemy_collisions: #if bullets collided with Big Bois...
                total_enemies_hit = list(bullet_bigenemy_collisions.values())[0] #fill a list with big enemy collisions' values
                for bigenemy in total_enemies_hit: #loop through those listed collisions
                    bigenemy.hp -= 1 #subtract HP from EACH Big Boi
                    bigenemy.knockback(bullet)
                    if bigenemy.hp <= 0: #if the HP of a specific big boi is 0 or lower...
                        bigenemy.kill() #ded
                        self.score+=3 #one point!
                        self.score_surface = self.font.render(str(self.score), True, (255, 255, 255)) 

            for bullet in self.bullets: #check dem bullets
                if bullet.rect.left > self.settings.screen_WIDTH or bullet.rect.right < 0: #kill the bullets if they go off-screen
                    bullet.kill() #KILL
                if bullet.rect.top > self.settings.screen_HEIGHT or bullet.rect.bottom < 0: #kill the bullets if they go off-screen, twice
                    bullet.kill() #KILL THEM ALL
                bullet.draw(self) #Draw moar bullet
                bullet.update() #Updates them there bullets
            
            for medkit in self.medkits:
                medkit.draw(self)
                medkit.heal_player(self.player)

            enemy = Enemy(self) 
            big_enemy = BigEnemy(self)
            medkit = Medkit(self)
            
            self.player.update() #update the player, mainly its position, tho
            self.player.blit(self) #draw the player
            
            if self.enemies_spawned > 0.3*self.level_threshold:
                self.settings.spawnrate = 1
            if (self.enemies_spawned - self.enemies_killed) < 0.3*self.level_threshold:
                self.settings.spawnrate = 0.8

            if len(self.big_enemies) < self.biglevel_threshold and self.bigenemies_spawned < self.biglevel_threshold: #if the length of them big bois is higher than the threshold for em...
                self.big_enemies.add(BigEnemy(self)) #add them to the list
                self.bigenemies_spawned += 1 #increment the spawn counter
            for big_enemy in self.big_enemies: #Gotta check the WHOLE DAMN LIST OF ENEMIES
                big_enemy.draw(self) #Spawn the little twits
                big_enemy.update(self.player) #update those little shits
                big_enemy.check_collide(self.player)
                if big_enemy.hp <= 0:
                    big_enemy.kill()

            if random.random() >self.settings.spawnrate and self.enemies_spawned < self.level_threshold: #if the Gambler is lucky...
                self.enemies.add(enemy) #add the cannon fodder
                self.enemies_spawned += 1 #add to the valuse of enemies spawned [DEBUGGING]


            for enemy in self.enemies: #Gotta check the WHOLE DAMN LIST OF ENEMIES
                #if random.random() < self.settings.ENEMY_FLASH_RATE: 
                enemy.draw(self)
                enemy.update(self.player) #update those little shits
                enemy.check_collide(self.player)
                if enemy.hp <= 0:
                    enemy.kill()
                    self.enemies_killed+=1
            if self.player.HP > 50:
                self.player.HP = 50
            if self.player.HP <= 0:
                self.screen.fill("black")
                self.screen.blit(self.death_surface, (self.settings.screen_WIDTH//2.25,self.settings.screen_HEIGHT//2))
            pygame.display.flip() #updtae the ENTIRE display
            
            if self.enemies_killed >= self.level_threshold: 
                self.wave_number += 1 
                self.enemies_spawned = 0 
                self.enemies_killed = 0
                """for enemy in self.enemies:
                    enemy.kill()"""
                for big_enemy in self.big_enemies:
                    big_enemy.kill()
                if self.wave_number <= 10:
                    self.level_threshold = 5 + 5*self.wave_number 
                elif self.wave_number > 10: 
                    self.level_threshold = 5 + 7*self.wave_number
                if self.wave_number <= 10: 
                    self.biglevel_threshold = math.floor(self.wave_number // 5)
                elif self.wave_number > 10: 
                    self.biglevel_threshold = math.floor(self.wave_number // 3) 
                self.bigenemies_spawned = 0
            self.clock.tick(self.settings.FPS) 
            self.frame_count += 1 
 

game = Game() 
game.run()