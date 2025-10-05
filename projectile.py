import pygame
from config import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game

        self._layer = PROJECTILE_LAYER
        self.groups = self.game.all_sprites, self.game.projectiles
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x 
        self.y = y

        self.radius = 5
        self.width = self.radius * 2
        self.height = self.radius * 2

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA) 
        pygame.draw.circle(self.image, RED, (self.width // 2, self.height // 2), self.width // 2)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.direction = random.choice(["up", "down", "left", "right"])
        self.speed = 2
    
    def movement(self):
        if self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed

    def collide(self):
        # Destroy if hits walls
        if pygame.sprite.spritecollideany(self, self.game.walls):
            self.kill()
        # collide with player
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.health -= 20
            if self.game.health <= 0:
                self.playing = False
                self.game.game_over()

            self.kill()
    
    def update(self):
        self.movement()
        self.collide()

    