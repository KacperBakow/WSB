from pgzero.builtins import Actor, animate
from random import uniform, randint
from static import pociski


WIDTH = 800
HEIGHT = 600
LVL = 1
class PociskAnimacja:
    def __init__(self, screen):
        self.screen = screen
        self.overflow = 600

    @staticmethod
    def get_speed():
        return uniform(LVL, LVL)

    def set_screen(self, screen):
        self.screen = screen

    def animate_pocisk(self):
        pociski.x = randint(0, WIDTH)
