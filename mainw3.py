from random import randint
import pygame_gui as pg_gui
import pygame as pg

# я люблю пуки и каки
pg.init()

sc = pg.display.set_mode((620, 820))

pg.display.set_caption("КАЛЬЯННЫЙ ГОНЩИК: ВОЗМЕЗДИЕ")

GREEN_APPLES = ('sprites/Green_Apple/1.png', 'sprites/Green_Apple/2.png',
                'sprites/Green_Apple/3.png', 'sprites/Green_Apple/4.png',
                'sprites/Green_Apple/5.png', 'sprites/Green_Apple/6.png')
GREEN_APPLES_NEW = []
for i in GREEN_APPLES:
    image = pg.image.load(i)
    scaled_image = pg.transform.scale(image, (200, 200))
    GREEN_APPLES_NEW.append(scaled_image)


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
bg = pg.transform.scale(bg, (620, 820))

bg_music1 = pg.mixer.Sound('bg_lvl1.mp3')
menu_music = pg.mixer.Sound('menu.mp3')
menu_music.play(-1)
menu_music.set_volume(0.05)
bg_music1.set_volume(0.05)

clock = pg.time.Clock()

image_size = (200, 200)
x = 287
y = 750
width = 30
height = 30
speed = 2

left = False
right = False
stay = True
animCount = 0




def drawWindow():
    global animCount
    sc.blit(bg, (0, 0))
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

    apples.draw(sc)

    pg.display.update()

#инциализуруем переменные для pg_gui и вводим кнопки нашего меню
manager = pg_gui.UIManager((620,820))

hello_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((0, 100), (200, 50)),
                                             text='НАЧАТЬ БЕЗУМИЕ',
                                             manager=manager)
exit_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((0, 300), (200, 50)),
                                             text='Я БОЮСЬ',
                                             manager=manager)

#цикл меню, который работает через pygame_gui, при нажатии кнопки hello_button запускает игровой цикл

logo = pg.image.load('logo.png')
logo = pg.transform.scale(logo, (500,500))
sc.blit(logo, (65,120))
pg.display.update()

pg.time.delay(1500)


menu = True
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

class Apple(pg.sprite.Sprite):

    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у машин будет разная скорость
        self.speed = 1

    def update(self):
        if self.rect.y < 620:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх, а удаляем из всех групп
            self.kill()


apples = pg.sprite.Group()

# добавляем первую машину,
# которая появляется сразу
Apple(randint(100, 540), GREEN_APPLES_NEW[randint(0, 1)], apples)



while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_a] and x > 5:
        left = True
        right = False
        stay = False
        x -= speed
        animCount = 0
    elif keys[pg.K_d] and x < 620 - width - 5:
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
    if keys[pg.K_s] and y < 800 - height - 5:
        y += speed


    drawWindow()
    pg.mixer.init()
    pg.mixer.music.load('bg_lvl1.mp3')
    pg.mixer.music.play(loops=-1)
    pg.mixer.music.set_volume(0.2)
    clock.tick(60)

pg.quit()
