
import pygame
from config import *
import math

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

        self.image = self.game.player_spritesheet.get_sprite(0*32, 17*32, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        self.collide()
    
    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
    
    def animate(self):
        left_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 17*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 17*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 17*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 17*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 17*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 17*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(7*32, 17*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(8*32, 17*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(9*32, 17*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(10*32, 17*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(11*32, 17*32, self.width, self.height),
            
        ]
        right_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 19*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 19*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 19*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 19*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 19*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 19*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(7*32, 19*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(8*32, 19*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(9*32, 19*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(10*32, 19*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(11*32, 19*32, self.width, self.height)
        ]
        up_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 16*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 16*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 16*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 16*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 16*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 16*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(7*32, 16*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(8*32, 16*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(9*32, 16*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(10*32, 16*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(11*32, 16*32, self.width, self.height)
        ]
        down_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 18*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 18*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 18*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 18*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 18*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 18*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(7*32, 18*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(8*32, 18*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(9*32, 18*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(10*32, 18*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(11*32, 18*32, self.width, self.height)
        ]
        if self.facing == "left":
            self.image = left_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= len(left_animations):
                self.kill()
        if self.facing == "right":
            self.image = right_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= len(right_animations):
                self.kill()
        if self.facing == "up":
            self.image = up_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= len(up_animations):
                self.kill()
        if self.facing == "down":
            self.image = down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.5
            if self.animation_loop >= len(down_animations):
                self.kill()
