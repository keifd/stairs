import pygame
from config import *
import random

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, wall_type):
        self.game = game
        self._layer = WALL_LAYER
        self.groups = self.game.all_sprites, self.game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        wall_1 = [40*32, 18*32]
        wall_2 = [41*32, 18*32]
        wall_3 = [42*32, 18*32]
        wall_4 = [43*32, 18*32]
        wall_5 = [44*32, 18*32]
        wall_6 = [45*32, 18*32]
        wall_7 = [46*32, 18*32]
        wall_list = [wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7]
        wall = random.choice(wall_list)

        self.image = self.game.character_spritesheet.get_sprite(wall[0], wall[1], self.width, self.height)
            
            
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y