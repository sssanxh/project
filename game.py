from random import randint
from random import randrange
import pygame_gui as pg_gui
import pygame as pg

pg.init()

pg.time.set_timer(pg.USEREVENT, 10000)

sc = pg.display.set_mode((620, 620))
pg.display.set_caption("КАЛЬЯННЫЙ ГОНЩИК: ВОЗМЕЗДИЕ")

BAD_APPLES = ('sprites/Bad_Apple/1.png', 'sprites/Bad_Apple/2.png',
              'sprites/Bad_Apple/3.png', 'sprites/Bad_Apple/4.png',
              'sprites/Bad_Apple/5.png', 'sprites/Bad_Apple/6.png')
BAD_APPLES_NEW = [pg.transform.scale(pg.image.load(i), (150, 150)) for i in BAD_APPLES]

GREEN_APPLES = ('sprites/Green_Apple/1.png', 'sprites/Green_Apple/2.png',
                'sprites/Green_Apple/3.png', 'sprites/Green_Apple/4.png',
                'sprites/Green_Apple/5.png', 'sprites/Green_Apple/6.png')
GREEN_APPLES_NEW = [pg.transform.scale(pg.image.load(i), (150, 150)) for i in GREEN_APPLES]

RED_APPLES = ('sprites/Red_Apple/1.png', 'sprites/Red_Apple/2.png',
              'sprites/Red_Apple/3.png')
RED_APPLES_NEW = [pg.transform.scale(pg.image.load(i), (150, 150)) for i in RED_APPLES]

HOOKAH = ('sprites/Hookah/1.png', 'sprites/Hookah/2.png', 'sprites/Hookah/3.png',
          'sprites/Hookah/4.png', 'sprites/Hookah/5.png', 'sprites/Hookah/6.png',)
HOOKAH_NEW = [pg.transform.scale(pg.image.load(i), (200, 200)) for i in HOOKAH]

HOOKAH_LEFT = pg.transform.scale(pg.image.load('sprites/Hookah/left.png'), (200, 200))
HOOKAH_RIGHT = pg.transform.scale(pg.image.load('sprites/Hookah/right.png'), (200, 200))

LEVELS_BG = ('bg1.jpg', 'bg2.jpg', 'bg3.jpg')
LEVELS_MUSIC = ('sounds/bg_lvl1.mp3', 'sounds/bg_lvl2.mp3', 'sounds/bg_lvl3.mp3')

bg = pg.image.load('bg1.jpg')

bg = pg.transform.scale(bg, (620, 620))
logo = pg.image.load('logo.png')
logo = pg.transform.scale(logo, (300, 300))
logomini = logo.copy()

bg_music1 = pg.mixer.Sound('sounds/bg_lvl1lol.mp3')
menu_music = pg.mixer.Sound('sounds/menu.mp3')
hit_sound = pg.mixer.Sound('sounds/hit.mp3')
heal_sound = pg.mixer.Sound('sounds/heal.mp3')
exp_sound = pg.mixer.Sound('sounds/exp.mp3')
lose = pg.mixer.Sound('sounds/lose.mp3')
menu_music.play(-1)
menu_music.set_volume(0.05)
bg_music1.set_volume(0.05)
hit_sound.set_volume(0.09)
exp_sound.set_volume(0.09)
heal_sound.set_volume(0.09)
lose.set_volume(0.09)

clock = pg.time.Clock()

x = 220
y = 450
width = 30
height = 30
speed = 2
level = 1

level_up = False
left = False
right = False
stay = True
animCount = 0
run = None

hp = 3
hp_image = pg.image.load('sprites/HP_and_EXP/hp.png')
hp_bg_image = pg.image.load('sprites/HP_and_EXP/hpbg.png')
hp_name = pg.image.load('sprites/HP_and_EXP/healthname.png')


exp = 0
exp_image = pg.image.load('sprites/HP_and_EXP/exp.png')
exp_name = pg.image.load('sprites/HP_and_EXP/expname.png')
exp_bg_image = pg.image.load('sprites/HP_and_EXP/expbg.png')

'''Фукнция шкалы ЖИЗЯК)'''
def HealthBar():
    sc.blit(hp_bg_image, (10, 0))
    sc.blit(hp_name, (160, 0))
    x = 10
    show = 0
    while show != hp:
        sc.blit(hp_image, (x, 0))
        x += 50
        show += 1

'''Функция шкалы ОПЫТА?!'''
def ExpBar():
    sc.blit(exp_bg_image, (0, 30))
    sc.blit(exp_name, (310, 30))
    x = 10
    show = 0
    while show != exp:
        sc.blit(exp_image, (x, 30))
        x += 50
        show += 1


def drawWindow():
    global animCount
    global Alive
    global level_up
    global hp
    global exp
    # sc.blit(bg, (0, bg_y))
    # sc.blit(bg, (0, bg_y + 620))
    if animCount + 1 >= 30:
        animCount = 0
    if stay:
        sc.blit(HOOKAH_NEW[animCount // 5], (x, y))
        animCount += 1
    else:
        if left:
            sc.blit(HOOKAH_LEFT, (x, y))
        elif right:
            sc.blit(HOOKAH_RIGHT, (x, y))

    HOOKAH_rect = pg.Rect(x + 60, y + 20, 60, 30)
    for exp_apple in exp_apples:
        if HOOKAH_rect.colliderect(exp_apple.rect):
            exp_apples.remove(exp_apple)
            exp_sound.play(0)
            if exp < 5:
                exp += 1
            if exp == 5:
                level_up = True

    for heal_apple in heal_apples:
        if HOOKAH_rect.colliderect(heal_apple.rect):
            heal_apples.remove(heal_apple)
            heal_sound.play(0)
            if hp < 3:
                hp += 1
    for bad_apple in bad_apples:
        if HOOKAH_rect.colliderect(bad_apple.rect):
            bad_apples.remove(bad_apple)
            hit_sound.play(0)
            # дается три жизни
            hp -= 1
            if hp == 0:
                Alive = False
                bg_music1.stop()
                lose.play(-1)

    heal_apples.draw(sc)
    exp_apples.draw(sc)
    bad_apples.draw(sc)

    HealthBar()
    ExpBar()

    pg.display.update()


# инциализуруем переменные для pg_gui и вводим кнопки нашего меню
manager = pg_gui.UIManager((620, 620))

hello_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((15, 200), (175, 50)),
                                        text='НАЧАТЬ БЕЗУМИЕ',
                                        manager=manager)
exit_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((15, 350), (175, 50)),
                                       text='Я БОЮСЬ',
                                       manager=manager)

font = pg.font.Font('Fixedsys.ttf', size=32)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, False, text_col)
    sc.blit(img, (x, y))


# экран проигрыша
def losewindow(): #доделать функцию
    sc.fill((0, 0, 0))
    huager = pg_gui.UIManager((620, 620))
    hello_button2 = pg_gui.elements.UIButton(relative_rect=pg.Rect((40, 200), (200, 50)),
                                             text='ЕЩЁ РАЗ НЕ ***',
                                             manager=huager)
    exit_button2 = pg_gui.elements.UIButton(relative_rect=pg.Rect((40, 350), (200, 50)),
                                            text='Я БОЮСЬ',
                                            manager=huager)
    dead = True
    while dead:
        time_delta2 = clock.tick(60) / 1000
        for i in pg.event.get():
            if i.type == pg.QUIT:
                quit()
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    quit()
            if i.type == pg.MOUSEBUTTONDOWN:
                if exit_button2.rect.collidepoint(i.pos):
                    quit()
                if hello_button2.rect.collidepoint(i.pos):
                    pass #придумать как сделать рестарт

            huager.process_events(i)
        huager.update(time_delta2)
        huager.draw_ui(sc)
        pg.display.update()


def fade_out(surface, fade_speed, x, y, ):  # Функция для плавного исчезновения
    alpha = 255
    while alpha > 0:
        alpha -= fade_speed
        surface.set_alpha(alpha)
        sc.fill((0, 0, 0))
        sc.blit(surface, (x, y))
        pg.display.update()
        clock.tick(60)


def fade_in(surface, fade_speed, x, y, ):  # Функция для плавного появления
    alpha = 0
    while alpha < 255:
        alpha += fade_speed
        surface.set_alpha(alpha)
        sc.fill((0, 0, 0))
        sc.blit(surface, (x, y))
        pg.display.update()
        clock.tick(60)


fade_in(logo, 1, 150, 150)
fade_out(logo, 6, 150, 150)  # затухание логотипа вначале (поверхность, скорость изменения альфа, координаты х у)

sc.blit(bg, (0, 0))  # (фон для менюшки, лого в нижнем углу и текст)
sc.blit(pg.transform.scale(logomini, (165, 165)), (430, 450))
draw_text('КАЛЬЯННЫЙ ГОНЩИК', font, (255, 255, 255), 15, 110)

# цикл меню, который работает через pygame_gui, при нажатии кнопки hello_button запускает игровой цикл
menu = True  # цикл для gui менюшки
while menu:
    time_delta = clock.tick(60) / 1000.0
    for i in pg.event.get():
        if i.type == pg.QUIT:
            menu = False
        if i.type == pg_gui.UI_BUTTON_PRESSED:
            if i.ui_element == hello_button:
                run = True
                menu = False
                menu_music.stop()
                bg_music1.play(-1)
            if i.ui_element == exit_button:
                menu = False
                run = False
        manager.process_events(i)
    manager.update(time_delta)
    manager.draw_ui(sc)

    pg.display.update()


class HealApple(pg.sprite.Sprite):
    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.images = surf.copy()
        self.cur = 0
        self.image = self.images[self.cur]
        self.rect = self.image.get_rect(center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у машин будет разная скорость
        self.speed = 3

    def update(self):
        self.cur = (self.cur + 1) % len(self.images)
        self.image = self.images[self.cur]
        if self.rect.y < 620:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх, а удаляем из всех групп
            self.kill()


class ExpApple(pg.sprite.Sprite):
    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.images = surf.copy()
        self.cur = 0
        self.image = self.images[self.cur]
        self.rect = self.image.get_rect(center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у машин будет разная скорость
        self.speed = 3

    def update(self):
        self.cur = (self.cur + 1) % len(self.images)
        self.image = self.images[self.cur]
        if self.rect.y < 620:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх, а удаляем из всех групп
            self.kill()


class BadApple(pg.sprite.Sprite):
    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.images = surf.copy()
        self.cur = 0
        self.image = self.images[self.cur]
        self.rect = self.image.get_rect(center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у машин будет разная скорость
        self.speed = randint(3, 4)

    def update(self):
        self.cur = (self.cur + 1) % len(self.images)
        self.image = self.images[self.cur]
        if self.rect.y < 620:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх, а удаляем из всех групп
            self.kill()


heal_apples = pg.sprite.Group()
exp_apples = pg.sprite.Group()
bad_apples = pg.sprite.Group()

bg_y = 0
bad_timer = pg.USEREVENT + 1
red_timer = bad_timer + 100  # xd
green_timer = bad_timer + 1000  # xd
pg.time.set_timer(bad_timer, 1000)  # частота появления гнилых яблок
pg.time.set_timer(red_timer, 8000)  # частота появления красных яблок
pg.time.set_timer(green_timer, 10000)  # частота появления зеленых яблок

Alive = True
# главный цикл
while run:
    if Alive:
        # Движение заднего фона
        sc.blit(bg, (0, bg_y))
        sc.blit(bg, (0, bg_y - 620))
        bg_y += 2
        if bg_y == 620:
            bg_y = 0

        for i in pg.event.get():
            if i.type == pg.QUIT:
                run = False
                pg.quit()

            elif i.type == bad_timer:
                BadApple(randrange(106, 533, 205), BAD_APPLES_NEW, bad_apples)
            elif i.type == red_timer:
                HealApple(randrange(106, 533, 205), RED_APPLES_NEW, heal_apples)
            elif i.type == green_timer:
                ExpApple(randrange(106, 533, 205), GREEN_APPLES_NEW, exp_apples)

        keys = pg.key.get_pressed()
        if keys[pg.K_a] and x > 5:
            left = True
            right = False
            stay = False
            x -= speed + 4
            animCount = 0
        elif keys[pg.K_d] and x < 450 - width - 5:
            left = False
            right = True
            stay = False
            x += speed + 4
            animCount = 0
        else:
            left = False
            right = False
            stay = True
        if keys[pg.K_w] and y > 5:
            y -= speed
        if keys[pg.K_s] and y < 600 - height - 5:
            y += speed
        drawWindow()
    else:
        losewindow()
    if level_up == True:
        sc.fill((0, 0, 0))
        draw_text('уровень 1 пройден(продолжение следует)', font, (255, 255, 255), 40, 50)
    pg.display.update()
    pg.time.delay(0)
    clock.tick(60)
    heal_apples.update()
    exp_apples.update()
    bad_apples.update()
