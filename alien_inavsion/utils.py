import sys
import os
import pygame
from alien_inavsion.bullet import Bullet
from alien_inavsion.alien import Alien
from time import sleep


def check_event(ai_settings, game_stats, screen, ship, bullets, aliens, play_button):
    """监控鼠标键盘事件"""
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            sys.exit(0)
        # 响应鼠标点击事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_button_click(ai_settings, game_stats, screen, ship, bullets, aliens, play_button, mouse_x, mouse_y)
        # 键盘按下事件
        elif event.type == pygame.KEYDOWN:
            check_key_down_event(event, ai_settings, game_stats, screen, ship, bullets, aliens)
        # 键盘松开事件
        elif event.type == pygame.KEYUP:
            check_key_up_event(event, ship)


def check_key_down_event(event, ai_settings, game_stats, screen, ship, bullets, aliens):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_SPACE:
        fire(ai_settings, screen, ship, bullets)
    # q键被按下，退出游戏
    elif event.key == pygame.K_q:
        sys.exit(1)
    # p键被按下，开始游戏
    elif event.key == pygame.K_p:
        start_game(ai_settings, game_stats, screen, ship, bullets, aliens)


def check_key_up_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False


def fire(ai_settings, screen, ship, bullets):
    """当屏幕上可见的子弹数量小于设定的允许的子弹数目时就创建一颗子弹，并将其放入子弹编组中"""
    # 当按一下空格键时创建一颗子弹，并将其加入到子弹组中
    if len(bullets) < ai_settings.bullets_size:
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)


def check_aliens_edge(ai_settings, aliens):
    """检测外星人是否移动到屏幕边缘"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_aliens_direction(ai_settings, aliens)
            break


def change_aliens_direction(ai_settings, aliens):
    """将外星人下移，并改变其方向"""
    for alien in aliens.sprites():
        alien.y = alien.rect.y + ai_settings.alien_speed_y
        alien.rect.y = alien.y
    ai_settings.alien_direction *= -1


def update_aliens(ai_settings, game_stats, screen, ship, bullets, aliens):
    check_aliens_edge(ai_settings, aliens)
    aliens.update()
    # 检测外星人与飞船是否相撞
    if pygame.sprite.spritecollideany(ship, aliens):
        restart(ai_settings, game_stats, screen, ship, bullets, aliens)
    # 检测外星人是否抵达窗口底部
    check_aliens_bottom(ai_settings, game_stats, screen, ship, bullets, aliens)


def check_aliens_bottom(ai_settings, game_stats, screen, ship, bullets, aliens):
    """检测外星人是否达到屏幕底部"""
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen.get_rect().bottom:
            restart(ai_settings, game_stats, screen, ship, bullets, aliens)


def update_bullets(ai_settings, game_stats, screen, bullets, aliens):
    """移动子弹并删除已经移动到屏幕外的子弹"""
    bullets.update()
    # 检测子弹是否击中外星人，若击中，就将子弹和外星人分别从各自组里删除
    check_bullet_alien_collision(ai_settings, game_stats, screen, bullets, aliens)
    # 删除已经消失的子弹
    for bullet in bullets.sprites():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)


def check_button_click(ai_settings, game_stats, screen, ship, bullets, aliens, play_button, mouse_x, mouse_y):
    """检测按钮是否被点击"""
    # 如果按钮被点击了，就开始游戏，将游戏的激活状态设置为True
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_stats.game_active:
        start_game(ai_settings, game_stats, screen, ship, bullets, aliens)


def start_game(ai_settings, game_stats, screen, ship, bullets, aliens):
    """开始游戏"""
    # 重置游戏状态
    game_stats.reset()
    # 将游戏状态设置为激活状态
    game_stats.game_active = True
    # 隐藏游戏光标
    pygame.mouse.set_visible(False)
    # 飞船的剩余生命数减一
    game_stats.ship_left -= 1
    # 清空子弹与外星人组
    bullets.empty()
    aliens.empty()
    # 重建一群外星人
    create_aliens(ai_settings, screen, aliens)
    # 将飞船居中
    ship.center()

def restart(ai_settings, game_stats, screen, ship, bullets, aliens):
    """飞船与外星人碰撞后做的操作"""
    # 如果飞船的剩余生命小于活等于0，表示游戏结束
    if game_stats.ship_left <= 0:
        game_stats.game_active = False
        pygame.mouse.set_visible(True)
    # 将飞船的生命减一，表示该飞船已经阵亡
    game_stats.ship_left -= 1
    # 删除所有上局游戏的数据
    bullets.empty()
    aliens.empty()
    # 新建一群外星人
    create_aliens(ai_settings, screen, aliens)
    # 将飞船位置还原到初始位置
    ship.center()
    # 暂停一段时间
    sleep(0.5)


def check_bullet_alien_collision(ai_settings, game_stats, screen, bullets, aliens):
    """响应子弹与外星人碰撞事件"""
    collide = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collide:
        game_stats.score += 10
    if len(aliens) == 0:
        # 当外星人被消灭完以后，创建一群新的外星人，并加快外星人的速度，以提高游戏难度
        bullets.empty()
        create_aliens(ai_settings, screen, aliens)
        ai_settings.alien_speed_y *= ai_settings.speed_scale
        ai_settings.alien_speed_x *= ai_settings.speed_scale


def create_aliens(ai_settings, screen, aliens):
    """创建外星人群组"""
    # 首先创建一个外星人，通过这个外星人可以获取到外星人rect的参数
    alien = Alien(ai_settings, screen)
    # 计算x轴上最多可以容纳多少个外星人
    aliens_x = (ai_settings.screen_width - 2*alien.rect.width) // (2*alien.rect.width)
    # 计算y轴上可以容纳多少行外星人，假设外星人只能到y轴二分之一的位置
    aliens_y = (ai_settings.screen_height//2 - 2*alien.rect.height) // (2*alien.rect.height)

    for i in range(aliens_x):
        for j in range(aliens_y):
            alien = Alien(ai_settings, screen)
            # 重新指定每个外星人x的坐标
            alien.rect.x = alien.rect.width + 2*alien.rect.width*i
            alien.rect.y = alien.rect.height + 2*alien.rect.height*j
            aliens.add(alien)


def update_screen(ai_settings, game_stats, screen, ship, aliens, bullets, play_button, score_board):
    """刷新屏幕"""
    # 填充背景色
    screen.fill(ai_settings.bg_color)
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    aliens.draw(screen)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw()
    # 绘制开始按钮
    if not game_stats.game_active:
        play_button.draw()
    score_board.blitme()
    # 让刷新的屏幕显示最前端
    pygame.display.flip()


def get_path():
    return os.path.split(os.path.abspath(__file__))[0]


def load_image(file):
    return pygame.image.load(os.path.join(get_path(), 'images', file))
