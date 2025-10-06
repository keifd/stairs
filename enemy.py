import pygame
from config import *
import math
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, chase_player = False):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.chase_player = chase_player
        if not chase_player:
            self.x = x * TILE_SIZE
            self.y = y * TILE_SIZE
        else:
            self.x = x
            self.y = y
            
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0
        self.facing = random.choice(["left", "right", "up", "down"])
        self.max_travel = random.randint(20,200)
        self.movement_loop = 0
        self.animation_loop = 0

        self.image = self.game.skeleton_spritesheet.get_sprite(0*32, 10*32, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.movement()
        self.animate()
        
        self.rect.x += self.x_change
        self.collide(self.x_change, 0)
        self.rect.y += self.y_change
        self.collide(0, self.y_change)


        self.x_change = 0
        self.y_change = 0

    def movement(self):
        if self.chase_player:
            player = self.game.player

            if player.rect.x > self.rect.x:
                self.x_change = ENEMY_SPEED
                self.facing = "right"
            elif player.rect.x < self.rect.x:
                self.x_change = -ENEMY_SPEED
                self.facing = "left"
            if player.rect.y > self.rect.y:
                self.y_change = ENEMY_SPEED
                self.facing = "down"
            elif player.rect.y < self.rect.y:
                self.y_change = -ENEMY_SPEED
                self.facing = "up"
        else:
            if self.facing == "right":
                self.x_change += ENEMY_SPEED
                self.movement_loop += 1
                if self.movement_loop >= self.max_travel:
                    self.facing = "left" 
            if self.facing == "left":
                self.x_change -= ENEMY_SPEED
                self.movement_loop -= 1
                if self.movement_loop <= 0:
                    self.facing = "right"
            if self.facing == "down":
                self.y_change += ENEMY_SPEED
                self.movement_loop += 1
                if self.movement_loop >= self.max_travel:
                    self.facing = "up"
            if self.facing == "up":
                self.y_change -= ENEMY_SPEED
                self.movement_loop -= 1
                if self.movement_loop <= 0:
                    self.facing = "down"
    
    def animate(self):
        left_animations = [
            self.game.skeleton_spritesheet.get_sprite(1*32, 9*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(2*32, 9*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(3*32, 9*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(4*32, 9*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(5*32, 9*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(6*32, 9*32, self.width, self.height)
        ]
        right_animations = [
            self.game.skeleton_spritesheet.get_sprite(1*32, 11*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(2*32, 11*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(3*32, 11*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(4*32, 11*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(5*32, 11*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(6*32, 11*32, self.width, self.height)
        ]
        up_animations = [
            self.game.skeleton_spritesheet.get_sprite(1*32, 8*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(2*32, 8*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(3*32, 8*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(4*32, 8*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(5*32, 8*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(6*32, 8*32, self.width, self.height)
        ]
        down_animations = [
            self.game.skeleton_spritesheet.get_sprite(1*32, 10*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(2*32, 10*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(3*32, 10*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(4*32, 10*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(5*32, 10*32, self.width, self.height),
            self.game.skeleton_spritesheet.get_sprite(6*32, 10*32, self.width, self.height)
        ]
        if self.facing == "left":
            if self.y_change == 0 and self.x_change ==0:
                self.image =  self.game.skeleton_spritesheet.get_sprite(0*32, 9*32, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > len(left_animations) - 1:
                    self.animation_loop = 0
        if self.facing == "right":
            if self.y_change == 0 and self.x_change == 0:
                self.image =  self.game.skeleton_spritesheet.get_sprite(0*32, 11*32, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > len(right_animations) - 1:
                    self.animation_loop = 0
        if self.facing == "up":
            if self.x_change == 0 and self.y_change == 0:
                self.image =  self.game.skeleton_spritesheet.get_sprite(0*32, 8*32, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > len(up_animations) - 1:
                    self.animation_loop = 0
        if self.facing == "down":
            if self.x_change == 0 and self.y_change == 0:
                self.image =  self.game.skeleton_spritesheet.get_sprite(0*32, 10*32, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > len(down_animations) - 1:
                    self.animation_loop = 0

    def collide(self, x_change, y_change):
        for wall in self.game.walls:
            if pygame.sprite.collide_rect(self, wall):
                if x_change > 0:
                    self.rect.right = wall.rect.left
                if x_change < 0:
                    self.rect.left = wall.rect.right
                if y_change > 0:
                    self.rect.bottom = wall.rect.top
                if y_change < 0:
                    self.rect.top = wall.rect.bottom
    
    