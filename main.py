import pygame
from sprites import *
from config import *
import maps
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.caption = pygame.display.set_caption("Dungeon Fighter")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('VT323-Regular.ttf', 32)

        # if the player hasn't died
        self.running = True

        self.character_spritesheet = Spritesheet("img/dungeon.png")
        self.player_spritesheet = Spritesheet("img/player_32x32.png")
        self.skeleton_spritesheet = Spritesheet("img/skeleton_32x32.png")

        self.intro_background = BLUE
        self.end_background = RED
    


    def createTilemap(self, tilemap):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'W':
                    Wall(self, j, i, column)
                if column == 'P':
                    self.player = Player(self, j, i)
                if column == 'E':
                    Enemy(self, j ,i)
                if column == 'H':  
                    HealthPot(self, j, i)
                if column == "D":
                    DeathPot(self, j , i)

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

        self.healthpot = pygame.sprite.LayeredUpdates()

        self.deathpot = pygame.sprite.LayeredUpdates()     


        self.createTilemap(maps.world_1.stage_1)
        
        self.player.current_hp = MAX_HP
        self.player_health_bar = HealthBar(10, 10, 200, 20)
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == "up":
                        Attack(self, self.player.rect.x, self.player.rect.y - TILE_SIZE)
                    if self.player.facing == "down":
                        Attack(self, self.player.rect.x, self.player.rect.y + TILE_SIZE)
                    if self.player.facing == "left":
                        Attack(self, self.player.rect.x - TILE_SIZE, self.player.rect.y)
                    if self.player.facing == "right":
                        Attack(self, self.player.rect.x + TILE_SIZE, self.player.rect.y)

    def update(self):
        self.all_sprites.update()


    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        
        # draw player health bar
        self.player_health_bar.draw(self.screen, self.player.current_hp)

        self.clock.tick(FPS)
        pygame.display.update()


    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        end = True

        title = self.font.render('Game Over', True, BLACK)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT// 4))
        restart_button = Button(WINDOW_WIDTH//2 - 50, WINDOW_HEIGHT//4 +100, 100,50, WHITE, BLACK, 'Restart', 32)
        
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.rect.collidepoint(event.pos):
                        end = False
                        self.new()
                        self.main()
                
                          
            self.screen.fill(self.end_background)
            self.screen.blit(title, title_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
        
    def intro_screen(self):
        intro = True

        title = self.font.render('Dungeon Fighter', True, BLACK)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT// 4))

        play_button = Button(WINDOW_WIDTH//2 - 50, WINDOW_HEIGHT// 4 + 100, 100, 50 , WHITE, BLACK, 'Play', 32)
        exit_button = Button(WINDOW_WIDTH//2 - 50, WINDOW_HEIGHT//4 + 170, 100, 50, WHITE, BLACK, 'Exit', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.rect.collidepoint(event.pos):
                        intro = False
                    if exit_button.rect.collidepoint(event.pos):
                        intro = False
                        self.running = False

            self.screen.fill(self.intro_background)
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()



if __name__ == "__main__":
    g = Game()
    g.intro_screen()
    g.new()
    while g.running:
        g.main()
        g.game_over()

    pygame.quit()
    sys.exit()
