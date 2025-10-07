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

        self.attack = False
        
    
    def animate(self):
        walk_left_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 9*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 9*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 9*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 9*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 9*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 9*32, self.width, self.height)
        ]
        walk_right_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 11*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 11*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 11*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 11*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 11*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 11*32, self.width, self.height)
        ]
        walk_up_animations = [
            self.game.player_spritesheet.get_sprite(1*32, 8*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(2*32, 8*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(3*32, 8*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(4*32, 8*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(5*32, 8*32, self.width, self.height),
            self.game.player_spritesheet.get_sprite(6*32, 8*32, self.width, self.height)
        ]
        walk_down_animations = [
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

        # player is attacking
        if self.attack:
            if self.facing == "left":
                self.image = self.game.player_spritesheet.get_sprite(12*32, 17*32, self.width, self.height)
            elif self.facing == "right":
                self.image = self.game.player_spritesheet.get_sprite(12*32, 19*32, self.width, self.height)
            elif self.facing == "up":
                self.image = self.game.player_spritesheet.get_sprite(12*32, 16*32, self.width, self.height)
            elif self.facing == "down":
                self.image = self.game.player_spritesheet.get_sprite(12*32, 18*32, self.width, self.height)
            return
        
        # player is sprinting
        if self.sprinting:
            if self.facing == "left":
                if self.y_change == 0 and self.x_change ==0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 9*32, self.width, self.height)
                else:
                    self.image = sprint_left_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(sprint_left_animations) - 1:
                        self.animation_loop = 0
            if self.facing == "right":
                if self.y_change == 0 and self.x_change == 0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 11*32, self.width, self.height)
                else:
                    self.image = sprint_right_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(sprint_right_animations) - 1:
                        self.animation_loop = 0
            if self.facing == "up":
                if self.x_change == 0 and self.y_change == 0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 8*32, self.width, self.height)
                else:
                    self.image = sprint_up_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(sprint_up_animations) - 1:
                        self.animation_loop = 0
            if self.facing == "down":
                if self.x_change == 0 and self.y_change == 0:
                    self.image =  self.game.player_spritesheet.get_sprite(0*32, 10*32, self.width, self.height)
                else:
                    self.image = sprint_down_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(sprint_down_animations) - 1:
                        self.animation_loop = 0
            return
        
        # player is walking
        if self.facing == "left":
            if self.y_change == 0 and self.x_change ==0:
                self.image =  self.game.player_spritesheet.get_sprite(0*32, 9*32, self.width, self.height)
            else:
                self.image = walk_left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > len(walk_left_animations) - 1:
                    self.animation_loop = 0
        if self.facing == "right":
            if self.y_change == 0 and self.x_change == 0:
                self.image =  self.game.player_spritesheet.get_sprite(0*32, 11*32, self.width, self.height)
            else:
                self.image = walk_right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > len(walk_right_animations) - 1:
                    self.animation_loop = 0
        if self.facing == "up":
            if self.x_change == 0 and self.y_change == 0:
                self.image =  self.game.player_spritesheet.get_sprite(0*32, 8*32, self.width, self.height)
            else:
                self.image = walk_up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > len(walk_up_animations) - 1:
                    self.animation_loop = 0
        if self.facing == "down":
            if self.x_change == 0 and self.y_change == 0:
                self.image =  self.game.player_spritesheet.get_sprite(0*32, 10*32, self.width, self.height)
            else:
                self.image = walk_down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop > len(walk_down_animations) - 1:
                    self.animation_loop = 0
    
            
        
    
    def update(self):
        self.movement()
        self.animate()

        self.collide_enemy()
        self.collide_boss()
        
        self.rect.x += self.x_change
        self.collide_wall()

        self.rect.y += self.y_change
        self.collide_wall()

        # reset movement each frame
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        keys = pygame.key.get_pressed()
        speed = PLAYER_SPEED
        self.sprinting = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

        # disable player attacking and moving at the same time
        if not self.attack:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                speed = PLAYER_SPEED * 1.5

            if keys[pygame.K_a]:
                self.x_change -= speed
                self.facing = 'left'
            elif keys[pygame.K_d]:
                self.x_change += speed
                self.facing = 'right'
            elif keys[pygame.K_w]:
                self.y_change -= speed
                self.facing = 'up'
            elif keys[pygame.K_s]:
                self.y_change += speed
                self.facing = 'down'

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            if self.facing == "right":
                self.x_change -= PLAYER_SPEED * KNOCK_DISTANCE
            elif self.facing == "left":
                self.x_change += PLAYER_SPEED * KNOCK_DISTANCE
            elif self.facing == "up":
                self.y_change += PLAYER_SPEED * KNOCK_DISTANCE
            elif self.facing == "down":
                self.y_change -= PLAYER_SPEED * KNOCK_DISTANCE
            
             # Decrement health directly
            self.game.health -= 10

            # Check for game over
            if self.game.health <= 0:
                self.game.playing = False
                self.game.game_over()

    def collide_boss(self):
        hits = pygame.sprite.spritecollide(self, self.game.bosses, False)
        if hits:
            if self.facing == "right":
                self.x_change -= PLAYER_SPEED * KNOCK_DISTANCE
            elif self.facing == "left":
                self.x_change += PLAYER_SPEED * KNOCK_DISTANCE
            elif self.facing == "up":
                self.y_change += PLAYER_SPEED * KNOCK_DISTANCE
            elif self.facing == "down":
                self.y_change -= PLAYER_SPEED * KNOCK_DISTANCE
            
             # Decrement health directly
            self.game.health -= 10

            # Check for game over
            if self.game.health <= 0:
                self.game.playing = False
                self.game.game_over()
                

    def collide_wall(self):
        # Wall collision
        for wall in self.game.walls:
            if pygame.sprite.collide_rect(self, wall):
                if self.x_change > 0:
                    self.rect.right = wall.rect.left
                if self.x_change < 0:
                    self.rect.left = wall.rect.right
                if self.y_change > 0:
                    self.rect.bottom = wall.rect.top
                if self.y_change < 0:
                    self.rect.top = wall.rect.bottom
    



        