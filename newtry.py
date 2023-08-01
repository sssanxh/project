from random import randint
import pygame_gui as pg_gui
import pygame as pg

pg.init()
pg.time.set_timer(pg.USEREVENT, 10000)  # ЧАСТОТА ПОЯВЛЕНИЯ ЯБЛОК

sc = pg.display.set_mode((620, 620))

pg.display.set_caption("КАЛЬЯННЫЙ ГОНЩИК: ВОЗМЕЗДИЕ")

green_apple = pg.image.load('sprites/Green_Apple/1.png')
green_apple = pg.transform.scale(green_apple, (100, 100))
green_apple_y = 0

HOOKAH = ('sprites/Hookah/1.png', 'sprites/Hookah/2.png', 'sprites/Hookah/3.png',
          'sprites/Hookah/4.png', 'sprites/Hookah/5.png', 'sprites/Hookah/6.png',
          'sprites/Hookah/7.png')
HOOKAH_NEW = []
for i in HOOKAH:
    image = pg.image.load(i)
    scaled_image = pg.transform.scale(image, (200, 200))
    HOOKAH_NEW.append(scaled_image)

LEFT = pg.image.load('sprites/Hookah/left.png')
RIGHT = pg.image.load('sprites/Hookah/right.png')
HOOKAH_LEFT = pg.transform.scale(LEFT, (200, 200))
HOOKAH_RIGHT = pg.transform.scale(RIGHT, (200, 200))

bg = pg.image.load('bg.png')
bg = pg.transform.scale(bg, (620, 620))
logo = pg.image.load('logo.png')
logo = pg.transform.scale(logo, (500, 500))
logomini = logo.copy()

bg_music1 = pg.mixer.Sound('sounds/bg_lvl1.mp3')
menu_music = pg.mixer.Sound('sounds/menu.mp3')
hit_sound = pg.mixer.Sound('sounds/hit.mp3')
heal_sound = pg.mixer.Sound('sounds/heal.mp3')
menu_music.play(-1)
menu_music.set_volume(0.05)
bg_music1.set_volume(0.05)

clock = pg.time.Clock()

image_size = (200, 200)
x = 287
y = 500
width = 30
height = 30
speed = 2

left = False
right = False
stay = True
green_apple_stay = True
animCount = 0
animCount2 = 0
green_apple_timer = pg.USEREVENT + 1
pg.time.set_timer(green_apple_timer, 1000)

run = None

def drawWindow():
    global animCount
    global animCount2
    # sc.blit(bg, (0, bg_y))
    # sc.blit(bg, (0, bg_y + 620))
    if animCount + 1 >= 30:
        animCount = 0
    if animCount2 + 1 >= 30:
        animCount2 = 0
    if stay:
        sc.blit(HOOKAH_NEW[animCount // 5], (x, y))
        animCount += 1
    else:
        if left:
            sc.blit(HOOKAH_LEFT, (x, y))
        elif right:
            sc.blit(HOOKAH_RIGHT, (x, y))

    HOOKAH_rect = pg.Rect(x + 40, y + 30, 150, 50)
    GREEN_APPLE_rect = pg.Rect(250, green_apple_y, 150, 50)

    if HOOKAH_rect.colliderect(GREEN_APPLE_rect):
        heal_sound.play(0)

    # apples.draw(sc)
    # badapples.draw(sc)

    pg.display.update()


# инциализуруем переменные для pg_gui и вводим кнопки нашего меню
manager = pg_gui.UIManager((620, 620))

hello_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((40, 200), (200, 50)),
                                        text='НАЧАТЬ БЕЗУМИЕ',
                                        manager=manager)
exit_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((40, 350), (200, 50)),
                                       text='Я БОЮСЬ',
                                       manager=manager)

# цикл меню, который работает через pygame_gui, при нажатии кнопки hello_button запускает игровой цикл
font = pg.font.SysFont('Fixedsys', size=32)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, False, text_col)
    sc.blit(img, (x, y))


def fade_out(surface, fade_speed, x, y, ):  # Функция для плавного исчезновения
    alpha = 255
    while alpha > 0:
        alpha -= fade_speed
        surface.set_alpha(alpha)
        sc.fill((0, 0, 0))
        sc.blit(surface, (x, y))
        pg.display.update()
        clock.tick(60)
        pg.time.delay(16)


fade_out(logo, 1, 60, 65)  # затухание логотипа вначале (поверхность, скорость изменения альфа, координаты х у)

sc.blit(bg, (0, 0))  # (фон для менюшки, лого в нижнем углу и текст)
sc.blit(pg.transform.scale(logomini, (165, 165)), (410, 450))
draw_text('КАЛЬЯННЫЙ ГОНЩИК', font, (255, 255, 255), 40, 50)

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

bg_y = 0

# run = True
# главный цикл
while run:

    """Движение заднего фона"""
    sc.blit(bg, (0, bg_y))
    sc.blit(bg, (0, bg_y - 620))
    bg_y += 2
    if bg_y == 620:
        bg_y = 0

    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
            pg.quit()
        if i.type == green_apple_timer:
            green_apple_list

    keys = pg.key.get_pressed()
    if keys[pg.K_a] and x > 5:
        left = True
        right = False
        stay = False
        x -= speed
        animCount = 0
    elif keys[pg.K_d] and x < 500 - width - 5:
        left = False
        right = True
        stay = False
        x += speed
        animCount = 0
    else:
        left = False
        right = False
        stay = True
    if keys[pg.K_w] and y > 5:
        y -= speed
    if keys[pg.K_s] and y < 600 - height - 5:
        y += speed

    sc.blit(green_apple, (250, green_apple_y))
    green_apple_y += 10

    drawWindow()
    pg.display.update()
    pg.time.delay(0)
    pg.mixer.init()
    pg.mixer.music.load('sounds/bg_lvl1.mp3')
    pg.mixer.music.play(loops=-1)
    pg.mixer.music.set_volume(0.2)
    clock.tick(60)

