from pygame.font import SysFont


class ScoreBoard(object):
    """几分面板类"""
    def __init__(self, ai_settings, game_status, screen):
        self.ai_settings = ai_settings
        self.game_stats = game_status
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_font = SysFont(None, 18)
        self.text_color = (120, 30, 30)


    def pre_socre(self):
        self.text_img = self.text_font.render(str(self.game_stats.score), True, self.text_color, self.ai_settings.bg_color)
        self.text_img_rect = self.text_img.get_rect()
        self.text_img_rect.right = self.screen_rect.right - 10
        self.text_img_rect.top = 5

    def blitme(self):
        self.pre_socre()
        self.screen.blit(self.text_img, self.text_img_rect)