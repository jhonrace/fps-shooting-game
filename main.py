import pygame
import sys
from game import Game

def main():
    pygame.init()
    
    # 游戏配置
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    FPS = 60
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("FPS Shooting Game")
    clock = pygame.time.Clock()
    
    # 创建游戏
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE and game.game_over:
                    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        # 更新游戏
        game.update(pygame.key.get_pressed(), pygame.mouse.get_pos())
        
        # 渲染游戏
        screen.fill((0, 0, 0))
        game.draw(screen)
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
