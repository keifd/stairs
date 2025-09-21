import pygame
from config import *
from player import *
from enemy import *
from attack import *
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x,y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite
    

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


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = self.game.character_spritesheet.get_sprite(0*32, 15*32, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('VT323-Regular.ttf', fontsize)

        self.image = pygame.Surface((width, height,))
        self.image.fill(bg)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        
        self.text = self.font.render(content, True, fg)
        self.text_rect = self.text.get_rect(center=(width/2, height/2))
        self.image.blit(self.text,self.text_rect)


            