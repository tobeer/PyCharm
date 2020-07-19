import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    '''screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien invasion")
    bg_color = (230, 230, 230)'''
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    ship = Ship(screen)
    # 开始游戏的主循环
    while True:
        screen.fill(ai_settings.bg_color)  # 设置背景色
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 让最近绘制的屏幕可见
        ship.blitme()
        pygame.display.flip()


run_game()
