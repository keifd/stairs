import pygame
from config import *

class Boss(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.bosses
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE

        self.scale_factor = 2
        self.width = TILE_SIZE * self.scale_factor
        self.height = TILE_SIZE * self.scale_factor

        self.x_change = 0
        self.y_change = 0
        self.animation_loop = 0

        self.image = self.game.character_spritesheet.get_sprite(0*32, 2*32, TILE_SIZE, TILE_SIZE)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.max_health = 200
        self.health = self.max_health

        self.bar_width = 400  # full width of the bar
        self.bar_height = 20
        self.bar_x = (self.game.screen.get_width() - self.bar_width) // 2  # center horizontally
        self.bar_y = self.game.screen.get_height() - self.bar_height - 20  # 20 px from bottom

    def update(self):
        self.movement()
        self.animate()

        self.charge_attack()
        
        self.rect.x += self.x_change
        self.collide(self.x_change, 0)
        self.rect.y += self.y_change
        self.collide(0, self.y_change)


        self.x_change = 0
        self.y_change = 0

    def movement(self):
        player = self.game.player

        if player.rect.x > self.rect.x:
            self.x_change = BOSS_SPEED
            self.facing = "right"
        elif player.rect.x < self.rect.x:
            self.x_change = -BOSS_SPEED
            self.facing = "left"
        if player.rect.y > self.rect.y:
            self.y_change = BOSS_SPEED
            self.facing = "down"
        elif player.rect.y < self.rect.y:
            self.y_change = -BOSS_SPEED
            self.facing = "up"
    
    def animate(self):
        pass

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
    
    def take_damadge(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.kill()
            self.game.boss_stage = False
    
    def draw(self, surface):

        # Draw boss health bar (full width at bottom)
        health_ratio = self.health / self.max_health
        fill_width = int(self.bar_width * health_ratio)

        # background
        pygame.draw.rect(surface, CHARCOAL, (self.bar_x, self.bar_y, self.bar_width, self.bar_height))
        # fill
        pygame.draw.rect(surface, RED, (self.bar_x, self.bar_y, fill_width, self.bar_height))
        # Optional: white border
        pygame.draw.rect(surface, WHITE, (self.bar_x, self.bar_y, self.bar_width, self.bar_height), 2)

    def charge_attack(self):
        pass
