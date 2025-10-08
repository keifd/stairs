
import pygame
from config import *

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game

        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x 
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.animation_loop = 0

        self.facing = self.game.player.facing

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # fully transparent
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y

        self.hit = False

    def update(self):
        self.animate()
        self.collide()
    
    def collide(self):
        if not self.hit:
            hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
            if hits:
                self.game.currency += 5

            hits = pygame.sprite.spritecollide(self, self.game.bosses, False)
            for boss in hits:
                boss.take_damadge(10)
                self.hit = True  
                break  
    
    def animate(self):
        # increment the animation loop
        self.animation_loop += 0.5
        # destroy the sprite after some duration (example: 12 frames)
        if self.animation_loop >= 5:
            self.game.player.attack = False
            self.kill()
