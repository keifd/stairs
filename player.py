import pygame
from config import *
import math
import random
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        # specifies the layer the player will be show first
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        # adding in the player to the old sprite group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = "right"
        self.animation_loop = 0

        self.image = self.game.player_spritesheet.get_sprite(0*32, 10*32, self.width, self.height)


        # where the image is posiitoned, size
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def animate(self):
        left_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 9*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 9*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 9*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 9*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 9*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 9*32, self.width, self.height)
        ]
        right_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 11*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 11*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 11*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 11*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 11*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 11*32, self.width, self.height)
        ]
        up_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 8*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 8*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 8*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 8*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 8*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 8*32, self.width, self.height)
        ]
        down_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 10*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 10*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 10*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 10*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 10*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 10*32, self.width, self.height)
        ]
        sprint_left_animations = [
            self.game.player_spritesheet.get_sprite(0*32, 39*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(1*32, 39*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 39*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 39*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 39*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 39*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 39*32, self.width, self.height)
        ]
        sprint_right_animations = [
            self.game.player_spritesheet.get_sprite(0*32, 41*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(1*32, 41*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 41*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 41*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 41*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 41*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 41*32, self.width, self.height)
        ]
        sprint_up_animations = [
            self.game.player_spritesheet.get_sprite(0*32, 38*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(1*32, 38*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 38*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 38*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 38*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 38*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 38*32, self.width, self.height)
        ]
        sprint_down_animations = [
            self.game.player_spritesheet.get_sprite(0*32, 40*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(1*32, 40*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 40*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 40*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 40*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 40*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 40*32, self.width, self.height)
        ]
        if self.sprinting:
            if self.facing == "left":
                if self.y_change == 0 and self.x_change ==0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 9*32, self.width, self.height)
                else:
                    self.image = sprint_left_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(left_animations) - 1:
                        self.animation_loop = 0
            if self.facing == "right":
                if self.y_change == 0 and self.x_change == 0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 11*32, self.width, self.height)
                else:
                    self.image = sprint_right_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(right_animations) - 1:
                        self.animation_loop = 0
            if self.facing == "up":
                if self.x_change == 0 and self.y_change == 0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 8*32, self.width, self.height)
                else:
                    self.image = sprint_up_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(up_animations) - 1:
                        self.animation_loop = 0
            if self.facing == "down":
                if self.x_change == 0 and self.y_change == 0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 10*32, self.width, self.height)
                else:
                    self.image = sprint_down_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(down_animations) - 1:
                        self.animation_loop = 0
        else:
            if self.facing == "left":
                if self.y_change == 0 and self.x_change ==0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 9*32, self.width, self.height)
                else:
                    self.image = left_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(left_animations) - 1:
                        self.animation_loop = 0
            if self.facing == "right":
                if self.y_change == 0 and self.x_change == 0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 11*32, self.width, self.height)
                else:
                    self.image = right_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(right_animations) - 1:
                        self.animation_loop = 0
            if self.facing == "up":
                if self.x_change == 0 and self.y_change == 0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 8*32, self.width, self.height)
                else:
                    self.image = up_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(up_animations) - 1:
                        self.animation_loop = 0
            if self.facing == "down":
                if self.x_change == 0 and self.y_change == 0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 10*32, self.width, self.height)
                else:
                    self.image = down_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(down_animations) - 1:
                        self.animation_loop = 0
    
            
        
    
    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.collide(self.x_change, 0)

        self.rect.y += self.y_change
        self.collide(0, self.y_change)

        self.animate()

        # reset movement each frame
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        keys = pygame.key.get_pressed()
        speed = PLAYER_SPEED
        self.sprinting = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
    
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            speed = PLAYER_SPEED * 1.5

        if keys[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += speed
            self.x_change -= speed
            self.facing = 'left'
        elif keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= speed
            self.x_change += speed
            self.facing = 'right'
        elif keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += speed
            self.y_change -= speed
            self.facing = 'up'
        elif keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= speed
            self.y_change += speed
            self.facing = 'down'


    def collide(self, x_change, y_change):
        # Enemy collision
        if pygame.sprite.spritecollide(self, self.game.enemies, False):
            if self.facing == "left":
                for sprite in self.game.all_sprites:
                    sprite.rect.x += PLAYER_SPEED * KNOCK_DISTANCE

        # Wall collision
        for wall in self.game.walls:
            if pygame.sprite.collide_rect(self, wall):
                if x_change > 0:
                    self.rect.right = wall.rect.left
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += x_change  # use the real movement
                if x_change < 0:
                    self.rect.left = wall.rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += x_change
                if y_change > 0:
                    self.rect.bottom = wall.rect.top
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += y_change
                if y_change < 0:
                    self.rect.top = wall.rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += y_change


        