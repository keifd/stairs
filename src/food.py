import pygame
from config import *
import random

class Food(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = FOOD_LAYER
        self.groups = self.game.all_sprites, self.game.foods
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        hp_1 = [34*32, 23*32]
        hp_2 = [35*32, 23*32]
        hp_3 = [36*32, 23*32]
        hp_4 = [37*32, 23*32]
        hp_5 = [38*32, 23*32]
        hp_6 = [39*32, 23*32]
        hp_7 = [40*32, 23*32]
        hp_list = [hp_1, hp_2, hp_3, hp_4, hp_5, hp_6, hp_7]
        hp = random.choice(hp_list)

        self.image = self.game.character_spritesheet.get_sprite(hp[0], hp[1], self.width, self.height)
            
            
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.collide()
    
    def collide(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.health += 20
            if self.game.health > self.game.MAX_HP:
                self.game.health = self.game.MAX_HP
            self.kill()