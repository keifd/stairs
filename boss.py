import pygame
from config import *
from projectile import *
from portal import *
from enemy import *

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

        self.facing = "down"
        self.x_change = 0
        self.y_change = 0
        self.animation_loop = 0

        if self.game.world == 1:
            self.image = self.game.boss1_spritesheet.get_sprite(0*32, 10*32, TILE_SIZE, TILE_SIZE)
        elif self.game.world == 2:
            self.image = self.game.boss2_spritesheet.get_sprite(0*32, 10*32, TILE_SIZE, TILE_SIZE)
        elif self.game.world == 3:
            self.image = self.game.boss3_spritesheet.get_sprite(0*32, 10*32, TILE_SIZE, TILE_SIZE)
            
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

        self.projectile_time = 0
        self.spawn_time = 0
        self.last_area_attack_time = 0
        self.area_attack_flag = False

    def update(self):
        if self.game.world == 1:
            self.movement()
            self.animate()
            self.shoot_projectile()
        elif self.game.world == 2:
            self.animate()
            self.spawn_enemy()
        elif self.game.world == 3:
            self.movement()
            self.animate()
            self.area_attack()
        


        # Apply movement and collisions for all worlds
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
        if self.game.world == 1:
            left_animations = [
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(1*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(2*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(3*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(4*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(5*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(6*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(7*32, 9*32, 32, 32), (self.width, self.height))
            ]
            right_animations = [
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(1*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(2*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(3*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(4*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(5*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(6*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(7*32, 11*32, 32, 32), (self.width, self.height))
            ]
            up_animations = [
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(1*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(2*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(3*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(4*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(5*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(6*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(7*32, 8*32, 32, 32), (self.width, self.height))
            ]
            down_animations = [
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(1*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(2*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(3*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(4*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(5*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(6*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(7*32, 10*32, 32, 32), (self.width, self.height))
            ]

            if self.facing == "left":
                if self.y_change == 0 and self.x_change == 0:
                    self.image = pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(0*32, 9*32, 32, 32), (self.width, self.height))
                else:
                    self.image = left_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(left_animations) - 1:
                        self.animation_loop = 0

            if self.facing == "right":
                if self.y_change == 0 and self.x_change == 0:
                    self.image = pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(0*32, 11*32, 32, 32), (self.width, self.height))
                else:
                    self.image = right_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(right_animations) - 1:
                        self.animation_loop = 0

            if self.facing == "up":
                if self.x_change == 0 and self.y_change == 0:
                    self.image = pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(0*32, 8*32, 32, 32), (self.width, self.height))
                else:
                    self.image = up_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(up_animations) - 1:
                        self.animation_loop = 0

            if self.facing == "down":
                if self.x_change == 0 and self.y_change == 0:
                    self.image = pygame.transform.scale(self.game.boss1_spritesheet.get_sprite(0*32, 10*32, 32, 32), (self.width, self.height))
                else:
                    self.image = down_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(down_animations) - 1:
                        self.animation_loop = 0
        elif self.game.world == 2:
            down_animations = [
                pygame.transform.scale(self.game.boss2_spritesheet.get_sprite(1*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss2_spritesheet.get_sprite(2*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss2_spritesheet.get_sprite(3*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss2_spritesheet.get_sprite(4*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss2_spritesheet.get_sprite(5*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss2_spritesheet.get_sprite(6*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss2_spritesheet.get_sprite(7*32, 10*32, 32, 32), (self.width, self.height))

            ]
            self.image = down_animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop > len(down_animations) - 1:
                self.animation_loop = 0
        elif self.game.world == 3:
            left_animations = [
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(1*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(2*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(3*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(4*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(5*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(6*32, 9*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(7*32, 9*32, 32, 32), (self.width, self.height))
            ]
            right_animations = [
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(1*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(2*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(3*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(4*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(5*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(6*32, 11*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(7*32, 11*32, 32, 32), (self.width, self.height))
            ]
            up_animations = [
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(1*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(2*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(3*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(4*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(5*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(6*32, 8*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(7*32, 8*32, 32, 32), (self.width, self.height))
            ]
            down_animations = [
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(1*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(2*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(3*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(4*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(5*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(6*32, 10*32, 32, 32), (self.width, self.height)),
                pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(7*32, 10*32, 32, 32), (self.width, self.height))
            ]

            if self.facing == "left":
                if self.y_change == 0 and self.x_change == 0:
                    self.image = pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(0*32, 9*32, 32, 32), (self.width, self.height))
                else:
                    self.image = left_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(left_animations) - 1:
                        self.animation_loop = 0

            if self.facing == "right":
                if self.y_change == 0 and self.x_change == 0:
                    self.image = pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(0*32, 11*32, 32, 32), (self.width, self.height))
                else:
                    self.image = right_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(right_animations) - 1:
                        self.animation_loop = 0

            if self.facing == "up":
                if self.x_change == 0 and self.y_change == 0:
                    self.image = pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(0*32, 8*32, 32, 32), (self.width, self.height))
                else:
                    self.image = up_animations[math.floor(self.animation_loop)]
                    self.animation_loop += 0.1
                    if self.animation_loop > len(up_animations) - 1:
                        self.animation_loop = 0

            if self.facing == "down":
                if self.x_change == 0 and self.y_change == 0:
                    self.image = pygame.transform.scale(self.game.boss3_spritesheet.get_sprite(0*32, 10*32, 32, 32), (self.width, self.height))
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
    
    def take_damadge(self, amount):
        self.health -= amount
        if self.health <= 0:
            if self.game.world == 3:
                self.game.end_screen()
            else:
                self.health = 0
                self.kill()
                self.game.currency += 100
                self.game.boss_stage = False
                Portal(self.game, self.rect.centerx, self.rect.centery)
    
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

    def shoot_projectile(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.projectile_time > 2000:
            self.projectile_time = current_time
            # spawns 3 projectiles at a time
            offsets = [-15, 0, 15]  # horizontal spread
            for offset in offsets:
                Projectile(self.game, self.rect.centerx + offset, self.rect.centery)
    
    def spawn_enemy(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time > 2000:
            self.spawn_time = current_time
            # spawns 2 enemies at a time
            offsets = [-15, 15]  # horizontal spread
            for offset in offsets:
                Enemy(self.game, self.rect.centerx + offset, self.rect.centery, True)
    
    def area_attack(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_area_attack_time > 5000:
            self.last_area_attack_time = current_time
            self.area_attack_flag = True

            # Damage player if inside radius
            player = self.game.player
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            distance = (dx**2 + dy**2)**0.5

            if distance <= 100:
                self.game.health -= 30
                if self.game.health <= 0:
                    self.game.playing = False
                    self.game.game_over()
                    

                # optional: play a sound or animation

