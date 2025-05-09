#import dem modules
import pygame
import random
import math



#import dem other file
from spritesheet import SpriteSheet



#Them Classic MOTHERFUCKING zombies!
class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        """Basic Bois"""
        super().__init__()


        
        #Initialize the game and settings for this little shit
        self.game = game
        self.settings = game.settings



        #give this little shit its stats
        self.hp = 2
        self.type = "normal"
        self.speed = self.settings.enemy_SPEED



        #random spawn direction handlers
        spawn = random.choice(['top', 'bottom', 'left', 'right'])
        if spawn == 'top':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = 0
        elif spawn == 'bottom':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = self.settings.screen_HEIGHT
        elif spawn == 'left':
            self.x = 0
            self.y = random.randint(0, self.settings.screen_HEIGHT)
        elif spawn == 'right':
            self.x = self.settings.screen_WIDTH
            self.y = random.randint(0, self.settings.screen_HEIGHT)



        #set up spritesheet
        self.spritesheet = SpriteSheet(r"sprites/zombWalk.png")
        self.sprites = self.spritesheet.get_images(0,0,32,32,8)
        self.image = self.sprites[0]
        


        #define the hitbox based on given spritesheet
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)



        #set a frame count
        self.frame = 0



    def check_collide(self, player):
        if player:
            if self.rect.colliderect(player.rect):
                if player.shield > 0:
                    player.shield -=1
                else:
                    player.HP -= 1 #maybe we should add a damage variable?
                self.hp -= 2



    def knockback(self, bullet):
        self.x+= bullet.direction[0]*self.settings.KNOCKBACK_AMOUNT
        self.y+= bullet.direction[1]*self.settings.KNOCKBACK_AMOUNT



    def update(self, player):
        """Update the Enemies"""
        if player:  # Ensure player is not None
            self.target = player.rect.center
            distance = [
                self.target[0] - self.x,
                self.target[1] - self.y
            ]
            normalize = math.sqrt(distance[0]**2 + distance[1]**2)
            
            if normalize > 0:  # Prevent division by zero
                self.direction = [distance[0] / normalize, distance[1] / normalize]
                self.x += self.direction[0] * self.speed
                self.y += self.direction[1] * self.speed
            
            self.rect.topleft = (self.x, self.y)

        if self.game.frame_count % 15 == 0:
            self.frame = (self.frame+1)% len(self.sprites)
        self.image = self.sprites[self.frame]



    def draw(self, game):
        """Draw them little shits"""
        game.screen.blit(self.image, self.rect.topleft) 



#Start the SPECIALS!
class BigEnemy(pygame.sprite.Sprite):
    count = 0
    def __init__(self, game):
        """BEEG BOI"""
        super().__init__()
        #initialize game and settings of this CHONKer
        self.game = game
        self.settings = self.game.settings



        #Initialize his BEEFY stats
        self.hp = 3
        self.type = "special"
        self.speed = self.settings.big_boi_SPEED



        #set up its spritesheet
        self.spritesheet = SpriteSheet(r"sprites\bigguyWalk.png")
        self.sprites = self.spritesheet.get_images(0,0,48,48,8)
        self.image = self.sprites[0]
        


        #define its FAT hitbox based on its spreitesheet
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)



        #handle its random spawn direction
        spawn = random.choice(['top', 'bottom', 'left', 'right'])
        if spawn == 'top':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = 0
        elif spawn == 'bottom':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = self.settings.screen_HEIGHT
        elif spawn == 'left':
            self.x = 0
            self.y = random.randint(0, self.settings.screen_HEIGHT)
        elif spawn == 'right':
            self.x = self.settings.screen_WIDTH
            self.y = random.randint(0, self.settings.screen_HEIGHT)



        #handle its frames for its sprites
        self.frame = 0
        self.count += 1 
    


    def check_collide(self, player):
        if player:
            if self.rect.colliderect(player.rect):
                if player.shield > 0:
                    player.shield -=1
                else:
                    player.HP -= 1 #maybe we should add a damage variable?
                self.hp -= 3



    def knockback (self, bullet):
        self.x+= bullet.direction[0]*self.settings.KNOCKBACK_AMOUNT
        self.y+= bullet.direction[1]*self.settings.KNOCKBACK_AMOUNT



    def update(self, player):
        """Update the BEEG mf"""
        if player:  # Ensure player is not None
            self.target = player.rect.center
            distance = [
                self.target[0] - self.x,
                self.target[1] - self.y
            ]
            normalize = math.sqrt(distance[0]**2 + distance[1]**2)
            
            if normalize > 0:  # Prevent division by zero
                self.direction = [distance[0] / normalize, distance[1] / normalize]
                self.x += self.direction[0] * self.speed
                self.y += self.direction[1] * self.speed
            
            self.rect.topleft = (self.x, self.y)

        if self.game.frame_count % 15 == 0:
            self.frame = (self.frame+1)% len(self.sprites)
        self.image = self.sprites[self.frame]



    def draw(self, game):
        """Draw them little shits"""
        game.screen.blit(self.image, self.rect.topleft)



    def __del__(self):
        self.count -= 1 

class SpeedyBoi(pygame.sprite.Sprite):

    #need to count how many exist?
    count = 0

    def __init__(self, game):
        """Speedy Boi"""
        super().__init__()



        #initialize game and settings
        self.game = game
        self.settings = self.game.settings



        #initialize attributes
        self.hp = 1
        self.type = "special"
        self.speed = self.settings.speedy_boi_SPEED



        #initialize its speedy spritesheet
        self.spritesheet = SpriteSheet(r"sprites\Runner.png")
        self.sprites = self.spritesheet.get_images(0,0,32,32,1)
        self.image = self.sprites[0]
        


        #define hitbox based on speedy sprites 
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)



        #handle that random spawn direction
        spawn = random.choice(['top', 'bottom', 'left', 'right'])
        if spawn == 'top':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = 0
        elif spawn == 'bottom':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = self.settings.screen_HEIGHT
        elif spawn == 'left':
            self.x = 0
            self.y = random.randint(0, self.settings.screen_HEIGHT)
        elif spawn == 'right':
            self.x = self.settings.screen_WIDTH
            self.y = random.randint(0, self.settings.screen_HEIGHT)



        #Sprite frame handling
        self.frame = 0
        self.count += 1 
    


    def check_collide(self, player):
        if player:
            if self.rect.colliderect(player.rect):
                if player.shield > 0:
                    player.shield -= 2
                else:
                    player.HP -= 10 #maybe we should add a damage variable?
                self.hp -= 1
                player.knockback(self, 50)



    def knockback (self, bullet):
        self.x+= bullet.direction[0]*self.settings.KNOCKBACK_AMOUNT
        self.y+= bullet.direction[1]*self.settings.KNOCKBACK_AMOUNT



    def update(self, player):
        """Update the BULB mf"""
        if player:  # Ensure player is not None
            self.target = player.rect.center
            distance = [
                self.target[0] - self.x,
                self.target[1] - self.y
            ]
            normalize = math.sqrt(distance[0]**2 + distance[1]**2)
            
            if normalize > 0:  # Prevent division by zero
                self.direction = [distance[0] / normalize, distance[1] / normalize]
                self.x += self.direction[0] * self.speed
                self.y += self.direction[1] * self.speed
            
            self.rect.topleft = (self.x, self.y)

        if self.game.frame_count % 15 == 0:
            self.frame = (self.frame+1)% len(self.sprites)
        self.image = self.sprites[self.frame]



    def draw(self, game):
        """Draw them little shits"""
        game.screen.blit(self.image, self.rect.topleft)



    def __del__(self):
        self.count -= 1 



#BOSSES HERE!
class ZipperSkull(pygame.sprite.Sprite):
    def __init__(self, game):
        """OH LAWD HE COMIN!"""
        super().__init__()



        #initialize game ande settings
        self.game = game
        self.settings = game.settings



        #initialize attributes of OH LAWD
        self.speed = self.settings.zipper_SPEED
        self.hp = 50
        self.type = "boss"



        #handle random spawn direction
        spawn = random.choice(['top', 'bottom', 'left', 'right'])
        if spawn == 'top':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = 0
        elif spawn == 'bottom':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = self.settings.screen_HEIGHT
        elif spawn == 'left':
            self.x = 0
            self.y = random.randint(0, self.settings.screen_HEIGHT)
        elif spawn == 'right':
            self.x = self.settings.screen_WIDTH
            self.y = random.randint(0, self.settings.screen_HEIGHT)



        #Handle its spriteshee- OH HE COMIN'
        self.spritesheet = SpriteSheet(r"sprites/Zipperhead.png")
        self.sprites = self.spritesheet.get_images(0,0,80,60,8)
        self.image = self.sprites[0]
        


        #BEEG HITBOX!
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)



        #SET THE FRAME BEFORE HE IS HERE!
        self.frame = 0



    def check_collide(self, player):
        if player:
            if self.rect.colliderect(player.rect):
                if player.shield > 0:
                    player.shield = 0
                else:
                    player.HP -= 20
                player.knockback(self, 250)



    def knockback(self, bullet):
        self.x+= bullet.direction[0]*self.settings.KNOCKBACK_AMOUNT
        self.y+= bullet.direction[1]*self.settings.KNOCKBACK_AMOUNT



    def update(self, player):
        """Update the Enemies"""
        if player:  # Ensure player is not None
            self.target = player.rect.center
            distance = [
                self.target[0] - self.x,
                self.target[1] - self.y
            ]
            normalize = math.sqrt(distance[0]**2 + distance[1]**2)
            
            if normalize > 0:  # Prevent division by zero
                self.direction = [distance[0] / normalize, distance[1] / normalize]
                self.x += self.direction[0] * self.speed
                self.y += self.direction[1] * self.speed
            
            self.rect.topleft = (self.x, self.y)

        if self.game.frame_count % 15 == 0:
            self.frame = (self.frame+1)% len(self.sprites)
        self.image = self.sprites[self.frame]



    def draw(self, game):
        """Draw them little shits"""
        game.screen.blit(self.image, self.rect.topleft) 







#JOKE ENEMIES!
class BlindBulb(pygame.sprite.Sprite):
    count = 0
    def __init__(self, game):
        """Run?"""
        super().__init__()



        #initialize the game and settings, getting old yet?
        self.game = game
        self.settings = self.game.settings



        #attributes, got that?
        self.hp = 3
        self.type = "special"
        self.speed = self.settings.blindBulb_SPEED



        #spritesheet, this is starting to get old.
        self.spritesheet = SpriteSheet(r"sprites\BlindBulb.png")
        self.sprites = self.spritesheet.get_images(0,0,32,32,8)
        self.image = self.sprites[0]
        


        #hitbox definition, this is definitely getting old, even for me.
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)



        #time to handle the random spawn direction
        spawn = random.choice(['top', 'bottom', 'left', 'right'])
        if spawn == 'top':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = 0
        elif spawn == 'bottom':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = self.settings.screen_HEIGHT
        elif spawn == 'left':
            self.x = 0
            self.y = random.randint(0, self.settings.screen_HEIGHT)
        elif spawn == 'right':
            self.x = self.settings.screen_WIDTH
            self.y = random.randint(0, self.settings.screen_HEIGHT)



        #frame counters
        self.frame = 0
        self.count += 1 
    


    def check_collide(self, player):
        if player:
            if self.rect.colliderect(player.rect):
                self.hp -= 3



    def knockback (self, bullet):
        self.x+= bullet.direction[0]*self.settings.KNOCKBACK_AMOUNT
        self.y+= bullet.direction[1]*self.settings.KNOCKBACK_AMOUNT



    def update(self, player):
        """FEAR ITS UPDATE!"""
        if player:  # Ensure player is not None
            self.target = player.rect.center
            distance = [
                self.target[0] - self.x,
                self.target[1] - self.y
            ]
            normalize = math.sqrt(distance[0]**2 + distance[1]**2)
            
            if normalize > 0:  # Prevent division by zero
                self.direction = [distance[0] / normalize, distance[1] / normalize]
                self.x += self.direction[0] * self.speed
                self.y += self.direction[1] * self.speed
            
            self.rect.topleft = (self.x, self.y)

        if self.game.frame_count % 15 == 0:
            self.frame = (self.frame+1)% len(self.sprites)
        self.image = self.sprites[self.frame]



    def draw(self, game):
        """A new threat has been drawn"""
        game.screen.blit(self.image, self.rect.topleft)



    def __del__(self):
        self.count -= 1 



class DeathBulb(pygame.sprite.Sprite):
    count = 0
    def __init__(self, game):
        """RUN"""
        super().__init__()

        

        #set up game and settings
        self.game = game
        self.settings = self.game.settings



        #initialize stats
        self.hp = 1
        self.type = "special"
        self.speed = self.settings.big_boi_SPEED



        #spritesheet... check...
        self.spritesheet = SpriteSheet(r"sprites\DeathBulb.png")
        self.sprites = self.spritesheet.get_images(0,0,32,32,12)
        self.image = self.sprites[0]
        


        #hitbox... check...
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)
        spawn = random.choice(['top', 'bottom', 'left', 'right'])



        #random spawn direction handler... check
        if spawn == 'top':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = 0
        elif spawn == 'bottom':
            self.x = random.randint(0, self.settings.screen_WIDTH)
            self.y = self.settings.screen_HEIGHT
        elif spawn == 'left':
            self.x = 0
            self.y = random.randint(0, self.settings.screen_HEIGHT)
        elif spawn == 'right':
            self.x = self.settings.screen_WIDTH
            self.y = random.randint(0, self.settings.screen_HEIGHT)



        #And the frame count, onto the functions...
        self.frame = 0
        self.count += 1 
    



    def check_collide(self, player):
        if player:
            if self.rect.colliderect(player.rect):
                self.hp -= 1



    def update(self, player):
        """FEAR ITS UPDATE!"""
        if player:  # Ensure player is not None
            self.target = player.rect.center
            distance = [
                self.target[0] - self.x,
                self.target[1] - self.y
            ]
            normalize = math.sqrt(distance[0]**2 + distance[1]**2)
            
            if normalize > 0:  # Prevent division by zero
                self.direction = [distance[0] / normalize, distance[1] / normalize]
                self.x += self.direction[0] * self.speed
                self.y += self.direction[1] * self.speed
            
            self.rect.topleft = (self.x, self.y)

        if self.game.frame_count % 15 == 0:
            self.frame = (self.frame)% len(self.sprites)
        self.image = self.sprites[self.frame]



    def draw(self, game):
        """A new threat has been drawn"""
        game.screen.blit(self.image, self.rect.topleft)



    def __del__(self):
        self.count -= 1 