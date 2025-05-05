#import dem modules
import pygame
import random
import math

#import dem other file
from spritesheet import SpriteSheet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        """Basic Bois"""
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.hp = 2
        self.type = "normal"
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

        self.spritesheet = SpriteSheet(r"sprites/zombWalk.png")
        self.sprites = self.spritesheet.get_images(0,0,32,32,8)
        self.image = self.sprites[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)

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
                speed = 2  # Set a speed for the enemy
                self.x += self.direction[0] * speed
                self.y += self.direction[1] * speed
            
            self.rect.topleft = (self.x, self.y)

        if self.game.frame_count % 15 == 0:
            self.frame = (self.frame+1)% len(self.sprites)
        self.image = self.sprites[self.frame]

    def draw(self, game):
        """Draw them little shits"""
        game.screen.blit(self.image, self.rect.topleft) 



class BigEnemy(pygame.sprite.Sprite):
    count = 0
    def __init__(self, game):
        """BEEG BOI"""
        super().__init__()
        self.game = game
        self.settings = self.game.settings
        self.hp = 3
        self.type = "special"
        self.speed = self.settings.big_boi_SPEED


        self.spritesheet = SpriteSheet(r"sprites\bigguyWalk.png")
        self.sprites = self.spritesheet.get_images(0,0,48,48,8)
        self.image = self.sprites[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)
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
                speed = 2  # Set a speed for the enemy
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
    count = 0
    def __init__(self, game):
        """Speedy Boi"""
        super().__init__()
        self.game = game
        self.settings = self.game.settings

        self.hp = 1
        self.type = "special"
        self.speed = self.settings.speedy_boi_SPEED

        self.spritesheet = SpriteSheet(r"sprites\machete.png")
        self.sprites = self.spritesheet.get_images(0,0,48,48,1)
        self.image = self.sprites[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)
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
                speed = 2  # Set a speed for the enemy
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


#JOKE ENEMIES!

class BlindBulb(pygame.sprite.Sprite):
    count = 0
    def __init__(self, game):
        """Run?"""
        super().__init__()
        self.game = game
        self.settings = self.game.settings

        self.hp = 3
        self.type = "special"
        self.speed = self.settings.blindBulb_SPEED


        self.spritesheet = SpriteSheet(r"sprites\BlindBulb.png")
        self.sprites = self.spritesheet.get_images(0,0,32,32,8)
        self.image = self.sprites[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)
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
                speed = 2  # Set a speed for the enemy
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
        self.game = game
        self.settings = self.game.settings

        self.hp = 1
        self.type = "special"
        self.speed = self.settings.big_boi_SPEED


        self.spritesheet = SpriteSheet(r"sprites\DeathBulb.png")
        self.sprites = self.spritesheet.get_images(0,0,32,32,12)
        self.image = self.sprites[0]
        
        self.rect = self.image.get_rect()
        self.rect.center = (-1000,-1000)
        spawn = random.choice(['top', 'bottom', 'left', 'right'])
        self.cycle = 0 
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


        self.frame = 0
        self.count += 1 
    
    def check_collide(self, player):
        if player:
            if self.rect.colliderect(player.rect):
                self.hp -= 1

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
                speed = 2  # Set a speed for the enemy
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