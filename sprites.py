import pygame
from config import *
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x,y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

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


    def collide(self, x_change, y_change):
        # Enemy collision
        if pygame.sprite.spritecollide(self, self.game.enemies, False):
            self.game.playing = False

        # Wall collision
        for wall in self.game.walls:
            if pygame.sprite.collide_rect(self, wall):
                if x_change > 0:
                    self.rect.right = wall.rect.left
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if x_change < 0:
                    self.rect.left = wall.rect.right
                    for sprite in self.game.all_sprites:
                         sprite.rect.x -= PLAYER_SPEED
                if y_change > 0:
                    self.rect.bottom = wall.rect.top
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if y_change < 0:
                    self.rect.top = wall.rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED

        



    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        elif keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        elif keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        elif keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

        
    

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

        wall_dict = {
            1 : (40*32, 18*32),
            2 : (41*32, 18*32),
            3 : (42*32, 18*32),
            4 : (43*32, 18*32),
            5 : (44*32, 18*32),
            6 : (45*32, 18*32),
            7 : (46*32, 18*32)
        }

        column, row = wall_dict.get(wall_type, (0, 0))
        self.image = self.game.character_spritesheet.get_sprite(column, row, self.width, self.height)
            
            
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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.x_change = 0
        self.y_change = 0
        self.facing = random.choice(["left", "right", "up", "down"])
        self.max_travel = random.randint(7,120)
        self.movement_loop = 0
        self.animation_loop = 0

        self.image = self.game.skeleton_spritesheet.get_sprite(0*32, 10*32, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.collide(self.x_change, 0)
        self.rect.y += self.y_change
        self.collide(0, self.y_change)
        self.animate()


        self.x_change = 0
        self.y_change = 0

    def movement(self):
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



            