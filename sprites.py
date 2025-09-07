import pygame
from config import *
import math
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        # specifies the layer the player will be show first
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        # adding in the player to the old sprite group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        # where the image is posiitoned, size
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        move = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            move.x -= 1
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            move.x += 1
            self.facing = 'right'
        if keys[pygame.K_UP]:
            move.y -= 1
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            move.y += 1
            self.facing = 'down'

        # Normalize diagonal movement
        if move.length() > 0:
            move = move.normalize() * PLAYER_SPEED

        # Apply movement to x_change and y_change
        self.x_change = move.x
        self.y_change = move.y

            
        
