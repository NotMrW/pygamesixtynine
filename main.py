#import modules
import random
import pygame
from pygame import mixer
import math



#import classes from other files
from settings import Settings
from player import Player
from enemy import Enemy, BigEnemy, SpeedyBoi, BlindBulb, DeathBulb
from bullet import Bullet
from item import Medkit, Shield



#Define the Game as a CLASS
class Game():
    frame_count = 0
    def __init__(self):
        """Initialize da Gaem"""



        #mixer code
        mixer.init()
        mixer.music.load("Audio\The _Beginning nor End_..mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()



        #Main Setup
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



        #Setup the Player
        self.player = Player(self)
        


        #Setup the items
        self.medkits = pygame.sprite.Group()
        self.shields = pygame.sprite.Group()



        #Setup the sexy bullets
        self.bullets = pygame.sprite.Group()



        #Setup every enemy type
        self.enemies = pygame.sprite.Group()
        self.big_enemies = pygame.sprite.Group()
        self.speedy_bois = pygame.sprite.Group()
        self.blind_bulbs = pygame.sprite.Group()
        self.death_bulbs = pygame.sprite.Group()



        #Enemy-Specific Data Setup
        self.bigenemies_spawned = 0
        self.bulbs_spawned = 0
        self.enemies_spawned = 0
        self.enemies_killed = 0
        self.speedy_bois_spawned = 0
        self.speedy_bois_killed = 0



        #Wave Setup
        self.wave_number = 999
        self.wave_surface = self.font.render(f"Wave: {self.wave_number}", True, (255, 255, 255)) 
        self.spawn_counter = 0
        self.level_threshold = 5 + 5*self.wave_number
        self.biglevel_threshold = math.floor(self.wave_number // 5)
        self.speedylevel_threshold = 0+math.floor(self.wave_number//7)



        #Setup Booleans
        self.running = True #I guess we can have a loop for the gaem...dwa



    def run(self): 
        """"Da function to run da gaem"""
        while self.running: #we use "running" value here for loop? Huh, neat
            print(self.player.status, self.player.HP) 

            
            #DEBUGGING
            #print(self.player.status, self.player.HP, self.player.shield)



            #Keayboard-Based Events
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



                #More Keayboard-Based events
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.player.moving_left = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.player.moving_right = False
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.player.moving_up = False
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.player.moving_down = False
                


                # *Le Gasp* Mouse-Based Events?!
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.player.firing = True
                if event.type == pygame.MOUSEBUTTONUP:
                        self.player.firing = False
            


            #Player Status handlers
            if self.player.status == "blind":
                game.screen.fill("white")
                pygame.display.flip()
                endblindtimer = pygame.time.get_ticks()
                print(blindtimer, endblindtimer)
                if endblindtimer >= blindtimer:
                    self.player.status = "none"
            else: #THIS STILL WORKS, ACE!
                bg_image = pygame.image.load('sprites\grasstile.png')
                bg_image = pygame.transform.scale(bg_image, (self.settings.screen_WIDTH, self.settings.screen_HEIGHT))
                game.screen.blit(bg_image, (0, 0))
                game.screen.blit(self.score_surface, (50,100))
                self.wave_surface = self.font.render(f"Wave: {self.wave_number}", True, (255, 255, 255))
                game.screen.blit(self.wave_surface, (50, 50))



            #Individual Bullet/Enemy Collision Setup
            bullet_enemy_collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, False) #Bullet/Little_shit collisions
            bullet_bigenemy_collisions = pygame.sprite.groupcollide(self.bullets, self.big_enemies, True, False)
            bullet_speedy_collisions = pygame.sprite.groupcollide(self.bullets, self.speedy_bois, True, False)
            bullet_blindbulb_collisions = pygame.sprite.groupcollide(self.bullets, self.blind_bulbs, True, False)
            bullet_deathbulb_collisions = pygame.sprite.groupcollide(self.bullets, self.death_bulbs, True, False)



            #Individual Bullet/Enemy Collision Setup
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
                        if random.random() <= 0.05:
                            medkit.rect.topleft = (enemy.x, enemy.y)
                            self.medkits.add(medkit)
                        if random.random() <= 0.001:
                            shield.rect.topleft = (enemy.x, enemy.y)
                            self.shields.add(shield)
                        
            if bullet_speedy_collisions:
                total_enemies_hit = list(bullet_speedy_collisions.values())[0]
                for speedyboi in total_enemies_hit:
                    speedyboi.hp -= 1
                    speedyboi.knockback(bullet)
                    if speedyboi.hp <= 0:
                        speedyboi.kill()
                        self.speedy_bois_killed +=1
                        self.score+=1
                        self.score_surface = self.font.render(str(self.score), True, (255, 255, 255))
                        if random.random() <= 0.05:
                            medkit.rect.topleft = (enemy.x, enemy.y)
                            self.medkits.add(medkit)
                        if random.random() <= 0.001:
                            shield.rect.topleft = (enemy.x, enemy.y)
                            self.shields.add(shield)

            if bullet_bigenemy_collisions: #if bullets collided with Big Bois...
                total_enemies_hit = list(bullet_bigenemy_collisions.values())[0] #fill a list with big enemy collisions' values
                for bigenemy in total_enemies_hit: #loop through those listed collisions
                    bigenemy.hp -= 1 #subtract HP from EACH Big Boi
                    bigenemy.knockback(bullet)
                    if bigenemy.hp <= 0: #if the HP of a specific big boi is 0 or lower...
                        bigenemy.kill() #ded
                        self.score+=3 #one point!
                        self.score_surface = self.font.render(str(self.score), True, (255, 255, 255)) 

            if bullet_blindbulb_collisions:
                total_enemies_hit = list(bullet_blindbulb_collisions.values())[0]
                for blind_bulb in total_enemies_hit:
                    blind_bulb.hp -= 1
                    blind_bulb.knockback(bullet)
                    if blind_bulb.hp <= 0:
                        self.player.status = "blind"
                        blind_bulb.kill()
                        blindtimer = pygame.time.get_ticks() + 5000
                        
            if bullet_deathbulb_collisions:
                total_enemies_hit = list(bullet_deathbulb_collisions.values())[0]
                for death_bulb in total_enemies_hit:
                    death_bulb.hp -= 1
                    self.player.status = "permablind"
                    death_bulb.kill()
                        


            if self.player.firing == True:
                bullet = Bullet(self)
                self.bullets.add(bullet)

            #Bullet/Edge-Edge-of-Screen behaviors
            for bullet in self.bullets: #check dem bullets
                if bullet.rect.left > self.settings.screen_WIDTH or bullet.rect.right < 0: #kill the bullets if they go off-screen
                    bullet.kill() #KILL
                if bullet.rect.top > self.settings.screen_HEIGHT or bullet.rect.bottom < 0: #kill the bullets if they go off-screen, twice
                    bullet.kill() #KILL THEM ALL
                bullet.draw(self) #Draw moar bullet
                bullet.update() #Updates them there bullets
            


            #Item Behavior Handlers
            for medkit in self.medkits:
                medkit.draw(self)
                medkit.heal_player(self.player)
            for shield in self.shields:
                shield.draw(self)
                shield.add_shield(self.player)



            #INDIVIDUAL Enemy Setup
            enemy = Enemy(self) 
            big_enemy = BigEnemy(self)
            speedy_boi = SpeedyBoi(self)
            blind_bulb = BlindBulb(self)
            death_bulb = DeathBulb(self)
            


            #INDIVIDUAL Item Setup
            medkit = Medkit(self)
            shield = Shield(self)



            #Player-related existence On-Screen
            self.player.update() #update the player, mainly its position, tho
            self.player.blit(self) #draw the player
            


            #Wave Threshold Handlers
            if self.enemies_spawned > 0.3*self.level_threshold:
                self.settings.spawnrate = 1

            if (self.enemies_spawned - self.enemies_killed) < 0.3*self.level_threshold:
                self.settings.spawnrate = 0.8



            #Enemy Spawn Handlers
            if len(self.big_enemies) < self.biglevel_threshold and self.bigenemies_spawned < self.biglevel_threshold: #if the length of them big bois is higher than the threshold for em...
                self.big_enemies.add(big_enemy) #add them to the list
                self.bigenemies_spawned += 1 #increment the spawn counter
            
            if random.random() >self.settings.spawnrate and self.enemies_spawned < 1   : #if the Gambler is lucky...
                self.enemies.add(enemy) #add the cannon fodder
                self.enemies_spawned += 1 #add to the valuse of enemies spawned [DEBUGGING]
            
            if random.random() < 0.2 and self.speedy_bois_spawned < self.speedylevel_threshold:
                self.speedy_bois.add(speedy_boi)
                self.speedy_bois_spawned +=1

            if random.random() < 1.001 and self.bulbs_spawned < 1:
                if random.random() < 1.00001:
                    self.death_bulbs.add(death_bulb)
                    self.bulbs_spawned += 1
                else:
                    self.blind_bulbs.add(blind_bulb)
                    self.bulbs_spawned += 1



            #Enemy Drawing Handlers
            for big_enemy in self.big_enemies: #Gotta check ALL of them big bois
                big_enemy.draw(self) #Spawn the large lads
                big_enemy.update(self.player) #update them
                big_enemy.check_collide(self.player)
                if big_enemy.hp <= 0:
                    big_enemy.kill() #if no HP, then DIE... DUH!

            for speedy_boi in self.speedy_bois:
                speedy_boi.draw(self)
                speedy_boi.update(self.player)
                speedy_boi.check_collide(self.player)
                if speedy_boi.hp<= 0:
                    speedy_boi.kill()
                
            for blind_bulb in self.blind_bulbs:
                blind_bulb.draw(self)
                blind_bulb.update(self.player)
                blind_bulb.check_collide(self.player)
                if blind_bulb.hp <= 0:
                    self.player.status = "blind"
                    blindtimer = pygame.time.get_ticks() + 5000
                    blind_bulb.kill()
                
            for death_bulb in self.death_bulbs:
                death_bulb.draw(self)
                death_bulb.update(self.player)
                death_bulb.check_collide(self.player)
                if death_bulb.hp <= 0:
                    self.player.status = "permablind"
                    self.player.HP = 0
                    death_bulb.kill()
                    
            for enemy in self.enemies: #Gotta check the WHOLE DAMN LIST OF ENEMIES
                #if random.random() < self.settings.ENEMY_FLASH_RATE: 
                enemy.draw(self)
                enemy.update(self.player) #update those little shits
                enemy.check_collide(self.player)
                if enemy.hp <= 0:
                    enemy.kill()
                    self.enemies_killed+=1



            #Player HP Handlers
            if self.player.HP > 50:
                self.player.HP = 50 #prevent overheal
            if self.player.HP <= 0:
                if self.player.status == "permablind":
                    self.death_surface = self.font.render("YOU ARE PERMANENTLY BLIND: U R DED", True, (0, 0, 0))
                    self.screen.fill("white")
                else:
                    self.screen.fill("black")
                self.screen.blit(self.death_surface, (self.settings.screen_WIDTH//2.25,self.settings.screen_HEIGHT//2))
                for enemy in self.enemies:
                    enemy.kill()
                for big_enemy in self.big_enemies:
                    big_enemy.kill()
                for speedy_boi in self.speedy_bois:
                    speedy_boi.kill()
                for blind_bulb in self.blind_bulbs:
                    blind_bulb.kill()
                for death_bulb in self.death_bulbs:
                    death_bulb.kill()    
            


            #Player Status Handlers
            if self.player.status != "blind":
                pygame.display.flip() #update the ENTIRE display
            if self.player.status == "permablind":
                self.player.HP = 0
                self.screen.blit(self.death_surface, (self.settings.screen_WIDTH//2.25,self.settings.screen_HEIGHT//2))
            


            #Wave-Related code
            if self.enemies_killed >= self.level_threshold: 
                self.wave_number += 1 
                self.enemies_spawned = 0 
                self.enemies_killed = 0
                self.speedy_bois_spawned = 0
                self.bigenemies_spawned = 0
                self.bulbs_spawned = 0
                for big_enemy in self.big_enemies:
                    big_enemy.kill()
                for bulb in self.blind_bulbs:
                    blind_bulb.kill()
                for bulb in self.death_bulbs:
                    death_bulb.kill()
                if self.wave_number <= 10:
                    self.level_threshold = 5 + 5*self.wave_number 
                elif self.wave_number > 10: 
                    self.level_threshold = 5 + 7*self.wave_number
                if self.wave_number <= 10: 
                    self.biglevel_threshold = math.floor(self.wave_number // 5)
                elif self.wave_number > 10: 
                    self.biglevel_threshold = math.floor(self.wave_number // 3)
                for medkit in self.medkits:
                    medkit.kill()
            self.clock.tick(self.settings.FPS) 
            self.frame_count += 1 
 


#RUN THAT SHIT!
game = Game() 
game.run()