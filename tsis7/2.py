import time
import pygame as pg
pg.init()

f = "/Users/asus2/OneDrive/Рабочий стол/pp2/tsis7/11.mp3"
s= "/Users/asus2/OneDrive/Рабочий стол/pp2/tsis7/22.mp3"
t= "/Users/asus2/OneDrive/Рабочий стол/pp2/tsis7/33.mp3"
screen = pg.display.set_mode((400, 400))
pg.display.set_caption("Music Player")
clock = pg.time.Clock()
a = pg.mixer.music.load(f)
b = pg.mixer.music.load(s)
c = pg.mixer.music.load(t)
musi = [a,b,c]
pg.mixer.music.play(-1)
play = False
run = True
i = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                play = not play
                if play:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT:
                
                i += 1
                if i == len(musi):
                    i = 0
                pg.mixer.music.load(musi[i])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                i -= 1
                if i == -1: 
                    i = len(musi)-1
                pg.mixer.music.load(musi[i])
                pg.mixer.music.play()


    pg.display.flip()
    clock.tick(60)