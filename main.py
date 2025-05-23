#import modules
import random
import pygame
from pygame import mixer
import math



#import classes from other files
from settings import Settings
from player import Player
from enemy import Enemy, BigEnemy, SpeedyBoi, BlindBulb, DeathBulb, ZipperSkull
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

        self.dead_music_playing = False

        #Main Setup
        self.settings = Settings() #initialize settings
        self.clock = pygame.time.Clock() #get a clock going
        self.screen = pygame.display.set_mode((self.settings.screen_WIDTH, self.settings.screen_HEIGHT)) #set the screen up
        self.rect = self.screen.get_rect() #get that rect
        pygame.display.set_caption("ZambiFuckers") #name game window
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
        self.time1 = 250
        self.fire_rate = 0


        #Setup every enemy type
        self.enemies = pygame.sprite.Group()
        self.big_enemies = pygame.sprite.Group()
        self.speedy_bois = pygame.sprite.Group()
        self.blind_bulbs = pygame.sprite.Group()
        self.death_bulbs = pygame.sprite.Group()
        self.zipperskulls = pygame.sprite.Group()


        #Enemy-Specific Data Setup
        self.bigenemies_spawned = 0
        self.bulbs_spawned = 0
        self.enemies_spawned = 0
        self.enemies_killed = 0
        self.speedy_bois_spawned = 0
        self.speedy_bois_killed = 0
        self.zipperskulls_spawned = 0
        self.zipperskulls_killed = 0


        #Wave Setup
        self.wave_number = 6
        self.wave_surface = self.font.render(f"Wave: {self.wave_number}", True, (255, 255, 255)) 
        self.spawn_counter = 0
        self.level_threshold = 5 + 5*self.wave_number
        self.biglevel_threshold = math.floor(self.wave_number // 5)
        self.speedylevel_threshold = 0+math.floor(self.wave_number//7)
        self.zipperlevel_threshold = 0


        #Setup Booleans
        self.running = True #I guess we can have a loop for the gaem...



    def run(self): 
        """"Da function to run da gaem"""
        while self.running: #we use "running" value here for loop? Huh, neat 

            
            #DEBUGGING
            print(self.player.weapon, self.fire_rate, self.time1, self.player.firing)



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
                        self.player.firing = True
                    if event.key == pygame.K_k:
                        for enemy in self.enemies:
                            enemy.kill()
                            self.enemies_killed +=1
                    if event.key == pygame.K_e:
                        if self.player.weapon == "pistol":
                            self.player.weapon  = "automatica"

                        elif self.player.weapon == "automatica":
                            self.player.weapon  = "shotgun"

                        elif self.player.weapon == "shotgun": #semi-auto
                            self.player.weapon = "pistol"

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
                    if event.key == pygame.K_SPACE:
                        self.player.firing = False
                


                # *Le Gasp* Mouse-Based Events?!
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.player.firing = True
                if event.type == pygame.MOUSEBUTTONUP:
                        self.player.firing = False
            
            if self.player.rect.left < 0:
                self.player.rect.left = 0
            elif self.player.rect.right > self.settings.screen_WIDTH:
                self.player.rect.right = self.settings.screen_WIDTH
            elif self.player.rect.top < 0:
                self.player.rect.top = 0
            elif self.player.rect.bottom > self.settings.screen_HEIGHT:
                self.player.rect.bottom = self.settings.screen_HEIGHT
            #Player Status handlers
            if self.player.status == "blind":
                game.screen.fill("white")
                pygame.display.flip()
                endblindtimer = pygame.time.get_ticks()
                if endblindtimer >= blindtimer:
                    self.player.status = "none"
            else: #THIS STILL WORKS, ACE!
                bg_image = pygame.image.load('sprites\grasstile.png')
                bg_image = pygame.transform.scale(bg_image, (self.settings.screen_WIDTH, self.settings.screen_HEIGHT))
                game.screen.blit(bg_image, (0, 0))
                game.screen.blit(self.score_surface, (50,100))
                self.wave_surface = self.font.render(f"Wave: {self.wave_number}", True, (255, 255, 255))
                game.screen.blit(self.wave_surface, (50, 50))

            if self.player.firing == False:
                self.time1 = 250

            if self.player.weapon == "pistol" and self.player.firing == False:
                self.fire_rate = 248
            elif self.player.weapon == "shotgun" and self.player.firing == False:
                self.fire_rate = 245
            elif self.player.firing == False:
                self.fire_rate = 0


            #Individual Bullet/Enemy Collision Setup
            bullet_enemy_collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, False) #Bullet/Little_shit collisions
            bullet_bigenemy_collisions = pygame.sprite.groupcollide(self.bullets, self.big_enemies, True, False)
            bullet_speedy_collisions = pygame.sprite.groupcollide(self.bullets, self.speedy_bois, True, False)
            bullet_blindbulb_collisions = pygame.sprite.groupcollide(self.bullets, self.blind_bulbs, True, False)
            bullet_deathbulb_collisions = pygame.sprite.groupcollide(self.bullets, self.death_bulbs, True, False)
            bullet_zipperskull_collisions = pygame.sprite.groupcollide(self.bullets, self.zipperskulls, True, False)



            #Individual Bullet/Enemy Collision Setup
            if bullet_enemy_collisions:
                total_enemies_hit = list(bullet_enemy_collisions.values())[0]
                for enemy in total_enemies_hit:
                    if self.player.weapon == "pistol":
                        enemy.hp -= 1
                    if self.player.weapon == "automatica":
                        enemy.hp -= 0.5
                    if self.player.weapon == "devlogger":
                        enemy.hp -= 10
                    if self.player.weapon == "shotgun":
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
                    if self.player.weapon == "pistol":
                        speedy_boi.hp -= 1
                    if self.player.weapon == "automatica":
                        speedy_boi.hp -= 0.5
                    if self.player.weapon == "devlogger":
                        speedy_boi.hp -= 10
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
                    if self.player.weapon == "pistol":
                        bigenemy.hp -=1
                    if self.player.weapon == "automatica":
                        bigenemy.hp -= 0.5
                    if self.player.weapon == "devlogger":
                        bigenemy.hp -= 10
                    bigenemy.knockback(bullet)
                    if bigenemy.hp <= 0: #if the HP of a specific big boi is 0 or lower...
                        bigenemy.kill() #ded
                        self.score+=3
                        self.score_surface = self.font.render(str(self.score), True, (255, 255, 255)) 

            if bullet_blindbulb_collisions:
                total_enemies_hit = list(bullet_blindbulb_collisions.values())[0]
                for blind_bulb in total_enemies_hit:
                    if self.player.weapon == "pistol":
                        blind_bulb.hp -=1
                    if self.player.weapon == "automatica":
                        blind_bulb.hp -= 0.5
                    if self.player.weapon == "devlogger":
                        blind_bulb.hp -= 10
                    blind_bulb.knockback(bullet)
                    if blind_bulb.hp <= 0:
                        self.player.status = "blind"
                        blind_bulb.kill()
                        blindtimer = pygame.time.get_ticks() + 5000
                        
            if bullet_deathbulb_collisions:
                total_enemies_hit = list(bullet_deathbulb_collisions.values())[0]
                for death_bulb in total_enemies_hit:
                    if self.player.weapon == "pistol":
                        death_bulb.hp -=1
                    if self.player.weapon == "automatica":
                        death_bulb.hp -= 0.5
                    if self.player.weapon == "devlogger":
                        death_bulb.hp -= 10
                    if death_bulb.hp <= 0:
                        self.player.status = "permablind"
                        death_bulb.kill()

            if bullet_zipperskull_collisions:
                total_enemies_hit = list(bullet_zipperskull_collisions.values())[0]
                for zipperskull in total_enemies_hit:
                    if self.player.weapon == "pistol":
                        zipperskull.hp -=1
                    if self.player.weapon == "automatica":
                        zipperskull.hp -= 0.5
                    if self.player.weapon == "devlogger":
                        zipperskull.hp -= 10
                    if zipperskull.hp <= 0:
                        zipperskull.kill()
                        self.score+=50
                        self.score_surface = self.font.render(str(self.score), True, (255, 255, 255))
                        self.zipperskulls_killed+=1 
                        self.enemies_killed += 1



            #Gun Type Fire Rate handlers
            if self.player.firing:
                if self.player.weapon == "pistol":
                        self.fire_rate+=2
                        if self.fire_rate >= self.time1:
                            bullet = Bullet(self)
                            self.bullets.add(bullet)
                            self.time1 = 250
                            self.fire_rate = 200

                if self.player.weapon == "automatica":
                        self.fire_rate += 50
                        if self.fire_rate >= self.time1:
                            bullet = Bullet(self)
                            self.bullets.add(bullet)
                            self.time1 += 250
                
                if self.player.weapon == "shotgun": #semi-auto
                        self.fire_rate += 5
                        if self.fire_rate >= self.time1:
                            for i in range(8):
                                bullet = Bullet(self)
                                bullet.direction[0], bullet.direction[1] = bullet.get_shotgun(self, self.settings.bullet_SPREAD)
                                self.bullets.add(bullet)
                            print("[END GROUP]")
                            
                            self.time1 += 250

                if self.player.weapon == "devlogger":
                        self.fire_rate += 500
                        if self.fire_rate >= self.time1:
                            for i in range(16):
                                bullet = Bullet(self)
                                bullet.direction[0], bullet.direction[1] = bullet.get_shotgun(self, self.settings.bullet_SPREAD*2)
                                self.bullets.add(bullet)
                            self.bullets.add(bullet)
                            self.time1 += 250



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
            zipperskull = ZipperSkull(self)



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
            
            if random.random() >self.settings.spawnrate and self.enemies_spawned < self.level_threshold: #if the Gambler is lucky...
                self.enemies.add(enemy) #add the cannon fodder
                self.enemies_spawned += 1 #add to the valuse of enemies spawned [DEBUGGING]
            
            if random.random() < 0.2 and self.speedy_bois_spawned < self.speedylevel_threshold:
                self.speedy_bois.add(speedy_boi)
                self.speedy_bois_spawned +=1

            if random.random() < 0.00001 and self.bulbs_spawned < 1:
                if random.random() < 0.0000001:
                    self.death_bulbs.add(death_bulb)
                    self.bulbs_spawned += 1
                else:
                    self.blind_bulbs.add(blind_bulb)
                    self.bulbs_spawned += 1
            
            if self.zipperskulls_spawned < self.zipperlevel_threshold:
                self.zipperskulls.add(zipperskull)
                self.zipperskulls_spawned += 1



            #Enemy Drawing Handlers
            for big_enemy in self.big_enemies: #Gotta check ALL of them big bois
                big_enemy.draw(self) #Spawn the large lads
                big_enemy.update(self.player) #update them
                big_enemy.check_collide(self.player)
                if big_enemy.hp <= 0:
                    big_enemy.kill() #if no HP, then DIE... DUH!

            for zipperskull in self.zipperskulls:
                zipperskull.draw(self)
                zipperskull.update(self.player)
                zipperskull.check_collide(self.player)
                if zipperskull.hp <= 0:
                    zipperskull.kill()

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
                #mixer.init()
                if not self.dead_music_playing:
                    mixer.music.load("Audio\Death Theme.mp3")
                    mixer.music.play(3, 0, 6000)
                    self.dead_music_playing = True

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
            if self.wave_number%30 != 0 and self.enemies_killed >= self.level_threshold: 
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
                if self.wave_number%30 == 0:
                    self.zipperlevel_threshold = self.wave_number//30
                    if self.zipperlevel_threshold < 1:
                        self.zipperlevel_threshold == 1
                    self.level_threshold = 0
                else:
                    if self.wave_number <= 10:
                        self.level_threshold = 5 + 5*self.wave_number 
                    elif self.wave_number > 10: 
                        self.level_threshold = 5 + 7*self.wave_number
                    if self.wave_number <= 10: 
                        self.biglevel_threshold = math.floor(self.wave_number // 5)
                        self.speedylevel_threshold = 0+math.floor(self.wave_number//7)
                    elif self.wave_number > 10: 
                        self.biglevel_threshold = math.floor(self.wave_number // 3)
                        self.speedylevel_threshold = 0+math.floor(self.wave_number//6)
                for medkit in self.medkits:
                    medkit.kill()


            elif self.wave_number%30 == 0 and self.zipperskulls_killed >= self.level_threshold:
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
                if self.wave_number%30 == 0:
                    self.zipperlevel_threshold = self.wave_number//30
                    if self.zipperlevel_threshold < 1:
                        self.zipperlevel_threshold == 1
                    self.level_threshold = 1
                else:
                    if self.wave_number <= 10:
                        self.level_threshold = 5 + 5*self.wave_number 
                    elif self.wave_number > 10: 
                        self.level_threshold = 5 + 7*self.wave_number
                    if self.wave_number <= 10: 
                        self.biglevel_threshold = math.floor(self.wave_number // 5)
                        self.speedylevel_threshold = 0+math.floor(self.wave_number//7)
                    elif self.wave_number > 10: 
                        self.biglevel_threshold = math.floor(self.wave_number // 3)
                        self.speedylevel_threshold = 0+math.floor(self.wave_number//6)
                for medkit in self.medkits:
                    medkit.kill()
            self.clock.tick(self.settings.FPS) 
            self.frame_count += 1 
 


#RUN THAT SHIT!
game = Game() 
game.run()