from alien_inavsion.settings import Settings


class GameStats(object):
    """游戏信息统计类"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.init_speed_x_of_alien, self.init_speed_y_of_alien = ai_settings.alien_speed_x, ai_settings.alien_speed_y
        self.ship_left = self.ai_settings.ship_limit
        self.game_active = False
        self.score = 0

    def reset(self):
        """重置统计信息"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.ai_settings.alien_speed_x = self.init_speed_x_of_alien
        self.ai_settings.alien_speed_y = self.init_speed_y_of_alien
