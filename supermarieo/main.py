import pygame
from pygame.locals import *
import sys

SCREENWIDTH = 845
SCREENHEIGHT = 820
FPS = 30


class MyMap():

    def __init__(self, x, y):
        self.bg = pygame.image.load("image/bg.png").convert_alpha()
        self.x = x
        self.y = y

    def map_rolling(self):
        if self.x < -845:
            self.x = 845
        else:
            self.x -= 5

    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))

class Music_Button():
    is_open = True
    def __init__(self):
        self.open_image = pygame.image.load("image/btn_open.png").convert_alpha()
        self.close_image = pygame.image.load("image/btn_close.png").convert_alpha()
        self.bg_music = pygame.mixer.Sound("audio/bg_music.wav")

    def is_select(self):
        point_x,point_y = pygame.mouse.get_pos()
        w, h = self.open_image.get_size()
        in_x = point_x >20 and point_x<20+w
        in_y = point_y >20 and point_y<20+h
        return in_x and in_y

def main_game():
    score = 0
    over = False
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption("马尔福历险记")
    bg1 = MyMap(0, 0)
    bg2 = MyMap(900,0)

    music_button = Music_Button()
    btn_img = music_button.open_image
    music_button.bg_music.play(-1)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if music_button.is_select():
                    if music_button.is_open:
                        btn_img = music_button.close_image
                        music_button.is_open = False
                        music_button.bg_music.stop()
                    else:
                        btn_img = music_button.open_image
                        music_button.is_open = True
                        music_button.bg_music.play(-1)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        if over == False:
            bg1.map_update()
            bg1.map_rolling()
            bg2.map_update()
            bg2.map_rolling()
        SCREEN.blit(btn_img, (20, 20))


if __name__ == '__main__':
    main_game()
