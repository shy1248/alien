class Settings(object):
    """存储Aline Invasion所有的设置类"""

    def __init__(self):
        # 屏幕参数
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230 ,230)
        # 飞船参数
        self.ship_speed = 3
        self.ship_limit = 3
        # 子弹参数
        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_color = (255, 0, 0)
        self.bullet_speed = 6
        self.bullets_size = 5
        # 外星人参数
        self.alien_speed_x = 1.5
        self.alien_speed_y = 10
        self.alien_direction = 1
        self.speed_scale = 1.1
