from random import randint
import pygame as pg
pg.init()
import sys

pg.time.set_timer(pg.USEREVENT, 800)


W = 720
H = 720
wh = (W,H)
image_size = (40,80)
WHITE = (255, 255, 255)
CARS = ('car1.png', 'car2.png', 'car3.png', 'car4.png')
CARS_SURF = []
for car in CARS:
    image = pg.image.load(car)
    scaled_image = pg.transform.scale(image, image_size)
    CARS_SURF.append(scaled_image)

pg.display.set_caption("по встречке 220")

bg = pg.image.load('background.png')
bg = pg.transform.scale(bg, (wh))

sc = pg.display.set_mode((W, H))

pg.mixer.init()
pg.mixer.music.load('bgmusic.mp3')
pg.mixer.music.play(loops=-1)
pg.mixer.music.set_volume(0.02)



class Car(pg.sprite.Sprite):
    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у машин будет разная скорость
        self.speed = randint(2, 5)

    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх,
            # а удаляем из всех групп
            self.kill()


cars = pg.sprite.Group()

# добавляем первую машину,
# которая появляется сразу
Car(randint(100, W-100),
    CARS_SURF[randint(0, 3)], cars)

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.USEREVENT:
            Car(randint(100, W-100),
                CARS_SURF[randint(0, 3)], cars)

    sc.blit(bg, (0,0))
    cars.draw(sc)
    pg.display.update()
    pg.time.delay(0)


    cars.update()