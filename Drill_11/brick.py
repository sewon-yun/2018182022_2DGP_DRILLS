import random
from pico2d import *
import game_world
import game_framework

class Brick:
    image = None

    def __init__(self):

        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y, self.move_speed = 100, 200, 450
        self.dir = 1
    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.x > 1450:
            self.dir = -1
        elif self.x < 100:
            self.dir = 1
        self.x += self.dir * self.move_speed * game_framework.frame_time
