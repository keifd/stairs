import pygame
from config import *
from player import *
from enemy import *
from attack import *
from food import *
from deathpot import *
from wall import *
from ground import *
from stair import *
from key import *
from gate import *
from healthpot import *
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x,y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

class Void(pygame.sprite.Sprite):
    def __init__(self, game, x ,y):
        self.game = game
        self._layer = VOID_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y



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

class HealthBar:
    def __init__(self, x, y, width, height, max_hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_hp = max_hp

    def draw(self, surface, current_hp):
        # Background rectangle (full bar)
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))

        # Current health rectangle
        health_ratio = current_hp / self.max_hp
        current_width = self.width * health_ratio
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, current_width, self.height))
    
class Currency:
    def __init__(self, x, y, font):
        self.x = x
        self.y = y
        self.font = font
        self.color = YELLOW

    def draw(self, surface, current_currency):
        text = self.font.render(f"${current_currency}", True, self.color)
        surface.blit(text, (self.x, self.y))





        