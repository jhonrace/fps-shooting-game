import pygame

class UI:
    def __init__(self):
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        self.game_over_time = None
    
    def draw(self, screen, health, ammo, score, wave, game_over):
        """绘制游戏UI"""
        # 生命值
        health_text = self.font_small.render(f"Health: {health}", True, (0, 255, 0))
        screen.blit(health_text, (20, 20))
        
        # 弹药
        ammo_text = self.font_small.render(f"Ammo: {ammo}", True, (255, 255, 0))
        screen.blit(ammo_text, (20, 50))
        
        # 波数
        wave_text = self.font_small.render(f"Wave: {wave}", True, (0, 255, 255))
        screen.blit(wave_text, (20, 80))
        
        # 分数
        score_text = self.font_medium.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (1280 - 300, 20))
        
        # 游戏结束
        if game_over:
            game_over_text = self.font_large.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, (1280 // 2 - 150, 1280 // 2 - 100))
            
            restart_text = self.font_small.render("Press SPACE to restart", True, (255, 255, 255))
            screen.blit(restart_text, (1280 // 2 - 150, 1280 // 2 + 20))
            
            final_score_text = self.font_medium.render(f"Final Score: {score}", True, (255, 255, 0))
            screen.blit(final_score_text, (1280 // 2 - 150, 1280 // 2 - 40))
