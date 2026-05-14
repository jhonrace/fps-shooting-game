import pygame
import math
from bullet import Bullet

class Enemy:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.radius = 12
        self.health = 50
        self.max_health = 50
        self.speed = 2
        self.bullets = []
        self.shoot_cooldown = 0
        self.shoot_delay = 60  # 比玩家慢
        self.player = player
    
    def update(self, player):
        """更新敌人"""
        # 朝玩家移动
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed
        
        # 限制在屏幕内
        self.x = max(self.radius, min(1280 - self.radius, self.x))
        self.y = max(self.radius, min(720 - self.radius, self.y))
        
        # 更新冷却时间
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        
        # 更新子弹
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_out_of_bounds():
                self.bullets.remove(bullet)
        
        # 随机射击
        if distance < 400 and self.shoot_cooldown == 0:
            self.shoot(player)
    
    def shoot(self, player):
        """射击"""
        # 计算方向
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            vx = (dx / distance) * 5
            vy = (dy / distance) * 5
            
            bullet = Bullet(self.x, self.y, vx, vy, is_player=False)
            self.bullets.append(bullet)
            self.shoot_cooldown = self.shoot_delay
    
    def take_damage(self, damage):
        """受伤"""
        self.health = max(0, self.health - damage)
    
    def draw(self, screen):
        """绘制敌人"""
        # 敌人颜色根据生命值变化
        health_ratio = self.health / self.max_health
        color = (255, int(255 * health_ratio), 0)
        
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)
        
        # 绘制生命值条
        bar_width = 30
        bar_height = 5
        bar_x = self.x - bar_width // 2
        bar_y = self.y - self.radius - 10
        
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height))
        
        # 绘制子弹
        for bullet in self.bullets:
            bullet.draw(screen)
