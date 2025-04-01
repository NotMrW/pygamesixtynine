import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
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

        self.color = (0, 255, 0)
        self.rect = pygame.Rect(self.x, self.y, 20, 20)  # Corrected to pygame.Rect

    def update(self, player):
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

    def draw(self, game):
        pygame.draw.rect(game.screen, self.color, self.rect)