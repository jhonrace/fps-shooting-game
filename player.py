import pygame
import math
from bullet import Bullet

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.health = 100
        self.max_health = 100
        self.ammo = 100
        self.max_ammo = 100
        self.speed = 5
        self.bullets = []
        self.shoot_cooldown = 0
        self.shoot_delay = 10  # 帧数
    
    def update(self, keys, mouse_pos):
        """更新玩家位置和状态"""
        # 移动
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        
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
        
        # 射击
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] and self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot(mouse_pos)
    
    def shoot(self, target_pos):
        """射击"""
        if self.ammo > 0:
            # 计算方向
            dx = target_pos[0] - self.x
            dy = target_pos[1] - self.y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance > 0:
                vx = (dx / distance) * 8
                vy = (dy / distance) * 8
                
                bullet = Bullet(self.x, self.y, vx, vy, is_player=True)
                self.bullets.append(bullet)
                self.ammo -= 1
                self.shoot_cooldown = self.shoot_delay
    
    def take_damage(self, damage):
        """受伤"""
        self.health = max(0, self.health - damage)
    
    def heal(self, amount):
        """治疗"""
        self.health = min(self.max_health, self.health + amount)
    
    def draw(self, screen):
        """绘制玩家"""
        # 绘制玩家角色（中心十字线）
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), self.radius)
        
        # 绘制十字准星
        pygame.draw.line(screen, (0, 255, 0), (self.x - 20, self.y), (self.x + 20, self.y), 2)
        pygame.draw.line(screen, (0, 255, 0), (self.x, self.y - 20), (self.x, self.y + 20), 2)
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 5, 1)
        
        # 绘制子弹
        for bullet in self.bullets:
            bullet.draw(screen)
