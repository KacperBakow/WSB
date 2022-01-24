from static import *
from pgzero.builtins import mouse, Rect, music, sounds
import random
import sys
import time

WIDTH = 800
HEIGHT = 600

LVL = 1
BLACK = 0, 0, 0
GOLD = 255, 223, 0
WHITE = 255, 255, 255
LIFE = 3
LOST = False
rects = [[Rect(random.randint(0, WIDTH), 0, 20, 20), True] for _ in range(5+LVL)]


left = 6
STRATA = False
PKT =0
start = 0
def close_game(now):
    global start
    sounds.gameover.play()
    if not start:
        start = now
    elif abs(start - now) > 3:
        sys.exit(0)

def on_mouse_down(pos, button):
    global left, PKT
    if button != mouse.LEFT: #tylko klawisz lewy
        return
    for rect in rects:
        if rect[0].x <= pos[0] <= rect[0].x + 20 and \
            rect[0].y <= pos[1] <= rect[0].y + 20 and rect[1]:
            rect[1] = False
            left -= 1
            sounds.pointsound.play()
            PKT += 10
            break

def update():
    global STRATA,LVL
    for rect in rects:
        if not rect[1]:
            continue
        rect[0].x += random.randint(-LVL, LVL)
        rect[0].y += random.randint(1, 2)
        if rect[0].x <= -20:
            rect[0].x += 1
        if rect[0].x >= WIDTH:
            rect[0].x -= 1
        if rect[0].y >= HEIGHT:
            STRATA = True

def draw():
    global LVL, PKT, left, rects, LIFE, STRATA, LOST
    screen.fill(BLACK)
    background.draw()
    screen.draw.text(f'Poziom: {LVL}', (600, 0), color=WHITE, fontsize=25, sysfontname='Tahoma')
    screen.draw.text(f'Punkty: {PKT}', (700, 0), color=WHITE, fontsize=25, sysfontname='Tahoma')
    for lives in range(LIFE):
        screen.blit("nagrobek2", (5 + lives * 28, 10))
    for rect in rects:
        if rect[1]:
            screen.draw.filled_rect(rect[0], GOLD)
    if left == 0:
        LVL += 1
        #sounds.lvlup.play()
        PKT += 50
        left = LVL + 5
        rects = [[Rect(random.randint(0, WIDTH), 0, 20, 20), True] for _ in range(5 + LVL)]

    if STRATA:
        LIFE = LIFE -1
        if LIFE > 0:
            sounds.miss.play()
            rects = [[Rect(random.randint(0, WIDTH), 0, 20, 20), True] for _ in range(5 + LVL)]
            left = LVL + 5
            STRATA = False
        else:
            close_game(time.time())

music.play('song1')
music.set_volume(0.3)
pgzrun.go()
