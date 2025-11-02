import pygame
from sprites import *
from config import *
import maps
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.caption = pygame.display.set_caption("Stairs")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('font/VT323-Regular.ttf', 32)

        # if the player hasn't died
        self.running = True

        self.character_spritesheet = Spritesheet("img/dungeon.png")
        self.player_spritesheet = Spritesheet("img/player_32x32.png")
        self.skeleton_spritesheet = Spritesheet("img/skeleton_32x32.png")

    
        self.boss1_spritesheet = Spritesheet("img/boss1_32x32.png")
        self.boss2_spritesheet = Spritesheet("img/boss2_32x32.png")
        self.boss3_spritesheet = Spritesheet("img/boss3_32x32.png")

        self.background = pygame.transform.scale(pygame.image.load("img/background.png").convert(), (WINDOW_WIDTH, WINDOW_HEIGHT))
       
        self.worlds = ['world_1', 'world_2', 'world_3']

        self.world_stages = {
            'world_1': ['stage_1', 'stage_2', 'stage_3', 'stage_4', 'boss_stage'],
            'world_2': ['stage_1', 'stage_2', 'stage_3', 'stage_4', 'stage_5', 'boss_stage'],
            'world_3': ['stage_1', 'stage_2', 'stage_3', 'boss_stage']
        }


    


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
                if column == 'F':  
                    Food(self, j, i)
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
                if column == 'G':
                    Gate(self, j, i)
                if column == 'H':
                    HealthPot(self, j, i)
                if column == 'B':
                    self.boss = Boss(self, j, i)


    def new(self):
        # if the player is still playing
        self.playing = True
        self.MAX_HP = 100
        self.health = self.MAX_HP
        self.currency = 0
        self.key = 0

        # dont change this
        self.world = 1

        # group of sprites that we can control, allow us to update all the sprites at once
        self.all_sprites = pygame.sprite.LayeredUpdates()
        # storing immovable walls
        self.walls = pygame.sprite.LayeredUpdates()      
        # storing enemies
        self.enemies = pygame.sprite.LayeredUpdates()   
        # storing attacks
        self.attacks = pygame.sprite.LayeredUpdates()  

        self.foods = pygame.sprite.LayeredUpdates()

        self.deathpots = pygame.sprite.LayeredUpdates()   

        self.stairs = pygame.sprite.LayeredUpdates()  

        self.keys = pygame.sprite.LayeredUpdates() 

        self.gates = pygame.sprite.LayeredUpdates()

        self.healthpots = pygame.sprite.LayeredUpdates()

        self.bosses = pygame.sprite.LayeredUpdates()

        self.projectiles = pygame.sprite.LayeredUpdates()
        
        self.portals = pygame.sprite.LayeredUpdates()

        self.createTilemap(maps.worlds['world_1']['stage_1'])
        
        self.player_health_bar = HealthBar(15, 15, 200, 30)
        self.currency_number = Currency(
                                self.player_health_bar.x,
                                self.player_health_bar.y + self.player_health_bar.height + 15,
                                self.font,
                                )
        
        self.current_stage_index = 0

        self.boss_stage = False

        pygame.mixer.init()
        pygame.mixer.music.load('audio/03 Cave Dungeon LOOP.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        
    
    def clear_sprites(self):
        self.all_sprites.empty()
        self.enemies.empty()
        self.walls.empty()
        self.foods.empty()
        self.deathpots.empty()
        self.stairs.empty()
        self.attacks.empty()
        self.keys.empty()
        self.gates.empty()
        self.healthpots.empty()
        self.bosses.empty()
        self.projectiles.empty()
        self.portals.empty()

    def change_stage(self, direction, spawn):
        self.clear_sprites()

        if direction == "down":
            self.current_stage_index += 1
            world = self.worlds[self.world - 1]
            stage = self.world_stages[world][self.current_stage_index]
            self.createTilemap(maps.worlds[world][stage])
            self.spawn_beside = spawn
        elif direction == "up":
            self.current_stage_index -= 1
            world = self.worlds[self.world - 1]
            stage = self.world_stages[world][self.current_stage_index]
            self.createTilemap(maps.worlds[world][stage])
            self.player.rect.topleft = self.spawn_beside

    def change_world(self):
        self.clear_sprites()

        self.current_stage_index = 0
        self.world += 1
        world = self.worlds[self.world - 1]
        stage = self.world_stages[world][self.current_stage_index]
        self.createTilemap(maps.worlds[world][stage])
        pygame.mixer.music.stop()
        if self.world == 1:
            pygame.mixer.music.load('audio/03 Cave Dungeon LOOP.wav')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        elif self.world == 2:
            pygame.mixer.music.load('audio/09 Jungle Dungeon LOOP.wav')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        elif self.world == 3:
            pygame.mixer.music.load('audio/11 Lava Dungeon LOOP.wav')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)


    def change_boss(self):
        self.clear_sprites()

        # goes to the last stage in the stages list
        self.current_stage_index = -1
        world = self.worlds[self.world - 1]
        stage = self.world_stages[world][self.current_stage_index]
        self.createTilemap(maps.worlds[world][stage])
        self.boss_stage = True
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load('audio/12 Boss Theme Loop.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)



    
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
                        self.player.attack = True
                    if self.player.facing == "down":
                        Attack(self, self.player.rect.x, self.player.rect.y + TILE_SIZE)
                        self.player.attack = True
                    if self.player.facing == "left":
                        Attack(self, self.player.rect.x - TILE_SIZE, self.player.rect.y)
                        self.player.attack = True
                    if self.player.facing == "right":
                        Attack(self, self.player.rect.x + TILE_SIZE, self.player.rect.y)
                        self.player.attack = True

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
        self.player_health_bar.draw(self.screen, self.health, self.MAX_HP)

        # draw boss health when boss stage is True
        if self.boss_stage:
            self.boss.draw(self.screen)

            if self.boss.area_attack_flag:
                pygame.draw.circle(
                self.screen,                  # surface
                BLUE,                          # color
                (
                    self.boss.rect.centerx - self.camera_x,
                    self.boss.rect.centery - self.camera_y
                ),                           # position
                100,                             # radius
                10                              # thickness
            )
            self.boss.area_attack_flag = False



        self.clock.tick(FPS)
        pygame.display.update()


    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        pygame.mixer.music.stop()

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
                
                          
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
        
    def intro_screen(self):
        intro = True

        title = self.font.render('Stairs', True, WHEAT)
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

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
    
    def pause_screen(self):
        pygame.mixer.music.pause()

        pause = True

        title = self.font.render('Paused', True, WHEAT)
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
                        pygame.mixer.music.unpause()

                    if exit_button.rect.collidepoint(event.pos):
                        pause = False
                        self.running = False
                        self.playing = False


            self.screen.blit(self.background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(continue_button.image, continue_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)

            controls = [
            "W - Move Up",
            "A - Move Left",
            "S - Move Down",
            "D - Move Right",
            "SPACE - Attack"
            ]

            y = WINDOW_HEIGHT // 4 + 260
            for text in controls:
                label = self.font.render(text, True, WHEAT)
                label_rect = label.get_rect(center=(WINDOW_WIDTH // 2, y))
                self.screen.blit(label, label_rect)
                y += 30

            self.clock.tick(FPS)
            pygame.display.update()

    def end_screen(self):
        pygame.mixer.music.stop()

        end = True

        title = self.font.render('You Won!', True, WHEAT)
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
                
                          
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)


            self.clock.tick(FPS)
            pygame.display.update()



# to run the game
if __name__ == "__main__":
    g = Game()
    g.intro_screen()
    while g.running:
        g.new()
        g.main()

    pygame.quit()
    sys.exit()
