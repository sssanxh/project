from random import randint
from random import randrange
import pygame_gui as pg_gui
import pygame as pg

pg.init()

pg.time.set_timer(pg.USEREVENT, 10000)
clock = pg.time.Clock()

sc = pg.display.set_mode((620, 620))
pg.display.set_caption("КАЛЬЯННЫЙ ГОНЩИК: ВОЗМЕЗДИЕ")

icon = pg.image.load('logoblack.png')
pg.display.set_icon(icon)

BAD_COOMARS = ('sprites/Bad_Coomar/1.png','sprites/Bad_Coomar/2.png',)
BAD_COOMARS_NEW = [pg.transform.scale(pg.image.load(i), (300, 150)) for i in BAD_COOMARS]

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

bg = pg.image.load('bg1.jpg')
bg = pg.transform.scale(bg, (620, 620))
logo = pg.image.load('logo.png')
logo = pg.transform.scale(logo, (300, 300))
logomini = logo.copy()

bg_music = pg.mixer.Sound('sounds/bg1.mp3')
menu_music = pg.mixer.Sound('sounds/menu.mp3')
hit_sound = pg.mixer.Sound('sounds/hit.mp3')
heal_sound = pg.mixer.Sound('sounds/heal.mp3')
exp_sound = pg.mixer.Sound('sounds/exp.mp3')
lose = pg.mixer.Sound('sounds/lose.mp3')
menu_music.play(-1)
menu_music.set_volume(0.5)
bg_music.set_volume(0.5)
hit_sound.set_volume(0.9)
exp_sound.set_volume(0.9)
heal_sound.set_volume(0.9)
lose.set_volume(0.9)


x = 220
y = 450
width = 30
height = 30
speed = 2
level = 1

left = False
right = False
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



def HealthBar():
    sc.blit(hp_bg_image, (10, 0))
    sc.blit(hp_name, (160, 0))
    x = 10
    show = 0
    while show != hp:
        sc.blit(hp_image, (x, 0))
        x += 50
        show += 1


def control():
    global left
    global right
    global x
    global y
    global animCount
    keys = pg.key.get_pressed()
    if keys[pg.K_a] and x > 5:
        left = True
        right = False
        x -= speed + 2 + level * 2
        animCount = 0
    elif keys[pg.K_d] and x < 450 - width - 5:
        left = False
        right = True
        x += speed + 2 + level * 2
        animCount = 0
    else:
        left = False
        right = False
    if keys[pg.K_w] and y > 5:
        y -= speed
    if keys[pg.K_s] and y < 600 - height - 5:
        y += speed
    if keys[pg.K_ESCAPE]:
        pause()


def ExpBar():
    sc.blit(exp_bg_image, (0, 30))
    sc.blit(exp_name, (250, 30))
    x = 10
    show = 0
    while show != exp:
        sc.blit(exp_image, (x, 30))
        x += 50
        show += 1

    # Движение заднего фона


def BgAnimation():
    global bg_y
    global bg
    sc.blit(bg, (0, bg_y))
    sc.blit(bg, (0, bg_y - 620))
    bg_y += 2
    if bg_y == 620:
        bg_y = 0


def drawWindow():
    global animCount
    global Alive
    global level
    global hp
    global exp
    global bg_music
    global bg
    if animCount + 1 >= 30:
        animCount = 0
    if left:
        sc.blit(HOOKAH_LEFT, (x, y))
    elif right:
        sc.blit(HOOKAH_RIGHT, (x, y))
    else:
        sc.blit(HOOKAH_NEW[animCount // 5], (x, y))
        animCount += 1

    HOOKAH_rect = pg.Rect(x + 65, y + 45, 60, 75)
    # exp = 0
    for exp_apple in exp_apples:
        if HOOKAH_rect.colliderect(exp_apple.rect):
            exp_apples.remove(exp_apple)
            exp_sound.play(0)
            if exp < 5:
                exp += 1
            if exp == 5:
                if level < 4:
                    level += 1
                if level == 2:
                    bg_music.stop()
                    bg_music = pg.mixer.Sound('sounds/bg2.mp3')
                    bg_music.play(-1)
                    bg = pg.image.load('bg2.jpg')
                    bg = pg.transform.scale(bg, (620, 620))
                if level == 3:
                    bg_music.stop()
                    bg_music = pg.mixer.Sound('sounds/bg3.mp3')
                    bg_music.play(-1)
                    bg = pg.image.load('bg3.jpg')
                    bg = pg.transform.scale(bg, (620, 620))
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
    for bad_coomar in bad_coomars:
        if HOOKAH_rect.colliderect(bad_coomar.rect):
            bad_apples.remove(bad_coomar)
            hit_sound.play(0)
            # дается три жизни
            hp -= 1
            if hp == 0:
                Alive = False

    heal_apples.draw(sc)
    exp_apples.draw(sc)
    bad_apples.draw(sc)
    bad_coomars.draw(sc)

    HealthBar()
    ExpBar()

    pg.display.update()


# инциализуруем переменные для pg_gui и вводим кнопки нашего меню
manager = pg_gui.UIManager((620, 620))

hello_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((15, 250), (175, 50)),
                                        text='НАЧАТЬ БЕЗУМИЕ',
                                        manager=manager)
exit_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((15, 325), (175, 50)),
                                       text='Я БОЮСЬ',
                                       manager=manager)

font = pg.font.Font('Fixedsys.ttf', size=32)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, False, text_col)
    sc.blit(img, (x, y))


def pause( ):
    transparent = pg.Surface((620,620))
    transparent.set_alpha(60)


    #переход
    for i in range(7):
        sc.blit(transparent,(0,0))
        pg.display.flip()
        pg.time.wait(30)

    manager = pg_gui.UIManager((620, 620))
    hello_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((15, 200), (195, 50)),
                                            text='ПРОДОЛЖИТЬ?',
                                            manager=manager)
    exit_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((15, 350), (195, 50)),
                                           text='СТРАХ СЛИШКОМ СИЛЁН',
                                           manager=manager)
    pause = True
    while pause:
        time_delta2 = clock.tick(60) / 1000
        for i in pg.event.get():
            if i.type == pg.QUIT:
                quit()
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    pause = not pause

            if i.type == pg.MOUSEBUTTONDOWN:
                if exit_button.rect.collidepoint(i.pos):
                    quit()
                if hello_button.rect.collidepoint(i.pos):
                    pause = not pause


            manager.process_events(i)
        manager.update(time_delta2)
        manager.draw_ui(sc)
        draw_text('ПАУЗА', font, (255, 255, 255), 70, 280)
        pg.display.update()


lose_img = pg.image.load('loseimg.png')
# экран проигрыша
def losewindow():  # доделать функцию
    global Alive
    global hp
    global exp
    global x
    global y
    global level
    sc.fill((0, 0, 0))
    huager = pg_gui.UIManager((620, 620))
    hello_button2 = pg_gui.elements.UIButton(relative_rect=pg.Rect((100, 400), (200, 50)),
                                             text='ЕЩЕ РАЗ',
                                             manager=huager)
    exit_button2 = pg_gui.elements.UIButton(relative_rect=pg.Rect((320, 400), (200, 50)),
                                            text='Я БОЮСЬ',
                                            manager=huager)

    dead = True
    bg_music.stop()
    lose.play(-1)
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
                    Alive = True
                    dead = False
                    hp = 3
                    exp = 0
                    x = 220
                    y = 450
                    lose.stop()
                    bg_music.play(-1)
            huager.process_events(i)
        huager.update(time_delta2)
        sc.blit(lose_img, (0, 0))
        huager.draw_ui(sc)
        pg.display.update()


def fade_out(surface, fade_speed, x, y):  # Функция для плавного исчезновения
    alpha = 255
    while alpha > 0:
        alpha -= fade_speed
        surface.set_alpha(alpha)
        sc.fill((0, 0, 0))
        sc.blit(surface, (x, y))
        pg.display.update()
        clock.tick(60)


def fade_in(surface, fade_speed, x, y):  # Функция для плавного появления
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

menu_img = pg.image.load('menu.png')
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
                bg_music.play(-1)
            if i.ui_element == exit_button:
                menu = False
                run = False
        manager.process_events(i)
    sc.blit(menu_img, (0, 0))
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
class BadCoomar(pg.sprite.Sprite):
    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.images = surf.copy()
        self.cur = 0
        self.image = self.images[self.cur]
        self.rect = self.image.get_rect(center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у машин будет разная скорость
        self.speed = 2

    def update(self):
        self.cur = (self.cur + 1) % len(self.images)
        self.image = self.images[self.cur]
        if self.rect.y < 620:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх, а удаляем из всех групп
            self.kill()

bad_coomars = pg.sprite.Group()
heal_apples = pg.sprite.Group()
exp_apples = pg.sprite.Group()
bad_apples = pg.sprite.Group()

bg_y = 0
bad_timer = pg.USEREVENT + 1
red_timer = bad_timer + 100  # xd
very_bad_timer = bad_timer + 100  # xd
bad_coom_timer = bad_timer + 1
green_timer = bad_timer + 1000  # xd
pg.time.set_timer(very_bad_timer, 10000)
pg.time.set_timer(bad_coom_timer, 2000)
pg.time.set_timer(bad_timer, 2500)  # частота появления гнилых яблок
pg.time.set_timer(red_timer, 8000)  # частота появления красных яблок
pg.time.set_timer(green_timer, 10000)  # частота появления зеленых яблок

tolvl1_img = pg.image.load('tolvl1.png')
tolvl2_img = pg.image.load('tolvl2.png')
tolvl3_img = pg.image.load('tolvl3.png')
winscreen = pg.image.load('winscreen.png')
tolvl1 = tolvl2 = tolvl3 = 1

man = pg_gui.UIManager((620, 620))

exit_button3 = pg_gui.elements.UIButton(relative_rect=pg.Rect((235, 325), (175, 50)),
                                                    text='ПРОЩАЙ, КАЛИК!',
                                                    manager=man)


def LEVEL1():
    if i.type == pg.QUIT:
        pg.quit()
    elif i.type == bad_timer:
        BadApple(randrange(106, 533, 205), BAD_APPLES_NEW, bad_apples)
    elif i.type == red_timer:
        HealApple(randrange(106, 533, 205), RED_APPLES_NEW, heal_apples)
    elif i.type == green_timer:
        ExpApple(randrange(106, 533, 205), GREEN_APPLES_NEW, exp_apples)

def LEVEL2():
    if i.type == pg.QUIT:
        pg.quit()
    # elif i.type == bad_coom_timer:
    #     BadCoomar(randrange(106, 320, 205), BAD_COOMARS_NEW, bad_coomars)
    elif i.type == very_bad_timer:
        BadApple(randrange(106, 533, 205), BAD_APPLES_NEW, bad_apples)
    elif i.type == green_timer:
        ExpApple(randrange(106, 533, 205), GREEN_APPLES_NEW, exp_apples)
    elif i.type == red_timer:
        HealApple(randrange(106, 533, 205), RED_APPLES_NEW, heal_apples)

def LEVEL3():
    if i.type == pg.QUIT:
        pg.quit()
    elif i.type == very_bad_timer:
        BadApple(randrange(106, 533, 205), BAD_APPLES_NEW, bad_apples)
    elif i.type == green_timer:
        ExpApple(randrange(106, 533, 205), GREEN_APPLES_NEW, exp_apples)
    elif i.type == red_timer:
        HealApple(randrange(106, 533, 205), RED_APPLES_NEW, heal_apples)

def WIN():
    if i.type == pg.QUIT:
        pg.quit()
    if i.type == pg.MOUSEBUTTONDOWN:
        if exit_button3.rect.collidepoint(i.pos):
            quit()




Alive = True
# главный цикл
while run:
    if Alive:
        control()
        if level == 1:
            if tolvl1 == 1:
                fade_in(tolvl1_img, 2, 0, 0)
                fade_out(tolvl1_img, 2, 0, 0)
                hp = 3
                exp = 0
                tolvl1 = 0
            for i in pg.event.get():
                LEVEL1()
            BgAnimation()
            drawWindow()
        elif level == 2:
            if tolvl2 == 1:
                fade_in(tolvl2_img, 2, 0, 0)
                fade_out(tolvl2_img, 2, 0, 0)
                hp = 3
                exp = 0
                tolvl2 = 0
            for i in pg.event.get():
                LEVEL2()
            BgAnimation()
            drawWindow()
        elif level == 3:
            if tolvl3 == 1:
                fade_in(tolvl3_img, 2, 0, 0)
                fade_out(tolvl3_img, 2, 0, 0)
                hp = 3
                exp = 0
                tolvl3 = 0
            for i in pg.event.get():
                LEVEL3()
            BgAnimation()
            drawWindow()
        elif level == 4:
            sc.blit(winscreen, (0, 0))
            man.update(time_delta)
            man.draw_ui(sc)
            pg.display.update()
            for i in pg.event.get():
                WIN()
        '''ПОМОГИТЕ КНОПКУ ВЫХОДА СДЕЛАТЬ КОВШ!!!'''

    else:
        # level = 1
        losewindow()

    pg.display.update()
    pg.time.delay(0)
    clock.tick(60)
    heal_apples.update()
    exp_apples.update()
    bad_coomars.update()
    bad_apples.update()
