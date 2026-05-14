import pygame
import random
from player import Player
from enemy import Enemy
from ui import UI

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(width // 2, height // 2)
        self.enemies = []
        self.ui = UI()
        self.wave = 1
        self.score = 0
        self.game_over = False
        self.spawn_wave()
    
    def spawn_wave(self):
        """生成一波敌人"""
        num_enemies = 3 + self.wave
        for _ in range(num_enemies):
            # 随机生成敌人位置（远离玩家）
            angle = random.uniform(0, 360)
            distance = random.uniform(300, 500)
            x = self.player.x + distance * pygame.math.Vector2(1, 0).rotate(angle).x
            y = self.player.y + distance * pygame.math.Vector2(1, 0).rotate(angle).y
            
            # 限制在屏幕内
            x = max(50, min(self.width - 50, x))
            y = max(50, min(self.height - 50, y))
            
            enemy = Enemy(x, y, self.player)
            self.enemies.append(enemy)
    
    def update(self, keys, mouse_pos):
        """更新游戏状态"""
        if self.game_over:
            return
        
        # 更新玩家
        self.player.update(keys, mouse_pos)
        
        # 更新敌人
        for enemy in self.enemies[:]:
            enemy.update(self.player)
            
            # 检查敌人子弹是否击中玩家
            for bullet in enemy.bullets[:]:
                if bullet.collides_with_player(self.player):
                    self.player.take_damage(10)
                    enemy.bullets.remove(bullet)
            
            # 检查玩家子弹是否击中敌人
            for bullet in self.player.bullets[:]:
                if bullet.collides_with_enemy(enemy):
                    enemy.take_damage(25)
                    if bullet in self.player.bullets:
                        self.player.bullets.remove(bullet)
                    
                    if enemy.health <= 0:
                        self.score += 100
                        self.enemies.remove(enemy)
                        break
        
        # 检查玩家是否与敌人接触
        for enemy in self.enemies:
            distance = ((self.player.x - enemy.x)**2 + (self.player.y - enemy.y)**2)**0.5
            if distance < 30:
                self.player.take_damage(5)
        
        # 检查游戏是否结束
        if self.player.health <= 0:
            self.game_over = True
            self.ui.game_over_time = pygame.time.get_ticks()
        
        # 检查是否完成一波
        if len(self.enemies) == 0 and not self.game_over:
            self.wave += 1
            self.spawn_wave()
    
    def draw(self, screen):
        """绘制游戏"""
        # 绘制玩家
        self.player.draw(screen)
        
        # 绘制敌人
        for enemy in self.enemies:
            enemy.draw(screen)
        
        # 绘制UI
        self.ui.draw(screen, self.player.health, self.player.ammo, self.score, self.wave, self.game_over)
