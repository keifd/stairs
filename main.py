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
        self.pause_background = BLACK

    


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
                if column == 'D':
                    DeathPot(self, j , i)
                if column == 'S':
                    Stair(self, j ,i, 'down')
                if column == 'U':
                    Stair(self, j, i, 'up')
                if column == 'K':
                    Key(self, j, i)
                if column == ' ':
                    Void(self, j, i)


    def new(self):
        # if the player is still playing
        self.playing = True
        self.health = MAX_HP
        self.currency = 0
        self.key = 0

        # group of sprites that we can control, allow us to update all the sprites at once
        self.all_sprites = pygame.sprite.LayeredUpdates()
        # storing immovable walls
        self.walls = pygame.sprite.LayeredUpdates()      
        # storing enemies
        self.enemies = pygame.sprite.LayeredUpdates()   
        # storing attacks
        self.attacks = pygame.sprite.LayeredUpdates()  

        self.healthpots = pygame.sprite.LayeredUpdates()

        self.deathpots = pygame.sprite.LayeredUpdates()   

        self.stairs = pygame.sprite.LayeredUpdates()  

        self.keys = pygame.sprite.LayeredUpdates() 


        self.createTilemap(maps.worlds['world_1']['stage_1'])
        
        self.player_health_bar = HealthBar(15, 15, 200, 30)
        self.currency_number = Currency(
            self.player_health_bar.x + self.player_health_bar.width + 20,
                                 self.player_health_bar.y,
                                 self.font,
                                )
        
        self.current_stage_index = 0
    
    def change_map(self, direction, spawn):


        self.all_sprites.empty()
        self.enemies.empty()
        self.walls.empty()
        self.healthpots.empty()
        self.deathpots.empty()
        self.stairs.empty()
        self.attacks.empty()
        self.keys.empty()

        if direction == "down":
            self.current_stage_index += 1
            stage = maps.stages[self.current_stage_index]
            self.createTilemap(maps.worlds['world_1'][stage])
            self.spawn_beside = spawn
        elif direction == "up":
            self.current_stage_index -= 1
            stage = maps.stages[self.current_stage_index]
            self.createTilemap(maps.worlds['world_1'][stage])
            self.player.rect.topleft = self.spawn_beside
        


    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause_screen()

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

        self.camera_x = self.player.rect.centerx - WINDOW_WIDTH // 2
        self.camera_y = self.player.rect.centery - WINDOW_HEIGHT // 2


    def draw(self):
        self.screen.fill(BLACK)

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, (sprite.rect.x - self.camera_x, sprite.rect.y - self.camera_y))
        
        # draw player health bar
        self.currency_number.draw(self.screen, self.currency)
        self.player_health_bar.draw(self.screen, self.health)

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
        exit_button = Button(WINDOW_WIDTH//2 - 50, WINDOW_HEIGHT//4 + 170, 100, 50, WHITE, BLACK, 'Exit', 32)

        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.rect.collidepoint(event.pos):
                        end = False
                        self.playing = False
                    if exit_button.rect.collidepoint(event.pos):
                        end = False
                        self.running = False
                        self.playing = False
                
                          
            self.screen.fill(self.end_background)
            self.screen.blit(title, title_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
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
    
    def pause_screen(self):
        pause = True

        title = self.font.render('Dungeon Fighter', True, BLACK)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT// 4))

        continue_button = Button(WINDOW_WIDTH//2 - 50, WINDOW_HEIGHT// 4 + 100, 100, 50 , WHITE, BLACK, 'Continue', 32)
        exit_button = Button(WINDOW_WIDTH//2 - 50, WINDOW_HEIGHT//4 + 170, 100, 50, WHITE, BLACK, 'Exit', 32)

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = False
                    self.running = False
                    self.playing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if continue_button.rect.collidepoint(event.pos):
                        pause = False
                    if exit_button.rect.collidepoint(event.pos):
                        pause = False
                        self.running = False
                        self.playing = False


            self.screen.fill(self.pause_background)
            self.screen.blit(title, title_rect)
            self.screen.blit(continue_button.image, continue_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()




if __name__ == "__main__":
    g = Game()
    g.intro_screen()
    while g.running:
        g.new()
        g.main()

    pygame.quit()
    sys.exit()
