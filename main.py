import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.caption = pygame.display.set_caption("Dungeon Fighter")
        self.clock = pygame.time.Clock()

        # if the player hasn't died
        self.running = True

        self.character_spritesheet = Spritesheet("img/dungeon.png")

        sheet = pygame.image.load("img/player.png").convert_alpha()
        sheet_32 = pygame.transform.scale(sheet, (416, 1728))  # 50% size
        pygame.image.save(sheet_32, "img/player_32x32.png")
        self.player_spritesheet = Spritesheet("img/player_32x32.png")

        sheet = pygame.image.load("img/skeleton.png").convert_alpha()
        sheet_32 = pygame.transform.scale(sheet, (832, 2496))
        pygame.image.save(sheet_32, "img/skeleton_32x32.png")
        self.skeleton_spritesheet = Spritesheet("img/skeleton_32x32.png")

        print(sheet.get_width(), sheet.get_height())


    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column in [1,2,3,4,5,6,7]:
                    Wall(self, j, i, column)
                if column == 90:
                    Player(self, j, i)
                if column == 200:
                    Enemy(self, j ,i)

    def new(self):
        # if the player is still playing
        self.playing = True

        # group of sprites that we can control, allow us to update all the sprites at once
        self.all_sprites = pygame.sprite.LayeredUpdates()
        # storing immovable walls
        self.walls = pygame.sprite.LayeredUpdates()      
        # storing enemies
        self.enemies = pygame.sprite.LayeredUpdates()   
        # storing attacks
        self.attacks = pygame.sprite.LayeredUpdates()     

        self.createTilemap()
        
    
    def events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.playing = False


    def update(self):
        self.all_sprites.update()


    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # set the frame rate
        self.clock.tick(FPS)
        pygame.display.update()


    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass
    def intro_screen(self):
        pass


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
