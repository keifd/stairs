import pygame
from config import *
import math

class Portal(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PORTAL_LAYER
        self.groups = self.game.all_sprites, self.game.portals
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE

       
        self.image = self.game.character_spritesheet.get_sprite(29*32, 15*32, self.width, self.height)
            
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.animation_loop = 0
    
    def animate(self):
        animations = [
            self.game.character_spritesheet.get_sprite(29*32, 15*32, self.width, self.height),
            self.game.character_spritesheet.get_sprite(30*32, 15*32, self.width, self.height)
        ]
        self.image = animations[math.floor(self.animation_loop)]
        self.animation_loop += 0.1
        if self.animation_loop > len(animations) - 1:
            self.animation_loop = 0

    
    def collide(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.change_world()

    def update(self):
        self.animate()
        self.collide()
    
