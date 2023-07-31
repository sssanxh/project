from random import randint
import pygame as pg
import sys

pg.init()
sc = pg.display.set_mode((620, 620))

pg.display.set_caption("КАЛЬЯННЫЙ ГОНЩИК: ВОЗМЕЗДИЕ")

x = 50
y = 50
width = 40
height = 5
speed = 5
W = 620
H = 620

GREEN_APPLES = [pg.image.load('sprites/Green_Apple/1.png'), pg.image.load('sprites/Green_Apple/2.png'),
                pg.image.load('sprites/Green_Apple/3.png'), pg.image.load('sprites/Green_Apple/4.png'),
                pg.image.load('sprites/Green_Apple/5.png'), pg.image.load('sprites/Green_Apple/6.png')]

APPLES = 'Double_Apple_1.png'
APPLES_SURF = []

bg = pg.image.load('bg.png')


wh = (W, H)
left = False
right = False
image_size = (100, 100)
WHITE = (255, 255, 255)
animCount = 0


def drawWindow():
    global animCount

    if animCount + 1 >= 30:
        animCount = 0

    sc.blit(bg, (0, 0))
    apples.draw(sc)
    apples.update()


for apple in APPLES:
    image = pg.image.load('sprites/Green_Apple/1.png')
    scaled_image = pg.transform.scale(image, image_size)
    APPLES_SURF.append(scaled_image)


pg.mixer.init()
pg.mixer.music.load('bg_lvl1.mp3')
pg.mixer.music.play(loops=-1)
pg.mixer.music.set_volume(0.2)


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
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх,
            # а удаляем из всех групп
            self.kill()


apples = pg.sprite.Group()

# добавляем первую машину,
# которая появляется сразу
Apple(randint(100, W - 100), APPLES_SURF[randint(0, 1)], apples)

while 1:
    pg.time.delay(0)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.USEREVENT:
            Apple(randint(100, W - 100), APPLES_SURF[2], apples)
    drawWindow()


