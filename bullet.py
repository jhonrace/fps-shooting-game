import pygame
import math

class Bullet:
    def __init__(self, x, y, vx, vy, is_player=True):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = 3
        self.is_player = is_player
        self.lifetime = 300  # 帧数
    
    def update(self):
        """更新子弹位置"""
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1
    
    def is_out_of_bounds(self):
        """检查是否超出屏幕"""
        return (self.x < 0 or self.x > 1280 or 
                self.y < 0 or self.y > 720 or
                self.lifetime <= 0)
    
    def collides_with_player(self, player):
        """检查是否击中玩家"""
        dx = self.x - player.x
        dy = self.y - player.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance < player.radius + self.radius
    
    def collides_with_enemy(self, enemy):
        """检查是否击中敌人"""
        dx = self.x - enemy.x
        dy = self.y - enemy.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance < enemy.radius + self.radius
    
    def draw(self, screen):
        """绘制子弹"""
        if self.is_player:
            color = (0, 255, 0)  # 玩家子弹-绿色
        else:
            color = (255, 0, 0)  # 敌人子弹-红色
        
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
