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

        if self.game.world == 1:
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
        elif self.game.world == 2:
            wall_1 = [12*32, 17*32]
            wall_2 = [13*32, 17*32]
            wall_3 = [14*32, 17*32]
            wall_4 = [15*32, 17*32]
            wall_5 = [16*32, 17*32]
            wall_6 = [17*32, 17*32]
            wall_7 = [18*32, 17*32]
            wall_8 = [19*32, 17*32]
            wall_9 = [20*32, 17*32]
            wall_10 = [21*32, 17*32]
            wall_list = [wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_9, wall_10]
            wall = random.choice(wall_list)

            self.image = self.game.character_spritesheet.get_sprite(wall[0], wall[1], self.width, self.height) 
        elif self.game.world == 3:
            wall_1 = [0*32, 14*32]
            wall_2 = [1*32, 14*32]
            wall_3 = [2*32, 14*32]
            wall_4 = [3*32, 14*32]
            wall_5 = [4*32, 14*32]
            wall_6 = [5*32, 14*32]
            wall_7 = [6*32, 14*32]
            wall_8 = [7*32, 14*32]
            wall_list = [wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8]
            wall = random.choice(wall_list)

            self.image = self.game.character_spritesheet.get_sprite(wall[0], wall[1], self.width, self.height)
            
            
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y