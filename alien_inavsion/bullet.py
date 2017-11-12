import  pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹类"""

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self, *args):
        """重写Sprite的update方法"""
        self.move()

    def move(self):
        """子弹移动"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed
        # 更新表示子弹位置的rect
        self.rect.y = self.y

    def draw(self):
        """在屏幕上画出自己"""
        pygame.draw.rect(self.screen, self.color, self.rect)
