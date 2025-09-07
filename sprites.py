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

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        # where the image is posiitoned, size
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        pass

        
    
