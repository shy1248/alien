import pygame
from pygame.sprite import Group
from alien_inavsion.settings import Settings
from alien_inavsion.ship import Ship
import alien_inavsion.utils as utils
from alien_inavsion.game_stats import GameStats
from alien_inavsion.button import Button
from alien_inavsion.score_board import ScoreBoard


def start():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aline Invasion")
    game_stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, 'Play')
    score_board = ScoreBoard(ai_settings, game_stats, screen)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个子弹编组，用于控制多颗子弹
    bullets = Group()
    # 创建外星人群
    aliens = Group()
    utils.create_aliens(ai_settings, screen, aliens)
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        utils.check_event(ai_settings, game_stats, screen, ship, bullets, aliens, play_button)
        if game_stats.game_active:
            ship.move()
            utils.update_bullets(ai_settings, game_stats, screen, bullets, aliens)
            utils.update_aliens(ai_settings, game_stats, screen, ship, bullets, aliens)
        # 每次循环都要刷新屏幕
        utils.update_screen(ai_settings, game_stats, screen, ship, aliens, bullets, play_button, score_board)


if __name__ == '__main__':
    start()
