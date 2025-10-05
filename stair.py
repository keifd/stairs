import pygame
from config import *

class Stair(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction):
        self.game = game
        self._layer = STAIR_LAYER
        self.groups = self.game.all_sprites, self.game.stairs
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.direction = direction
        up_stair = [42*32,15*32]
        down_stair = [41*32,15*32]

        if direction == "up":
            self.image = self.game.character_spritesheet.get_sprite(up_stair[0], up_stair[1], self.width, self.height)
        elif direction == "down":
             self.image = self.game.character_spritesheet.get_sprite(down_stair[0], down_stair[1], self.width, self.height)
        
        self.spawn = (self.x - TILE_SIZE, self.y)
            
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.collide()
    
    def collide(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.change_stage(self.direction, self.spawn)
