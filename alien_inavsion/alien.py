from pygame.sprite import Sprite
from alien_inavsion import utils as utils
from pygame.transform import scale


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载外星人的图片
        image = utils.load_image('alien.bmp')
        rect = image.get_rect()
        # 对图片进行缩放,并获取缩放后的rect
        self.image = scale(image, (rect.width//2, rect.height//2))
        self.rect = self.image.get_rect()

        self.screen_rect = self.screen.get_rect()
        # 每个外星人最初的位置，在屏幕左上角距离屏幕边缘为外星人图片的宽度和高度
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人准确的位置，float可以保存小数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edge(self):
        """检测外星人是否到达窗口边缘"""
        screen_rect = self.screen_rect
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self, *args):
        self.move()

    def move(self):
        """外星人移动"""
        self.x = self.rect.x + (self.ai_settings.alien_speed_x*self.ai_settings.alien_direction)
        self.rect.x = self.x

    def blitme(self):
        """将自己绘制在屏幕上"""
        self.screen.blit(self.image, self.rect)
