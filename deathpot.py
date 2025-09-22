import pygame
from config import *

class DeathPot(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = DEATH_POT_LAYER
        self.groups = self.game.all_sprites, self.game.deathpot
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        hp = [28*32, 24*32]

        self.image = self.game.character_spritesheet.get_sprite(hp[0], hp[1], self.width, self.height)
            
            
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.collide()
    
    def collide(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.health -= 90
            if self.game.health <= 0:
                self.game.playing = False
                self.game.game_over()
            self.kill()