import pygame
from config import *

class HealthPot(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = HEALTH_POT_LAYER
        self.groups = self.game.all_sprites, self.game.healthpots
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        hp = [2*32, 25*32]

        self.image = self.game.character_spritesheet.get_sprite(hp[0], hp[1], self.width, self.height)
            
            
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.collide()
    
    def collide(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.MAX_HP += 20
            self.game.health = self.game.MAX_HP
            if self.game.player_health_bar.width < 600:
                self.game.player_health_bar.width += 20
            self.kill()
