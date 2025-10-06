import pygame
from config import *

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

        if self.game.world == 1:
            self.image = self.game.character_spritesheet.get_sprite(0*32, 15*32, self.width, self.height)
        elif self.game.world == 2:
            self.image = self.game.character_spritesheet.get_sprite(7*32, 15*32, self.width, self.height)
        elif self.game.world == 3:
            self.image = self.game.character_spritesheet.get_sprite(14*32, 13*32, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y