#!/usr/bin/python3

import pygame, sys
from random import choice
# from eg import file_manager
pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("CubeTimer")

fonts = pygame.font.SysFont("comicsans", 30)

fps = pygame.time.Clock()
FPS = 100

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

timings = []
txt = open("timings.txt", "a")
option = 0

cube_moves = ["L ", "L' ", "R ", "R' ", "L2 ", "R2 ", "U ", "U' ", "U2 ", "F ", "F' ", "F2 ", "D ", "D' ", "D2 ", "B ", "B' ", "B2 "]

# f = file_manager("timings.txt")

class Timer:
    def __init__(self):
        self.t = 0
        self.sec = 0
        self.min = 0
        self.sec_fonts = pygame.font.SysFont("comicsans", 200)
        self.min_fonts = pygame.font.SysFont("comicsans", 75)
        self.milli_fonts = pygame.font.SysFont("comicsans", 75)
        self.is_start = False
        self.moves = ""
        self.n = 20
        for i in range(self.n):
            self.moves += choice(cube_moves)

    def show(self):
        self.sec_img = self.sec_fonts.render(str(self.sec), 1, white)
        self.min_img = self.min_fonts.render(str(self.min), 1, white)
        self.milli_img = self.milli_fonts.render(str(self.t), 1, white)

        moves_text = fonts.render("Shuffle:   " + self.moves, 1, white)
        window.blit(moves_text, ((width-moves_text.get_width())/2, 500))

        window.blit(self.sec_img, (350, 250))
        window.blit(self.min_img, (250, 150))
        window.blit(self.milli_img, (500, 400))

    def start(self):
        if self.t == 100:
            self.t = 0
            self.sec += 1

        if self.sec == 60:
            self.sec = 0
            self.min += 1

        if self.min == 60:
            self.t = 0
            self.sec = 0
            self.min = 0

        self.sec_img = self.sec_fonts.render(str(self.sec), 1, white)
        self.min_img = self.min_fonts.render(str(self.min), 1, white)
        self.milli_img = self.milli_fonts.render(str(self.t), 1, white)

        window.blit(self.sec_img, (350, 250))
        window.blit(self.min_img, (250, 150))
        window.blit(self.milli_img, (500, 400))

    def reset(self):
        timings.append(str("%02d" % self.min) + ":" + str("%02d" % self.sec) + ":" + str("%02d" % self.t))
        self.moves = ""
        for i in range(self.n):
            self.moves += choice(cube_moves)
        self.t = 0
        self.min = 0
        self.sec = 0
        for timing in timings:
            txt.write(str(timing) + "\n")
        # f.doing_its_stuff(window)

timer = Timer()

def render():
    window.fill(black)

    # f.doing_its_stuff(window)

    text1 = fonts.render("Press SpaceBar for Start/Stop", 1, yellow)
    text2 = fonts.render("Press R for reset and to save your timings", 1, red)
    window.blit(text1, (10, 10))
    window.blit(text2, (width - text2.get_width() - 10, 10))

    timer.show()

    if timer.is_start == True:
        timer.start()
        timer.t += 1

    pygame.display.update()
    fps.tick(FPS)

def loop():
    while True:
        global option
        render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    option += 1
                    if option % 2 != 0:
                        timer.is_start = True
                    else:
                        timer.is_start = False
                if event.key == pygame.K_r:
                    timer.reset()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

loop()
