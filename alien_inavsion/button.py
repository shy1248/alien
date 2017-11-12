import pygame
from pygame.font import SysFont

class Button(object):
    """游戏的开始按钮"""
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = self.screen.get_rect()
        # 设置按钮各种属性
        self.width, self.height = 100, 25
        self.button_color = (0, 250, 0)
        self.text_color = (255, 255, 255)
        self.text_font = SysFont(None, 24)
        # 画出按钮
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 将按钮上的文字渲染为图片，并将其与按钮居中对齐
        self.text_image = self.text_font.render(msg, True, self.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw(self):
        """绘制"""
        # 绘制按钮外形
        self.screen.fill(self.button_color, self.rect)
        # 绘制被渲染过的文字图片
        self.screen.blit(self.text_image, self.text_image_rect)
