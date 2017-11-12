import alien_inavsion.utils as utils
from pygame.transform import scale

class Ship(object):

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        # 加载飞船图片并获取其外接矩形
        image = utils.load_image('ship.bmp')
        rect = image.get_rect()
        # 飞船图标缩小二分之一并获取缩小后的rect参数
        self.image = scale(image, (rect.width//2, rect.height//2))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 初始化飞船的位置，屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.speed = ai_settings.ship_speed
        # 飞船是否移动的标志，监听到相应的鼠标事件后修改标志位
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def move(self):
        """移动位置"""
        if self.move_right and self.rect.right <= self.screen_rect.right:
            self.rect.centerx += self.speed
        if self.move_down and self.rect.bottom <= self.screen_rect.bottom:
            self.rect.centery += self.speed
        if self.move_left and self.rect.left >= self.screen_rect.left:
            self.rect.centerx -= self.speed
        if self.move_up and self.rect.top >= self.screen_rect.top:
            self.rect.centery -= self.speed

    def center(self):
        """将飞船底部居中"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """将自己绘制出来"""
        self.screen.blit(self.image, self.rect)
