import pgzrun
from pgzero.builtins import Actor
from pgzero.screen import Screen
import random
screen: Screen


WIDTH = 800
HEIGHT = 600

BASE_WIDTH = 2000
BASE_HEIGHT = 1143

background = Actor('bga.png', pos=(0,0), anchor=(0,0))
pociski = Actor('nagrobek2', pos=(0,WIDTH), anchor=(0,0))