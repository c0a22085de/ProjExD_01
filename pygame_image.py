import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") #練習1
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True, False)]*2

    kk_img = pg.image.load("ex01/fig/3.png") #練習2
    kk_img = pg.transform.flip(kk_img, True, False) #練習2
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)] #練習3
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%1600
        for i in range(4):
            screen.blit(bg_imgs[i], [1600*i-x, 0])
        #screen.blit(bg_img, [-x, 0]) #練習4
        #screen.blit(bg_img, [1600-x, 0])
        screen.blit(kk_imgs[tmr%100//50], [300, 200]) #練習5
        pg.display.update()
        tmr += 1       
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()