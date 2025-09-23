import pygame
from config import *
import random

class Key(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = KEY_LAYER
        self.groups = self.game.all_sprites, self.game.keys
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        key = [54*32, 45*32]

        self.image = self.game.character_spritesheet.get_sprite(key[0], key[1], self.width, self.height)
            
            
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.collide()
    
    def collide(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.key += 1