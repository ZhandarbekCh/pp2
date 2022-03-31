
import pygame as pg
import sys
pg.init()
sc = pg.display.set_mode((400, 300))

x=0

music=["chase.mp3", "still.mp3", "N.mp3"]

done=False

while not done:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                done=True
            
            press=pg.key.get_pressed()
            
            if press[pg.K_s]:
                pg.mixer.music.load(music[x])
                pg.mixer.music.play()

            if press[pg.K_p]:
                pg.mixer.music.pause()

            if press[pg.K_u]:
                pg.mixer.music.unpause() 

            if press[pg.K_KP_MINUS]:
                pg.mixer.music.set_volume(0.2)

            if press[pg.K_KP_PLUS]:
                pg.mixer.music.set_volume(1)

            if press[pg.K_RIGHT]:
                x=x+1
                if x>2:
                    x=0
                    pg.mixer.music.load(music[x])
                    pg.mixer.music.play()
                    print(x)
                else:
                    pg.mixer.music.load(music[x])
                    pg.mixer.music.play()
                    print(x)
            if press[pg.K_LEFT]:
                x=x-1
                if x<0:
                    x=2
                    pg.mixer.music.load(music[x])
                    pg.mixer.music.play()
                    print(x)
                else:
                    pg.mixer.music.load(music[x])
                    pg.mixer.music.play()
                    print(x)
    pg.display.flip()

